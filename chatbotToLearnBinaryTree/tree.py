import tkinter as tk
from tkinter import ttk

# TreeNode class represents a single node in the tree
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Function to insert a new node in the tree
def insert_node(root, parent_value, new_value, position):
    if root is None:
        return None
    
    if root.value == parent_value:
        new_node = TreeNode(new_value)
        if position == "left":
            if root.left is None:
                root.left = new_node
            else:
                print(f"Left node already exists under {root.value}")
        elif position == "right":
            if root.right is None:
                root.right = new_node
            else:
                print(f"Right node already exists under {root.value}")
        return root

    # Traverse through the tree to find the parent node
    if root.left:
        insert_node(root.left, parent_value, new_value, position)
    if root.right:
        insert_node(root.right, parent_value, new_value, position)
    
    return root

# Function to draw the tree recursively
def draw_tree(canvas, node, x, y, x_offset=100, y_offset=100):
    if node is None:
        return
    
    # Draw the current node
    canvas.create_oval(x-20, y-20, x+20, y+20, fill="lightblue")
    canvas.create_text(x, y, text=node.value, font=("Arial", 12))
    
    # Draw the left child if exists
    if node.left:
        canvas.create_line(x, y, x - x_offset, y + y_offset)
        draw_tree(canvas, node.left, x - x_offset, y + y_offset, x_offset, y_offset)
    
    # Draw the right child if exists
    if node.right:
        canvas.create_line(x, y, x + x_offset, y + y_offset)
        draw_tree(canvas, node.right, x + x_offset, y + y_offset, x_offset, y_offset)

# Function to handle inserting a left node with user input
def on_insert_left_button(canvas, root, parent_value_entry, new_value_entry):
    try:
        parent_value = int(parent_value_entry.get())  # Get parent value from entry
        new_value = int(new_value_entry.get())  # Get new node value from entry
        root = insert_node(root, parent_value, new_value, "left")
        canvas.delete("all")  # Clear the canvas
        draw_tree(canvas, root, 300, 100)  # Redraw the tree
    except ValueError:
        print("Invalid input. Please enter valid integers.")

# Function to handle inserting a right node with user input
def on_insert_right_button(canvas, root, parent_value_entry, new_value_entry):
    try:
        parent_value = int(parent_value_entry.get())  # Get parent value from entry
        new_value = int(new_value_entry.get())  # Get new node value from entry
        root = insert_node(root, parent_value, new_value, "right")
        canvas.delete("all")  # Clear the canvas
        draw_tree(canvas, root, 300, 100)  # Redraw the tree
    except ValueError:
        print("Invalid input. Please enter valid integers.")

def main():
    root_window = tk.Tk()
    root_window.title("Binary Tree Visualizer")
    root_window.geometry("800x600")
    
    # Create the root node (the root of the tree)
    root_node = TreeNode(1)  # Root node starts with value 1
    
    # Create a canvas for drawing the tree
    canvas = tk.Canvas(root_window, width=800, height=400)
    canvas.pack(pady=20)

    # Entry frame to hold input fields
    entry_frame = ttk.Frame(root_window)
    entry_frame.pack(pady=10)

    # Labels and entry fields for parent node and new node values
    ttk.Label(entry_frame, text="Parent Node Value:").grid(row=0, column=0, padx=5, pady=5)
    parent_value_entry = ttk.Entry(entry_frame)
    parent_value_entry.grid(row=0, column=1, padx=5, pady=5)
    
    ttk.Label(entry_frame, text="New Node Value:").grid(row=1, column=0, padx=5, pady=5)
    new_value_entry = ttk.Entry(entry_frame)
    new_value_entry.grid(row=1, column=1, padx=5, pady=5)

    # Button frame for inserting left or right nodes
    button_frame = ttk.Frame(root_window)
    button_frame.pack(pady=10)

    # Buttons to insert left or right nodes
    ttk.Button(button_frame, text="Insert Left Node", command=lambda: on_insert_left_button(canvas, root_node, parent_value_entry, new_value_entry)).grid(row=0, column=0, padx=10)
    ttk.Button(button_frame, text="Insert Right Node", command=lambda: on_insert_right_button(canvas, root_node, parent_value_entry, new_value_entry)).grid(row=0, column=1, padx=10)

    # Draw the initial tree
    draw_tree(canvas, root_node, 400, 50)

    # Start the Tkinter event loop
    root_window.mainloop()

if __name__ == "__main__":
    main()