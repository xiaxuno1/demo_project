# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: ctk_1
# Author: xiaxu
# DATA: 2023/9/27
# Description:
# ---------------------------------------------------
import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x150")


        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callbck)
        self.button.pack(padx=20, pady=20)

    def button_callbck(self):
        print("button clicked")

app = App()
app.mainloop()