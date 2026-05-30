# Source Coverage

## Reviewed Coverage

| Area | Coverage | Notes |
|---|---:|---|
| TTS narration package | Complete for assigned file | Reviewed Modules 0-7 TTS segments, duration notes, disclaimers, pronunciation notes, and SME flags. |
| Narration CSV guidance | Complete | `NARRATION_DRAFT.csv` created from reviewed TTS source. |
| Media placeholder guidance | Complete as planning guidance | No media generated. |
| JSON/schema expectations | Complete as coordinator guidance | Based on TTS source and assignment guardrails. |
| App location suggestions | Complete as proposed map | Uses required patterns including `dashboard.hero`, `modules.m1.overview`, `modules.m1.l1.c02a`, `final.assessment.splash`, `certificate.gate.status`, and `clinical.unit01.overview`. |

## Blocked Coverage

| Area | Coverage | Reason |
|---|---:|---|
| `standalone-course-mvp/screenshots/v2-design` file list | Not completed | Local PowerShell failed before shell startup; GitHub fallback did not expose this path. |
| `standalone-course-mvp/src/data` wiring review | Not completed | Local PowerShell failed before shell startup; GitHub fallback did not expose this path. |
| `standalone-course-mvp/src/pages` wiring review | Not completed | Local PowerShell failed before shell startup; GitHub fallback did not expose this path. |

## Coordinator Follow-Up Needed

- Run local file enumeration for `standalone-course-mvp/screenshots/v2-design`.
- Inspect TSX imports/usages in `standalone-course-mvp/src/pages`.
- Inspect content data structures in `standalone-course-mvp/src/data`.
- Confirm that app routes and data adapters preserve `app.location`, SME flags, exam flags, optional support boundaries, and disabled certificate status.
