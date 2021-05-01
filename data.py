import requests

parameter = {
    "amount": 10,
    "category": 9,
    "type": "boolean"
}
response = requests.get("https://opentdb.com/api.php", params=parameter)
response.raise_for_status()
data = response.json()
question_data = data['results']

# question_data = [
#     """Question data imported from (https://opentdb.com/)"""
#     {
#         "category": "Science: Computers",
#         "type": "multiple",
#         "difficulty": "hard",
#         "question": "What was the name of the security vulnerability found in Bash in 2014?",
#         "correct_answer": "Shellshock",
#         "incorrect_answers": [
#             "Heartbleed",
#             "Bashbug",
#             "Stagefright"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "medium",
#         "question": "The very first recorded computer &quot;bug&quot; was a moth found inside a Harvard Mark II computer.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "multiple",
#         "difficulty": "medium",
#         "question": "On which computer hardware device is the BIOS chip located?",
#         "correct_answer": "Motherboard",
#         "incorrect_answers": [
#             "Hard Disk Drive",
#             "Central Processing Unit",
#             "Graphics Processing Unit"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "The logo for Snapchat is a Bell.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "hard",
#         "question": "DHCP stands for Dynamic Host Configuration Port.",
#         "correct_answer": "False",
#         "incorrect_answers": [
#             "True"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "boolean",
#         "difficulty": "easy",
#         "question": "&quot;HTML&quot; stands for Hypertext Markup Language.",
#         "correct_answer": "True",
#         "incorrect_answers": [
#             "False"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "multiple",
#         "difficulty": "medium",
#         "question": "Laserjet and inkjet printers are both examples of what type of printer?",
#         "correct_answer": "Non-impact printer",
#         "incorrect_answers": [
#             "Impact printer",
#             "Daisywheel printer",
#             "Dot matrix printer"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "multiple",
#         "difficulty": "easy",
#         "question": "The C programming language was created by this American computer scientist. ",
#         "correct_answer": "Dennis Ritchie",
#         "incorrect_answers": [
#             "Tim Berners Lee",
#             "al-Khwārizmī",
#             "Willis Ware"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "multiple",
#         "difficulty": "easy",
#         "question": "How long is an IPv6 address?",
#         "correct_answer": "128 bits",
#         "incorrect_answers": [
#             "32 bits",
#             "64 bits",
#             "128 bytes"
#         ]
#     },
#     {
#         "category": "Science: Computers",
#         "type": "multiple",
#         "difficulty": "hard",
#         "question": "What is the codename of the eighth generation Intel Core micro-architecture launched in October 2017?",
#         "correct_answer": "Coffee Lake",
#         "incorrect_answers": [
#             "Sandy Bridge",
#             "Skylake",
#             "Broadwell"
#         ]
#     }
# ]
