import '../css/LangSelect.css'

export const LANGUAGES = [
    { code: 'en', label: 'English' },
    { code: 'es', label: 'Español' },
    { code: 'zh-CN', label: '中文 (简体)' },
    { code: 'hi', label: 'हिन्दी' },
    { code: 'ar', label: 'العربية' },
    { code: 'fr', label: 'Français' },
    { code: 'bn', label: 'বাংলা' },
    { code: 'pt', label: 'Português' },
    { code: 'ja', label: '日本語' },
];

export function getInitialLanguage() {
    try {
        const saved = localStorage.getItem('lang');
        if (saved && LANGUAGES.some((l) => l.code === saved)) return saved;
    } catch {}

    const nav = navigator.language || 'en';
    const exact = LANGUAGES.find((l) => l.code.toLowerCase() === nav.toLowerCase());
    const base = LANGUAGES.find((l) => l.code.split('-')[0] === nav.slice(0, 2).toLowerCase());
    return (exact || base)?.code || 'en';
}

function LangSelect({value, onChange}) {
    function handleChange(e) {
        const code = e.target.value;
        try { localStorage.setItem('lang', code); } catch {}
        onChange(code);
    }

    return (
        <label className="language-select">
            <span>Language: </span>
            <select value={value} onChange={handleChange}>
                {LANGUAGES.map((l) => (
                    <option key={l.code} value={l.code}>{l.label}</option>
                ))}
            </select>
        </label>
    );
    
}
export default LangSelect;