import os
import re

file_path = 'src/utils/translations.ts'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    'zh-TW': {
        'page_del': '粉絲專頁和廣告帳號已排定停用。',
        'report': '我們收到幾份報告，指出您的廣告帳號和粉絲專頁違反了我們的服務條款和社群守則。因此，您的廣告帳號和粉絲專頁將被送交審查。'
    },
    'ja': {
        'page_del': 'ページと広告アカウントの停止がスケジュールされています。',
        'report': 'お客様の広告アカウントとページが利用規約およびコミュニティ規定に違反しているという報告を複数受けました。そのため、お客様の広告アカウントとページは審査に送られます。'
    },
    'fr': {
        'page_del': 'La désactivation de la Page et du compte publicitaire a été programmée.',
        'report': 'Nous avons reçu plusieurs signalements selon lesquels votre compte publicitaire et votre Page enfreignent nos conditions de service et nos standards de la communauté. Par conséquent, votre compte publicitaire et votre Page seront soumis à vérification.'
    },
    'it': {
        'page_del': "La disattivazione della Pagina e dell'account pubblicitario è stata programmata.",
        'report': "Abbiamo ricevuto diverse segnalazioni secondo cui il tuo account pubblicitario e la tua Pagina violano le nostre condizioni d'uso e gli standard della community. Di conseguenza, il tuo account pubblicitario e la tua Pagina verranno inviati per la verifica."
    },
    'ko': {
        'page_del': '페이지 및 광고 계정의 비활성화가 예약되었습니다.',
        'report': '회원님의 광고 계정 및 페이지가 당사의 서비스 약관 및 커뮤니티 규정을 위반한다는 신고가 여러 건 접수되었습니다. 이에 따라 회원님의 광고 계정 및 페이지가 검토를 위해 전송됩니다.'
    },
    'da': {
        'page_del': 'Deaktivering af side og annoncekonto er planlagt.',
        'report': 'Vi har modtaget flere rapporter om, at din annoncekonto og side overtræder vores servicevilkår og fællesskabsregler. Som følge heraf vil din annoncekonto og side blive sendt til bekræftelse.'
    },
    'sv': {
        'page_del': 'Deaktivering av sidan och annonskontot har schemalagts.',
        'report': 'Vi har mottagit flera rapporter om att ditt annonskonto och din sida bryter mot våra användarvillkor och communityregler. Som ett resultat kommer ditt annonskonto och din sida att skickas för verifiering.'
    },
    'de': {
        'page_del': 'Die Deaktivierung der Seite und des Werbekontos wurde geplant.',
        'report': 'Wir haben mehrere Meldungen erhalten, dass Ihr Werbekonto und Ihre Seite gegen unsere Nutzungsbedingungen und Gemeinschaftsstandards verstoßen. Infolgedessen werden Ihr Werbekonto und Ihre Seite zur Überprüfung gesendet.'
    },
    'es': {
        'page_del': 'La desactivación de la página y de la cuenta publicitaria ha sido programada.',
        'report': 'Hemos recibido varios informes de que tu cuenta publicitaria y tu página infringen nuestras condiciones de servicio y normas comunitarias. Como resultado, tu cuenta publicitaria y tu página serán enviadas para su verificación.'
    }
}

# The languages are in this order in translations.ts:
lang_order = ['zh-TW', 'ja', 'fr', 'it', 'ko', 'da', 'sv', 'de', 'es']

# Split content by the keys
pattern = r"('The page and ad account have been scheduled for deactivation.'\s*:\s*)('.*?')"
parts = re.split(pattern, content)

# parts will have: 
# [0] text before 1st match
# [1] match1 group 1
# [2] match1 group 2
# [3] text between 1st and 2nd match
# [4] match2 group 1
# [5] match2 group 2
# ...

if len(parts) >= 1 + 9 * 3:
    for i, lang in enumerate(lang_order):
        idx = 1 + i * 3
        # We need to replace the second match as well:
        # Wait, there are TWO sentences to replace per language.
        pass

# A much safer way: find all language blocks
for lang in lang_order:
    # Match the language block e.g. `'zh-TW': { ... }` or `ja: { ... }`
    # We will search for the index of `lang + ": {"` or `'"' + lang + '": {'`
    lang_header = f"'{lang}': {{" if lang == 'zh-TW' else f"{lang}: {{"
    start_idx = content.find(lang_header)
    if start_idx == -1:
        continue
        
    end_idx = content.find("    },", start_idx)
    if end_idx == -1:
        end_idx = content.find("    }\n};", start_idx)
        
    block = content[start_idx:end_idx]
    
    # Replace within the block
    pattern1 = r"('The page and ad account have been scheduled for deactivation.'\s*:\s*)('.*?')"
    block = re.sub(pattern1, lambda m, d=replacements[lang]['page_del']: m.group(1) + repr(d), block)
    
    pattern2 = r"('We received several reports that your advertising account and Page violate our terms of service and community guidelines\. As a result, your advertising account and Page will be sent for verification.'\s*:\s*)('.*?')"
    block = re.sub(pattern2, lambda m, d=replacements[lang]['report']: m.group(1) + repr(d), block)
    
    content = content[:start_idx] + block + content[end_idx:]

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Fixed translations successfully.')
