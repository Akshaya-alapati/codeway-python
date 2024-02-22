import random

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_welcome_message(self):
        print("Welcome to the Entertainment Quiz!")
        print("Answer the following questions to test your knowledge.\n")

    def present_quiz_questions(self):
        random.shuffle(self.questions)
        for q in self.questions:
            print(q['question'])
            if 'choices' in q:
                for i, choice in enumerate(q['choices'], 1):
                    print(f"{i}. {choice}")
            user_answer = input("Your answer: ").strip().lower()
            self.evaluate_user_answer(user_answer, q['answer'])
            print(f"Score for this question: {self.score}/{len(self.questions)}")
            print()

    def evaluate_user_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect.")
            print(f"The correct answer is: {correct_answer}")

    def display_final_results(self):
        print(f"\nQuiz completed! Your final score is: {self.score}/{len(self.questions)}")
        if self.score / len(self.questions) < 0.5:
            print("Better luck next time!")
        else:
            print("Well done!")

def main():
    questions = [
        {
            'question': "Who played the role of Harry Potter in the movie series?",
            'answer': "Daniel Radcliffe"
        },
        {
            'question': "Which animated movie features the song 'Let It Go'?",
            'answer': "Frozen"
        },
        {
            'question': "Who is the lead actor in the movie 'The Shawshank Redemption'?",
            'answer': "Tim Robbins"
        },
        {
            'question': "What is the highest-grossing film of all time (as of 2022)?",
            'answer': "Avatar"
        },
        {
            'question': "Which TV show features characters named Rachel, Ross, and Joey?",
            'answer': "Friends"
        }
    ]

    quiz = Quiz(questions)
    quiz.display_welcome_message()
    quiz.present_quiz_questions()
    quiz.display_final_results()

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        main()
    else:
        print("Goodbye!")

if __name__ == "__main__":
    main()

           
          
    
