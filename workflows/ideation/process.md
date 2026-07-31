# Ideation Workflow

## Overview

The ideation process is the first step in the production pipeline. It transforms raw trends and brand goals into validated content concepts.

## Step-by-Step Process

1. **Trend Input**: The Strategy Agent scans `viral_engine/trend_analysis` for current high-performing topics.
2. **Concept Generation**: The Agent generates 5-10 concepts based on the Brand Bible.
3. **Scoring**: Each concept is evaluated using the `viral_engine/scoring_system`.
4. **Validation**: The QA Agent reviews the top-scored ideas for safety and educational alignment.
5. **Output**: A "Viral Idea Document" is created and moved to the Scripting workflow.

## Workflow Inputs & Outputs

| Stage | Input | Responsible Agent | Output |
| :--- | :--- | :--- | :--- |
| **Scanning** | Trend Data | Strategy Agent | Trend Report |
| **Drafting** | Trend Report + Brand Bible | Strategy Agent | Concept List |
| **Scoring** | Concept List | Strategy Agent | Scored Concepts |
| **Review** | Scored Concepts | QA Agent | Approved Idea Doc |
