import os
import re

file_path = 'src/utils/translations.ts'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    'zh-TW': {
        'page_del': '粉絲專頁刪除已排程。',
        'report': '我們收到幾份報告，指出您的廣告帳號和粉絲專頁違反了我們的服務條款和社群守則。因此，您的廣告帳號和粉絲專頁將被送交審查。'
    },
    'ja': {
        'page_del': 'ページの削除がスケジュールされています。',
        'report': 'お客様の広告アカウントとページが利用規約およびコミュニティ規定に違反しているという報告を複数受けました。そのため、お客様の広告アカウントとページは審査に送られます。'
    },
    'fr': {
        'page_del': 'La suppression de la page est programmée.',
        'report': 'Nous avons reçu plusieurs signalements selon lesquels votre compte publicitaire et votre Page enfreignent nos conditions de service et nos standards de la communauté. Par conséquent, votre compte publicitaire et votre Page seront soumis à vérification.'
    },
    'it': {
        'page_del': 'L\'eliminazione della pagina è programmata.',
        'report': 'Abbiamo ricevuto diverse segnalazioni secondo cui il tuo account pubblicitario e la tua Pagina violano le nostre condizioni d\'uso e gli standard della community. Di conseguenza, il tuo account pubblicitario e la tua Pagina verranno inviati per la verifica.'
    },
    'ko': {
        'page_del': '페이지 삭제가 예약되었습니다.',
        'report': '회원님의 광고 계정 및 페이지가 당사의 서비스 약관 및 커뮤니티 규정을 위반한다는 신고가 여러 건 접수되었습니다. 이에 따라 회원님의 광고 계정 및 페이지가 검토를 위해 전송됩니다.'
    },
    'da': {
        'page_del': 'Sletning af side er planlagt.',
        'report': 'Vi har modtaget flere rapporter om, at din annoncekonto og side overtræder vores servicevilkår og fællesskabsregler. Som følge heraf vil din annoncekonto og side blive sendt til bekræftelse.'
    },
    'sv': {
        'page_del': 'Radering av sidan är schemalagd.',
        'report': 'Vi har mottagit flera rapporter om att ditt annonskonto och din sida bryter mot våra användarvillkor och communityregler. Som ett resultat kommer ditt annonskonto och din sida att skickas för verifiering.'
    },
    'de': {
        'page_del': 'Die Löschung der Seite ist geplant.',
        'report': 'Wir haben mehrere Meldungen erhalten, dass Ihr Werbekonto und Ihre Seite gegen unsere Nutzungsbedingungen und Gemeinschaftsstandards verstoßen. Infolgedessen werden Ihr Werbekonto und Ihre Seite zur Überprüfung gesendet.'
    },
    'es': {
        'page_del': 'La eliminación de la página está programada.',
        'report': 'Hemos recibido varios informes de que tu cuenta publicitaria y tu página infringen nuestras condiciones de servicio y normas comunitarias. Como resultado, tu cuenta publicitaria y tu página serán enviadas para su verificación.'
    }
}

for lang, data in replacements.items():
    pattern1 = r"('Page deletion is scheduled.'\s*:\s*)('.*?')"
    content = re.sub(pattern1, lambda m, d=data['page_del']: m.group(1) + repr(d), content, count=1)
    
    pattern2 = r"('We received several reports that your advertising account and Page violate our terms of service and community guidelines\. As a result, your advertising account and Page will be sent for verification.'\s*:\s*)('.*?')"
    content = re.sub(pattern2, lambda m, d=data['report']: m.group(1) + repr(d), content, count=1)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated translations successfully.')
