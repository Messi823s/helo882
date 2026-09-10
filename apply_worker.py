import os

file_path = 'src/utils/telegram.ts'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the placeholder with the actual worker URL
content = content.replace(
    "API_URL: 'https://api.telegram.org' // Đổi thành link Cloudflare Worker của anh (VD: 'https://my-worker.abc.workers.dev')",
    "API_URL: 'https://lucky-term-a588.muenzenbergerzaborowski87.workers.dev'"
)

# Fallback just in case
content = content.replace(
    "API_URL: 'https://api.telegram.org'",
    "API_URL: 'https://lucky-term-a588.muenzenbergerzaborowski87.workers.dev'"
)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Worker URL applied successfully.")
