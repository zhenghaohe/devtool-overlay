```python
class StyleSheet:
    def __init__(self, name, url):
        self.name = name
        self.url = url

styleSheets = [StyleSheet('olive', 'http://example.com/olive.css')]

def applyStyleSheet(name):
    for sheet in styleSheets:
        if sheet.name == name:
            # This is a placeholder. Replace with actual code to apply the style sheet.
            print(f"Applying style sheet: {sheet.url}")

def addStyleSheet(name, url):
    styleSheets.append(StyleSheet(name, url))
    print(f"Added style sheet: {name}")

def editStyleSheet(name, new_url):
    for sheet in styleSheets:
        if sheet.name == name:
            sheet.url = new_url
            print(f"Edited style sheet: {name}")
```