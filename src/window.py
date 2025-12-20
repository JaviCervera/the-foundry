import pyray as rl


class Window:
    _FONT_SIZE = 20

    def __init__(self) -> None:
        rl.init_window(800, 600, "The Foundry")
        rl.set_target_fps(60)
        self._bck = rl.load_texture("assets/background.png")
        self._base = [rl.load_texture(f"assets/base_{i + 1}.png") for i in range(0, 3)]
        self._mine = [rl.load_texture(f"assets/mine_{i + 1}.png") for i in range(0, 2)]
        self._military = [rl.load_texture(f"assets/military_{i + 1}.png") for i in range(0, 2)]
        self._upgrade = rl.load_texture("assets/upgrade.png")

    def update(self) -> bool:
        return not rl.window_should_close()

    def close(self) -> None:
        rl.close_window()

    def draw(self) -> None:
        rl.begin_drawing()
        rl.draw_texture_pro(
            self._bck,
            rl.Rectangle(0, 0, self._bck.width, self._bck.height),
            rl.Rectangle(0, 0, rl.get_screen_width(), rl.get_screen_height()),
            rl.Vector2(0, 0),
            0,
            rl.WHITE,
        )
        self._draw_elem(
            self._base[0], rl.get_screen_width() * 0.5, rl.get_screen_height() * 0.4, "Base", 1
        )
        self._draw_elem(
            self._mine[0], rl.get_screen_width() * 0.25, rl.get_screen_height() * 0.75, "Mine", 1
        )
        self._draw_elem(
            self._military[0],
            rl.get_screen_width() * 0.75,
            rl.get_screen_height() * 0.75,
            "Military",
            1,
        )
        rl.end_drawing()

    def _draw_elem(self, tex: rl.Texture, x: float, y: float, name: str, level: int) -> None:
        self._draw_tex(tex, x, y)
        text = f"{name} (Level {level})"
        rl.draw_text(
            text,
            int(x - rl.measure_text(text, self._FONT_SIZE) / 2),
            int(y - self._FONT_SIZE - 8),
            self._FONT_SIZE,
            rl.WHITE,
        )
        self._draw_button(self._upgrade, x, y + 40)

    def _draw_tex(self, tex: rl.Texture, x: float, y: float) -> None:
        """Draws the texture horizontally centered and bottom aligned"""
        rl.draw_texture(tex, int(x - tex.width / 2), int(y - tex.height), rl.WHITE)

    def _draw_button(self, tex: rl.Texture, x: float, y: float) -> None:
        """Draws the button centered"""
        rl.draw_texture(tex, int(x - tex.width / 2), int(y - tex.height / 2), rl.WHITE)
