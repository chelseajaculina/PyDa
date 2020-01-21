# Phase 1

import wikipedia

while True:
    input = raw_input("Question: ")

    # modify the infromation to another language
    wikipedia.set_lang("es")
    # print wikipedia.summary(input) # shorten the input
    print wikipedia.summary(input, sentences = 2)
