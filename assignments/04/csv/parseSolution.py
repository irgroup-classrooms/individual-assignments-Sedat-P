import re
from collections import Counter

def main():
    # Read the CSV file with the product orders
    with open('C:/Users/ismai/Desktop/dis8/orders.csv') as f_in:
        text = f_in.read()
    
    # Extract all order numbers
    order_numbers = re.findall(r'\d+', text)
    print("Order Numbers:", order_numbers)
    
    # Extract all product names
    product_names = re.findall(r'[a-zA-Z ]+', text)
    print("Product Names:", product_names)
    
    # Extract all prices
    prices = re.findall(r'\$\d+\.\d{2}', text)
    print("Prices:", prices)
    
    # Extract all order dates
    dates = re.findall(r'\d{4}-\d{2}-\d{2}', text)
    print("Order Dates:", dates)
    
    # Filter products priced over $500
    high_price_orders = [price for price in prices if float(price[1:]) > 500]
    print("Products over $500:", high_price_orders)
    
    # Change date format from YYYY-MM-DD to DD/MM/YYYY
    formatted_dates = [re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3/\2/\1', date) for date in dates]
    print("Formatted Dates (DD/MM/YYYY):", formatted_dates)
    
    # Extract product names with more than 6 characters
    long_product_names = [name for name in product_names if len(name) > 6]
    print("Product Names with more than 6 characters:", long_product_names)
    
    # Count the occurrence of each product
    product_count = Counter(product_names)
    print("Product Count:", dict(product_count))
    
    # Extract orders with prices ending in .99
    prices_ending_in_99 = [price for price in prices if price.endswith('.99')]
    print("Prices ending in .99:", prices_ending_in_99)
    
    # Find the cheapest product
    prices_float = [float(price[1:]) for price in prices]  # Convert price strings to float
    cheapest_price = min(prices_float)
    print("Cheapest Price:", f"${cheapest_price:.2f}")

if __name__ == '__main__':
    main()
