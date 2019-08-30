import tkinter as tk

from myFrame.frame_size import FrameSize    # 第一个子框-长宽设定框
from myFrame.frame_direction_char import FrameDirectionChar    # 第二个子框-方向符号文本框
from myFrame.frame_special_char import FrameSpecialChar    # 第三个子框-起止符文本框
from myFrame.frame_direction import FrameDirection    # 第四个子框-时针方向单选框和箭头方向单选框
from myFrame.frame_start_point import FrameStartPoint    # 第五个子框-起点位置单选框
from myFrame.frame_message import FrameMessage    # 底部显示信息
from myFrame.frame_show import FrameShow    # 结果显示信息
from src.button_rasengan import Rasengan


class Application:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("what the hello!")
        self.main_window.geometry("800x550")

        # 左边父框-操作栏，右边父框-显示栏
        self.frame_left = tk.Frame(self.main_window, bg="LightBlue")
        self.frame_left.pack(fill=tk.Y, side=tk.LEFT)
        self.frame_controls = tk.Frame(self.frame_left, bg="LightBlue")
        self.frame_controls.pack(pady=5)
        self.frame_right = tk.Frame(self.main_window, bg="CornFLowerBlue")
        self.frame_right.pack(fill=tk.BOTH, expand=tk.YES)
        self.frame_show = FrameShow(self.frame_right)
        self.frame_show.pack(fill=tk.BOTH, expand=tk.YES)

        # 左：第一个子框-长宽设定框
        self.frame_size = FrameSize(self.frame_controls)

        # 左：第二个子框-方向符号文本框
        self.frame_direction_char = FrameDirectionChar(self.frame_controls)

        # 左：第三个子框-起止符文本框
        self.frame_special_char = FrameSpecialChar(self.frame_controls)

        # 左：第四个子框-时针方向单选框和箭头方向单选框
        self.frame_direction = FrameDirection(self.frame_controls)
        self.frame_direction.radio_clock.select()
        self.frame_direction.radio_in.select()

        # 左：第五个子框-起点位置单选框
        self.frame_start_point = FrameStartPoint(self.frame_controls)
        self.frame_start_point.radio_up_left.select()

        # 左：带图的按钮
        image = tk.PhotoImage(file="img/Rasengan.gif")
        self.button = tk.Button(self.frame_controls, image=image, text="Rasengan！", command=self.rasengan)

        # 右：提示标签
        self.frame_message = FrameMessage(self.frame_right)

        # 加入布局
        self.frame_size.pack(fill=tk.X, padx=6, pady=3)
        self.frame_direction_char.pack(fill=tk.X, padx=6, pady=3)
        self.frame_special_char.pack(fill=tk.X, padx=6, pady=3)
        self.frame_direction.pack(fill=tk.X, padx=6, pady=3)
        self.frame_start_point.pack(fill=tk.X, padx=6, pady=3)
        self.button.pack(pady=3)
        self.frame_message.pack()

        self.main_window.mainloop()

    def rasengan(self):
        rasengan = Rasengan()

        # 设置长宽
        length = self.frame_size.input_length.get()
        width = self.frame_size.input_width.get()
        rasengan.set_length_width(length, width)

        # 设置方向符
        up_left = self.frame_direction_char.input_up_left.get()
        up = self.frame_direction_char.input_up.get()
        up_right = self.frame_direction_char.input_up_right.get()
        left = self.frame_direction_char.input_left.get()
        right = self.frame_direction_char.input_right.get()
        down_left = self.frame_direction_char.input_down_left.get()
        down = self.frame_direction_char.input_down.get()
        down_right = self.frame_direction_char.input_down_right.get()
        rasengan.set_up_char(up_left, up, up_right)
        rasengan.set_mid_char(left, right)
        rasengan.set_down_char(down_left, down, down_right)

        # 设置起止符
        start_char = self.frame_special_char.input_start_char.get()
        end_char = self.frame_special_char.input_end_char.get()
        rasengan.set_special_char(start_char, end_char)

        # 设置方向
        clk_direction = self.frame_direction.clk_dir_int.get()
        inout_direction = self.frame_direction.inout_dir_int.get()
        rasengan.set_direction(clk_direction, inout_direction)

        # 设置起点
        start_point = self.frame_start_point.start_point_int.get()
        rasengan.set_start_point(start_point)

        rasengan.walk()
        str_result = rasengan.get_result()
        str_message = rasengan.get_message()
        self.frame_show.str_show.set(str_result)
        self.frame_message.str_message.set(str_message)
        # tk.messagebox.showinfo(self.length_input.get() + self.width_input.get())


if __name__ == "__main__":
    Application()
