import sys
import datetime

STOCK_PRICES = {
    "AAPL": 180.00,  # Apple
    "TSLA": 250.00,  # Tesla
    "GOOGL": 140.00, # Google
    "AMZN": 135.00,  # Amazon
    "MSFT": 330.00,  # Microsoft
    "NFLX": 450.00   # Netflix
}

def display_available_stocks():
    """Displays the list of stocks available in our hardcoded system."""
    print("\n--- Market Data (Available Stocks) ---")
    print(f"{'Ticker':<10} | {'Price ($)':<10}")
    print("-" * 25)
    for ticker, price in STOCK_PRICES.items():
        print(f"{ticker:<10} | {price:<10.2f}")
    print("-" * 25)

def get_user_portfolio():
    """
    Prompts the user to input stock tickers and quantities.
    Returns a list of dictionaries representing the portfolio.
    """
    portfolio = []
    
    print("\n--- Enter Your Portfolio ---")
    print("Type 'DONE' when finished adding stocks.")
    
    while True:
        ticker_input = input("\nEnter Stock Ticker (e.g., AAPL): ").strip().upper()
        
        if ticker_input == 'DONE':
            break
        
        if ticker_input not in STOCK_PRICES:
            print(f"❌ Error: '{ticker_input}' is not in our system. Please choose from the list above.")
            continue
            
        try:
            quantity_input = input(f"Enter quantity for {ticker_input}: ").strip()
            quantity = float(quantity_input)
            
            if quantity < 0:
                print("❌ Error: Quantity cannot be negative.")
                continue
                
            portfolio.append({
                "ticker": ticker_input,
                "quantity": quantity,
                "current_price": STOCK_PRICES[ticker_input]
            })
            print(f"✅ Added {quantity} shares of {ticker_input}.")
            
        except ValueError:
            print("❌ Error: Please enter a valid number for the quantity.")
    
    return portfolio

def calculate_portfolio_value(portfolio):
    """
    Calculates the total value for each holding and the grand total.
    Returns the total value and the detailed breakdown.
    """
    total_value = 0.0
    detailed_report = []

    for stock in portfolio:
        current_val = stock['quantity'] * stock['current_price']
        total_value += current_val
        detailed_report.append({
            "ticker": stock['ticker'],
            "quantity": stock['quantity'],
            "price": stock['current_price'],
            "total_value": current_val
        })
        
    return total_value, detailed_report

def generate_report(portfolio, total_value, detailed_report):
    """Generates a formatted string report of the portfolio."""
    report_lines = []
    report_lines.append("\n" + "="*40)
    report_lines.append("       PORTFOLIO SUMMARY REPORT       ")
    report_lines.append("="*40)
    report_lines.append(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append("-" * 40)
    report_lines.append(f"{'Ticker':<10} | {'Qty':<8} | {'Price':<8} | {'Value ($)':<10}")
    report_lines.append("-" * 40)
    
    for item in detailed_report:
        line = f"{item['ticker']:<10} | {item['quantity']:<8.1f} | {item['price']:<8.1f} | {item['total_value']:<10.2f}"
        report_lines.append(line)
        
    report_lines.append("-" * 40)
    report_lines.append(f"TOTAL PORTFOLIO VALUE: ${total_value:,.2f}")
    report_lines.append("="*40 + "\n")
    
    return "\n".join(report_lines)

def save_report_to_file(report_content, filename="portfolio_summary.txt"):
    """Saves the generated report string to a text file."""
    try:
        with open(filename, "w") as file:
            file.write(report_content)
        print(f"\n✅ Report successfully saved to '{filename}'")
    except IOError as e:
        print(f"\n❌ Error saving file: {e}")

def main():
    print("💰 WELCOME TO THE STOCK PORTFOLIO TRACKER 💰")
    
    display_available_stocks()
    
    user_portfolio = get_user_portfolio()
    
    if not user_portfolio:
        print("\nNo stocks added. Exiting program.")
        sys.exit()
        
    total_val, details = calculate_portfolio_value(user_portfolio)
    
    full_report = generate_report(user_portfolio, total_val, details)
    
    print(full_report)
    
    save_option = input("Do you want to save this report? (yes/no): ").strip().lower()
    if save_option in ['yes', 'y']:
        save_report_to_file(full_report)
    else:
        print("Report not saved.")

if __name__ == "__main__":
    main()