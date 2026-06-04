# Module Dry Run Shell

This folder is the reusable dry-run shell for NATP Modules 10–17.

## App root

```text
Module_Dry_Run/standalone-course-mvp
```

## Source authority rule

For each run, use only the approved module PDF outside this folder as source authority, for example:

```text
CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-10.pdf
CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-11.pdf
...
CNA-Recert-Course/CNA_Modules/cccco-na-model-curriculum-module-17.pdf
```

Do not use backup folders, old ContentV2, copied course packages, or prior generated dry-run outputs as source authority.

## Output convention

Existing Module 10 outputs are preserved here:

```text
Module_Dry_Run/_module10_dryrun_outputs
```

For future modules, use module-specific output roots inside this folder, e.g.:

```text
Module_Dry_Run/_module11_dryrun_outputs
Module_Dry_Run/_module12_dryrun_outputs
...
Module_Dry_Run/_module17_dryrun_outputs
```

## Narration batching rule

Do not use CSV narration import for future dry runs. Use JSON-based narration batch packages/manifests, for example:

```text
_moduleXX_dryrun_outputs/audio/narration_batch_import_package.json
_moduleXX_dryrun_outputs/audio/audio_manifest.json
```

Speech audio remains gated until scripts are source-validated and generation is explicitly authorized.
