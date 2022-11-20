#If the name contains a "u," print out the name plus "U are so Uniquely U!"
#Otherwise if the name contains an "i," print out the name plus "I bet you're
#Impressively Intelligent!"
#Otherwise if the name contains an "o," print out the name plus "O My! How
#Original!"
#Otherwise, print the name plus "Ehh, a's and e's are so ordinary."

disney_characters = ["simba", "ariel", "pumba", "flounder", "nala", "ursula",
"scar", "flotsam", "timon"]

for letters in disney_characters:
    if "u" in letters:
        print ("U are so Uniquely U!")

    elif "i" in letters:
        print ("I bet you're Impressively Intelligent!")

    elif "o" in letters:
        print ("O My! How Original")

    else :
        print ("Ehh, a's and e's are so ordinary")
