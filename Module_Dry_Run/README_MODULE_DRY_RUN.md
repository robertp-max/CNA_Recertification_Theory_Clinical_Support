# Module Dry Run Shell

This folder is the reusable dry-run shell for NATP Modules 1–17.

## App root

```text
Module_Dry_Run/standalone-course-mvp
```

## Source authority rule

For each run, use only the approved module PDF outside this folder as source authority, for example:

```text
CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-1.pdf
CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-2.pdf
...
CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-17.pdf
```

Do not use backup folders, old ContentV2, copied course packages, or prior generated dry-run outputs as source authority.

## Output convention

Module-specific output roots are preserved inside this folder, e.g.:

```text
Module_Dry_Run/_module1_dryrun_outputs
Module_Dry_Run/_module2_dryrun_outputs
...
Module_Dry_Run/_module17_dryrun_outputs
```

Batch-generated remaining-module artifacts are documented in:

```text
Module_Dry_Run/_remaining_modules_work/remaining_modules_batch_manifest.json
Module_Dry_Run/_remaining_modules_work/remaining_modules_validation_summary.md
```

## Narration batching rule

Do not use CSV narration import for future dry runs. Use JSON-based narration batch packages/manifests, for example:

```text
_moduleXX_dryrun_outputs/audio/narration_batch_import_package.json
_moduleXX_dryrun_outputs/audio/audio_manifest.json
```

Speech audio remains gated until scripts are source-validated and generation is explicitly authorized.
