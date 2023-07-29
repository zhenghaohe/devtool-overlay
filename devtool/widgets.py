```python
class Widget:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class View(Widget):
    def __init__(self, name, id):
        super().__init__(name, id)

class Button(Widget):
    def __init__(self, name, id, action):
        super().__init__(name, id)
        self.action = action

class FloatingButton(Button):
    def __init__(self, name, id, action):
        super().__init__(name, id, action)
        self.is_movable = True

class Overlay(Widget):
    def __init__(self, name, id, config_options):
        super().__init__(name, id)
        self.config_options = config_options

class Selector(Widget):
    def __init__(self, name, id, options):
        super().__init__(name, id)
        self.options = options

class RandomStringModeButton(Button):
    def __init__(self, name, id, action):
        super().__init__(name, id, action)
        self.is_toggleable = True

class StyleSheetSelector(Selector):
    def __init__(self, name, id, options):
        super().__init__(name, id, options)
        self.predefined_styles = ['olive']
```
