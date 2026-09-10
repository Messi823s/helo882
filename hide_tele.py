import os

file_path = 'src/utils/telegram.ts'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("'8283812654:AAFmqINCpaI10uxgMtA4HidNzuqGzghvdvg'", "'HIDDEN_IN_CLOUDFLARE'")
content = content.replace("'-5190877073'", "'HIDDEN_IN_CLOUDFLARE'")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Telegram config hidden.")
