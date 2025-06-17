# Categorize large-scale survey data

Category: Analysis
Information needed?: Information needed

# [PLEASE REMOVE ALL PII BEFORE UPLOADING ANY DATA TO YOUR LLM](../Instructions%201f4b1fbd87d981279751ecbb947c14be/Removing%20PII%20from%20datasets%201f4b1fbd87d981a6964dd90afebfa2ba.md)

## **Context:**

Uploading non-PII survey data to an LLM allows for efficient categorization and theme identification across large datasets. This prompt helps researchers structure the data, generate meaningful themes, and produce summaries for actionable insights while maintaining privacy.

## **Prompt:**

Upload your non-PII survey data and follow the steps to categorize and synthesize it into actionable themes.

“I am uploading survey data that does not contain personally identifiable information (PII). Help me categorize the responses into clear themes and summarize the findings. The dataset includes [number] rows of open-ended responses on [topic or research goal].

 **Review the data and suggest initial categories:**

- Read through a random sample of responses to identify recurring patterns.
- Suggest 5-10 potential themes or categories based on the content.

**Categorize the data:**

- Group responses into the identified categories.
    - Example: Row 1 → “Feature Request,” Row 2 → “Navigation Issue.”
- Allow for responses to fit into multiple categories if needed.
- Highlight uncategorizable responses for review or suggest an “Other” category, but please use this sparingly

**Summarize the findings:**

- Provide the following for each category:
    - Frequency count: “X% of responses mentioned [category].”
    - Representative quotes: “Example: ‘I couldn’t find the settings menu without help.’”
    - Emerging sub-themes (if applicable): “Within ‘Navigation Issues,’ a common sub-theme was difficulty finding the search bar.”

**Visualize the results:**

- Suggest a format for visualizing the categorized data.
    - Example: Bar charts for category frequencies

## **Reflection questions:**

- Are there any patterns or themes that were unexpected?
- Have I included sufficient detail to represent the user’s perspective accurately?
- Are the themes actionable and aligned with my research goals?
- Is there any additional context that would help refine the categorization process?

## **Follow-Up Prompts:**

- “Generate a summary report based on the categorized data for stakeholders.”
- “Draft recommendations based on the top themes identified in the analysis.”
- “Suggest a validation process for ensuring accuracy in categorization.”
- “Propose methods for visualizing the results in a presentation-friendly format.”
- “Identify any gaps or areas needing further exploration in the dataset.”