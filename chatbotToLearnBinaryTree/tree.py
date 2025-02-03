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

# Function to handle inserting a left node
def on_insert_left_button(canvas, root):
    parent_value = "Root"  # Example: could be taken from an input field
    new_value = "Left"  # New node value from input
    root = insert_node(root, parent_value, new_value, "left")
    canvas.delete("all")  # Clear the canvas
    draw_tree(canvas, root, 300, 100)  # Redraw the tree

# Function to handle inserting a right node
def on_insert_right_button(canvas, root):
    parent_value = "Root"  # Example: could be taken from an input field
    new_value = "Right"  # New node value from input
    root = insert_node(root, parent_value, new_value, "right")
    canvas.delete("all")  # Clear the canvas
    draw_tree(canvas, root, 300, 100)  # Redraw the tree

def main():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=600, height=400)
    canvas.pack()

    # Create the root node
    root_node = TreeNode("Root")
    
    # Button to insert nodes
    button_frame = ttk.Frame(root)
    button_frame.pack()
    
    ttk.Button(button_frame, text="Insert Left Node", command=lambda: on_insert_left_button(canvas, root_node)).grid(row=0, column=0)
    ttk.Button(button_frame, text="Insert Right Node", command=lambda: on_insert_right_button(canvas, root_node)).grid(row=0, column=1)

    # Draw the initial tree
    draw_tree(canvas, root_node, 300, 100)
    
    root.mainloop()

if __name__ == "__main__":
    main()