time = 8

if time < 9:
    print ("Morning is wonderful. Its only drawback is that it comes at such an inconvenient time of day.")
    #if time is less than (before) 9am, it prints "Morning is wonderful..."

elif time <= 1600:
    print ("Working hard or hardly working?")
    #if time is less than (before) or equal to 4pm (1600 hrs), it prints "Working hard or hardly working?"

elif time < 2000:
    print ("How did it get so late so soon?")
    #if time is before 8pm (2000 hrs), it prints "How did it get so late so soon?"

elif time < 2200:
    print ("A day without sunshine is like, you know, night. ")
    #if time is before 10pm (2200 hrs) , it prints "A day without sunshine..."

elif time >= 2200:
    print ("Burning the midnight oil!")
    #if time is 10pm (2200 hrs) or later, it prints "Burning the midnight oil"
