def remainingwords(phrase):
    splitter=phrase.split()
    remains = splitter[1:]
    rest = " ".join(remains)
    return rest

#print(remainingwords("the quick brown fox"))