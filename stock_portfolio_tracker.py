

STOCK_PRICES = {
    "AAPL": 180.00,
    "TSLA": 250.00,
    "GOOGL": 165.00,
    "MSFT": 420.00,
    "AMZN": 190.00,
}


def main():
    print("=" * 42)
    print("       STOCK PORTFOLIO TRACKER")
    print("=" * 42)
    print("\nAvailable stocks:")
    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol}: ${price:.2f} per share")

    portfolio = []
    total_investment = 0.0

    while True:
        symbol = input("\nEnter a stock symbol (or 'done' to finish): ").strip().upper()

        if symbol == "DONE":
            break

        if symbol not in STOCK_PRICES:
            print("Sorry, that stock is not in the list. Please try again.")
            continue

        try:
            quantity = int(input(f"How many shares of {symbol} do you own? "))
            if quantity <= 0:
                print("Quantity must be greater than zero.")
                continue
        except ValueError:
            print("Please enter a whole number for the quantity.")
            continue

        price = STOCK_PRICES[symbol]
        value = price * quantity
        total_investment += value
        portfolio.append((symbol, quantity, price, value))
        print(f"{quantity} share(s) of {symbol} = ${value:,.2f}")

    print("\n" + "=" * 42)
    print("PORTFOLIO SUMMARY")
    print("=" * 42)

    if not portfolio:
        print("No stocks were added.")
    else:
        print(f"{'Stock':<10}{'Quantity':>10}{'Price':>10}{'Value':>12}")
        print("-" * 42)
        for symbol, quantity, price, value in portfolio:
            print(f"{symbol:<10}{quantity:>10}{price:>10.2f}{value:>12.2f}")
        print("-" * 42)
        print(f"Total investment: ${total_investment:,.2f}")

        save = input("\nSave this summary to portfolio.txt? (yes/no): ").strip().lower()
        if save in ("yes", "y"):
            with open("portfolio.txt", "w", encoding="utf-8") as file:
                file.write("STOCK PORTFOLIO SUMMARY\n")
                file.write("=" * 30 + "\n")
                for symbol, quantity, price, value in portfolio:
                    file.write(
                        f"{symbol}: {quantity} shares x ${price:.2f} = ${value:.2f}\n"
                    )
                file.write(f"\nTotal investment: ${total_investment:.2f}\n")
            print("Summary saved as portfolio.txt.")

    print("\nThanks for using Stock Portfolio Tracker!")


if __name__ == "__main__":
    main()
