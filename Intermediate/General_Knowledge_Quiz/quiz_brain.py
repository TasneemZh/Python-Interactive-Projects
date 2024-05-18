class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = (input(f"Q.{self.question_number+1} {current_question.text} True or "
                             f"False? ").lower())
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong!\n"
                  f"The correct answer is {correct_answer}")
        print(f"You current score is {self.score}/{self.question_number}\n\n")


