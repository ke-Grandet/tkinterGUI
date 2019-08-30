# 输出杨辉三角
def yang_hui_triangle(n):
    list_old = [1]
    list_new = [1, 1]
    print(list_old)
    print(list_new)
    for i in range(1, n, 1):
        list_old = list_new
        list_new = list_new + [1]
        for j in range(1, list_old.__len__(), 1):
            list_new[j] = list_old[j - 1] + list_old[j]
        print(list_new)

    # def yang_hui_pyramid():

    # 输出旋涡数组：
    '''
    clock_direction = 1  # 1为顺时针；-1为逆时针
    walk_direction = 0   # 0为右，1为下，2为左，3为上
    inout_direction = 1  # 1为旋进；0为旋出
    up, down, left, right = '→', '↓', '←', '↑'
    up_left, up_right, down_left, down_right = '↖', '↗', '↙', '↘'
    '''


class Whirlpool:
    UP, DOWN, LEFT, RIGHT = ' ↑ ', ' ↓ ', '←', '→'
    UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT = '↖', '↗', '↙', '↘'
    __length, __width = 5, 5
    __start_x, __start_y = 0, 0
    up, down, left, right = UP, DOWN, LEFT, RIGHT
    up_left, up_right, down_left, down_right = UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT
    start_char = "go"
    end_char = "gg"
    clock_direction = 1
    inout_direction = 1
    use_start_char = False
    use_end_char = False
    walk_direction = None
    arr = None

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        if value > 2:
            self.__length = value
        else:
            self.__length = 2

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value > 2:
            self.__width = value
        else:
            self.__width = 2

    @property
    def start_x(self):
        return self.__start_x

    @start_x.setter
    def start_x(self, value):
        if value > 0:
            self.__start_x = self.length - 1
        else:
            self.__start_x = 0

    @property
    def start_y(self):
        return self.__start_y

    @start_y.setter
    def start_y(self, value):
        if value > 0:
            self.__start_y = self.width - 1
        else:
            self.__start_y = 0

    def __init__(self, length=5, width=5, clock_direction=1, inout_direction=1, start_x=0, start_y=0):
        self.length = length
        self.width = width
        self.start_x = start_x
        self.start_y = start_y
        if clock_direction > 0:
            self.clock_direction = 1
        else:
            self.clock_direction = -1

        if inout_direction > 0:
            self.inout_direction = 1
        else:
            self.inout_direction = 0

    def show_time(self):
        for i in range(0, self.width, 1):
            for j in range(0, self.length, 1):
                print(self.arr[i][j], end='\t')
            print()
        print("大小：{0} × {1} = {2}".format(self.length, self.width, self.length * self.width))
        if self.clock_direction == 1:
            clock_direction = "顺时针"
        else:
            clock_direction = "逆时针"
        if self.inout_direction == 1:
            inout_direction = "旋进"
        else:
            inout_direction = "旋出"
        print("箭头方向：", clock_direction + inout_direction)

    def get_walk_direction(self):
        start_x = self.start_x
        start_y = self.start_y
        clk_direction = self.clock_direction
        walk_direction = None
        if (start_x > 0 and start_y == 0 and clk_direction == 1) \
                or (start_x > 0 and start_y > 0 and clk_direction == -1):
            walk_direction = 0
        elif (start_x == 0 and start_y > 0 and clk_direction == -1) \
                or (start_x > 0 and start_y > 0 and clk_direction == 1):
            walk_direction = 1
        elif (start_x == 0 and start_y == 0 and clk_direction == -1) \
                or (start_x == 0 and start_y > 0 and clk_direction == 1):
            walk_direction = 2
        elif (start_x == 0 and start_y == 0 and clk_direction == 1) \
                or (start_x > 0 and start_y == 0 and clk_direction == -1):
            walk_direction = 3
        return walk_direction

    def walk(self):
        point_x = self.start_x
        point_y = self.start_y
        walk_direction = self.get_walk_direction()
        arr = [['0'] * self.length for i in range(self.width)]
        i = 0
        end_x = point_x
        end_y = point_y
        while i < self.length * self.width:
            i = i + 1
            end_x = point_x
            end_y = point_y
            if walk_direction == 0:
                if point_x + 1 < self.length and arr[point_y][point_x + 1] == '0':
                    if self.inout_direction == 1:
                        arr[point_y][point_x] = self.right
                    else:
                        arr[point_y][point_x] = self.left
                    point_x = point_x + 1
                else:
                    walk_direction = (walk_direction + self.clock_direction + 4) % 4
                    if walk_direction == 1:
                        if self.inout_direction == 1:
                            arr[point_y][point_x] = self.down_right
                        else:
                            arr[point_y][point_x] = self.up_left
                        point_y = point_y + 1
                    elif walk_direction == 3:
                        if self.inout_direction == 1:
                            arr[point_y][point_x] = self.up_right
                        else:
                            arr[point_y][point_x] = self.down_left
                        point_y = point_y - 1
            elif walk_direction == 1:
                if point_y + 1 < self.width and arr[point_y + 1][point_x] == '0':
                    if self.inout_direction == 1:
                        arr[point_y][point_x] = self.down
                    else:
                        arr[point_y][point_x] = self.up
                    point_y = point_y + 1
                else:
                    walk_direction = (walk_direction + self.clock_direction + 4) % 4
                    if walk_direction == 2:
                        if self.inout_direction == 1:
                            arr[point_y][point_x] = self.down_left
                        else:
                            arr[point_y][point_x] = self.up_right
                        point_x = point_x - 1
                    elif walk_direction == 0:
                        if self.inout_direction == 1:
                            arr[point_y][point_x] = self.down_right
                        else:
                            arr[point_y][point_x] = self.up_left
                        point_x = point_x + 1
            elif walk_direction == 2:
                if point_x - 1 >= 0 and arr[point_y][point_x - 1] == '0':
                    if self.inout_direction == 1:
                        arr[point_y][point_x] = self.left
                    else:
                        arr[point_y][point_x] = self.right
                    point_x = point_x - 1
                else:
                    walk_direction = (walk_direction + self.clock_direction + 4) % 4
                    if walk_direction == 3:
                        if self.inout_direction == 1:
                            arr[point_y][point_x] = self.up_left
                        else:
                            arr[point_y][point_x] = self.down_right
                        point_y = point_y - 1
                    elif walk_direction == 1:
                        if self.inout_direction == 1:
                            arr[point_y][point_x] = self.down_left
                        else:
                            arr[point_y][point_x] = self.up_right
                        point_y = point_y + 1
            elif walk_direction == 3:
                if point_y - 1 >= 0 and arr[point_y - 1][point_x] == '0':
                    if self.inout_direction == 1:
                        arr[point_y][point_x] = self.up
                    else:
                        arr[point_y][point_x] = self.down
                    point_y = point_y - 1
                else:
                    walk_direction = (walk_direction + self.clock_direction + 4) % 4
                    if walk_direction == 0:
                        if self.inout_direction == 1:
                            arr[point_y][point_x] = self.up_right
                        else:
                            arr[point_y][point_x] = self.down_left
                        point_x = point_x + 1
                    elif walk_direction == 2:
                        if self.inout_direction == 1:
                            arr[point_y][point_x] = self.up_left
                        else:
                            arr[point_y][point_x] = self.down_right
                        point_x = point_x - 1
            else:
                print("Whirlpool.walk()发生错误！")
                break
        if self.use_start_char:
            if self.inout_direction == 1:
                arr[self.start_y][self.start_x] = self.start_char
            else:
                arr[end_y][end_x] = self.start_char
        if self.use_end_char:
            if self.inout_direction == 1:
                arr[end_y][end_x] = self.end_char
            else:
                arr[self.start_y][self.start_x] = self.end_char
        self.arr = arr


class Test:
    _length = 1

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        if value > 5:
            self._length = value
        else:
            print("f u")


if __name__ == "__main__":
    wp = Whirlpool(5, 5, -1, 1, 1, 1)
    wp.walk()
    wp.show_time()
    test = Test()
    write = input()
