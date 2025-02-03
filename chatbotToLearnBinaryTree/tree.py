import tkinter as tk
from tkinter import ttk

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTreeVisualizer:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def insert(self, parent_value, new_value, position):
        parent_node = self.find(self.root, parent_value)
        if parent_node:
            new_node = TreeNode(new_value)
            if position == "left":
                if not parent_node.left:
                    parent_node.left = new_node
                else:
                    print(f"Left node already exists under {parent_node.value}")
            elif position == "right":
                if not parent_node.right:
                    parent_node.right = new_node
                else:
                    print(f"Right node already exists under {parent_node.value}")
        else:
            print(f"Parent node with value {parent_value} not found.")

    def find(self, node, value):
        if node is None:
            return None
        if node.value == value:
            return node
        return self.find(node.left, value) or self.find(node.right, value)

    def draw_tree(self, canvas, node, x, y, x_offset=100, y_offset=100):
        if node is None:
            return
        # Draw the node
        canvas.create_oval(x-20, y-20, x+20, y+20, fill="lightblue")
        canvas.create_text(x, y, text=str(node.value), font=("Arial", 12))

        # Draw the left child
        if node.left:
            canvas.create_line(x, y, x - x_offset, y + y_offset)
            self.draw_tree(canvas, node.left, x - x_offset, y + y_offset, x_offset, y_offset)

        # Draw the right child
        if node.right:
            canvas.create_line(x, y, x + x_offset, y + y_offset)
            self.draw_tree(canvas, node.right, x + x_offset, y + y_offset, x_offset, y_offset)

class BinaryTreeApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Binary Tree Visualizer")
        self.master.geometry("800x600")

        # Create the binary tree visualizer instance
        self.tree = BinaryTreeVisualizer(1)

        # Canvas to draw the tree
        self.canvas = tk.Canvas(self.master, width=800, height=400)
        self.canvas.pack(pady=20)

        # Entry Frame for taking inputs
        self.entry_frame = ttk.Frame(self.master)
        self.entry_frame.pack(pady=10)

        ttk.Label(self.entry_frame, text="Parent Node Value:").grid(row=0, column=0, padx=5, pady=5)
        self.parent_value_entry = ttk.Entry(self.entry_frame)
        self.parent_value_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.entry_frame, text="New Node Value:").grid(row=1, column=0, padx=5, pady=5)
        self.new_value_entry = ttk.Entry(self.entry_frame)
        self.new_value_entry.grid(row=1, column=1, padx=5, pady=5)

        # Left/Right buttons to insert nodes
        self.button_frame = ttk.Frame(self.master)
        self.button_frame.pack(pady=10)

        ttk.Button(self.button_frame, text="Insert Left Node", command=self.insert_left).grid(row=0, column=0, padx=10)
        ttk.Button(self.button_frame, text="Insert Right Node", command=self.insert_right).grid(row=0, column=1, padx=10)

        # Draw the initial tree
        self.tree.draw_tree(self.canvas, self.tree.root, 400, 50)

    def insert_left(self):
        self.insert_node("left")

    def insert_right(self):
        self.insert_node("right")

    def insert_node(self, position):
        try:
            parent_value = int(self.parent_value_entry.get())
            new_value = int(self.new_value_entry.get())
            self.tree.insert(parent_value, new_value, position)
            self.canvas.delete("all")  # Clear the canvas
            self.tree.draw_tree(self.canvas, self.tree.root, 400, 50)  # Redraw the tree
        except ValueError:
            print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    root_window = tk.Tk()
    app = BinaryTreeApp(root_window)
    root_window.mainloop()