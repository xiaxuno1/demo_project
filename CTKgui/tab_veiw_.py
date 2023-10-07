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
        self.label = customtkinter.CTkLabel(master=self.tab("tab 1"),text='hello,tab1')
        self.label.grid(row=0, column=0, padx=20, pady=10)
        self.labe2 = customtkinter.CTkLabel(master=self.tab("tab 2"),text='hello,tab2')
        self.labe3 = customtkinter.CTkLabel(master=self.tab("tab 2"), text='helloo,tab2')
        self.labe2.grid(row=5, column=7, padx=20, pady=10)
        self.labe3.grid(row=1, column=7, padx=20, pady=10)

        # create CTk scrollbar,sticky为方向：ns:从呗到南
        self.ctk_textbox_scrollbar = customtkinter.CTkScrollbar(self.tab('tab 1'))
        self.ctk_textbox_scrollbar.grid(row=0, column=1, sticky="sn")



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.tab_view = MyTabView(master=self)
        self.tab_view.grid(row=0, column=0, padx=20, pady=20)


app = App()
app.mainloop()