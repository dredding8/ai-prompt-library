# Determine the ideal sample size

Category: Planning
Information needed?: Information needed

## **Context:**

Choosing the right sample size is critical for balancing research goals, timelines, and resources. This prompt helps you determine an appropriate sample size based on your research method, objectives, and the level of confidence needed for actionable insights.

## **Prompt:**

Copy and paste this into your LLM and follow the steps to identify the ideal sample size for your research.

“I need help determining the right sample size for my research project. Guide me through selecting a sample size that balances confidence, feasibility, and actionable insights.

**Define the research objectives and methods:**

- What is the purpose of the research?
    - Example: “Understand user frustrations with the checkout process.”
- What research method(s) will I be using?
    - Example: “Moderated usability testing and follow-up surveys.”
- What type of insights am I aiming for?
    - Example: “Identify usability issues and measure user satisfaction.”

**Consider the confidence level needed:**

- How confident do I need to be in the results?
    - Example: “For usability testing, I need directional insights, not statistical significance. For surveys, I need a confidence level of 95%.”
- How many segments/personas am I looking at in this study?
    - Example: “I am going to be conducting research on two separate segments and need to ensure the sample size is appropriate for both.”

**Estimate the sample size for qualitative methods:**

For qualitative research (e.g., usability testing, interviews):

1. Use a smaller sample size to uncover patterns and issues:
    1. Example: “5-8 participants per segment are sufficient for usability testing to identify 80% of major issues.”
2. Adjust based on audience diversity or goals:
    1. Example: “If testing multiple user personas, recruit 2-3 participants per persona.”

Calculate the sample size for quantitative methods:

For quantitative research (e.g., surveys, A/B tests):

1. Use the formula for sample size based on confidence level, margin of error, and population size:
    1. Sample Size = (Z² × p × (1-p)) / e²
        1. Where:
        2. Z = Z-score (e.g., 1.96 for 95% confidence)
        3. p = Expected proportion (e.g., 50%)
        4. e = Margin of error (e.g., 5%)
2. If you’re unsure, use an online calculator to simplify this step.
3. Adjust for practical constraints:
    1. Example: “If a perfect sample is 384 but resources are limited, a sample of 250 may still yield meaningful insights.”

## Reflection questions:

For qualitative research:

- Am I including enough participants to uncover key patterns without over-recruiting?
- Am I accounting for user diversity or unique perspectives in the sample?

**For quantitative research:**

- Am I ensuring enough participants to achieve statistical significance?
- Have I adjusted for potential dropouts or non-responses?

**Review the feasibility of the sample size:**

- What resources (time, budget, recruitment tools) are available?
    - Example: “We have a two-week timeline and a budget for 15 participants.”
- Does the sample size align with stakeholder expectations and goals?
    - Example: “The product team expects at least 100 survey responses to validate their assumptions.”

Please expand this into a comprehensive sample size recommendation based on my research goals, methods, and constraints.”

## **Follow-Up Prompts:**

- “Suggest ways to adjust sample size if recruitment falls short or resources are limited.”
- “Write a justification for the selected sample size to share with stakeholders.”
- “Propose methods for balancing smaller sample sizes with actionable insights (e.g., triangulation, mixed methods).”
- “Identify any risks associated with the sample size and suggest ways to mitigate them.”
- “Draft a timeline and cost estimate for recruiting participants based on the recommended sample size.”