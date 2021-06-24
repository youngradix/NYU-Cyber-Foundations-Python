def remainingwords(phrase):
    splitter=phrase.split()
    remains = " ".join for x in splitter[1:]
    return remains

print(remainingwords("the quick brown fox"))