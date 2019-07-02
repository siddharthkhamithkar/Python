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
    sure = raw_input("Are you sure? (y/n) ")
    if sure == str("y"):
        print "Are you Ronnie Corbito?"
    elif sure == str("n"):
        print "You're Ronie Corbito, aren't you?"
    else:
        raise NameError("Did you use (y/n)? ")
elif anime == str("Initial D"):
    print "You think drifting will make you a man."
    raise FileNotFoundError("dejavu.mp4 not found.")
elif anime == str("Naruto"):
    print "You're a normie."
elif anime == str("Fullmetal Alchemist"):
    print "You're cool!"
elif anime == str("Citrus"):
    sure = raw_input("What's your gender? (m/f) ")
    if sure == str("m"):
        print "You have bad taste."
    elif sure == str("f"):
        print "It's okay. Nobody cares."
    else:
        raise NameError("Did you use (y/n)? ")
else:
    raise NameError("This anime was not found.")
