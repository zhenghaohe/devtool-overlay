```python
class Locale:
    def __init__(self, name, code):
        self.name = name
        self.code = code

class LocaleSelector:
    def __init__(self, locales):
        self.locales = locales
        self.current_locale = self.locales[0]

    def switch_locale(self, locale_code):
        for locale in self.locales:
            if locale.code == locale_code:
                self.current_locale = locale
                return True
        return False

    def filter_locales(self, filter_string):
        return [locale for locale in self.locales if filter_string in locale.name]

locales = [
    Locale("English", "en"),
    Locale("Spanish", "es"),
    Locale("French", "fr"),
    # Add more locales as needed
]

locale_selector = LocaleSelector(locales)
```