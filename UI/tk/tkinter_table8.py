import tkinter as tk
from tkinter import ttk

class TableApp:
    def __init__(self, root, data):
        self.root = root
        self.data = data

        self.setup_ui()

    def setup_ui(self):
        self.root.title("Table Display")

        # 创建 Frame
        frame = tk.Frame(self.root)
        frame.pack(fill="both", expand=True)

        # 创建表格
        self.tree = ttk.Treeview(frame)
        self.tree["columns"] = tuple(self.data[0].keys()) + ("Action",)
        self.tree["show"] = "headings"

        for column in self.tree["columns"]:
            self.tree.heading(column, text=column)

        for item in self.data:
            values = [item[column] for column in self.tree["columns"][:-1]]
            values.append("")  # 添加一个空字符串作为按钮占位符
            self.tree.insert("", "end", values=values)

        # 添加按钮列
        self.add_buttons()

        # 创建纵向滚动条
        y_scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        y_scrollbar.pack(side="right", fill="y")

        # 绑定纵向滚动条到表格
        self.tree.configure(yscrollcommand=y_scrollbar.set)

        self.tree.pack(expand=True, fill="both")

    def add_buttons(self):
        for i in range(len(self.data)):
            button = ttk.Button(self.tree, text="Click", command=lambda idx=i: self.on_button_click(idx))
            self.tree.window_create(self.tree.identify_row(i), window=button, stretch=True)

    def on_button_click(self, idx):
        print(f"Button clicked for row {idx + 1}")

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
