import os

# Get all md files except index.md
files = [f for f in os.listdir('.') if f.endswith('.md') and f != 'index.md']
files.sort()

print("# AI Prompt Library")
print()
print("A comprehensive collection of prompts for user researchers and product managers.")
print()
print("## All Prompts")
print()

for file in files:
    title = file.replace('.md', '').replace('-', ' ').title()
    print(f"- [{title}]({file})")

print()
print("---")
print()
print(f"**Total: {len(files)} prompts**")
print()
print("**Repository:** [View on GitHub](https://github.com/dredding8/ai-prompt-library)")
