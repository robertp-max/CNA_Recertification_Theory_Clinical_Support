# Orchestration Control Rule Addendum

Status: Active replacement escalation / scheduling rule for this Module 10 dry run.

Control line:

> Do not stop the whole run just because one worker is blocked. Escalate, attempt orchestrator resolution for 10 minutes, then pause/reassign/terminate only the affected job unless a critical-path blocker eventually blocks all remaining safe work.

## Worker Escalation, Pause, Reassignment, and Termination Rule

The orchestration must keep workers active whenever safe work remains available.

Workers should not stop for routine, resolvable issues. They must attempt to resolve ordinary blockers within their approved scope before escalating.

### Worker-Level Resolution Window

If a worker encounters a non-critical issue, the worker must attempt to resolve it for up to 10 minutes.

A worker may resolve the issue and continue if the fix:

- stays inside the approved write scope;
- does not change source meaning;
- does not invent clinical content;
- does not introduce PHI;
- does not claim approval, credit, certificate readiness, or online competency;
- does not expose protected answer keys;
- does not modify deployment settings;
- does not commit, push, or create PR;
- does not edit outside the approved project/app scope.

If the worker cannot resolve the issue within 10 minutes, the worker must escalate to the orchestrator instead of stopping the whole run.

The escalation must include:

- worker name;
- active task;
- blocker description;
- files inspected;
- commands/checks attempted;
- what failed;
- whether the issue blocks only this worker or blocks downstream workers;
- recommended next action.

### Orchestrator-Level Resolution Window

When a worker escalates a blocker, the orchestrator has up to 10 minutes to resolve it.

The orchestrator may:

- correct the worker instruction;
- assign a narrow repair task;
- adjust non-source-changing implementation details;
- mark a non-critical artifact as queued or deferred;
- reassign the worker to another available task;
- terminate the worker and launch a replacement;
- continue other independent workers in parallel.

The orchestrator must not violate hard stops or compliance rules.

### Pause Instead of Stop

If the orchestrator cannot resolve the blocker within 10 minutes, the orchestrator must pause that specific job, not the whole run, unless the paused job is on the critical path.

A paused job must include a pause note with:

- reason paused;
- unresolved blocker;
- dependency impact;
- attempted fixes;
- whether the job is critical path;
- what is needed to resume.

### Reassign or Terminate Worker

If a worker is blocked and other safe jobs remain available, the orchestrator must assign the worker a different job or terminate/relaunch that worker with a new task.

Workers should remain active until there are no safe jobs left.

A worker may be terminated if:

- it repeatedly fails the same task;
- it drifts from source scope;
- it attempts to edit outside approved scope;
- it ignores guardrails;
- it is blocked and cannot be reassigned;
- it is consuming time without producing useful artifacts.

Worker termination must be documented in the final handoff.

### Critical Path Rule

The orchestration may pause the whole run only when:

- the blocked job is on the critical path; and
- all other safe independent jobs are complete, blocked, or dependent on the paused job; and
- the orchestrator cannot resolve the blocker within 10 minutes.

Examples of critical-path blockers:

- approved repo path mismatch;
- source PDF missing;
- source extraction incomplete and downstream work depends on it;
- app root missing;
- build system unusable and app integration depends on it;
- write-scope violation risk;
- PHI/compliance violation risk.

Examples of non-critical blockers that should be queued/deferred while other work continues:

- image generation unavailable;
- SFX asset not found;
- TTS generation gated;
- one optional visual missing;
- one activity needing later SME review;
- media asset generation not ready;
- wrapper timeout where the artifact exists and passes checks.

### Parallel Progress Rule

The orchestrator must keep independent workers moving in parallel where dependencies allow.

Do not idle all workers because one worker is blocked.

Examples:

- If image generation is blocked, continue source map, data model, activities, audio scripts, SFX manifest, and app integration with image placeholders or prompt queue.
- If TTS generation is blocked, continue with transcripts/audio manifest and app UI audio controls.
- If SFX sourcing is blocked, continue with SFX manifest entries marked queued.
- If app integration is blocked, continue validation/reporting of source map and data artifacts where possible.

### Wrapper Timeout Rule

If a worker wrapper times out, inspect the expected artifact.

If the artifact exists, is complete, and passes basic checks:

- mark the worker as artifact-complete;
- do not rerun solely because of wrapper timeout;
- continue the chain.

If the artifact is missing, incomplete, corrupt, outside scope, or unsafe:

- escalate to orchestrator;
- attempt resolution for up to 10 minutes;
- then pause/reassign/terminate according to this rule.

### Hard Stops Still Override This Rule

Immediately stop the affected task and escalate to orchestrator if:

- repo path does not match approved repo path;
- a worker is about to edit outside approved write scope;
- source file is missing and cannot be located inside approved repo;
- active scope changes to the wrong module/course;
- stale ContentV2 or backup content is used as source authority;
- PHI is introduced or requested;
- worker attempts to claim CDPH/TPRU approval;
- worker attempts to claim clinical-hour credit;
- worker attempts to claim online hands-on competency validation;
- worker attempts to expose protected answer keys;
- worker attempts to commit, push, or create PR without authorization;
- worker attempts to alter production/staging deployment settings.

Hard stops pause or terminate only the affected job when possible. The whole run stops only if the hard stop blocks the critical path and no other safe jobs remain.
