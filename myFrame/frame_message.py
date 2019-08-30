import tkinter as tk


# 底部显示信息
class FrameMessage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        bg_color = "AliceBlue"
        self.str_message = tk.StringVar()
        self.str_message.set("请输入长宽")
        self.label_message = tk.Label(master, bg=bg_color, textvariable=self.str_message)
        self.label_message.pack(fill=tk.X)
