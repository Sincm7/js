from c1_lookup import price_of


def price_or_zero(code: str) -> float:
    clean = code.strip()
    if clean == "":
        return 0.0

    price = price_of(clean)
    if price < 0:
        return 0.0
    else:
        return price


def add_vat(net: float, rate: float = 0.19) -> float:
    return net + net * rate


def order_total(code1: str, code2: str, code3: str) -> float:
    part1 = price_or_zero(code1)
    part2 = price_or_zero(code2)
    part3 = price_or_zero(code3)
    return round(add_vat(part1 + part2 + part3), 2)


def warn_if_unknown(code: str) -> None:
    clean = code.strip()
    if clean != "" and price_of(clean) < 0:
        print(f"Unknown code ignored: {clean}")


def main() -> None:
    code1 = input("Item 1: ")
    code2 = input("Item 2: ")
    code3 = input("Item 3: ")

    warn_if_unknown(code1)
    warn_if_unknown(code2)
    warn_if_unknown(code3)

    subtotal = price_or_zero(code1) + price_or_zero(code2) + price_or_zero(code3)
    total = order_total(code1, code2, code3)
    print(f"Subtotal: {subtotal:.2f} €")
    print(f"Total with VAT: {total:.2f} €")


if __name__ == "__main__":
    main()
