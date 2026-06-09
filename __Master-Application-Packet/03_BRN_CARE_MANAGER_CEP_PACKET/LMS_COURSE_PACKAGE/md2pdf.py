"""
Lightweight Markdown -> PDF renderer built on reportlab.

Supports the Markdown subset used by the BRN CM CE documentation packet:
  - Headings  # ## ### ####
  - Paragraphs with inline **bold**, *italic*, `code`
  - Bullet lists ( - or * ), one nested level ( two-space indent )
  - Numbered lists ( 1. )
  - Pipe tables (header row + --- separator)
  - Fenced code blocks ( ``` )
  - Horizontal rule ( --- )
  - Blockquote ( > )

This is a build helper. The PDF-ready Markdown files remain the editable source.
"""

import re
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    ListFlowable, ListItem, Preformatted, HRFlowable,
)

NAVY = colors.HexColor("#1F3864")
LIGHT = colors.HexColor("#DBE2F1")
GREY = colors.HexColor("#BFBFBF")
RED = colors.HexColor("#7F0000")


def _styles():
    ss = getSampleStyleSheet()
    styles = {
        "h1": ParagraphStyle("h1", parent=ss["Heading1"], textColor=NAVY,
                             fontSize=18, spaceBefore=10, spaceAfter=8, leading=22),
        "h2": ParagraphStyle("h2", parent=ss["Heading2"], textColor=NAVY,
                             fontSize=14, spaceBefore=10, spaceAfter=6, leading=18),
        "h3": ParagraphStyle("h3", parent=ss["Heading3"], textColor=NAVY,
                             fontSize=12, spaceBefore=8, spaceAfter=4, leading=15),
        "h4": ParagraphStyle("h4", parent=ss["Heading4"], textColor=NAVY,
                             fontSize=10.5, spaceBefore=6, spaceAfter=3, leading=13),
        "body": ParagraphStyle("body", parent=ss["BodyText"], fontSize=9.5,
                               leading=13, spaceAfter=5, alignment=TA_LEFT),
        "note": ParagraphStyle("note", parent=ss["BodyText"], fontSize=9,
                               leading=12, textColor=RED, spaceAfter=5),
        "cell": ParagraphStyle("cell", parent=ss["BodyText"], fontSize=8,
                               leading=10),
        "cellh": ParagraphStyle("cellh", parent=ss["BodyText"], fontSize=8,
                                leading=10, textColor=colors.white, fontName="Helvetica-Bold"),
        "code": ParagraphStyle("code", parent=ss["Code"], fontSize=8, leading=10),
    }
    return styles


def _esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _inline(t):
    t = _esc(t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<i>\1</i>", t)
    t = re.sub(r"`(.+?)`", r'<font face="Courier">\1</font>', t)
    return t


def _table(rows, styles, avail_width):
    data = []
    header = rows[0]
    body = rows[1:]
    data.append([Paragraph(_inline(c), styles["cellh"]) for c in header])
    for r in body:
        data.append([Paragraph(_inline(c), styles["cell"]) for c in r])
    ncols = len(header)
    col_w = avail_width / ncols
    tbl = Table(data, colWidths=[col_w] * ncols, repeatRows=1)
    tbl.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("GRID", (0, 0), (-1, -1), 0.4, GREY),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return tbl


def _split_table_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]


def markdown_to_pdf(md_text, out_path, avail_width=None):
    styles = _styles()
    if avail_width is None:
        avail_width = letter[0] - 1.4 * inch
    flow = []
    lines = md_text.split("\n")
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        stripped = line.strip()

        # fenced code block
        if stripped.startswith("```"):
            i += 1
            buf = []
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            flow.append(Preformatted("\n".join(buf), styles["code"]))
            flow.append(Spacer(1, 4))
            continue

        # blank
        if stripped == "":
            i += 1
            continue

        # horizontal rule
        if stripped == "---" or re.fullmatch(r"-{3,}", stripped):
            flow.append(Spacer(1, 2))
            flow.append(HRFlowable(width="100%", thickness=0.6, color=GREY))
            flow.append(Spacer(1, 4))
            i += 1
            continue

        # table block
        if stripped.startswith("|") and "|" in stripped[1:]:
            tbl_lines = []
            while i < n and lines[i].strip().startswith("|"):
                tbl_lines.append(lines[i])
                i += 1
            rows = [_split_table_row(l) for l in tbl_lines]
            rows = [r for r in rows if not all(re.fullmatch(r":?-{2,}:?", c or "-") for c in r)]
            if rows:
                flow.append(_table(rows, styles, avail_width))
                flow.append(Spacer(1, 6))
            continue

        # headings
        m = re.match(r"^(#{1,4})\s+(.*)$", stripped)
        if m:
            level = len(m.group(1))
            key = f"h{level}"
            flow.append(Paragraph(_inline(m.group(2)), styles[key]))
            i += 1
            continue

        # blockquote
        if stripped.startswith(">"):
            buf = []
            while i < n and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip()[1:].strip())
                i += 1
            txt = " ".join(buf)
            qs = ParagraphStyle("quote", parent=styles["note"], leftIndent=10,
                                borderColor=NAVY, borderWidth=0)
            flow.append(Paragraph(_inline(txt), qs))
            continue

        # bullet list
        if re.match(r"^\s*[-*]\s+", line):
            items = []
            while i < n and re.match(r"^\s*[-*]\s+", lines[i]):
                indent = len(lines[i]) - len(lines[i].lstrip())
                content = re.sub(r"^\s*[-*]\s+", "", lines[i])
                bullet = "circle" if indent >= 2 else "bullet"
                items.append(ListItem(Paragraph(_inline(content), styles["body"]),
                                      leftIndent=18 + (12 if indent >= 2 else 0),
                                      value=bullet))
                i += 1
            flow.append(ListFlowable(items, bulletType="bullet", start="bullet",
                                     leftIndent=10))
            flow.append(Spacer(1, 3))
            continue

        # numbered list
        if re.match(r"^\s*\d+\.\s+", line):
            items = []
            while i < n and re.match(r"^\s*\d+\.\s+", lines[i]):
                content = re.sub(r"^\s*\d+\.\s+", "", lines[i])
                items.append(ListItem(Paragraph(_inline(content), styles["body"])))
                i += 1
            flow.append(ListFlowable(items, bulletType="1", leftIndent=14))
            flow.append(Spacer(1, 3))
            continue

        # paragraph (gather until blank/structural)
        buf = [stripped]
        i += 1
        while i < n:
            nxt = lines[i].strip()
            if (nxt == "" or nxt.startswith("#") or nxt.startswith("|")
                    or nxt.startswith(">") or nxt.startswith("```")
                    or re.match(r"^\s*[-*]\s+", lines[i])
                    or re.match(r"^\s*\d+\.\s+", lines[i])
                    or re.fullmatch(r"-{3,}", nxt)):
                break
            buf.append(nxt)
            i += 1
        para = " ".join(buf)
        style = styles["note"] if para.startswith("[[") else styles["body"]
        flow.append(Paragraph(_inline(para), style))

    def _footer(canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 7)
        canvas.setFillColor(RED)
        canvas.drawString(0.7 * inch, 0.45 * inch,
                          "Draft / Pending BRN CEP Approval - not approved; no CEP number issued. "
                          "Do not advertise or issue certificates until a BRN CEP number is issued.")
        canvas.setFillColor(colors.grey)
        canvas.drawRightString(letter[0] - 0.7 * inch, 0.45 * inch,
                               f"Page {doc.page}")
        canvas.restoreState()

    doc = SimpleDocTemplate(out_path, pagesize=letter,
                            leftMargin=0.7 * inch, rightMargin=0.7 * inch,
                            topMargin=0.7 * inch, bottomMargin=0.7 * inch,
                            title="BRN CM CE Documentation - Draft / Pending BRN CEP Approval")
    doc.build(flow, onFirstPage=_footer, onLaterPages=_footer)
