import requests

parameters = {
    "amount":10,
    "type":"boolean",
}

response = requests.get(url="https://opentdb.com/api.php",params=parameters)
response.raise_for_status()

data = response.json()

question_data = data['results']
#print(question_data)





# question_data ={
#   "response_code": 0,
#   "results": [
#     {
#       "type": "boolean",
#       "difficulty": "medium",
#       "category": "General Knowledge",
#       "question": "Kraft &quot;Cheez Whiz&quot; contains cheese culture, but doesn&#039;t actually contain cheese",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     },
#     {
#       "type": "boolean",
#       "difficulty": "medium",
#       "category": "General Knowledge",
#       "question": "SCP-173 was the first SCP article written for the web-based collaborative fiction project known as the &quot;SCP Foundation&quot;",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     },
#     {
#       "type": "boolean",
#       "difficulty": "medium",
#       "category": "General Knowledge",
#       "question": "The British organisation CAMRA stands for The Campaign for Real Ale.",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     },
#     {
#       "type": "boolean",
#       "difficulty": "medium",
#       "category": "General Knowledge",
#       "question": "Instant mashed potatoes were invented by Canadian Edward Asselbergs in 1962.",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     },
#     {
#       "type": "boolean",
#       "difficulty": "medium",
#       "category": "General Knowledge",
#       "question": "The scientific name for the Southern Lights is Aurora Australis?",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     },
#     {
#       "type": "boolean",
#       "difficulty": "medium",
#       "category": "General Knowledge",
#       "question": "Francis Bacon died from a fatal case of pneumonia while he was attempting to preserve meat by stuffing a chicken with snow.",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     },
#     {
#       "type": "boolean",
#       "difficulty": "medium",
#       "category": "General Knowledge",
#       "question": "The sum of all the numbers on a roulette wheel is 666.",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     },
#     {
#       "type": "boolean",
#       "difficulty": "medium",
#       "category": "General Knowledge",
#       "question": "Furby was released in 1998.",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     },
#     {
#       "type": "boolean",
#       "difficulty": "medium",
#       "category": "General Knowledge",
#       "question": "Coca-Cola&#039;s original colour was green.",
#       "correct_answer": "False",
#       "incorrect_answers": [
#         "True"
#       ]
#     },
#     {
#       "type": "boolean",
#       "difficulty": "medium",
#       "category": "General Knowledge",
#       "question": "&quot;Santa Claus&quot; is a variety of melon.",
#       "correct_answer": "True",
#       "incorrect_answers": [
#         "False"
#       ]
#     }
#   ]
# }