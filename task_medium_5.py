import tkinter as tk
from tkinter import ttk


def create_app() -> tk.Tk:
    """Создать программу с вкладками Notebook."""
    root = tk.Tk()
    root.title("Задание №5 — Вкладки")
    root.geometry("420x240")

    notebook = ttk.Notebook(root)
    notebook.pack(
        expand=True,
        fill="both",
        padx=10,
        pady=10,
    )

    first_tab = ttk.Frame(notebook)
    second_tab = ttk.Frame(notebook)
    third_tab = ttk.Frame(notebook)

    notebook.add(first_tab, text="Главная")
    notebook.add(second_tab, text="Информация")
    notebook.add(third_tab, text="Настройки")

    ttk.Label(
        first_tab,
        text="Это главная вкладка.",
    ).pack(padx=20, pady=30)

    ttk.Label(
        second_tab,
        text="Лабораторная работа №5, вариант 5.",
    ).pack(padx=20, pady=30)

    ttk.Label(
        third_tab,
        text="Здесь могут находиться настройки.",
    ).pack(padx=20, pady=30)

    return root


if __name__ == "__main__":
    create_app().mainloop()
