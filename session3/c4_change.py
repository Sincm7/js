from typing import Optional


def take_coin(wallet: dict, remaining: int, coin: int) -> int:
    count = remaining // coin
    if count > 0:
        wallet[coin] = count
    return remaining % coin


def make_change(amount_cents: int) -> dict:
    wallet = {}
    amount_cents = take_coin(wallet, amount_cents, 500)
    amount_cents = take_coin(wallet, amount_cents, 200)
    amount_cents = take_coin(wallet, amount_cents, 100)
    amount_cents = take_coin(wallet, amount_cents, 50)
    amount_cents = take_coin(wallet, amount_cents, 20)
    amount_cents = take_coin(wallet, amount_cents, 10)
    amount_cents = take_coin(wallet, amount_cents, 5)
    amount_cents = take_coin(wallet, amount_cents, 2)
    amount_cents = take_coin(wallet, amount_cents, 1)
    return wallet


def change_for(price: float, paid: float) -> Optional[dict]:
    price_cents = round(price * 100)
    paid_cents = round(paid * 100)

    if paid_cents < price_cents:
        return None
    else:
        return make_change(paid_cents - price_cents)


def coin_text(coin: int, count: int) -> str:
    if coin >= 100:
        return f"{count} × {coin // 100}€"
    else:
        return f"{count} × {coin}¢"


def add_line(text: str, change: dict, coin: int) -> str:
    count = change.get(coin, 0)
    if count > 0:
        if text == "":
            return coin_text(coin, count)
        else:
            return text + ", " + coin_text(coin, count)
    else:
        return text


def format_change(change: dict) -> str:
    text = ""
    text = add_line(text, change, 500)
    text = add_line(text, change, 200)
    text = add_line(text, change, 100)
    text = add_line(text, change, 50)
    text = add_line(text, change, 20)
    text = add_line(text, change, 10)
    text = add_line(text, change, 5)
    text = add_line(text, change, 2)
    text = add_line(text, change, 1)

    if text == "":
        return "no change"
    else:
        return text


def main() -> None:
    price = float(input("Price: "))
    paid = float(input("Paid: "))
    change = change_for(price, paid)

    if change is None:
        print("Not enough money paid.")
    else:
        print(format_change(change))


if __name__ == "__main__":
    main()
