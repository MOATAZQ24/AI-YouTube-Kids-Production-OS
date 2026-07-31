# Decision Matrix & Scoring System

The AI-YouTube-Kids-Production-OS uses a strict, formula-based decision matrix to ensure consistency and quality. Randomness is eliminated by requiring agents to score outputs against specific criteria before proceeding to the next phase.

## Phase 2: Idea Generation Matrix (Viral Score)

The Strategy Agent must generate 5-10 ideas and score each one. Ideas scoring below 7/10 are automatically rejected.

**Formula**: `Viral Score = (Engagement Expectation * 0.4) + (Novelty * 0.3) + (Emotional Impact * 0.3)`

```json
{
  "idea_id": "string",
  "title": "string",
  "viral_score": 0.0,
  "engagement_expectation": 0.0,
  "novelty": 0.0,
  "emotional_impact": 0.0,
  "educational_score": 0.0,
  "character_focus": "string",
  "brief_story": "string",
  "status": "approved | rejected"
}
```

## Phase 3: Scripting Matrix (Educational & Structural Score)

The Writer Agent must score the script based on pedagogical value and adherence to the 5-Shot Cinematic Method.

**Formula**: `Script Score = (Educational Value * 0.5) + (Structural Adherence * 0.3) + (Pacing * 0.2)`

```json
{
  "script_id": "string",
  "educational_value": 0.0,
  "structural_adherence": 0.0,
  "pacing": 0.0,
  "final_score": 0.0,
  "bloom_taxonomy_level": "Remember | Understand | Apply | Analyze | Evaluate | Create",
  "status": "approved | needs_revision"
}
```

## Phase 5: Optimization Matrix (Safety & QA Score)

The QA Agent must run a red-teaming simulation and score the final output against safety and SEO criteria.

**Formula**: `QA Score = (Safety Compliance * 0.5) + (SEO Optimization * 0.3) + (Brand Alignment * 0.2)`

```json
{
  "project_id": "string",
  "safety_compliance": 0.0,
  "seo_optimization": 0.0,
  "brand_alignment": 0.0,
  "final_score": 0.0,
  "red_team_simulations": [
    {
      "scenario": "string",
      "reaction": "string",
      "risk_level": "low | medium | high"
    }
  ],
  "status": "ready_to_publish | blocked"
}
```

## Configuration Thresholds

These thresholds can be adjusted in the `config.json` file:

- `MIN_VIRAL_SCORE`: 7.0
- `MIN_SCRIPT_SCORE`: 8.0
- `MIN_QA_SCORE`: 9.0
- `MAX_RETRIES`: 3
