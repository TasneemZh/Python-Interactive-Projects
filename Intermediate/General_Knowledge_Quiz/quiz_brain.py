class QuizBrain:
    question_number = 0

    def __init__(self, question_list):
        self.correct_answer = ""
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.correct_answer = current_question.answer
        return f"Q.{self.question_number+1} {current_question.text} True or False? "

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer: str) -> bool:
        if user_answer == self.correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
