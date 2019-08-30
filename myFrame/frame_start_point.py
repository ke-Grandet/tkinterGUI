import tkinter as tk


# 第五个子框-起点位置单选框（弃用）
class FrameStartPoint(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        bg_color_start_point = "LightSkyBlue"
        bg_color_radio = "LightBlue"
        self.frame_temp = tk.Frame(self, bg=bg_color_start_point)
        self.label_start_point = tk.Label(self.frame_temp, bg=bg_color_start_point, text="起点位置")
        self.start_point_int = tk.IntVar()
        self.radio_up_left = tk.Radiobutton(self.frame_temp, bg=bg_color_radio, indicatoron=0,
                                            variable=self.start_point_int, value=0, text="左上")
        self.radio_up_right = tk.Radiobutton(self.frame_temp, bg=bg_color_radio, indicatoron=0,
                                             variable=self.start_point_int, value=1, text="右上")
        self.radio_down_left = tk.Radiobutton(self.frame_temp, bg=bg_color_radio, indicatoron=0,
                                              variable=self.start_point_int, value=2, text="左下")
        self.radio_down_right = tk.Radiobutton(self.frame_temp, bg=bg_color_radio, indicatoron=0,
                                               variable=self.start_point_int, value=3, text="右下")
        self.label_start_point.grid(row=0, column=0, rowspan=2)
        self.radio_up_left.grid(row=0, column=1, padx=2, pady=3)
        self.radio_up_right.grid(row=0, column=2, padx=2, pady=3)
        self.radio_down_left.grid(row=1, column=1, padx=2, pady=2)
        self.radio_down_right.grid(row=1, column=2, padx=2, pady=2)
        self.radio_up_left.select()
        self.frame_temp.pack(fill=tk.X, padx=2, pady=2, ipadx=1, ipady=1)


'''
        bg_color_start_point = "LightSkyBlue"
        bg_color_radio = "LightBlue"
        frame_start_point = tk.Frame(self.frame_controls)
        frame_temp = tk.Frame(frame_start_point, bg=bg_color_start_point)
        label_start_point = tk.Label(frame_temp, bg=bg_color_start_point, text="起点位置")
        start_point_int = tk.IntVar()
        radio_up_left = tk.Radiobutton(frame_temp, bg=bg_color_radio, indicatoron=0,
                                       variable=start_point_int, value=0, text="左上")
        radio_up_right = tk.Radiobutton(frame_temp, bg=bg_color_radio, indicatoron=0,
                                        variable=start_point_int, value=1, text="右上")
        radio_down_left = tk.Radiobutton(frame_temp, bg=bg_color_radio, indicatoron=0,
                                         variable=start_point_int, value=2, text="左下")
        radio_down_right = tk.Radiobutton(frame_temp, bg=bg_color_radio, indicatoron=0,
                                          variable=start_point_int, value=3, text="右下")
        label_start_point.grid(row=0, column=0, rowspan=2)
        radio_up_left.grid(row=0, column=1, padx=2, pady=3)
        radio_up_right.grid(row=0, column=2, padx=2, pady=3)
        radio_down_left.grid(row=1, column=1, padx=2, pady=2)
        radio_down_right.grid(row=1, column=2, padx=2, pady=2)
        frame_temp.pack(fill=tk.X, padx=2, pady=2, ipadx=1, ipady=1)
'''
