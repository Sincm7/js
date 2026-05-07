from datetime import datetime

from c1_lookup import name_of, price_of
from c3_discount import final_price
from c4_change import change_for


def print_item_line(code: str) -> None:
    price = price_of(code)
    if code.strip() != "" and price >= 0:
        print(f"  {name_of(code):16} {price:7.2f} €")


def print_change_line(change: dict, coin: int) -> None:
    count = change.get(coin, 0)
    if count > 0:
        if coin >= 100:
            print(f"    {count} × {coin // 100}€")
        else:
            print(f"    {count} × {coin}¢")


def total_before_tax(code1: str, code2: str, code3: str) -> float:
    price1 = price_of(code1)
    price2 = price_of(code2)
    price3 = price_of(code3)

    if price1 < 0:
        price1 = 0.0
    if price2 < 0:
        price2 = 0.0
    if price3 < 0:
        price3 = 0.0

    return price1 + price2 + price3


def print_discounts(subtotal: float, customer: str, hour: int) -> float:
    amount = subtotal
    kind = customer.strip().lower()

    if kind == "student":
        discount = amount * 0.10
        amount = amount - discount
        print(f"  Student -10%    -{discount:7.2f} €")
    elif kind == "staff":
        discount = amount * 0.25
        amount = amount - discount
        print(f"  Staff -25%      -{discount:7.2f} €")

    if hour >= 15 and hour <= 17:
        discount = amount * 0.15
        amount = amount - discount
        print(f"  Happy hour      -{discount:7.2f} €")

    if amount >= 20:
        amount = amount - 2.00
        print("  Big spender     -   2.00 €")

    if amount < 0:
        amount = 0.0

    return amount


def print_receipt(code1: str, code2: str, code3: str, customer: str, hour: int, paid: float) -> None:
    subtotal = total_before_tax(code1, code2, code3)
    total = final_price(subtotal, customer, hour)
    change = change_for(total, paid)

    if change is None:
        print("Payment is too low. No receipt printed.")
        return

    print("==============================")
    print("       CAFÉ LAMBDA")
    print("  " + datetime.now().strftime("%Y-%m-%d %H:%M"))
    print("------------------------------")
    print_item_line(code1)
    print_item_line(code2)
    print_item_line(code3)
    print("------------------------------")
    print(f"  Subtotal        {subtotal:7.2f} €")
    discounted = print_discounts(subtotal, customer, hour)
    vat = total - discounted
    print(f"  VAT 19%         {vat:7.2f} €")
    print(f"  TOTAL           {total:7.2f} €")
    print(f"  Paid            {paid:7.2f} €")
    print(f"  Change          {paid - total:7.2f} €")
    print_change_line(change, 500)
    print_change_line(change, 200)
    print_change_line(change, 100)
    print_change_line(change, 50)
    print_change_line(change, 20)
    print_change_line(change, 10)
    print_change_line(change, 5)
    print_change_line(change, 2)
    print_change_line(change, 1)
    print("==============================")
    print(f"    Thank you, {customer.strip().lower()}!")
    print("==============================")


def main() -> None:
    code1 = input("Code 1: ")
    code2 = input("Code 2: ")
    code3 = input("Code 3: ")
    customer = input("Customer type: ")
    hour = int(input("Hour: "))
    paid = float(input("Paid: "))
    print_receipt(code1, code2, code3, customer, hour, paid)


if __name__ == "__main__":
    main()
