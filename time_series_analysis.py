# List of stock prices for $AMC stock in January 2023 (weekdays only)
stock_prices = [34.68, 36.09, 34.94, 33.97, 34.68, 35.82, 43.41, 44.29, 44.65, 53.56, 
                49.85, 48.71, 48.71, 49.94, 48.53, 47.03, 46.59, 48.62, 44.21, 47.21]

# Function to get the price on a specific day x
def price_at(x):
    if 1 <= x <= len(stock_prices):
        return stock_prices[x - 1]  # Adjusting index to match day
    else:
        return "Invalid day, please enter a day between 1 and 20."

# Function to get the maximum price between day a and day b
def max_price(a, b):
    if 1 <= a <= len(stock_prices) and 1 <= b <= len(stock_prices) and a <= b:
        return max(stock_prices[a - 1:b])  
    else:
        return "Invalid range of days."

# Function to get the minimum price between day a and day b
def min_price(a, b):
    if 1 <= a <= len(stock_prices) and 1 <= b <= len(stock_prices) and a <= b:
        return min(stock_prices[a - 1:b]) 
    else:
        return "Invalid range of days."

# Test the functions
print(f"Price on day 5: {price_at(5)}")  # Output: 34.68
print(f"Max price from day 5 to day 10: {max_price(5, 10)}") 
print(f"Min price from day 5 to day 10: {min_price(5, 10)}")  
