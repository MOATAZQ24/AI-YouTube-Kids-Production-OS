# State Management System

The AI-YouTube-Kids-Production-OS relies on a persistent JSON state file to track the progress of each video through the 6-phase production pipeline. This ensures that if a process is interrupted, the system can resume seamlessly without losing context.

## State File Schema

```json
{
  "project_id": "unique-string-id",
  "status": "pending | active | completed | failed",
  "current_phase": 0,
  "metadata": {
    "created_at": "ISO-8601-timestamp",
    "updated_at": "ISO-8601-timestamp",
    "assigned_character": "character-name",
    "target_language": "en | es | fr | ar"
  },
  "phases": {
    "phase_1_research": {
      "status": "pending | completed | failed",
      "output": null,
      "decision_matrix": null
    },
    "phase_2_ideation": {
      "status": "pending | completed | failed",
      "output": null,
      "decision_matrix": null
    },
    "phase_3_scripting": {
      "status": "pending | completed | failed",
      "output": null,
      "decision_matrix": null
    },
    "phase_4_production": {
      "status": "pending | completed | failed",
      "output": null,
      "decision_matrix": null
    },
    "phase_5_optimization": {
      "status": "pending | completed | failed",
      "output": null,
      "decision_matrix": null
    },
    "phase_6_learning": {
      "status": "pending | completed | failed",
      "output": null,
      "decision_matrix": null
    }
  }
}
```

## State Machine Logic

1. **Initialization**: When a new project is requested, generate a `project_id`, set `current_phase` to `1`, and initialize the `metadata`.
2. **Phase Completion**: When a phase completes successfully, update its status to `completed`, save the JSON output, and increment `current_phase`.
3. **Phase Failure**: If a phase fails (e.g., viral score too low), update its status to `failed`. The system should either retry the phase (up to 3 times) or terminate the pipeline and set the overall `status` to `failed`.
4. **Resumption**: On startup, read the state file. If `status` is `active` and `current_phase` is > 0, resume from the phase that has a `pending` status.

## Integration Hooks

- **Read State**: `fs.readFileSync('./state/current_project.json')`
- **Write State**: `fs.writeFileSync('./state/current_project.json', JSON.stringify(state))`
- **Update Phase**: Update the specific phase object and increment `current_phase`.
