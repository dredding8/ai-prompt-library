# Create Job Stories

Prompt: Act as an experienced product manager for a <product>.

Create a set of similar job stories for <a new feature> based on the attached design and <key assumptions>. Focus on expressing the user’s situation, motivation, and the outcome they wish to achieve.

When writing job stories:
• Use the format: “When [situation], I want to [motivation], so I can [outcome].”
• Keep language so simple that a primary school graduate can understand.
• Ensure each job story clearly reflects how the feature helps the user accomplish a specific goal.

——

An example Job Story:

Title: Track Weekly Snack Spending

Description: When I’m preparing my weekly allowance for snacks (situation), I want to quickly see how much I’ve spent so far (motivation), so I can make sure I don’t run out of money before the weekend (outcome).

Design: [Figma link]
[Optional business rules and details that can’t be expressed in the acceptance criteria]

Acceptance criteria:
1. Display Spending Summary:
• A "Weekly Spending Overview" section is shown prominently on the homepage or spending dashboard.
• The section is visible only to users with at least one recorded expense for the week.
2. Real-Time Update:
• The total spending amount updates in real-time whenever a new expense is logged.
3. Progress Indicator:
• A progress bar or similar visual indicator shows the percentage of the weekly budget spent.
4. Remaining Budget Highlight:
• The remaining budget is displayed in a prominent and readable format (e.g., "$12 remaining for the week").
5. Detailed Spending Log:
• Users can click on the spending summary to access a detailed log, showing:
    ◦ A breakdown of individual snack expenses.
    ◦ The time and date of each purchase.
6. Notifications:
• If the spending exceeds 80% of the weekly allowance, a notification is displayed (e.g., "You’re close to your weekly budget limit!").
7. Weekend-Specific Reminder:
• If the weekly spending exceeds 90% by Thursday, a reminder is triggered: "Plan your snacks wisely to make it through the weekend!"
8. Access and Navigation:
• Clicking on a specific snack item from the log navigates the user to a detailed breakdown or associated category.
Category: Execution
Comment: More: https://www.productcompass.pm/p/how-to-write-user-stories