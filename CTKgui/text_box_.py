# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: text_box_
# Author: xiaxu
# DATA: 2023/9/28
# Description:
# ---------------------------------------------------
import customtkinter


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.textbox = customtkinter.CTkTextbox(master=self, width=400, corner_radius=0)
        self.textbox.grid(row=0, column=0, sticky="nsew")
        self.textbox.insert("0.0", "Some example text!\n" * 50)


app = App()
app.mainloop()