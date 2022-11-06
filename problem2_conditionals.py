angry = True
bored = True
hungry = False
tired = False

#Example `if` statement:
#if bored:
  #print("T-Rex roars! Rawr!")

if angry and hungry and bored:
    print ("T-Rex will eat the Triceratops")

elif tired and hungry:
    print ("T-Rex will eat the Iguanadon")

elif hungry and bored:
    print ("T-Rex will eat the Stegasaurus")

elif tired:
    print ("T-Rex will go to sleep")

elif angry and bored:
    print ("T-Rex will fight with the Velociraptor")

elif angry or bored:
    print ("T-Rex roars! Rawr")

else:
    print ("T-Rex gives a toothy smile")
