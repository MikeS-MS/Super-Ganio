class Vec4:
    def __init__(self, top, right, bottom, left):
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left
        self.width = abs(right - left)
        self.height = abs(bottom - top)

    @property
    def size(self) -> Vec2:
        return Vec2(self.width, self.height)

    def compare(self, other) -> int:
        other: Vec4
        """
        Returns -2 if only one component of left is either greater or smaller than the matching component of the right\n
        Returns -1 if both components of left are smaller than the components of the right\n
        Returns 0 if  both components of left are equal to the both components of right\n
        Returns 1 if both components of left are greater than the components of the right\n
        """
        if self.top > other.top and self.right < other.right and self.bottom < other.bottom and self.left > other.left:
            return -1
        elif self.top >= other.top and self.right <= other.right and self.bottom <= other.bottom and self.left >= other.left:
            return 0
        elif self.top < other.top and self.right > other.right and self.bottom > other.bottom and self.left < other.left:
            return 1
        else:
            return -2

    def __add__(self, other):
        self.top -= other.top
        self.right += other.right
        self.bottom += other.bottom
        self.left -= other.left

    def __sub__(self, other):
        self.top += other.top
        self.right -= other.right
        self.bottom -= other.bottom
        self.left += other.left


class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.x

    @property
    def height(self):
        return self.y

    def compare(self, other) -> int:
        """
        Returns -2 if only one component of left is either greater or smaller than the matching component of the right\n
        Returns -1 if both components of left are smaller than the components of the right\n
        Returns 0 if  both components of left are equal to the both components of right\n
        Returns 1 if both components of left are greater than the components of the right\n
        """
        if self.x < other.x and self.y < other.y:
            return -1
        elif self.x == other.x and self.y == other.y:
            return 0
        elif self.x > other.x and self.y > other.y:
            return 1
        else:
            return -2

    def __add__(self, other):
        self.x += other.x
        self.y += other.y

    def __sub__(self, other):
        self.x -= other.x
        self.y -= other.y

    def __mul__(self, other):
        self.x *= other.x
        self.y *= other.y

    def __divmod__(self, other):
        self.x /= other.x
        self.y /= other.y


class Math:
    @staticmethod
    def clamp_float(num: float, min_num: float, max_num: float) -> float:
        if num < min_num:
            return min_num
        elif num > max_num:
            return max_num
        return num

    @staticmethod
    def clamp_int(num: int, min_num: int, max_num: int) -> int:
        if num < min_num:
            return min_num
        elif num > max_num:
            return max_num
        return num

    @staticmethod
    def clamp_vec2(vector: Vec2, min_vec: Vec2, max_vec: Vec2) -> Vec2:
        if vector.compare(min_vec) < 0:
            return min_vec
        elif vector.compare(max_vec) == 1:
            return max_vec
        return vector

    @staticmethod
    def clamp_vec4(box: Vec4, min_box: Vec4, max_box: Vec4) -> Vec4:
        if box.compare(min_box) < 0:
            return min_box
        elif box.compare(max_box) == 1:
            return max_box
        return box


class Color:
    Transparent = (255, 255, 255, 0)
    White = (255, 255, 255, 255)
    Gray = (127, 127, 127, 255)
    Black = (0, 0, 0, 255)
    Red = (255, 0, 0, 255)
    Orange = (255, 127, 0, 255)
    Yellow = (255, 255, 0, 255)
    Lime = (127, 255, 0, 255)
    Green = (0, 255, 0, 255)
    Turquoise = (0, 255, 127, 255)
    Aqua = (0, 255, 255, 255)
    Light_Blue = (0, 127, 255, 255)
    Blue = (0, 0, 255, 255)
    Purple = (127, 0, 255, 255)
    Neon_Pink = (255, 0, 255, 255)
    Pink = (255, 0, 127, 255)

    def __init__(self, r, g, b, a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    @property
    def color(self) -> tuple:
        return self.r, self.g, self.b, self.a
