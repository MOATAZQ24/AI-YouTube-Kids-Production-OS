# n8n Automation Architecture

The AI-YouTube-Kids-Production-OS uses n8n to glue the different AI agents and platforms together.

## Core Workflows

### 1. Trend-to-Idea Workflow
- **Trigger**: Weekly cron job.
- **Action**: Scans YouTube Trends API and Google Trends.
- **Agent**: Strategy Agent generates ideas.
- **Output**: Pushes to a Notion database for human/QA review.

### 2. Script-to-Asset Workflow
- **Trigger**: Status change in Notion to "Approved".
- **Action**: Writer Agent generates script -> Visual Agent generates prompts -> Midjourney/DALL-E generates images.
- **Output**: Saves assets to the `assets/` directory in Google Drive.

## Integration Map

| Source | Destination | Purpose |
| :--- | :--- | :--- |
| **Google Drive** | GitHub | Syncing assets and documentation. |
| **OpenAI/Claude** | n8n | Processing agent prompts. |
| **YouTube API** | Analytics | Pulling performance data for the Memory system. |
| **Slack/Discord** | QA Agent | Notifications for review and approval. |
