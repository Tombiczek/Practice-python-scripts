import random
import string
import time


class Password:

    def __init__(self, n):
        self.level = n
        self.length = random.randint(10, 16)
        self.passpl = []
        self.passp = ''

    def generator(self):
        for x in range(self.length):
            b = random.randrange(len(self.level))
            self.passpl.append(self.level[b])
        self.passp = ''.join(self.passpl)
        print(self.passp)


if __name__ == '__main__':
    while True:
        i = input('How strong do you want your password to be in a scale through 1 - 3: ')
        try:
            ii = int(i)
        except ValueError:
            print('Not an integer, try again')
        else:
            if ii > 3 or ii < 1:
                print("Wrong value, try again")
            else:
                break
    if ii == 1:
        m = list(string.ascii_letters)
        weak = Password(m)
        print('You have chosen a weak option')
        time.sleep(0.25)
        print('Loading...')
        time.sleep(0.5)
        weak.generator()
    if ii == 2:
        f = list(string.ascii_letters)
        k = list(string.digits)
        for t in k:
            f.append(t)
        moderate = Password(f)
        print('You have chosen a moderate option')
        time.sleep(0.25)
        print('Loading...')
        time.sleep(0.5)
        moderate.generator()
    if ii == 3:
        f = list(string.ascii_letters)
        k = list(string.digits)
        o = list(string.punctuation)
        for t in k:
            f.append(t)
        for uy in o:
            f.append(uy)
        strong = Password(f)
        print('You have chosen a strong option')
        time.sleep(0.25)
        print('Loading...')
        time.sleep(0.5)
        strong.generator()



