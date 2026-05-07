def explain_price(subtotal: float, customer: str, hour: int) -> str:
    kind = customer.strip().lower()

    if subtotal == 0:
        return "Subtotal: 0.00 €\nFINAL: 0.00 €"

    amount = subtotal
    text = f"Subtotal: {subtotal:.2f} €"

    if kind == "student":
        discount = amount * 0.10
        amount = amount - discount
        text = text + f"\n - Student discount (-10%): -{discount:.2f} € → {amount:.2f} €"
    elif kind == "staff":
        discount = amount * 0.25
        amount = amount - discount
        text = text + f"\n - Staff discount (-25%): -{discount:.2f} € → {amount:.2f} €"

    if hour >= 15 and hour <= 17:
        discount = amount * 0.15
        amount = amount - discount
        text = text + f"\n - Happy hour (-15%): -{discount:.2f} € → {amount:.2f} €"

    if amount >= 20:
        amount = amount - 2.00
        text = text + f"\n - Big-spender bonus (-2.00 €): -2.00 € → {amount:.2f} €"

    vat = amount * 0.19
    amount = amount + vat
    amount = round(amount, 2)
    text = text + f"\n + VAT (19%): +{vat:.2f} € → {amount:.2f} €"
    text = text + f"\nFINAL: {amount:.2f} €"
    return text


def main() -> None:
    subtotal = float(input("Subtotal: "))
    customer = input("Customer type: ")
    hour = int(input("Hour: "))
    print(explain_price(subtotal, customer, hour))


if __name__ == "__main__":
    main()
