import os
import re

routes = ['src/app/api/send/route.ts', 'src/app/api/edit/route.ts', 'src/app/api/delete/route.ts']
for r in routes:
    with open(r, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove bot token from url
    content = content.replace("`${TELEGRAM_CONFIG.API_URL}/bot${TELEGRAM_CONFIG.TOKEN}/", "`${TELEGRAM_CONFIG.API_URL}/")
    
    # Remove chat_id from payload interface and object
    content = re.sub(r'chat_id:\s*string;\n\s*', '', content)
    content = re.sub(r'chat_id:\s*TELEGRAM_CONFIG\.CHAT_ID,\n\s*', '', content)
    
    with open(r, 'w', encoding='utf-8') as f:
        f.write(content)

print("Vercel routes updated to remove Telegram Token and Chat ID.")
