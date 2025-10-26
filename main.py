import random
import time


class KBC:

    def __init__(self):
        self.questions = [{
            "question":
            "What is the capital of India?",
            "options":
            ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
            "answer":
            "B",
            "prize":
            "₹1,000"
        }, {
            "question":
            "Who wrote the national anthem of India?",
            "options": [
                "A. Bankim Chandra", "B. Rabindranath Tagore",
                "C. Mahatma Gandhi", "D. Sarojini Naidu"
            ],
            "answer":
            "B",
            "prize":
            "₹2,000"
        }, {
            "question":
            "Which planet is known as the Red Planet?",
            "options": ["A. Venus", "B. Jupiter", "C. Mars", "D. Saturn"],
            "answer":
            "C",
            "prize":
            "₹3,000"
        }, {
            "question":
            "What is the largest ocean on Earth?",
            "options": [
                "A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean",
                "D. Pacific Ocean"
            ],
            "answer":
            "D",
            "prize":
            "₹5,000"
        }, {
            "question":
            "Who painted the Mona Lisa?",
            "options": [
                "A. Vincent van Gogh", "B. Pablo Picasso",
                "C. Leonardo da Vinci", "D. Michelangelo"
            ],
            "answer":
            "C",
            "prize":
            "₹10,000"
        }, {
            "question":
            "Which is the longest river in the world?",
            "options": ["A. Amazon", "B. Nile", "C. Ganges", "D. Yangtze"],
            "answer":
            "B",
            "prize":
            "₹20,000"
        }, {
            "question": "What is the chemical symbol for Gold?",
            "options": ["A. Go", "B. Gd", "C. Au", "D. Ag"],
            "answer": "C",
            "prize": "₹40,000"
        }, {
            "question":
            "In which year did India gain independence?",
            "options": ["A. 1942", "B. 1945", "C. 1947", "D. 1950"],
            "answer":
            "C",
            "prize":
            "₹80,000"
        }, {
            "question":
            "What is the speed of light in vacuum?",
            "options": [
                "A. 3 × 10⁸ m/s", "B. 3 × 10⁶ m/s", "C. 3 × 10⁷ m/s",
                "D. 3 × 10⁹ m/s"
            ],
            "answer":
            "A",
            "prize":
            "₹1,60,000"
        }, {
            "question":
            "Who is known as the Father of Computers?",
            "options": [
                "A. Alan Turing", "B. Charles Babbage", "C. Bill Gates",
                "D. Steve Jobs"
            ],
            "answer":
            "B",
            "prize":
            "₹3,20,000"
        }, {
            "question":
            "Which vitamin is known as ascorbic acid?",
            "options":
            ["A. Vitamin A", "B. Vitamin B", "C. Vitamin C", "D. Vitamin D"],
            "answer":
            "C",
            "prize":
            "₹6,40,000"
        }, {
            "question":
            "What is the powerhouse of the cell?",
            "options":
            ["A. Nucleus", "B. Mitochondria", "C. Ribosome", "D. Chloroplast"],
            "answer":
            "B",
            "prize":
            "₹12,50,000"
        }, {
            "question":
            "Which element has the atomic number 1?",
            "options": ["A. Helium", "B. Oxygen", "C. Hydrogen", "D. Carbon"],
            "answer":
            "C",
            "prize":
            "₹25,00,000"
        }, {
            "question":
            "Who developed the theory of relativity?",
            "options": [
                "A. Isaac Newton", "B. Nikola Tesla", "C. Albert Einstein",
                "D. Stephen Hawking"
            ],
            "answer":
            "C",
            "prize":
            "₹50,00,000"
        }, {
            "question":
            "What is the smallest country in the world?",
            "options": [
                "A. Monaco", "B. Vatican City", "C. San Marino",
                "D. Liechtenstein"
            ],
            "answer":
            "B",
            "prize":
            "₹1,00,00,000 (1 CRORE)"
        }]

        self.lifelines = {
            "50:50": True,
            "Phone a Friend": True,
            "Audience Poll": True
        }

        self.current_question = 0
        self.total_winnings = 0

    def display_header(self):
        print("\n" + "=" * 60)
        print("🎮  KAUN BANEGA CROREPATI  🎮")
        print("=" * 60)

    def display_lifelines(self):
        print("\n💡 Available Lifelines:")
        for lifeline, available in self.lifelines.items():
            status = "✅" if available else "❌"
            print(f"   {status} {lifeline}")

    def use_fifty_fifty(self, question):
        if not self.lifelines["50:50"]:
            print("❌ This lifeline has already been used!")
            return False

        self.lifelines["50:50"] = False
        print("\n🔄 Using 50:50 lifeline...")
        time.sleep(1)

        correct_answer = question["answer"]
        options_to_keep = [correct_answer]

        other_options = [
            opt[0] for opt in question["options"] if opt[0] != correct_answer
        ]
        options_to_keep.append(random.choice(other_options))

        print("\n📝 Remaining options:")
        for option in question["options"]:
            if option[0] in options_to_keep:
                print(f"   {option}")
        return True

    def use_phone_a_friend(self, question):
        if not self.lifelines["Phone a Friend"]:
            print("❌ This lifeline has already been used!")
            return False

        self.lifelines["Phone a Friend"] = False
        print("\n📞 Calling a friend...")
        time.sleep(2)

        friends = ["Rahul", "Priya", "Amit", "Sneha"]
        friend = random.choice(friends)

        if random.random() < 0.75:
            print(
                f"👤 {friend}: I think the answer is {question['answer']}. I'm about 75% sure!"
            )
        else:
            wrong_option = random.choice([
                opt[0] for opt in question["options"]
                if opt[0] != question["answer"]
            ])
            print(
                f"👤 {friend}: Hmm, I'm not entirely sure, but I think it might be {wrong_option}."
            )

        return True

    def use_audience_poll(self, question):
        if not self.lifelines["Audience Poll"]:
            print("❌ This lifeline has already been used!")
            return False

        self.lifelines["Audience Poll"] = False
        print("\n👥 Asking the audience...")
        time.sleep(2)

        correct_answer = question["answer"]
        percentages = {}

        correct_percentage = random.randint(40, 80)
        percentages[correct_answer] = correct_percentage

        remaining = 100 - correct_percentage
        other_options = [
            opt[0] for opt in question["options"] if opt[0] != correct_answer
        ]

        for i, opt in enumerate(other_options):
            if i == len(other_options) - 1:
                percentages[opt] = remaining
            else:
                p = random.randint(0, remaining)
                percentages[opt] = p
                remaining -= p

        print("\n📊 Audience Poll Results:")
        for option in question["options"]:
            opt_letter = option[0]
            print(
                f"   {opt_letter}: {'█' * (percentages[opt_letter] // 2)} {percentages[opt_letter]}%"
            )

        return True

    def ask_question(self, question_num):
        question = self.questions[question_num]

        print("\n" + "=" * 60)
        print(f"Question {question_num + 1} for {question['prize']}")
        print("=" * 60)
        print(f"\n{question['question']}\n")

        for option in question["options"]:
            print(f"   {option}")

        self.display_lifelines()

        while True:
            print("\n💬 Your choice (A/B/C/D, L for lifeline, Q to quit): ",
                  end="")
            choice = input().strip().upper()

            if choice == 'Q':
                return 'quit'
            elif choice == 'L':
                print("\n🎯 Choose a lifeline:")
                print("   1. 50:50")
                print("   2. Phone a Friend")
                print("   3. Audience Poll")
                print("   4. Go back")

                lifeline_choice = input("\nEnter your choice (1-4): ").strip()

                if lifeline_choice == '1':
                    self.use_fifty_fifty(question)
                elif lifeline_choice == '2':
                    self.use_phone_a_friend(question)
                elif lifeline_choice == '3':
                    self.use_audience_poll(question)
                elif lifeline_choice == '4':
                    continue
                else:
                    print("❌ Invalid choice!")
                continue
            elif choice in ['A', 'B', 'C', 'D']:
                return choice
            else:
                print("❌ Invalid input! Please enter A, B, C, D, L, or Q")

    def play(self):
        self.display_header()
        print("\n🎬 Welcome to Kaun Banega Crorepati!")
        print("Answer 15 questions correctly to win ₹1 CRORE!")
        print(
            "\nYou have 3 lifelines: 50:50, Phone a Friend, and Audience Poll")
        print("You can quit anytime and take home your winnings!")

        input("\n▶️  Press Enter to start the game...")

        for i in range(len(self.questions)):
            self.current_question = i

            answer = self.ask_question(i)

            if answer == 'quit':
                print(
                    f"\n💰 You're taking home: {self.questions[i-1]['prize'] if i > 0 else '₹0'}!"
                )
                print("👋 Thank you for playing Kaun Banega Crorepati!")
                return

            print("\n🤔 Checking your answer...")
            time.sleep(2)

            if answer == self.questions[i]["answer"]:
                print("✅ CORRECT! 🎉")
                self.total_winnings = self.questions[i]["prize"]
                print(f"💰 You've won: {self.total_winnings}")
                time.sleep(2)
            else:
                print(
                    f"❌ WRONG! The correct answer was {self.questions[i]['answer']}"
                )
                print(
                    f"💰 You're taking home: {self.questions[i-1]['prize'] if i > 0 else '₹0'}"
                )
                print("👋 Thank you for playing Kaun Banega Crorepati!")
                return

        print("\n" + "=" * 60)
        print("🎊 CONGRATULATIONS! 🎊")
        print("🏆 YOU'VE WON ₹1 CRORE! 🏆")
        print("=" * 60)
        print("🎉 You are a CROREPATI! 🎉")


if __name__ == "__main__":
    game = KBC()
    game.play()
