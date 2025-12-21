import pyray as rl


class Window:
    _FONT_SIZE = 20
    _BUTTON_Y_OFFSET = 40

    def __init__(self) -> None:
        rl.init_window(800, 600, "The Foundry")
        rl.set_target_fps(60)
        self._bck = rl.load_texture("assets/background.png")
        self._base = [rl.load_texture(f"assets/base_{i + 1}.png") for i in range(0, 3)]
        self._mine = [rl.load_texture(f"assets/mine_{i + 1}.png") for i in range(0, 2)]
        self._military = [rl.load_texture(f"assets/military_{i + 1}.png") for i in range(0, 2)]
        self._upgrade = rl.load_texture("assets/upgrade.png")
        self._attack = rl.load_texture("assets/attack.png")

    def update(self) -> bool:
        if rl.window_should_close():
            return False
        attack_pos = self._attack_pos()
        mine_pos = self._mine_upgrade_pos()
        mil_pos = self._military_upgrade_pos()
        if rl.is_mouse_button_pressed(rl.MouseButton.MOUSE_BUTTON_LEFT):
            if self._mouse_in_button(self._attack, attack_pos.x, attack_pos.y):
                print("Attack")
            elif self._mouse_in_button(self._upgrade, mine_pos.x, mine_pos.y):
                print("Mine upgrade")
            elif self._mouse_in_button(self._upgrade, mil_pos.x, mil_pos.y):
                print("Military upgrade")
        return True

    def close(self) -> None:
        rl.close_window()

    def draw(self) -> None:
        base_pos = self._base_pos()
        mine_pos = self._mine_pos()
        mil_pos = self._military_pos()
        rl.begin_drawing()
        rl.draw_texture_pro(
            self._bck,
            rl.Rectangle(0, 0, self._bck.width, self._bck.height),
            rl.Rectangle(0, 0, rl.get_screen_width(), rl.get_screen_height()),
            rl.Vector2(0, 0),
            0,
            rl.WHITE,
        )
        self._draw_elem(self._base[0], base_pos.x, base_pos.y, "Base", 1, False)
        self._draw_elem(self._mine[0], mine_pos.x, mine_pos.y, "Mine", 1, True)
        self._draw_elem(self._military[0], mil_pos.x, mil_pos.y, "Military", 1, True)
        rl.end_drawing()

    def _base_pos(self) -> rl.Vector2:
        return rl.Vector2(rl.get_screen_width() * 0.5, rl.get_screen_height() * 0.35)

    def _mine_pos(self) -> rl.Vector2:
        return rl.Vector2(rl.get_screen_width() * 0.25, rl.get_screen_height() * 0.75)

    def _military_pos(self) -> rl.Vector2:
        return rl.Vector2(rl.get_screen_width() * 0.75, rl.get_screen_height() * 0.75)

    def _attack_pos(self) -> rl.Vector2:
        rect = self._base_pos()
        rect.y += self._BUTTON_Y_OFFSET
        return rect

    def _mine_upgrade_pos(self) -> rl.Vector2:
        rect = self._mine_pos()
        rect.y += self._BUTTON_Y_OFFSET
        return rect

    def _military_upgrade_pos(self) -> rl.Vector2:
        rect = self._military_pos()
        rect.y += self._BUTTON_Y_OFFSET
        return rect

    def _draw_elem(
        self, tex: rl.Texture, x: float, y: float, name: str, level: int, upgradable: bool
    ) -> None:
        self._draw_tex(tex, x, y)
        if upgradable:
            text = f"{name} (Level {level})"
            button = self._upgrade
            sel_color = rl.YELLOW
        else:
            text = f"{name} (Power 10)"
            button = self._attack
            sel_color = rl.RED
        rl.draw_text(
            text,
            int(x - rl.measure_text(text, self._FONT_SIZE) / 2),
            int(y - self._FONT_SIZE - 8),
            self._FONT_SIZE,
            sel_color if self._mouse_in_button(tex, x, y) else rl.WHITE,
        )
        self._draw_button(button, x, y + self._BUTTON_Y_OFFSET, sel_color)

    def _draw_tex(self, tex: rl.Texture, x: float, y: float) -> None:
        """Draws the texture horizontally centered and bottom aligned"""
        rl.draw_texture(tex, int(x - tex.width / 2), int(y - tex.height), rl.WHITE)

    def _draw_button(self, tex: rl.Texture, x: float, y: float, sel_color: rl.Color) -> None:
        """Draws the button centered"""
        rect = self._button_rect(tex, x, y)
        color = sel_color if self._mouse_in_button(tex, x, y) else rl.WHITE
        rl.draw_texture(tex, int(rect.x), int(rect.y), color)

    def _mouse_in_button(self, tex: rl.Texture, x: float, y: float) -> bool:
        return rl.check_collision_point_rec(
            rl.Vector2(rl.get_mouse_x(), rl.get_mouse_y()), self._button_rect(tex, x, y)
        )

    def _button_rect(self, tex: rl.Texture, x: float, y: float) -> rl.Rectangle:
        return rl.Rectangle(x - tex.width / 2, y - tex.height / 2, tex.width, tex.height)
