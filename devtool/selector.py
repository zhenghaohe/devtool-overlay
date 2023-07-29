```python
import tkinter as tk
from .locales import locales
from .utils import send_message
from .config import configOptions, currentLocale, randomStringMode

class LocaleSelector:
    def __init__(self, parent):
        self.parent = parent
        self.selector = tk.OptionMenu(self.parent, currentLocale, *locales)
        self.selector.pack()

    def update_options(self):
        self.selector['menu'].delete(0, 'end')
        for locale in locales:
            self.selector['menu'].add_command(label=locale, command=tk._setit(currentLocale, locale, self.on_select))

    def on_select(self, *args):
        if not randomStringMode.get():
            send_message('switchLocale', currentLocale.get())
            configOptions['locale'] = currentLocale.get()

    def disable(self):
        self.selector.configure(state='disabled')

    def enable(self):
        self.selector.configure(state='normal')

class RandomStringModeButton:
    def __init__(self, parent):
        self.parent = parent
        self.button = tk.Button(self.parent, text="Random Long String Mode", command=self.on_click)
        self.button.pack()

    def on_click(self):
        randomStringMode.set(not randomStringMode.get())
        send_message('toggleRandomStringMode', randomStringMode.get())
        if randomStringMode.get():
            self.parent.disable()
        else:
            self.parent.enable()
```