name = raw_input("What is your name? ")
if name == str("Adithya"):
    print "No bulli pls."
elif name == str("Siddharth"):
    print "Hello myself!"
elif name == str("Achyuthan"):
    raise NameError("Not a valid name.")
elif name == str("Asha"):
    raise NameError("Name not found.")
else:
    print "You're not in the list! Get out!"
