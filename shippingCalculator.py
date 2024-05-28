# Input the weight from the user
weight = float(input("Enter the weight of the package: "))

# Shipping PREMIUM
shipping_cost_premium = 125.0

# Ground Shipping
if weight <= 2:
  shipping_cost = weight * 1.5 + 20.00
elif weight <= 6:
  shipping_cost = weight * 3.00 + 20.00
elif weight <= 10:
  shipping_cost = weight * 4.00 + 20.00
else:
  shipping_cost = weight * 4.75 + 20.00

print("Ground Shipping $", shipping_cost)

# Ground Shipping Premium
print("Ground Shipping Premium $", shipping_cost_premium)

# Drone Shipping (New)
if weight <= 2:
  drone_shipping_cost = weight * 4.50 + 0.00
elif weight <= 6:
  drone_shipping_cost = weight * 9.00 + 0.00
elif weight <= 10:
  drone_shipping_cost = weight * 12.00 + 0.00
else:
  drone_shipping_cost = weight * 14.25 + 0.00
  
print("Drone Shipping $", drone_shipping_cost)