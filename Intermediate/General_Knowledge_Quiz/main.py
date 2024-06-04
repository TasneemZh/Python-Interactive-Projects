import requests
import html
from interface import QuizzInterface
from question import Question
from quiz_brain import QuizBrain

question_bank = []
parameters = {
    "amount": 10,
    "type": "boolean"
}
data = requests.get("https://opentdb.com/api.php", params=parameters)
data.raise_for_status()
question_data = data.json()["results"]

for record in question_data:
    new_question = Question(html.unescape(record["question"]), record["correct_answer"])
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)
quiz_interface = QuizzInterface(quiz_brain)
