# Phase 0
# learning wolfram alpha API

import wolframalpha

input = raw_input("Question: ")
app_id = "2YTK5H-2VY3PPQVRP"
client = wolframalpha.Client(app_id)

result = client.query(input)
answer = next(result.results).text

print(answer)
