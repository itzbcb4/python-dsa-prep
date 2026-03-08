def main():
    name = input("What's your name?")
    greet(name)
    price = float(input("What's the price of the item? "))
    print(f"The total price with tax is: {format_total(price)}")

def greet(x):
  print("Hello,",x)

def format_total(price, tax_rate=0.07):
  total = price + (price * tax_rate)
  return total

main()
