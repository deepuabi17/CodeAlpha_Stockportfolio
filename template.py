import requests

class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            self.portfolio[symbol]['quantity'] += quantity
        else:
            self.portfolio[symbol] = {'quantity': quantity, 'price': self.get_current_price(symbol)}

    def remove_stock(self, symbol, quantity):
        if symbol in self.portfolio:
            if quantity >= self.portfolio[symbol]['quantity']:
                del self.portfolio[symbol]
            else:
                self.portfolio[symbol]['quantity'] -= quantity

    def get_current_price(self, symbol):
        # Replace 'YOUR_API_KEY' with your Alpha Vantage API key
        api_key = 'YOUR_API_KEY'
        url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}'
        response = requests.get(url)
        data = response.json()
        return float(data['Global Quote']['05. price'])

    def get_portfolio_value(self):
        total_value = 0
        for symbol, stock in self.portfolio.items():
            total_value += stock['quantity'] * stock['price']
        return total_value

    def display_portfolio(self):
        print("Stock Portfolio:")
        for symbol, stock in self.portfolio.items():
            print(f"{symbol}: Quantity - {stock['quantity']}, Price - ${stock['price']:.2f}")

if __name__ == "__main__":
    portfolio = StockPortfolio()
    while True:
        print("\nMenu:")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Display Portfolio")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            portfolio.add_stock(symbol, quantity)
        elif choice == '2':
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity to remove: "))
            portfolio.remove_stock(symbol, quantity)
        elif choice == '3':
            portfolio.display_portfolio()
            print(f"Total Portfolio Value: ${portfolio.get_portfolio_value():.2f}")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a valid option.")
