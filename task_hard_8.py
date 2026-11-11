import tkinter as tk
from tkinter import ttk


def open_child_window(parent: tk.Misc) -> None:
    """Открыть дополнительное окно приложения."""
    child = tk.Toplevel(parent)
    child.title("Второе окно")
    child.geometry("300x160")

    ttk.Label(
        child,
        text="Это второе окно приложения.",
    ).pack(
        pady=(35, 15),
    )

    ttk.Button(
        child,
        text="Закрыть",
        command=child.destroy,
    ).pack()


def create_app() -> tk.Tk:
    """Создать приложение с несколькими окнами."""
    root = tk.Tk()
    root.title("Повышенное №8 — Несколько окон")
    root.geometry("360x220")

    ttk.Label(
        root,
        text="Главное окно приложения",
    ).pack(
        pady=(45, 20),
    )

    ttk.Button(
        root,
        text="Открыть второе окно",
        command=lambda: open_child_window(root),
    ).pack()

    return root


if __name__ == "__main__":
    create_app().mainloop()
