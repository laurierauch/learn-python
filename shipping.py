weight = 41.5
gs_flat_charge = 20.00
gs_premium_flat_charge = 125.00

# ground shipping

if weight <= 2:
  gs_price = weight * 1.50
elif weight > 2 and weight <= 6:
  gs_price = weight * 3.00
elif weight > 6 and weight <= 10:
  gs_price = weight * 4.00
elif weight > 10:
  gs_price = weight * 4.75

gs_cost = gs_price + gs_flat_charge
gsp_cost = gs_price + gs_premium_flat_charge
print("Ground Shipping: $" + str(gs_cost))

print("Ground Shipping Premium: $" + str(gsp_cost))

# drone shipping

if weight <= 2:
  ds_price = weight * 4.50
elif weight > 2 and weight <= 6:
  ds_price = weight * 9.00
elif weight > 6 and weight <= 10:
  ds_price = weight * 12.00
elif weight > 10:
  ds_price = weight * 14.25

print("Drone Shipping: $" + str(ds_price))
