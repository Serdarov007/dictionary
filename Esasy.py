 dictionary = {"hello" : "salam",
               "apple" : "alma",
               "lemon" : "limon",
               "cat" : "pisik",
               "dog" : "it",
               "flag" : "baydak"}

while True:
   print("""* * * My Dictionary Program * * *
    1.Show
    2.Add
    3.Edit
    4.Delate
    5.Exit""")
    saylamak = int(input("Your choice: "))
    if 1 == saylamak:
        for i,j in dictionary():
            print(i, "-", j)
    elif 2 == saylamak:
        eng = input("English word: ")
        tkm = input("Turkmen word: ")
        dictionary[eng] = tkm 
        print("Added")
    elif 3 == saylamak:
        word = input("Enter the word in english: ")
        word2 = input("Enter the wor in turkmen: ")
        dictionary[word] = word2
        print("Edited")
    elif 4 == saylamak:
        soz = input("Enter the word in englis: ")
        del dictionary[soz]
        print("Delated")
    elif 5 == saylamak:
        print("Thank you for using our site!!!")
        break
    else:
        print("Wrong comand...")