import tkinter as tk


# 结果显示信息
class FrameShow(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        bg_color = "CornFlowerBlue"
        self.str_show = tk.StringVar()
        self.str_show.set("show_time")
        self.label_show = tk.Label(self, bg=bg_color, textvariable=self.str_show)
        self.label_show.pack(fill=tk.BOTH, expand=tk.YES)
