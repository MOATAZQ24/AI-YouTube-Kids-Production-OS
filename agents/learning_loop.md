# Learning Loop & Periodic Review System

The Learning Loop is the self-improvement mechanism of the AI-YouTube-Kids-Production-OS. It analyzes performance data after publishing and updates the Knowledge Base to make future content better. Additionally, the system runs a periodic review every 5 published videos to extract top lessons and generate a `git diff` for human approval.

## Phase 6: Learning Loop (Per-Video Analysis)

**Agent**: `Analytics Agent`
**System Prompt**:
```text
You are the Analytics Agent.
After a video is published, fetch the YouTube stats (views, watch time, engagement, drop-off points).
Identify what worked and what failed.
Propose specific changes to the Knowledge Base (characters, story structures, content pillars).
Output the performance analysis, learnings, and knowledge updates as a structured JSON object.
```
**Output Schema**:
```json
{
  "project_id": "string",
  "performance_analysis": {
    "views": 0,
    "watch_time_hours": 0,
    "ctr_percent": 0.0,
    "avd_percent": 0.0,
    "drop_off_points_sec": [15, 45]
  },
  "learnings": [
    {
      "observation": "High drop-off at 15 seconds during the intro.",
      "hypothesis": "The intro was too long and lacked a strong hook."
    }
  ],
  "knowledge_updates": [
    {
      "file": "knowledge/stories/story_bible.md",
      "proposed_change": "Reduce intro length to max 5 seconds."
    }
  ]
}
```

## Automated Periodic Review (Every 5 Videos)

**Agent**: `Strategy Agent (Retrospective)`
**System Prompt**:
```text
You are the Strategy Agent running a periodic retrospective.
Review the last 5 published videos and their Learning Loop data.
Extract the top 3 actionable lessons.
Generate a consolidated `git diff` format string representing the proposed Knowledge Base updates.
Output the retrospective report and the diff as a structured JSON object.
```
**Output Schema**:
```json
{
  "review_cycle": 1,
  "videos_analyzed": 5,
  "top_3_lessons": [
    "Bright blue backgrounds increase CTR by 15%.",
    "Animal sidekicks increase AVD by 40 seconds.",
    "Avoid dark colors in thumbnails to reduce drop-off."
  ],
  "knowledge_base_updates": {
    "action": "apply_updates",
    "diff_format": "@@ -1,5 +1,5 @@\n- Rule: Intros can be up to 15 seconds.\n+ Rule: Intros MUST be under 5 seconds.\n@@ -10,2 +10,2 @@\n- Visual Style: Any bright color.\n+ Visual Style: Prioritize bright blue backgrounds."
  },
  "status": "pending_human_approval"
}
```

## Integration Workflow

1. **Post-Publishing Trigger**: The YouTube API webhook triggers the Analytics Agent.
2. **Data Fetch**: The agent uses the YouTube Data API to pull analytics.
3. **Analysis**: The agent generates the Phase 6 JSON output.
4. **Cycle Counter**: A global counter tracks published videos. When `counter % 5 == 0`, the Periodic Review Agent is triggered.
5. **Human-in-the-Loop**: The `git diff` output is presented to the user for approval before modifying the actual Knowledge Base files.
