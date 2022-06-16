import random
import time


class Cows_And_Bulls:

    def __init__(self):
        self.random = str(random.randint(1000, 9999))
        self.trials = 0
        self.random_list = []
        self.choice_list = []

    @staticmethod
    def error_check(choice):
        assert len(choice) == 4

    def check(self, choice):
        for s1 in self.random:
            self.random_list.append(s1)
        for s in choice:
            self.choice_list.append(s)
        bull = 0
        cow = 0
        for ind, val in enumerate(choice):
            if self.random[ind] == val:
                cow += 1
                if self.random == choice:
                    print('You guessed it correctly!')
                    time.sleep(0.5)
                    print('It took you', self.trials, 'tries')
                    time.sleep(0.5)
                    print('Thanks for playing')
                    time.sleep(0.5)
                    exit()
                else:
                    continue
            elif val in self.random_list:
                bull += 1
            else:
                continue
        if cow == 1 and bull == 1:
            print(cow, 'cow', bull, 'bull')
        elif cow == 1 and bull != 1:
            print(cow, 'cow', bull, 'bulls')
        elif cow != 1 and bull == 1:
            print(cow, 'cows', bull, 'bull')
        else:
            print(cow, 'cows', bull, 'bulls')
        self.trials += 1


if __name__ == '__main__':
    print('Welcome to the Cows and Bulls Game!')
    u1 = Cows_And_Bulls()
    while True:
        guess = input("Enter you guess: ")
        if guess == '':
            exit()
        elif guess == 'help':
            print(u1.random)
            continue
        try:
            i = int(guess)
        except ValueError:
            print("Wrong input")
            continue
        else:
            try:
                u1.error_check(guess)
            except AssertionError:
                print("You guess is not 4-digit long")
            else:
                u1.check(guess)
