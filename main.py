import pyray as rl


def main() -> None:
    rl.init_window(800, 600, "The Foundry")
    rl.set_target_fps(60)

    bck = rl.load_texture("assets/background.png")

    while not rl.window_should_close():
        rl.begin_drawing()
        rl.clear_background(rl.RAYWHITE)
        rl.draw_texture_pro(
            bck,
            rl.Rectangle(0, 0, bck.width, bck.height),
            rl.Rectangle(0, 0, rl.get_screen_width(), rl.get_screen_height()),
            rl.Vector2(0, 0),
            0,
            rl.WHITE,
        )
        rl.end_drawing()

    rl.close_window()


if __name__ == "__main__":
    main()
