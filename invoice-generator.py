import math

print("=== FREELANCE INVOICE GENERATOR ===")

# 1. Gather Input
project_name = input("Enter project name: ")

# Do-while pattern: Python has no native do-while, so we use
# "while True" + "break" to guarantee the prompt runs at least once,
# then keep looping until the user gives a valid positive number.
while True:
    rate_input = input("Enter your hourly rate ($): ")
    if rate_input.replace(".", "", 1).isdigit() and float(rate_input) > 0:
        hourly_rate = float(rate_input)
        break
    print("Please enter a positive number (e.g. 25 or 25.50).")

while True:
    hours_input = input("Enter hours worked: ")
    if hours_input.replace(".", "", 1).isdigit() and float(hours_input) > 0:
        hours_worked = float(hours_input)
        break
    print("Please enter a positive number (e.g. 10 or 10.5).")

# 2. Math Calculations
subtotal = hourly_rate * hours_worked

# Augmented operator to add a 2.5% platform fee (subtotal * 1.025)
total_billed = subtotal
total_billed *= 1.025

# math.ceil to round tax withholding up to the nearest whole dollar
tax_withholding = math.ceil(total_billed * 0.25)
take_home_pay = total_billed - tax_withholding

# 3. Formatted Output (F-Strings)
print(f"\n--- INVOICE FOR: {project_name.title()} ---")
print(f"Subtotal:         ${subtotal:,.2f}") #2f is for 2 decimal places, since we are dealing with money
print(f"Total Billed:     ${total_billed:,.2f} (Includes 2.5% fee)")
print(f"Tax Withholding:  ${tax_withholding:,} (25% rounded up)")
print(f"Net Take-Home:    ${take_home_pay:,.2f}")
print("---------------------------------------")