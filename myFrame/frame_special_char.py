import tkinter as tk


# 第三个子框-起止符文本框
class FrameSpecialChar(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        bg_color_special_char = "LightSkyBlue"
        self.frame_special_char_temp = tk.Frame(self, bg=bg_color_special_char)
        self.frame_start = tk.Frame(self.frame_special_char_temp, bg=bg_color_special_char, pady=2)
        self.frame_end = tk.Frame(self.frame_special_char_temp, bg=bg_color_special_char)

        self.label_start_char = tk.Label(self.frame_start, bg=bg_color_special_char, text="起始符")
        self.label_end_char = tk.Label(self.frame_end, bg=bg_color_special_char, text="终止符")
        self.input_start_char = tk.Entry(self.frame_start, width=8, justify=tk.CENTER)
        self.input_end_char = tk.Entry(self.frame_end, width=8, justify=tk.CENTER)

        self.label_start_char.pack(side=tk.LEFT, padx=3)
        self.input_start_char.pack(padx=9)
        self.label_end_char.pack(side=tk.LEFT, padx=3)
        self.input_end_char.pack(padx=9)
        self.frame_start.pack()
        self.frame_end.pack()
        self.frame_special_char_temp.pack(fill=tk.X, padx=2, pady=2, ipady=1)


'''
        bg_color_special_char = "LightSkyBlue"
        frame_special_char = tk.Frame(self.frame_controls)
        frame_special_char_temp = tk.Frame(frame_special_char, bg=bg_color_special_char)
        label_start_char = tk.Label(frame_special_char_temp, bg=bg_color_special_char, text="起始符")
        label_end_char = tk.Label(frame_special_char_temp, bg=bg_color_special_char, text="终止符")
        input_start_char = tk.Entry(frame_special_char_temp, width=5)
        input_end_char = tk.Entry(frame_special_char_temp, width=5)
        check_use_char = tk.Checkbutton(frame_special_char_temp, activebackground=bg_color_special_char,
                                        bg=bg_color_special_char, text="启用起止符")
        label_start_char.grid(row=0, column=0, sticky=tk.W)
        label_end_char.grid(row=1, column=0, sticky=tk.W)
        input_start_char.grid(row=0, column=1, pady=2)
        input_end_char.grid(row=1, column=1, pady=0)
        check_use_char.grid(row=2, column=0, columnspan=2)
        frame_special_char_temp.pack(fill=tk.X, padx=2, pady=2)
'''
