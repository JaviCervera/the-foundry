from src.window import Window


def main() -> None:
    win = Window()
    while win.update():
        win.draw()
    win.close()


if __name__ == "__main__":
    main()
