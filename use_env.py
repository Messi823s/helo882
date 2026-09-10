import os
import re

file_path = 'src/utils/telegram.ts'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the hardcoded URL with process.env
content = re.sub(r"API_URL:\s*'https://lucky-term-[a-zA-Z0-9.-]+\.workers\.dev'", "API_URL: process.env.TELEGRAM_API_URL", content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated telegram.ts to use process.env")
