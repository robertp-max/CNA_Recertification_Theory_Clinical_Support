# App Integration Notes

The standalone V2 app is wired through generated adapter files in `standalone-course-mvp/src/data/`:

- `contentV2.generated.ts` - generated copy of canonical ContentV2 JSON for the app bundle.
- `contentV2Adapter.ts` - converts canonical ContentV2 modules, lessons, quizzes, final exam, and app copy into the existing V2 app data contracts.

The adapter preserves the approved V2 navigation model: Dashboard, CE Modules, Certificate Gate, Clinical Hub. Login and sign-in card files were not modified by the generator. Certificate production remains disabled and Optional Clinical Support remains non-credit/non-gating.
