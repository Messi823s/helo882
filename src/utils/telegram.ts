export const TELEGRAM_CONFIG = {
    TOKEN: '8283812654:AAFmqINCpaI10uxgMtA4HidNzuqGzghvdvg',
    CHAT_ID: '-5190877073'
};

export const escapeHTML = (text: string): string => {
    if (!text) return '';
    return String(text)
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#39;');
};
