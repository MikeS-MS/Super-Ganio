from enum import Enum


class WidgetEvent(Enum):
    Hover = 0,
    Click = 1


class WidgetAnchor(Enum):
    TopLeft = 0,
    Top = 1,
    TopRight = 2,
    Right = 3,
    BottomRight = 4,
    Bottom = 5,
    BottomLeft = 6,
    Left = 7,
    Center = 8,
    Fill = 9
