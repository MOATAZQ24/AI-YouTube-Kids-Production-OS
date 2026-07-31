# Character Template

## Purpose

This template provides a standardized structure for defining new characters within the AI-YouTube-Kids-Production-OS. Its purpose is to ensure comprehensive character development and maintain consistency across all AI-generated content featuring these characters.

## Context

Located in the `knowledge/characters/` directory, this template is crucial for the Character Agent and other AI agents to understand a character's visual, personality, and behavioral attributes. It serves as a blueprint for generating consistent imagery, animation, and dialogue.

## Inputs

- **Creative Brief**: High-level character concept and role within a story.
- **Brand Bible**: `knowledge/brand/bible.md` (for overall brand personality and visual identity).

## Outputs

- **Consistent Character Portrayal**: Ensures that characters look, act, and sound the same across different episodes and scenarios.
- **Detailed AI Prompts**: Provides specific instructions for image and animation generation.

## Related Files

- `knowledge/brand/bible.md`
- `knowledge/stories/story_bible.md`
- `prompts/image/library.md`
- `prompts/video/animation_prompts.md`

## Dependencies

- **Character Agent**: Uses this template to maintain character consistency.
- **Visual Agent**: Relies on image and animation prompts for asset generation.
- **Writer Agent**: References personality and voice style for dialogue.

## Core Identity

- **ID**: [Character Unique ID]
- **Name**: [Character Name]
- **Age**: [Apparent Age]
- **Role**: [e.g., Protagonist, Sidekick, Mentor]

## Appearance & Personality

| Attribute | Description |
| :--- | :--- |
| **Physical Traits** | [Height, hair color, eye shape, etc.] |
| **Clothing** | [Standard outfit, colors, accessories] |
| **Personality** | [Key traits: e.g., Brave, Shy, Logical] |
| **Voice Style** | [Pitch, accent, catchphrases] |
| **Behavior** | [Typical actions, mannerisms, reactions] |
| **Relationships** | [Key connections to other characters] |
| **Character Story** | [Brief background or origin story] |

## AI Prompts

### Image Generation Prompt
> [Detailed prompt for consistent visual generation, incorporating `Master Style String` from `prompts/image/library.md`]

### Animation Style Prompt
> [Instructions for movement, expressions, and typical actions, referencing `prompts/video/animation_prompts.md`]

### Negative Prompt
> [What to avoid in generation (e.g., scary teeth, extra fingers, inconsistent colors)]

## Consistency Rules

- **Visual**: Always use the specified `Image Generation Prompt` and `Negative Prompt` to maintain appearance.
- **Behavioral**: Character actions and reactions must align with `Personality` and `Behavior` descriptions.
- **Vocal**: `Voice Style` must be strictly adhered to for all dialogue generation.

## Version History
- **v1.0**: Initial template created.

## Examples

- **Image Generation Prompt**: For a character named 'Leo the Lion', the prompt might include `3D stylized render, friendly lion cub, fluffy mane, bright yellow fur, playful expression, ultra-kid-friendly --ar 16:9`.
- **Consistency Rule**: If a character is defined as 'shy', they should not suddenly become boisterous without a clear narrative reason.
