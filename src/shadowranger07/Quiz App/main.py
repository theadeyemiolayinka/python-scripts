from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for item in question_data:
    question = Question(item["question"], item["correct_answer"])
    question_bank.append(question)

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_questions():
    quiz_brain.next_question(quiz_brain.question_number, question_bank)
print("You've completed the quiz")
print(f"Your final score is {quiz_brain.score}/{quiz_brain.question_number}")