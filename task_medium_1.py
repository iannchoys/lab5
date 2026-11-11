import tkinter as tk


def create_app() -> tk.Tk:
    """Создать окно с кнопкой «Привет»."""
    root = tk.Tk()
    root.title("Задание №1 — Привет")
    root.geometry("320x180")

    label = tk.Label(root, text="Нажмите кнопку")
    label.pack(pady=(35, 15))

    def say_hello() -> None:
        label.config(text="Привет!")

    button = tk.Button(
        root,
        text="Привет",
        command=say_hello,
    )
    button.pack()

    return root


if __name__ == "__main__":
    create_app().mainloop()
