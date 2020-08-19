total_price = input("How much is the bill?")
service_level = input("How was the service? good, fair or bad?")
total_price = int(total_price)


if service_level == ("good"):
    tip_amount = (total_price * .2)
elif service_level == ("fair"):
    tip_amount = (total_price * .15)
elif service_level == ("bad"):
    tip_amount = (total_price * .1)
else:
    print("Go back and choose either good, fair or bad.")

tip_amount = int(tip_amount)
grand_total = {total_price + tip_amount}
    
print(f"Tip Amount: {tip_amount}, and your {grand_total} is your grand total.")


 