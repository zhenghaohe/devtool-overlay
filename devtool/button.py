```python
import tkinter as tk
from .overlay import mountOverlay
from .move import moveFloatingButton

class FloatingButton:
    def __init__(self, root):
        self.root = root
        self.button = tk.Button(root, text="DevTool", command=self.openOverlay)
        self.button.pack()

    def openOverlay(self):
        mountOverlay(self.root)

    def moveButton(self, event):
        moveFloatingButton(self.button, event)

def createFloatingButton(root):
    button = FloatingButton(root)
    root.bind("<B1-Motion>", button.moveButton)
    return button
```