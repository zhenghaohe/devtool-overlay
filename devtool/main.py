```python
from devtool.config import configOptions
from devtool.views import switchView
from devtool.locales import switchLocale
from devtool.random_string_mode import toggleRandomStringMode
from devtool.external_css import applyStyleSheet
from devtool.button import mountOverlay
from devtool.move import moveFloatingButton

def main():
    # Initialize the floating button
    floatingButton = mountOverlay(configOptions)

    # Attach event listeners to the floating button
    floatingButton.on('click', lambda: moveFloatingButton(floatingButton))

    # Initialize the view buttons
    viewButtons = [button for button in floatingButton.find('#viewButtons')]
    for button in viewButtons:
        button.on('click', lambda: switchView(button.id))

    # Initialize the locale selector
    localeSelector = floatingButton.find('#localeSelector')
    localeSelector.on('change', lambda: switchLocale(localeSelector.value))

    # Initialize the random string mode button
    randomStringModeButton = floatingButton.find('#randomStringModeButton')
    randomStringModeButton.on('click', toggleRandomStringMode)

    # Initialize the style sheet selector
    styleSheetSelector = floatingButton.find('#styleSheetSelector')
    styleSheetSelector.on('change', lambda: applyStyleSheet(styleSheetSelector.value))

if __name__ == "__main__":
    main()
```