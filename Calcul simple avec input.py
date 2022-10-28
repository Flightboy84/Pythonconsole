def main():
    walletvalue = int(input("Combien avez vous d\'argent: "))
    price = 50
    difference = walletvalue - price
    rest = ("Il vous reste :"+ str(difference))
    print(rest)
if __name__ == '__main__':
    main()
