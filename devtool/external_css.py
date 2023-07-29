```python
from devtool.utils import send_message
from devtool.stylesheets import StyleSheet

styleSheets = []

def applyStyleSheet(name):
    for sheet in styleSheets:
        if sheet.name == name:
            send_message('applyStyleSheet', sheet.url)
            return
    print(f"No stylesheet found with name {name}")

def addStyleSheet(name, url):
    new_sheet = StyleSheet(name, url)
    styleSheets.append(new_sheet)

def editStyleSheet(name, new_url):
    for sheet in styleSheets:
        if sheet.name == name:
            sheet.url = new_url
            return
    print(f"No stylesheet found with name {name}")

# Predefined style sheet
addStyleSheet('olive', 'https://example.com/olive.css')
```