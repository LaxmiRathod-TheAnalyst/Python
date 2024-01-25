known_users = ["Alice","Bob","Claire","Dan","Emma","Fred","Georgie","Harry"]
print(len(known_users)) #to know the number of elements in the list

while True: # run the code over and over again
    print("Hi! My name is Travis")
    name = input("What is your name?: ").strip().capitalize()#multiple methods and capitalize is used to save the name entered in capital

    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("would you like to be removed from the system (y/n)?: ").strip().lower()

        if remove == "y":
            known_users.remove(name)
        elif remove == "n":
            print("No problem, I didn't want you to leave anyway!")
        
            

    else:
        print("Hmmm I don't think i have met you yet {} ".format(name))
        add_me = input("Would you like to be added to the system (y/n)?: ").strip().lower()
        if add_me =="y":
            known_users.append(name) # add elements to the list using append()
        elif add_me == "n":
            print("No worries, see you around!")
        
            
         






        
