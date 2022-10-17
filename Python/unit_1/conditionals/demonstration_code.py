
has_coupon = False
total_price = 80

if total_price >= 100 and has_coupon:
    final_price = total_price * .5 # 96 * 1.1 + 96 + 9.6 105.6
elif total_price >= 100:
    final_price = total_price * .8
elif has_coupon:
    final_price = abs(total_price - 10)
else:
    final_price = total_price

# we need to add
final_price *= 1.1

print(final_price)