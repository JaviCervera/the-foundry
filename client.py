from client.screen import Screen


def main() -> None:
    screen = Screen()
    while screen.update():
        screen.draw()
    screen.close()


if __name__ == "__main__":
    main()
