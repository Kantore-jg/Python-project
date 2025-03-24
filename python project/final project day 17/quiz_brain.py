from main import question_bank
class Quizbrain:
    def __init__(self, q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0
    def still_has_question(self):
        return self.question_number<len(self.question_list)
        #     return True
        # else :
        #     return False
    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        user_answer=input(f"Q.{self.question_number}:{current_question.text} False/True: ")
        self.check_answer(user_answer,current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower()==correct_answer.lower():
            print("you got it right😎")
            self.score+=1
        else:
            print("that's wrong😑")
        print(f"the correct score was {correct_answer} 😛")
        print(f"your current score is {self.score}/{self.question_number}")
        print("\n")
    def check_score(self):
        if self.score>9:
            print(f"conglaturations your final score was {self.score}/{len(question_bank)} 🎊👑")
        elif self.score>6:
            print(f"wow your final score was {self.score}/{len(question_bank)} 🎆")
        
        else:
            print(f"you deserv nothing🤣 your final score was {self.score}/{len(question_bank)} 😏")
