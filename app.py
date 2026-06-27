import requests

print("=" * 55)
print("        🌍 Currency Exchange Converter 🌍")
print("=" * 55)

try:
    from_currency = input("Enter source currency (Example: USD): ").upper().strip()
    to_currency = input("Enter target currency (Example: INR): ").upper().strip()
    amount = float(input("Enter amount: "))

    url = f"https://open.er-api.com/v6/latest/{from_currency}"

    response = requests.get(url)
    data = response.json()

    if data["result"] != "success":
        print("\n❌ Invalid source currency code.")
    elif to_currency not in data["rates"]:
        print("\n❌ Invalid target currency code.")
    else:
        exchange_rate = data["rates"][to_currency]
        converted_amount = amount * exchange_rate

        print("\n" + "=" * 55)
        print("              Conversion Result")
        print("=" * 55)
        print(f"From Currency : {from_currency}")
        print(f"To Currency   : {to_currency}")
        print(f"Amount        : {amount:.2f}")
        print(f"Exchange Rate : 1 {from_currency} = {exchange_rate:.4f} {to_currency}")
        print(f"Converted     : {converted_amount:.2f} {to_currency}")
        print("=" * 55)

except ValueError:
    print("\n❌ Please enter a valid numeric amount.")

except requests.exceptions.ConnectionError:
    print("\n❌ No internet connection.")

except Exception as e:
    print(f"\n❌ Something went wrong: {e}")