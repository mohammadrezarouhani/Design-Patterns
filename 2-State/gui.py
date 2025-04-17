import tkinter as tk
from abc import ABC, abstractmethod

# State Interface
class Tool(ABC):
    @abstractmethod
    def mouse_down(self, event, canvas):
        pass

    @abstractmethod
    def mouse_up(self, event, canvas):
        pass

# Concrete States
class BrushTool(Tool):
    def mouse_down(self, event, canvas):
        canvas.old_x, canvas.old_y = event.x, event.y

    def mouse_up(self, event, canvas):
        canvas.create_line(canvas.old_x, canvas.old_y, event.x, event.y, fill="black", width=3)
        canvas.old_x, canvas.old_y = None, None

class EraserTool(Tool):
    def mouse_down(self, event, canvas):
        canvas.old_x, canvas.old_y = event.x, event.y

    def mouse_up(self, event, canvas):
        canvas.create_line(canvas.old_x, canvas.old_y, event.x, event.y, fill="white", width=10)
        canvas.old_x, canvas.old_y = None, None

class SelectionTool(Tool):
    def mouse_down(self, event, canvas):
        print(f"Selected at ({event.x}, {event.y})")

    def mouse_up(self, event, canvas):
        print(f"Released at ({event.x}, {event.y})")

# Context (Canvas)
class DrawingCanvas(tk.Canvas):
    def __init__(self, root):
        super().__init__(root, width=600, height=400, bg="white")
        self.pack()
        self.old_x = None
        self.old_y = None
        self.tool = None  # Default tool

        self.bind("<ButtonPress-1>", self.mouse_down)
        self.bind("<ButtonRelease-1>", self.mouse_up)

    def set_tool(self, tool):
        self.tool = tool

    def mouse_down(self, event):
        if self.tool:
            self.tool.mouse_down(event, self)

    def mouse_up(self, event):
        if self.tool:
            self.tool.mouse_up(event, self)

# UI Controller
class DrawingApp:
    def __init__(self, root):
        self.canvas = DrawingCanvas(root)
        self.brush_tool = BrushTool()
        self.eraser_tool = EraserTool()
        self.selection_tool = SelectionTool()

        # Buttons
        self.btn_brush = tk.Button(root, text="Brush", command=lambda: self.canvas.set_tool(self.brush_tool))
        self.btn_brush.pack(side=tk.LEFT)

        self.btn_eraser = tk.Button(root, text="Eraser", command=lambda: self.canvas.set_tool(self.eraser_tool))
        self.btn_eraser.pack(side=tk.LEFT)

        self.btn_select = tk.Button(root, text="Selection", command=lambda: self.canvas.set_tool(self.selection_tool))
        self.btn_select.pack(side=tk.LEFT)

# Run Application
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Drawing App with State Pattern")
    app = DrawingApp(root)
    root.mainloop()
