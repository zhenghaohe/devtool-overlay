```python
class View:
    def __init__(self, name, widget):
        self.name = name
        self.widget = widget

views = [
    View('View1', 'Widget1'),
    View('View2', 'Widget2'),
    View('View3', 'Widget3'),
    # Add more views as needed
]

currentView = views[0]

def switchView(viewName):
    global currentView
    for view in views:
        if view.name == viewName:
            currentView = view
            break

def getViewButtons():
    return [view.name for view in views]
```