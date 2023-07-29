```python
from devtool.utils import StyleSheet

styleSheets = []

def addStyleSheet(name, url):
    global styleSheets
    newStyleSheet = StyleSheet(name, url)
    styleSheets.append(newStyleSheet)

def editStyleSheet(name, newUrl):
    global styleSheets
    for sheet in styleSheets:
        if sheet.name == name:
            sheet.url = newUrl
            break

def applyStyleSheet(name):
    global styleSheets
    for sheet in styleSheets:
        if sheet.name == name:
            # Here you should implement the logic to apply the style sheet to your application
            # This is highly dependent on your application and can't be generically implemented
            pass
```