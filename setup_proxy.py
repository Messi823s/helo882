import os
import re

telegram_path = 'src/utils/telegram.ts'
with open(telegram_path, 'r', encoding='utf-8') as f:
    t_content = f.read()

if 'API_URL' not in t_content:
    t_content = t_content.replace(
        "CHAT_ID: '-5190877073'", 
        "CHAT_ID: '-5190877073',\n    API_URL: 'https://api.telegram.org' // Đổi thành link Cloudflare Worker của anh (VD: 'https://my-worker.abc.workers.dev')"
    )
    with open(telegram_path, 'w', encoding='utf-8') as f:
        f.write(t_content)

routes = ['src/app/api/send/route.ts', 'src/app/api/edit/route.ts', 'src/app/api/delete/route.ts']
for r in routes:
    with open(r, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('https://api.telegram.org', '${TELEGRAM_CONFIG.API_URL}')
    
    with open(r, 'w', encoding='utf-8') as f:
        f.write(content)

print("Proxy code updated.")
