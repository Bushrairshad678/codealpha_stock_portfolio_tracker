# Stock Portfolio Tracker

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 300,
    "AMZN": 200
}

total = 0

print("Available Stocks:")
for stock in stocks:
    print(stock)

while True:
    name = input("\nEnter Stock Name (or 'done' to finish): ").upper()

    if name == "DONE":
        break

    if name in stocks:
        quantity = int(input("Enter Quantity: "))
        investment = stocks[name] * quantity
        total += investment
        print("Investment =", investment)
    else:
        print("Stock not found!")

print("\nTotal Investment =", total)

file = open("portfolio.txt", "w")
file.write("Total Investment = " + str(total))
file.close()

print("Result saved in portfolio.txt")