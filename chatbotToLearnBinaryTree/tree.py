from tkinter import Tk, Canvas, ttk

# Global variables for tree visualization
node_radius = 20
canvas_width = 600
canvas_height = 400

# Store the tree structure as a dictionary for visualization
binary_tree = {"root": None}

def reinitialize(canvas):
    """Clear and reset the canvas."""
    canvas.delete("all")
    binary_tree["root"] = None

def insert_node_to_left(canvas):
    """Insert a node to the left of the root if it doesn't exist."""
    if binary_tree["root"] is None:
        binary_tree["root"] = "Root"
        draw_node(canvas, canvas_width // 2, 50, "Root")
    else:
        # Add a left child node and visualize
        draw_node(canvas, canvas_width // 3, 150, "Left")

def insert_node_to_right(canvas):
    """Insert a node to the right of the root if it doesn't exist."""
    if binary_tree["root"] is None:
        binary_tree["root"] = "Root"
        draw_node(canvas, canvas_width // 2, 50, "Root")
    else:
        # Add a right child node and visualize
        draw_node(canvas, 2 * canvas_width // 3, 150, "Right")

def draw_node(canvas, x, y, text):
    """Draw a circular node with text on the canvas."""
    canvas.create_oval(
        x - node_radius, y - node_radius, 
        x + node_radius, y + node_radius, 
        fill="lightblue"
    )
    canvas.create_text(x, y, text, font=("Arial", 12))

def main():
    root = Tk()
    root.title("Binary Tree Visualizer")

    # Canvas for drawing the tree
    canvas = Canvas(root, width=canvas_width, height=canvas_height, bg="white")
    canvas.pack()

    # Buttons for operations
    button_frame = ttk.Frame(root)
    button_frame.pack()

    ttk.Button(button_frame, text="Clear & Reinitialize", command=lambda: reinitialize(canvas)).grid(row=0, column=0)
    ttk.Button(button_frame, text="Insert Left Node", command=lambda: insert_node_to_left(canvas)).grid(row=0, column=1)
    ttk.Button(button_frame, text="Insert Right Node", command=lambda: insert_node_to_right(canvas)).grid(row=0, column=2)

    root.mainloop()


if __name__ == "__main__":
    main()