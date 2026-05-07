def customer_discount(subtotal: float, customer: str) -> float:
    kind = customer.strip().lower()

    if kind == "student":
        return subtotal * 0.90
    elif kind == "staff":
        return subtotal * 0.75
    else:
        return subtotal


def happy_hour_discount(amount: float, hour: int) -> float:
    if hour >= 15 and hour <= 17:
        return amount * 0.85
    else:
        return amount


def big_spender_bonus(amount: float) -> float:
    if amount >= 20:
        new_amount = amount - 2.00
        return new_amount
    else:
        return amount


def add_vat(net: float) -> float:
    return net + net * 0.19


def final_price(subtotal: float, customer: str, hour: int) -> float:
    after_customer = customer_discount(subtotal, customer)
    after_hour = happy_hour_discount(after_customer, hour)
    amount = big_spender_bonus(after_hour)

    if amount < 0:
        amount = 0.0

    return round(add_vat(amount), 2)


def main() -> None:
    subtotal = float(input("Subtotal: "))
    customer = input("Customer type: ")
    hour = int(input("Hour: "))

    kind = customer.strip().lower()
    if kind != "student" and kind != "staff" and kind != "regular":
        print("Unknown customer type, no discount used.")

    total = final_price(subtotal, customer, hour)
    print(f"Final price: {total:.2f} €")


if __name__ == "__main__":
    main()
