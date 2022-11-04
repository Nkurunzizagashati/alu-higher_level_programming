#!/usr/bin/python3
def multiple_returns(sentence):
    for i in sentence:
        if len(sentence) == 0:
            return None
        else:
            print("Length: {:d} - First character: {}".format(len(sentence), sentence(1)))
