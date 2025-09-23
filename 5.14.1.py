def nerd():

    a = input("Respond with a number 0-6")

    if a == "0":
        print("You selected Sunday.")
    elif a == "1":
        print("You selected Monday.")
    elif a == "2":
        print("You selected Tuesday.")
    elif a == "3":
        print("You selected Wednesday.")
    elif a == "4":
        print("You selected Thursday.")
    elif a == "5":
        print("You selected Friday.")
    elif a == "6":
        print("You selected Saturday.")
    elif a != "0" or "1" or "2" or "3" or "4" or "5" or "6":
        print("You did not select anything. Try again.")
nerd()
