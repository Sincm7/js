from menu import MENU


def normal_code(code: str) -> str:
    return code.strip().upper()


def find_item(code: str) -> dict:
    code = normal_code(code)
    return MENU.get(code, {})


def price_of(code: str) -> float:
    item = find_item(code)
    price = item.get("price", -1.0)
    return price


def name_of(code: str) -> str:
    item = find_item(code)
    return item.get("name", "unknown")


def category_of(code: str) -> str:
    item = find_item(code)
    return item.get("category", "unknown")


def describe(code: str) -> str:
    price = price_of(code)
    if price < 0:
        return "unknown item"
    else:
        return f"{name_of(code)} ({category_of(code)}), {price:.2f} €"


def main() -> None:
    code = input("Code: ")
    price = price_of(code)
    if price < 0:
        print("Unknown item.")
    else:
        print(f"That costs {price:.2f} €")


if __name__ == "__main__":
    main()
