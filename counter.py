x = " "
z = 0
yo = str(input("Welcome to counter: To start press \"enter\" twice, to get help press \"h\" Twice and to reset press \"r\" Twice: "))
y = yo.lower()
while x:
    y = input("")
    if y=="":
        z+=1
        print(z,end="\n")
    elif y=="r" or y=="rr":
        z = 0
        print("reset to",z)
    elif y=="s" or y=="ss":
        print("stop")
        break
    elif y=="h" or y =="hh":
        print("Help:\n")
        print("press \"enter key\" to start counting\n\npress \"r\" to reset the counter\n\npress \"s\" to stop the counter")
    else:
        print("Invalid choice\n")
        break
print("Thanks for using counter.\n  by rudra shah")

    