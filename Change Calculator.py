money = input("Enter an amount in dollars and cents: $")
money = str(round(float(money)*100))

q = int(int(money)/25)
money = str(int(money)%25)

d = int(int(money)/10)
money = str(int(money)%10)

n = int(int(money)/5)
money = str(int(money)%5)

p = int(int(money)/1)

print("The minimum number of coins is", str(q+d+n+p) + ":\n"
      + str(q), "quarters\n"
      + str(d), "dimes\n"
      + str(n), "nickels\n"
      + str(p), "pennies\n")