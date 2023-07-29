```python
import random
import string

def generate_random_string(length=100):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def filter_locales(locales, query):
    """Filter locales based on a query"""
    return [locale for locale in locales if query.lower() in locale.lower()]

def add_style_sheet(style_sheets, name, url):
    """Add a new style sheet"""
    style_sheets.append({"name": name, "url": url})
    return style_sheets

def edit_style_sheet(style_sheets, name, new_url):
    """Edit an existing style sheet"""
    for style_sheet in style_sheets:
        if style_sheet["name"] == name:
            style_sheet["url"] = new_url
    return style_sheets
```