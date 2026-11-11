import tkinter as tk
from tkinter import messagebox, ttk


RATES_TO_RUB = {
    "RUB": 1.0,
    "USD": 80.0,
    "EUR": 92.0,
    "CNY": 11.2,
}


def convert_currency(
    amount: float,
    source: str,
    target: str,
) -> float:
    """Конвертировать сумму между валютами."""
    if amount < 0:
        raise ValueError(
            "Сумма не может быть отрицательной."
        )

    rubles = amount * RATES_TO_RUB[source]
    return rubles / RATES_TO_RUB[target]


def create_app() -> tk.Tk:
    """Создать графический конвертер валют."""
    root = tk.Tk()
    root.title("Повышенное №6 — Конвертер валют")
    root.geometry("430x300")

    frame = ttk.Frame(root, padding=20)
    frame.pack(
        expand=True,
        fill="both",
    )

    ttk.Label(
        frame,
        text="Сумма:",
    ).grid(
        row=0,
        column=0,
        sticky="w",
        pady=5,
    )

    amount_entry = ttk.Entry(frame)
    amount_entry.grid(
        row=0,
        column=1,
        sticky="ew",
        pady=5,
    )
    amount_entry.insert(0, "100")

    currencies = tuple(RATES_TO_RUB)

    ttk.Label(
        frame,
        text="Из валюты:",
    ).grid(
        row=1,
        column=0,
        sticky="w",
        pady=5,
    )

    source_box = ttk.Combobox(
        frame,
        values=currencies,
        state="readonly",
    )
    source_box.grid(
        row=1,
        column=1,
        sticky="ew",
        pady=5,
    )
    source_box.set("USD")

    ttk.Label(
        frame,
        text="В валюту:",
    ).grid(
        row=2,
        column=0,
        sticky="w",
        pady=5,
    )

    target_box = ttk.Combobox(
        frame,
        values=currencies,
        state="readonly",
    )
    target_box.grid(
        row=2,
        column=1,
        sticky="ew",
        pady=5,
    )
    target_box.set("RUB")

    result_label = ttk.Label(
        frame,
        text="Результат: —",
    )
    result_label.grid(
        row=4,
        column=0,
        columnspan=2,
        pady=(15, 5),
    )

    ttk.Label(
        frame,
        text="Используются учебные фиксированные курсы.",
    ).grid(
        row=5,
        column=0,
        columnspan=2,
        pady=5,
    )

    def perform_conversion() -> None:
        try:
            amount = float(amount_entry.get())

            result = convert_currency(
                amount,
                source_box.get(),
                target_box.get(),
            )

        except (ValueError, KeyError):
            messagebox.showerror(
                "Ошибка",
                "Введите корректную сумму и выберите валюты.",
            )
            return

        result_label.config(
            text=f"Результат: {result:.2f}"
        )

    convert_button = ttk.Button(
        frame,
        text="Конвертировать",
        command=perform_conversion,
    )
    convert_button.grid(
        row=3,
        column=0,
        columnspan=2,
        pady=10,
    )

    frame.columnconfigure(1, weight=1)

    return root


if __name__ == "__main__":
    create_app().mainloop()
