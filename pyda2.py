# Phase 2
# Learning wikipedia API
# Learning how to combine wolfram and wikipedia API

import wikipedia

import wolframalpha

while True:
        input = raw_input("Enter your question: ")

        # try and except loop
        try:
            # wolfram
            app_id = "2YTK5H-2VY3PPQVRP"
            client = wolframalpha.Client(app_id)

            result = client.query(input)
            answer = next(result.results).text

            print(answer)

        except:
            # wikipedia
                # modify the infromation to another language
                #wikipedia.set_lang("es")
                # print wikipedia.summary(input) # shorten the input
            print wikipedia.summary(input, sentences = 2)
