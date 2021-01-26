#question one options A||B
#   if A
    # question two_A
        #options C||D
    #question three_A
        #options E||F
#   if B
    #question two_B
        #options G||F
    #question three_B
        #options H||j





#ask init question
ask_looks_power = ""
print("You are deciding what parts to get to upgrade your car.\nWhat type of upgrade do you want to start with\n")
ask_looks_power = str(input("AESTHETIC or POWER : ").upper())
"""
When troubleshooting, this statement should be an and not an or.  
This makes no sense.
Saving this comment to refer to later when I make the same error
"""
while (ask_looks_power != "AESTHETIC") and (ask_looks_power != "POWER"):
    print("ASK LOOK POWER : " + ask_looks_power)
    print(type(ask_looks_power))
    print("You did not pick a valid option. Please choose one of the examples from below : ")
    ask_looks_power = input("AESTHETIC or POWER : ")

#CHOSEN AESTHETIC
if(ask_looks_power.upper() == "AESTHETIC"):
    print("Good choice. Would you like to upgrade your wheels and coilovers,\n or would you like to upgrade body panels to carbon fiber?")
    looks_choice = input("STANCE or CARBON : ").upper()
    while looks_choice != "STANCE" and looks_choice != "CARBON":
            print("You did not pick a valid option. Please choose one of the examples from below : ")
            ask_looks_power = input("STANCE or CARBON : ")
    #CHOSE STANCE
    if(looks_choice == "STANCE"):
        print("Awesome! Would you like to do a widebody kit with that,\n or would you like to wrap the car a new color? : ")
        looks_choice_two = input("WIDEBODY or WRAP : ").upper()
        #CHOSE WIDEBODY
        while looks_choice_two != "WIDEBODY" and looks_choice_two != "WRAP":
            print("You did not pick a valid option. Please choose one of the examples from below : ")
            ask_looks_power = input("WIDEBODY or WRAP : ")
        if(looks_choice_two == "WIDEBODY"):
            print("You have chosen to upgrade your car with a some new wheels, new coilovers, and a sweet new widebody kit!")
        #CHOSE WRAP
        else: 
            print("You have chosen to upgrade your car with a some new wheels, new coilovers, and a sweet new wrap!")
    #CHOSE CARBON
    else : 
        print("Awesome! To go with that carbon, would you like to get matching carbon seats,\n or would you like to get some suede seats?")
        looks_choice_two = input("CARBON or SUEDE : ").upper()
        if looks_choice_two == "CARBON" :
            print("You have chosen to upgrade your car with some awesome new carbon fiber parts that look super sweet!")
        else:
            print("You have chosen to upgrade your car with carbon on the outside and beautiful suede on the inside!")
#CHOSEN POWER
else :
    print("Would you like to turbo or super charge your car")
    tubo_super = input("TURBO or SUPER : ").upper()
    while turbo_super != "TURBO" and tubo_super != "SUPER":
            print("You did not pick a valid option. Please choose one of the examples from below : ")
            ask_looks_power = input("TURBO or SUPER : ")
    #CHOSE TURBO
    if tubo_super == "TURBO" : 
        print("Awesome! Would you like to add a nice exhaust with that\n or add a pops and bangs tune?")
        exhaust_tune = input("EXHAUST or TUNE : ").upper()
        while exhaust_tune != "EXHAUST" and exhaust_tune != "TUNEP":
            print("You did not pick a valid option. Please choose one of the examples from below : ")
            ask_looks_power = input("EXHAUST or TUNE : ")
        #CHOSE EXHAUST
        if(exhaust_tune == "EXHAUST") :
            print("You now have a faster car and the sounds to go with it!")
        #CHOSE TUNE
        else:
            print("You now have a faster car and some nice pops and bangs to let people know you have a tuned car")
    #CHOSE SUPERCHARGER
    else:
        print("Awesome! Would you like to upgrade your cams,\n or straight pipe the car?")
        cams_pipes = input("CAMS or PIPES : ").upper()
        while cams_pipes != "CAMS" and cams_pipes != "PIPES":
            print("You did not pick a valid option. Please choose one of the examples from below : ")
            ask_looks_power = input("CAMS or PIPES : ")
        #CHOSE CAMS
        if (cams_pipes == "CAMS"):
            print("/n/nYou now have a supercharged car, and it has the cams to match that power coming out!")
        #CHOSE STRAIGHT PIP
        else:
            print("/n/nYou now have a supercharged car, and everyone else can hear it whine!")


