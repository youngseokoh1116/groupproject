class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.current = 0
        self.score = 0
        self.incorrect_questions = []

    def has_more_questions(self):
        return self.current < len(self.questions)

    def get_next_question(self):
        return self.questions[self.current]

    def answer_question(self, question, user_choice):
        correct = user_choice == question["answer"]
        if correct:
            self.score += self.get_score_by_difficulty(question["difficulty"])
        else:
            self.incorrect_questions.append(question)
        self.current += 1
        return correct

    def get_score_by_difficulty(self, level):
        return {"easy": 1, "medium": 2, "hard": 3}[level]
