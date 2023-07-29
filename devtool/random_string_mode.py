```python
import random
import string

def toggle_random_string_mode():
    global randomStringMode
    randomStringMode = not randomStringMode

    if randomStringMode:
        disable_locale_selector()
        override_ui_with_random_strings()
    else:
        enable_locale_selector()

def disable_locale_selector():
    localeSelector.disabled = True

def enable_locale_selector():
    localeSelector.disabled = False

def override_ui_with_random_strings():
    for element in document.body.getElementsByTagName('*'):
        if element.hasChildNodes():
            for child in element.childNodes:
                if child.nodeType == Node.TEXT_NODE:
                    child.nodeValue = generate_random_string()

def generate_random_string():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(100))
```