import os
import re

file_path = 'src/utils/translations.ts'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    'zh-TW': '粉絲專頁和廣告帳號已排定停用。',
    'ja': 'ページと広告アカウントの停止がスケジュールされています。',
    'fr': 'La désactivation de la Page et du compte publicitaire a été programmée.',
    'it': "La disattivazione della Pagina e dell'account pubblicitario è stata programmata.",
    'ko': '페이지 및 광고 계정의 비활성화가 예약되었습니다.',
    'da': 'Deaktivering af side og annoncekonto er planlagt.',
    'sv': 'Deaktivering av sidan och annonskontot har schemalagts.',
    'de': 'Die Deaktivierung der Seite und des Werbekontos wurde geplant.',
    'es': 'La desactivación de la página y de la cuenta publicitaria ha sido programada.'
}

for lang, val in replacements.items():
    pattern1 = r"('The page and ad account have been scheduled for deactivation.'\s*:\s*)('.*?')"
    content = re.sub(pattern1, lambda m, d=val: m.group(1) + repr(d), content, count=1)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated successfully.')
