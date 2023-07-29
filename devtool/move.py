```python
import tkinter as tk

def moveFloatingButton(event):
    global floatingButton
    floatingButton.place(x=event.x_root, y=event.y_root)

root = tk.Tk()
floatingButton = tk.Button(root, text="Config", command=mountOverlay)
floatingButton.pack()

floatingButton.bind('<B1-Motion>', moveFloatingButton)

root.mainloop()
```