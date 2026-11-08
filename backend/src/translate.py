from deep_translator import GoogleTranslator

_LANGUAGES = GoogleTranslator().get_supported_languages(as_dict=True)
_LANGUAGE_CODES = {code.lower(): code for code in _LANGUAGES.values()}


def normalize_language(language: str) -> str:
    language = language.strip().lower()
    return _LANGUAGES.get(language, _LANGUAGE_CODES.get(language, language))


def translate_text(text: str, source_lang: str, target_lang: str) -> str:
    return GoogleTranslator(
        source=normalize_language(source_lang),
        target=normalize_language(target_lang),
    ).translate(text)
