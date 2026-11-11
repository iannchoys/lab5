import subprocess
import sys
import tkinter as tk
from pathlib import Path
from tkinter import ttk


TASKS = (
    (
        "Среднее №1 — кнопка «Привет»",
        "task_medium_1.py",
    ),
    (
        "Среднее №5 — вкладки Notebook",
        "task_medium_5.py",
    ),
    (
        "Среднее №7 — меню File → Exit",
        "task_medium_7.py",
    ),
    (
        "Повышенное №6 — конвертер валют",
        "task_hard_6.py",
    ),
    (
        "Повышенное №8 — несколько окон",
        "task_hard_8.py",
    ),
)


def run_task(filename: str) -> None:
    """Запустить выбранное задание отдельным процессом."""
    script_path = Path(__file__).with_name(filename)

    subprocess.Popen(
        [
            sys.executable,
            str(script_path),
        ]
    )


def main() -> None:
    """Создать окно запуска заданий лабораторной работы №5."""
    root = tk.Tk()
    root.title("Лабораторная работа №5 — вариант 5")
    root.geometry("460x390")

    ttk.Label(
        root,
        text="Выберите задание",
        font=("TkDefaultFont", 14, "bold"),
    ).pack(
        pady=(25, 15),
    )

    for title, filename in TASKS:
        ttk.Button(
            root,
            text=title,
            command=lambda file=filename: run_task(file),
        ).pack(
            fill="x",
            padx=35,
            pady=6,
        )

    ttk.Button(
        root,
        text="Выход",
        command=root.destroy,
    ).pack(
        pady=20,
    )

    root.mainloop()


if __name__ == "__main__":
    main()
