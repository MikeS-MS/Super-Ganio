from game_data.engine.globals import *
from widget_styles import *
from utilities import *
import pygame


class Bounds:
    def __init__(self, box: pygame.Rect, padding: Vec4, margin: Vec4):
        self.resize(box, padding, margin)

    def resize(self, box: pygame.Rect, padding: Vec4, margin: Vec4):
        self.topleft = Vec2(box.topleft[0] - padding.left - margin.left, box.topleft[1] - padding.top - margin.top)
        self.top = Vec2(box.centerx, box.top - padding.top - margin.top)
        self.topright = Vec2(box.topright[0] + padding.right - margin.right, box.topright[1] - padding.top - margin.top)
        self.right = Vec2(box.right + padding.right + margin.right, box.centery)
        self.bottomright = Vec2(box.bottomright[0] + padding.right + margin.right, box.bottomright[1] + padding.bottom + margin.bottom)
        self.bottom = Vec2(box.centerx, box.bottom + padding.bottom + margin.bottom)
        self.bottomleft = Vec2(box.bottomleft[0] - padding.left - margin.left, box.bottomleft[1] + padding.bottom + margin.bottom)
        self.left = Vec2(box.left - padding.left - margin.left, box.centery)
        self.center = Vec2(box.centerx, box.centery)


class Widget:
    def __init__(self,
                 owner: object = None,
                 anchor: WidgetAnchor = WidgetAnchor.TopLeft,
                 position: Vec2 = Vec2(0, 0),
                 size: Vec2 = Vec2(100, 50),
                 padding: Vec4 = Vec4(0, 0, 0, 0),
                 margin: Vec4 = Vec4(0, 0, 0, 0),
                 background_color: Color = Color.Transparent):

        self.owner = owner
        self.children = []
        self.resize(anchor, position, size, padding, margin)
        self.background_color = background_color
        self.background = pygame.surface.Surface((self.size.width, self.size.height))

    # def resize_and_reposition(self) -> None:
    #     self.owner: Widget
    #     if self.owner is not None:
    #         self.owner.resize_and_reposition()
    #     else:
    #         for child in self.children:
    #             child: Widget
    #             child.change_size_and_position()
    #     self.resize()

    # def change_size_and_position(self) -> None:
    #     previous_child = self
    #     self.resize()
    #     for child in self.children:
    #         child: Widget
    #         previous_child: Widget
    #         child.change_size_and_position()
    #         child.resize(child.anchor,
    #                      previous_child.get_point_from_anchor(child.anchor),
    #                      Math.clamp_vec2(child.size, Vec2(0, 0), self.size),
    #                      child.padding,
    #                      child.margin)
    #         previous_child = child

    def get_point_from_anchor(self, anchor: WidgetAnchor) -> Vec2:
        if anchor == WidgetAnchor.TopLeft:
            return self.bounds.topleft
        elif anchor == WidgetAnchor.Top:
            return self.bounds.top
        elif anchor == WidgetAnchor.TopRight:
            return self.bounds.topright
        elif anchor == WidgetAnchor.Right:
            return self.bounds.right
        elif anchor == WidgetAnchor.BottomRight:
            return self.bounds.bottomright
        elif anchor == WidgetAnchor.Bottom:
            return self.bounds.bottom
        elif anchor == WidgetAnchor.BottomLeft:
            return self.bounds.bottomleft
        elif anchor == WidgetAnchor.Left:
            return self.bounds.left
        elif anchor == WidgetAnchor.Center:
            return self.bounds.center

    def resize(self,
               anchor: WidgetAnchor = WidgetAnchor.TopLeft,
               position: Vec2 = Vec2(0, 0),
               size: Vec2 = Vec2(100, 50),
               padding: Vec4 = Vec4(0, 0, 0, 0),
               margin: Vec4 = Vec4(0, 0, 0, 0)):

        self.anchor = anchor
        if self.owner is not None:
            self.owner: Widget
            self.position = position + self.owner.get_point_from_anchor(anchor)

        else:
            self.size = Vec2(Engine.window.get_window_size()[0] - padding.width, Engine.window.get_window_size()[1] - padding.height)
        left, top = position.x - size.width, position.y - size.height
        self.content = pygame.Rect(left, top, size.width, size.height)
        self.bounds = Bounds(self.content, padding, margin)
        self.padding = padding
        self.margin = margin

    def set_location_and_size(self,
                              origin_box: Vec4,
                              anchor: WidgetAnchor,
                              position: Vec2,
                              size: Vec2,
                              padding: Vec4,
                              margin: Vec4):

        if anchor == WidgetAnchor.Fill:
            self.size =
            self.size = Vec2(size.width - padding.width, size.height - padding.height)

    def add_widget(self, widget) -> None:
        self.children.append(widget)

    def draw(self, renderer: pygame.surface.Surface) -> None:
        self.background.fill(self.background_color.color)
        renderer.blit(self.background, self.content)

        for widget in self.children:
            widget: Widget
            widget.draw(renderer)

    def handle_event(self, event: WidgetEvent, mouse_pos: tuple) -> None:
        if self.content.collidepoint(mouse_pos):
            if event == WidgetEvent.Hover:
                self.event_on_hover()
            if event == WidgetEvent.Click:
                self.event_on_click()
        else:
            self.event_default()

        for widget in self.children:
            widget.handle_event(event, mouse_pos)

    def event_on_hover(self) -> None:
        pass

    def event_default(self) -> None:
        pass

    def event_on_click(self) -> None:
        pass
