total_price = input("How much is the bill? ")
service_level = input("How was the service? good, fair or bad? ")
split_quantity = input("Split between how many people? ")
total_price = float(total_price)
split_quantity = int(split_quantity)


if service_level == ("good"):
    tip_amount = (total_price * .2)
elif service_level == ("fair"):
    tip_amount = (total_price * .15)
elif service_level == ("bad"):
    tip_amount = (total_price * .1)
else:
    print("Go back and choose either good, fair or bad. ")

tip_amount = float(tip_amount)
grand_total = (total_price + tip_amount)
grand_total = float(grand_total)
per_person = (grand_total / split_quantity)

print(f'Your tip amount is {tip_amount}.')
print(f' Your grand total is {grand_total}.')
print(f' Your amount per person is {per_person}. ')



