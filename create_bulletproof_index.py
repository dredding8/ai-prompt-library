import os

files = [f for f in os.listdir('.') if f.endswith('.md') and f != 'index.md']
files.sort()

print(f'''<!DOCTYPE html>
<html>
<head>
    <title>AI Prompt Library</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, sans-serif; max-width: 900px; margin: 0 auto; padding: 20px; line-height: 1.6; }}
        h1 {{ color: #333; border-bottom: 3px solid #667eea; padding-bottom: 10px; }}
        .stats {{ background: #f8f9fa; padding: 15px; border-radius: 8px; margin: 20px 0; }}
        .all-prompts {{ columns: 2; column-gap: 40px; }}
        .all-prompts li {{ margin: 8px 0; break-inside: avoid; }}
        a {{ color: #0066cc; text-decoration: none; }}
        a:hover {{ text-decoration: underline; }}
        @media (max-width: 768px) {{ .all-prompts {{ columns: 1; }} }}
    </style>
</head>
<body>
    <h1>🚀 AI Prompt Library</h1>
    
    <div class="stats">
        <strong>{len(files)} prompts</strong> for user researchers and product managers.<br>
        Click any prompt to view the template. Copy/paste into ChatGPT, Claude, etc.
    </div>
    
    <div class="all-prompts">
        <ul>''')

for file in files:
    # Convert filename to readable title
    title = file.replace('.md', '').replace('-', ' ').title()
    # Fix common title issues
    title = title.replace(' And ', ' and ').replace(' To ', ' to ').replace(' For ', ' for ')
    title = title.replace(' A ', ' a ').replace(' The ', ' the ').replace(' Of ', ' of ')
    title = title.replace(' With ', ' with ').replace(' Or ', ' or ').replace(' In ', ' in ')
    
    print(f'            <li><a href="{file}">{title}</a></li>')

print(f'''        </ul>
    </div>
    
    <p style="margin-top: 40px; text-align: center; color: #666;">
        <a href="https://github.com/dredding8/ai-prompt-library">View on GitHub</a>
    </p>
</body>
</html>''')
