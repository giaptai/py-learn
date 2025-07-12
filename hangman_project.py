import random


class Hangman:

    def __init__(self, word="", attemp=6, answer=[]):
        self.word = word
        self.attemp = attemp
        self.action = ["python", "java", "c++", "router"]
        self.answer = answer

    def word_selection(self):
        self.word = random.choice(self.action)
        self.answer = ["_" for _ in self.word]  # list comprehension

    def word_display(self):
        return self.answer

    def guess_handling(self):
        while self.attemp > 0 and "_" in self.answer:
            print(self.word_display())
            print("Attemp: " + str(self.attemp))

            user_guess = input("Your guess: ").lower()
            for i in range(len(self.word)):
                if user_guess == self.word[i] and self.answer[i] == "_":
                    self.answer[i] = user_guess
                    break
                elif user_guess == self.word[i] and self.answer[i] != "_":
                    continue
                elif i == len(self.word) - 1:
                    self.attemp -= 1

        if self.attemp == 0:
            print(f"You lost, the answer is {self.word}")
        else:
            print(f"You win {self.word_display()}")


hang_man = Hangman()
hang_man.word_selection()
hang_man.guess_handling()
