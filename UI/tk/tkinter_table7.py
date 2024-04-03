import tkinter as tk
from tkinter import ttk

class TableApp:
    def __init__(self, root, data):
        self.root = root
        self.data = data

        self.setup_ui()

    def setup_ui(self):
        self.root.title("Table Display")

        # 创建 Notebook
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True)

        # 第一个 sheet
        frame1 = ttk.Frame(notebook)
        notebook.add(frame1, text="Sheet 1")
        self.create_table(frame1)

        # 第二个 sheet
        frame2 = ttk.Frame(notebook)
        notebook.add(frame2, text="Sheet 2")
        self.create_table(frame2)

    def create_table(self, parent):
        # 创建表格
        tree = ttk.Treeview(parent)
        tree["columns"] = tuple(self.data[0].keys())
        tree["show"] = "headings"

        for column in tree["columns"]:
            tree.heading(column, text=column)

        for item in self.data:
            values = [item[column] for column in tree["columns"]]
            tree.insert("", "end", values=values)

        # 创建纵向滚动条
        y_scrollbar = ttk.Scrollbar(parent, orient="vertical", command=tree.yview)
        y_scrollbar.pack(side="right", fill="y")

        # 绑定纵向滚动条到表格
        tree.configure(yscrollcommand=y_scrollbar.set)

        tree.pack(expand=True, fill="both")

def main():
    # 数据
    data = [
        {"Name": "Alice", "Age": 25, "Occupation": "Engineer"},
        {"Name": "Bob", "Age": 30, "Occupation": "Doctor"},
        {"Name": "Charlie", "Age": 35, "Occupation": "Artist"}
    ]

    # 创建窗口
    root = tk.Tk()

    # 启动应用
    app = TableApp(root, data)

    # 进入主循环
    root.mainloop()

if __name__ == "__main__":
    main()
