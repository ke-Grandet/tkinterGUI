import tkinter as tk


# 第一个子框-长宽设定框
class FrameSize(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        checkCMD = master.register(check_digit)
        bg_color_size = "LightSkyBlue"
        self.frame_size_temp = tk.Frame(self, bg=bg_color_size)
        self.label_length = tk.Label(self.frame_size_temp, bg=bg_color_size, text="长")
        self.label_width = tk.Label(self.frame_size_temp, bg=bg_color_size, text="宽")
        self.input_length = tk.Entry(self.frame_size_temp, width=5, validate='key', validatecommand=(checkCMD, '%P'))
        self.input_width = tk.Entry(self.frame_size_temp, width=5, validate='key', validatecommand=(checkCMD, '%P'))
        self.label_length.pack(side=tk.LEFT)
        self.input_length.pack(side=tk.LEFT, padx=5)
        self.input_width.pack(side=tk.RIGHT, padx=5)
        self.label_width.pack(side=tk.RIGHT)
        self.frame_size_temp.pack(fill=tk.X, padx=2, pady=2, ipadx=2, ipady=2)


def check_digit(text):
        if text.isdigit() or text == "":
            return True
        else:
            return False


if __name__ == "__main":
    pass

'''
        bg_color_size = "LightSkyBlue"
        frame_size = tk.Frame(frame_controls)
        frame_size_temp = tk.Frame(frame_size, bg=bg_color_size)
        label_length = tk.Label(frame_size_temp, bg=bg_color_size, text="长")
        label_width = tk.Label(frame_size_temp, bg=bg_color_size, text="宽")
        input_length = tk.Entry(frame_size_temp, width=5)
        input_width = tk.Entry(frame_size_temp, width=5)
        label_length.pack(side=tk.LEFT)
        input_length.pack(side=tk.LEFT, padx=5)
        input_width.pack(side=tk.RIGHT, padx=5)
        label_width.pack(side=tk.RIGHT)
        frame_size_temp.pack(fill=tk.X, padx=2, pady=2, ipadx=2, ipady=2)
'''
