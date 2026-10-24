import csv
from datetime import datetime

# Store portfolio details
portfolio = []

print("=" * 45)
print("       STOCK PORTFOLIO PERFORMANCE TRACKER")
print("=" * 45)

while True:
    ticker = input("\nEnter stock ticker (or 'done' to finish): ").upper()

    if ticker == "DONE":
        break

    try:
        buy_price = float(input("Enter buy price per share: "))
        quantity = int(input("Enter number of shares: "))
        current_price = float(input("Enter current price per share: "))

        if buy_price <= 0 or quantity <= 0 or current_price < 0:
            print("Please enter valid positive values.")
            continue

        # Calculate investment and current value
        invested = buy_price * quantity
        current_value = current_price * quantity

        # Calculate profit or loss
        profit_loss = current_value - invested
        percentage = (profit_loss / invested) * 100

        # Store stock details
        stock = {
            "Ticker": ticker,
            "Buy Price": buy_price,
            "Quantity": quantity,
            "Current Price": current_price,
            "Invested": invested,
            "Current Value": current_value,
            "Profit/Loss": profit_loss,
            "Percentage": percentage
        }

        portfolio.append(stock)

        print("\nStock added successfully!")

    except ValueError:
        print("Invalid input! Please enter numbers correctly.")

# Display portfolio summary
if portfolio:

    total_invested = sum(stock["Invested"] for stock in portfolio)
    total_value = sum(stock["Current Value"] for stock in portfolio)
    total_profit_loss = total_value - total_invested

    print("\n" + "=" * 65)
    print("              PORTFOLIO SUMMARY")
    print("=" * 65)

    print(f"{'Ticker':<10}{'Invested':>12}{'Current Value':>16}"
          f"{'Profit/Loss':>15}")

    print("-" * 65)

    for stock in portfolio:
        print(
            f"{stock['Ticker']:<10}"
            f"{stock['Invested']:>12.2f}"
            f"{stock['Current Value']:>16.2f}"
            f"{stock['Profit/Loss']:>15.2f}"
        )

    print("-" * 65)

    print(f"Total Investment : Rs. {total_invested:.2f}")
    print(f"Current Value   : Rs. {total_value:.2f}")
    print(f"Total Profit/Loss: Rs. {total_profit_loss:.2f}")

    if total_invested > 0:
        total_percentage = (
            total_profit_loss / total_invested
        ) * 100

        print(f"Overall Return  : {total_percentage:.2f}%")

    # Save results to CSV file
    filename = "portfolio_summary.csv"

    fieldnames = [
        "Ticker",
        "Buy Price",
        "Quantity",
        "Current Price",
        "Invested",
        "Current Value",
        "Profit/Loss",
        "Percentage"
    ]

    with open(filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(portfolio)

    print(f"\nPortfolio saved successfully to {filename}")

else:
    print("\nNo stocks were added to the portfolio.")