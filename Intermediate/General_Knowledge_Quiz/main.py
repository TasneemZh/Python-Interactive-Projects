from question import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for record in question_data:
    new_question = Question(record["question"], record["correct_answer"])
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

print("You have completed the quiz.\n"
      f"Your final score is {quiz_brain.score}/{quiz_brain.question_number}")
