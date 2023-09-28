# --------------------------------------------------
# coding=utf8
# !/usr/bin/python
# PN: test_tool
# FN: scroll_bar_
# Author: xiaxu
# DATA: 2023/9/28
# Description:
# ---------------------------------------------------
import customtkinter


app = customtkinter.CTk()
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)

# create scrollable textbox
tk_textbox = customtkinter.CTkTextbox(app, activate_scrollbars=False)
tk_textbox.grid(row=0, column=0, sticky="nsew")

# create CTk scrollbar,sticky为方向：ns:从呗到南
ctk_textbox_scrollbar = customtkinter.CTkScrollbar(app, command=tk_textbox.yview)
ctk_textbox_scrollbar.grid(row=0, column=1, sticky="sn")

def segmented_button_callback(value):
    print("segmented button clicked:", value)

#段button
segemented_button_var = customtkinter.StringVar(value="Value 1")
segemented_button = customtkinter.CTkSegmentedButton(app, values=["Value 1", "Value 2", "Value 3"],
                                                     command=segmented_button_callback,
                                                     variable=segemented_button_var)
segemented_button.grid(row=1, column=1, sticky="sn")
# connect textbox scroll event to CTk scrollbar
tk_textbox.configure(yscrollcommand=ctk_textbox_scrollbar.set)

def slider_event(value):
    print(value)
#滑动条
slider = customtkinter.CTkSlider(app, from_=0, to=100, command=slider_event)
slider.grid(row=2, column=1, sticky="sn")

def switch_event():
    print("switch toggled, current value:", switch_var.get())

#开关
switch_var = customtkinter.StringVar(value="on")
switch = customtkinter.CTkSwitch(app, text="CTkSwitch", command=switch_event,
                                 variable=switch_var, onvalue="on", offvalue="off")
switch.grid(row=3, column=1, sticky="sn")


app.mainloop()