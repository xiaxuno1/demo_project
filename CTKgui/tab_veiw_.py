# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: tab_veiw_
# Author: xiaxu
# DATA: 2023/9/28
# Description:
# ---------------------------------------------------
import customtkinter


class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.add("tab 1")
        self.add("tab 2")

        # add widgets on tabs
        self.label = customtkinter.CTkLabel(master=self.tab("tab 1"))
        self.label.grid(row=0, column=0, padx=20, pady=10)
        self.label = customtkinter.CTkLabel(master=self.tab("tab 1"))
        self.label.grid(row=0, column=0, padx=20, pady=10)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.tab_view = MyTabView(master=self)
        self.tab_view.grid(row=0, column=0, padx=20, pady=20)


app = App()
app.mainloop()