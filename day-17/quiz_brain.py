class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question (self):
        current_question = self.question_list [self.question_number].text
        current_answer = self.question_list [self.question_number].answer
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}: {current_question} (True/False): ')
        self.check_answer(user_answer, current_answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
            print (f"Your current score is {self.score}")
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer}")