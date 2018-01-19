print "This will tell what your favorite anime says about you!"
print "Please type in the full anime name exactly and it is case sensitive."
anime = raw_input("What is your favorite anime? ")
if anime == str("Evangelion"):
    print "You want to try piloting unit 1"
elif anime == str("Sword Art Online"):
    print "You think swords are cool?."
elif anime == str("No Game No Life"):
    print "You think getting stuck in another world is fun."
elif anime == str("Log Horizon"):
    print "You think Sword Art Online wasn't enough."
elif anime == str("Kantai Collection"):
    print "Are you Ronie Corbito?"
elif anime == str("Initial D"):
    print "You think drifting will make you a man."
    raise Exception("dejavu.mp4 not found.")
elif anime == str("Naruto"):
    print "You're a normie."
elif anime == str("Fullmetal Alchemist"):
    print "You're cool!"
else:
    raise NameError("This anime was not found.")
