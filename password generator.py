### password generator tool ###

#made by jeff stevens
#last update: 8/14/16

def helpfunc():
    print("Press 1 to generate 10 completely random passwords")

    print("Press 2 to add specifications to random password generation")

    print("Press 3 to generate memorable, although weaker passwords")
    
    print("Press 4 to view some tips on password management and creation")

    print("Press Q to quit")

import random

password_specifications = ""

saved_pw_length = ""

response = "" #variable that temporarily holds the results of input

print("Jeff's Password Generator\nLast updated 8/8/16\n")

print("Press 1 to generate 10 completely random passwords")

print("Press 2 to add specifications to random password generation")

print("Press 3 to generate memorable, although weaker passwords")

print("Press 4 to view some tips on password management and creation")

print("Press Q to quit")

main_while_loop = True

while main_while_loop == True:

    response = input()

    if response == "1":

        available_chars = """abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-=_+[]\{}|;',./:"<>?/*"""

        list(available_chars)

        counter = 10

        while counter >= 1:

            password = ""

            password_length = random.randint(8, 13)

            while password_length >= 0:

                password += available_chars[(random.randrange(len(available_chars)))]

                password_length -= 1

            print(password + "\n")

            counter -= 1

        helpfunc()

    elif response == "2":

        print("\nDo you want to allow capital letters (Y/N)?")

        responding = True

        while responding == True:

            response = input()

            if response == "y" or response == "Y" or response == "yes":

                password_specifications = "1" #binary for True

                responding = False

            elif response == "n" or response == "N" or response == "no":

                password_specifications = "0" #binary for False

                responding = False

            else:

                print("I could not read what you just typed! Please enter y for yes or n for no.")

        print("Do you want to allow numbers (Y/N)?")

        responding = True

        while responding == True:

            response = input()

            if response == "y" or response == "Y" or response == "yes":

                password_specifications += "1"

                responding = False

            elif response == "n" or response == "N" or response == "no":

                password_specifications += "0"

                responding = False

            else:

                print("I could not read what you just typed! Please enter y for yes or n for no.")

        print("""Do you want to allow special characters: !@#$%^&*()-=_+[]\;',./{}|:"<>?/*- (Y/N)?""")

        responding = True

        while responding == True:

            response = input()

            if response == "y" or response == "Y" or response == "yes":

                password_specifications += "1"

                responding = False

            elif response == "n" or response == "N" or response == "no":

                password_specifications += "0"

                responding = False

            else:

                print("I could not read what you just typed! Please enter y for yes or n for no.")

        print("Please enter the desired length of your password")

        responding = True

        while responding == True:

            password_length = input() #will break if float or other type entered entered?

            try:

                x = int(password_length)

                if x > 0:
                
                    responding = False

                else:

                    print("You either typed zero or a negative value. Enter a valid number.")

            except:

                print("That's not a valid length, please enter a number.")
            

        available_chars = "abcdefghijklmnopqrstuvwxyz"

        if password_specifications[0] == "1":

            available_chars = available_chars + "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        if password_specifications[1] == "1":

            available_chars = available_chars + "1234567890"

        if password_specifications[2] == "1":

            available_chars = available_chars + """!@#$%^&*()-=_+[]\;',./{}|:"<>?/*-"""
            
        counter = 10

        password_length = int(password_length)

        saved_pw_length = password_length

        while counter >= 1:

            password = ""

            password_length = saved_pw_length

            while password_length >= 0:

                password += available_chars[(random.randrange(len(available_chars)))]

                password_length -= 1

            print(password + "\n")

            counter -= 1

        helpfunc()

    elif response == "3":

        with open('words.txt') as rd:

            word_list = rd.readlines()

        counter = 10

        while counter >= 1:

            password = ""

            password += str(word_list[random.randint(0,186)])

            password = password.rstrip()

            password += str(random.randint(1, 999))

            print(password + "\n")

            counter -= 1

        helpfunc()

    elif response == "4":

        print("\nTo keep track of your passwords, create a text document on your PC containing all of your passwords. Make sure it is well hidden"
              " among your other documents. I recommend using the glary utilties file encrypter to make sure your password document has its own security."
              "\nThe weaker passwords created by this program are NOT recommended for longterm/important use. Sure, you might remember them more easily, "
              "but the way they are written is specifically targeted by hacking programs in order to crack your password. This is why I suggest keeping "
              "a digital document to hold your passwords. \nIf you want to keep your passwords on a physical document, please be VERY careful. You might "
              "lose the document and another person will instantly have control of all of your online information.\n")


    elif response == "q" or response == "Q":

        quit()
    

    else:

        print("I didn't understand that!")

        helpfunc()

            

        

            
      
      

                
        
