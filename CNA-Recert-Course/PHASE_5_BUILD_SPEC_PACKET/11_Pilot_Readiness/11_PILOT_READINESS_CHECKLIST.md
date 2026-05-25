# Pilot Readiness Checklist

**Pilot go/no-go rule:** Do not pilot with live certificate issuance unless certificate gates, active-time control, affidavit, certificate fields, audit packet, privacy controls, and rollback procedure pass QA.

---

## Readiness Checklist

| Area | Readiness Item | Pass Criteria | Owner | Status |
|---|---|---|---|---|
| Compliance blockers | CDPH provider/course approval documented | Approval metadata active or certificate issuance disabled | Compliance Lead | TBD |
| Compliance blockers | NAC# documented | NAC# in restricted approval archive or certificate disabled | Compliance Lead | TBD |
| Compliance blockers | Approved course list documented | Course titles/hours/objectives mapped to Moodle shell | Program Director | TBD |
| Compliance blockers | Approved certificate wording documented | Template wording approved or certificate disabled | Registrar | TBD |
| Compliance blockers | Affidavit method documented | E-sign approved or wet-sign fallback configured | Legal/Compliance | TBD |
| Certificate blockers | All certificate gates configured | Gate matrix implemented in staging | Moodle Admin | TBD |
| Certificate blockers | Negative certificate tests pass | QA-001 through QA-020 pass as applicable | QA Manager | TBD |
| Certificate blockers | Clinical support not a certificate gate | Skipping clinical hub does not block certificate | QA Manager | TBD |
| Certificate blockers | Manual override control works | Unauthorized override denied; authorized override logged | Compliance Lead | TBD |
| Moodle blockers | Required/optional sections separated | Learner sees required theory and optional support separately | Moodle Admin | TBD |
| Moodle blockers | Active-time tool validated | Active-time validation plan passed or manual/custom fallback built | Moodle Admin | TBD |
| Moodle blockers | Cron/scheduled tasks working | Completion, reports, notifications, backups update as expected | Moodle Admin | TBD |
| Learner UX blockers | Mobile browser path tested | Learner can complete prototype path on phone | UX Tester | TBD |
| Learner UX blockers | No new video dependency | Required path works without video | ID Lead | TBD |
| Learner UX blockers | Learner copy reviewed | Partial credit, online cap, active time, support copy approved for pilot | Compliance Reviewer | TBD |
| Privacy blockers | No-PHI warnings live | Warning appears before upload/free text areas | Privacy Officer | TBD |
| Privacy blockers | PHI incident workflow tested | Simulated PHI upload is quarantined/rejected/escalated | Privacy Officer | TBD |
| Audit blockers | Audit packet sample exported | Packet includes required identity, time, interaction, exam, affidavit, certificate, version records | Compliance Lead | TBD |
| Audit blockers | Retention path documented | Four-year minimum retention or counsel-approved schedule documented | Operations Lead | TBD |
| Support blockers | Support scripts ready | Staff can answer partial credit, active-time, certificate hold, clinical support questions | Support Lead | TBD |
| Support blockers | Staffing ready | Pilot support coverage and escalation owners assigned | Program Owner | TBD |
| Backup/restore blockers | Backup configured | Database/files/course snapshot backup complete | IT/Security | TBD |
| Backup/restore blockers | Restore tested | Staging restore test documented | IT/Security | TBD |
| Rollback triggers | Certificate defect rollback | Owner can disable certificate activity immediately | Moodle Admin / Registrar | TBD |
| Rollback triggers | Incorrect certificate issued | Void/reissue/escalation procedure documented | Registrar | TBD |
| Rollback triggers | PHI incident | Quarantine/delete/escalate procedure documented | Privacy Officer | TBD |
| Rollback triggers | Support overload | Pause enrollment or extend SLA decision path documented | Program Owner | TBD |

## Pilot Readiness Decision

Use one of:

- `Go - certificate disabled only`.
- `Go - certificate-enabled pilot`.
- `No-go - compliance blocker`.
- `No-go - technical blocker`.
- `No-go - privacy blocker`.
- `No-go - audit blocker`.
- `No-go - support blocker`.

## Minimum Certificate-Enabled Pilot Criteria

Certificate-enabled pilot requires:

1. Approval metadata active.
2. Certificate wording approved.
3. Affidavit method approved.
4. Active-time validation passed or fallback implemented.
5. Required/optional separation tested.
6. Optional clinical support skipped without blocking certificate.
7. Audit packet exported for test learner.
8. PHI controls tested.
9. Rollback procedure ready.
