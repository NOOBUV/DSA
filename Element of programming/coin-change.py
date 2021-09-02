def coin_change():
    coins = input("Enter coins array: ").split()
    amount = int(input("Enter amount to be changed: "))
    coins = [int(i) for i in coins]
    coins.sort()
    coins.reverse()
    num_coins = 0
    for coin in coins:
        num_coins += amount//coin
        amount %= coin
    print(num_coins)


coin_change()
