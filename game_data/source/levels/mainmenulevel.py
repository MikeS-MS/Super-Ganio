from game_data.source.buttons.custombuttons import *
from game_data.source.levels.BaseLevel import *
from game_data.engine.base.level import *
from game_data.engine.base.widgets import *
import os


class MainMenu(Level):
    def __init__(self, instance):
        super().__init__(instance)

        abs_path = os.path.dirname(os.path.abspath("assets"))
        abs_path = os.path.join(abs_path, 'game_data\\assets\\music\\Terraria Music - Day.mp3')
        self.game_instance.music.load(abs_path)
        self.game_instance.music.play(-1)
        self.game_instance.music.set_volume(0.2)

        screen_size = self.game_instance.window.get_window_size()

        main_menu_widget = Widget((screen_size[0] / 2, screen_size[1] / 2 - 100), 50, 100, "Super Ganio!", 80)
        play_menu_widget = Widget((self.game_instance.window.get_window_size()[0] / 2, screen_size[1] / 2 - 250), 50, 100, "Select a Level", 80)

        sprites_credits = Widget((screen_size[0] / 2 - 150, 50), 50, 100, "Art was inspired by:", 30)
        music_credits = Widget((screen_size[0] / 2 - 150, 90), 50, 100, "The music taken from:", 30)
        credited_game = Widget((screen_size[0] / 2 + 150, 70), 50, 100, "Terraria", 100)

        main_menu_widget.add_widget(PlayButton(True, True, 'Play', 60, owner=self, custom_data=[play_menu_widget]))
        main_menu_widget.add_widget(ExitButton(True, True, 'Exit', 60, owner=self))

        play_menu_widget.add_widget(StartLevelButton(True, True, 'Level1', 60, owner=self, custom_data=[BaseLevel(self.game_instance, "./game_data/assets/levels/level1/level.tmx")]))
        play_menu_widget.add_widget(StartLevelButton(True, True, 'Level2', 60, owner=self, custom_data=[BaseLevel(self.game_instance, "./game_data/assets/levels/level2/level.tmx")]))
        play_menu_widget.add_widget(StartLevelButton(True, True, 'Level3', 60, owner=self, custom_data=[BaseLevel(self.game_instance, "./game_data/assets/levels/level3/level.tmx")]))
        play_menu_widget.add_widget(OpenFileBrowser(True, True, 'Load custom', 60, owner=self, custom_data=[self.game_instance]))
        play_menu_widget.add_widget(BackButtonWidget(True, True, 'Back', 60, owner=self, custom_data={main_menu_widget: True, sprites_credits: False, music_credits: False, credited_game: False}))

        self.background_color = (0, 100+50, 70+50)
        self.set_widget(main_menu_widget, True)
        self.set_widget(sprites_credits)
        self.set_widget(music_credits)
        self.set_widget(credited_game)
