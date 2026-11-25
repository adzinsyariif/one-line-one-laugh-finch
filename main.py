import os

LINE = "My houseplants have a group chat, and I'm only in it so they can talk about me to my face."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
