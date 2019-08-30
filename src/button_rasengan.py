from src.hello import Whirlpool


class Rasengan:
    whirlpool = Whirlpool()

    def __init__(self):
        pass

    # 设置长宽
    def set_length_width(self, length, width):
        if length:
            self.whirlpool.length = int(length)
        if width:
            self.whirlpool.width = int(width)

    # 设置方向符
    def set_up_char(self, up_left, up, up_right):
        self.whirlpool.up_left = up_left or self.whirlpool.UP_LEFT
        self.whirlpool.up = up or self.whirlpool.UP
        self.whirlpool.up_right = up_right or self.whirlpool.UP_RIGHT

    def set_mid_char(self, left, right):
        self.whirlpool.left = left or self.whirlpool.LEFT
        self.whirlpool.right = right or self.whirlpool.RIGHT

    def set_down_char(self, down_left, down, down_right):
        self.whirlpool.down_left = down_left or self.whirlpool.DOWN_LEFT
        self.whirlpool.down = down or self.whirlpool.DOWN
        self.whirlpool.down_right = down_right or self.whirlpool.DOWN_RIGHT

    # 设置起止符
    def set_special_char(self, start_char, end_char):
        if start_char:
            self.whirlpool.use_start_char = True
            self.whirlpool.start_char = start_char
        else:
            self.whirlpool.use_start_char = False
        if end_char:
            self.whirlpool.use_end_char = True
            self.whirlpool.end_char = end_char
        else:
            self.whirlpool.use_end_char = False

    # 设置方向
    def set_direction(self, clk_direction, inout_direction):
        self.whirlpool.clock_direction = clk_direction
        self.whirlpool.inout_direction = inout_direction

    # 设置出发点
    def set_start_point(self, point):
        x, y = 0, 0
        if point == 1:
            x, y = 1, 0
        elif point == 2:
            x, y = 0, 1
        elif point == 3:
            x, y = 1, 1
        self.whirlpool.start_x = x
        self.whirlpool.start_y = y

    def walk(self):
        self.whirlpool.walk()
        self.whirlpool.show_time()

    def get_result(self):
        length = self.whirlpool.length
        width = self.whirlpool.width
        arr = self.whirlpool.arr
        str_result = ""
        for i in range(width - 1):
            for j in range(length - 1):
                str_result += arr[i][j] + ' '
            str_result += arr[i][length - 1] + '\n'
        for k in range(length - 1):
            str_result += arr[width - 1][k] + ' '
        str_result += arr[width - 1][length - 1]
        return str_result

    def get_message(self):
        length = self.whirlpool.length
        width = self.whirlpool.width
        clk_dir = self.whirlpool.clock_direction
        inout_dir = self.whirlpool.inout_direction
        str_size = "大小：{0} × {1} = {2}".format(length, width, length*width)
        str_dir = "方向："
        if clk_dir == 1:
            str_dir += "顺时针"
        else:
            str_dir += "逆时针"
        if inout_dir == 1:
            str_dir += "旋进"
        else:
            str_dir += "旋出"
        str_message = str_size + '\t' + str_dir
        return str_message


if __name__ == "__main__":
    print("waste")
