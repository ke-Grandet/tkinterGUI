import tkinter as tk


# 第四个子框-时针方向单选框和箭头方向单选框（弃用）
class FrameDirection(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        bg_color_direction = "LightSkyBlue"
        self.frame_direction_temp = tk.Frame(self)
        self.frame_clk_direction = tk.Frame(self.frame_direction_temp, bg=bg_color_direction)
        self.clk_dir_int = tk.IntVar()
        self.radio_clock = tk.Radiobutton(self.frame_clk_direction, activebackground=bg_color_direction,
                                          bg=bg_color_direction, variable=self.clk_dir_int, value=1, text="顺时针")
        self.radio_anti_clock = tk.Radiobutton(self.frame_clk_direction, activebackground=bg_color_direction,
                                               bg=bg_color_direction, variable=self.clk_dir_int, value=-1, text="逆时针")
        self.radio_clock.pack()
        self.radio_anti_clock.pack()
        self.radio_clock.select()
        self.frame_clk_direction.pack(fill=tk.X, side=tk.LEFT, pady=2)

        self.frame_inout_direction = tk.Frame(self.frame_direction_temp, bg=bg_color_direction)
        self.inout_dir_int = tk.IntVar()
        self.radio_in = tk.Radiobutton(self.frame_inout_direction, activebackground=bg_color_direction,
                                       bg=bg_color_direction, variable=self.inout_dir_int, value=1, text="旋进")
        self.radio_out = tk.Radiobutton(self.frame_inout_direction, activebackground=bg_color_direction,
                                        bg=bg_color_direction, variable=self.inout_dir_int, value=0, text="旋出")
        self.radio_in.pack()
        self.radio_out.pack()
        self.radio_in.select()
        self.frame_inout_direction.pack(fill=tk.X, pady=2)

        self.frame_direction_temp.pack(fill=tk.X, padx=2)


'''
        bg_color_direction = "LightSkyBlue"
        frame_direction = tk.Frame(self.frame_controls)
        frame_direction_temp = tk.Frame(frame_direction)
        frame_clk_direction = tk.Frame(frame_direction_temp, bg=bg_color_direction)
        clk_dir_int = tk.IntVar()
        radio_clock = tk.Radiobutton(frame_clk_direction, activebackground=bg_color_direction,
                                     bg=bg_color_direction, variable=clk_dir_int, value=0, text="顺时针")
        radio_anti_clock = tk.Radiobutton(frame_clk_direction, activebackground=bg_color_direction,
                                          bg=bg_color_direction, variable=clk_dir_int, value=1, text="逆时针")
        radio_clock.pack()
        radio_anti_clock.pack()
        frame_clk_direction.pack(fill=tk.X, side=tk.LEFT, pady=2)
        
        frame_walk_direction = tk.Frame(frame_direction_temp, bg=bg_color_direction)
        walk_dir_int = tk.IntVar()
        radio_in = tk.Radiobutton(frame_walk_direction, activebackground=bg_color_direction, bg=bg_color_direction,
                                  variable=walk_dir_int, value=0, text="旋进")
        radio_out = tk.Radiobutton(frame_walk_direction, activebackground=bg_color_direction, bg=bg_color_direction,
                                   variable=walk_dir_int, value=1, text="旋出")
        radio_in.pack()
        radio_out.pack()
        frame_walk_direction.pack(fill=tk.X, pady=2)
        
        frame_direction_temp.pack(fill=tk.X, padx=2)
'''
