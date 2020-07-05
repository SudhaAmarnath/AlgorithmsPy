def initials(phrase):
    my_initals = ''.join([s[:1].upper() for s in phrase.split(' ')])
    return my_initals


print(initials("Universal Serial Bus"))  # Should be: USB
print(initials("local area network"))  # Should be: LAN
print(initials("Operating system"))  # Should be: OS