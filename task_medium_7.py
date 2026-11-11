import tkinter as tk


def create_app() -> tk.Tk:
    """Создать окно с меню File → Exit."""
    root = tk.Tk()
    root.title("Задание №7 — Меню")
    root.geometry("360x200")

    menu_bar = tk.Menu(root)

    file_menu = tk.Menu(
        menu_bar,
        tearoff=0,
    )
    file_menu.add_command(
        label="Exit",
        command=root.destroy,
    )

    menu_bar.add_cascade(
        label="File",
        menu=file_menu,
    )

    root.config(menu=menu_bar)

    label = tk.Label(
        root,
        text="Для выхода выберите File → Exit",
    )
    label.pack(expand=True)

    return root


if __name__ == "__main__":
    create_app().mainloop()
