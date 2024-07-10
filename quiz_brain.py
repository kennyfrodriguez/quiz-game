class QuizBrain:
    def __init__(self, q_list):
        self.q_num = 0
        self.correct = 0
        self.q_list = q_list

    def still_has_questions(self):
        return self.q_num < len(self.q_list)

    def return_final_score(self):
        print(f"\n Your final score is {self.correct}/{self.q_num} correct.")

    def check_amount_correct(self, is_correct):
        if is_correct:
            print("Correct!")
            self.correct += 1
            print(f"You have gotten {self.correct}/{self.q_num + 1} correct.")
        else:
            print("Incorrect!")
            print(f"You have gotten {self.correct}/{self.q_num + 1} correct.")

    def next_question(self):
        if self.q_num < len(self.q_list):
            current_question = self.q_list[self.q_num]
            current_answer = input(f"Q:{self.q_num + 1}:{current_question.text}  (True/False)")
            if current_answer == current_question.answer:
                self.check_amount_correct(True)
            else:
                self.check_amount_correct(False)
            self.q_num += 1
