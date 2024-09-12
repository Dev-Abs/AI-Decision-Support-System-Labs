# task 1
# text = input('Please enter some english text: \n')
# if text[0] == 'a' or text[0] == 'i' or text[0] == 'o' or text[0] == 'e' or text[0] == 'u':
#     print(text + 'hay')
# else:
#     firstChar = text[0]
#     text = text[1:]
#     text = text + firstChar
#     print(text + 'ay')


# task 2

# def Fibonacci(n):
#     a = 0
#     b = 1
#     add = a + b
#     print('Fibonacci: \n' + str(a) + '\n' + str(b))
#     while n > add:
#         print(add)
#         a = b
#         b = add
#         add = a + b
#     return
#
#
# def main():
#     n = input('Please input number upto which you want to find Fibonacci series: \n')
#     Fibonacci(int(n))
#     return
#
#
# main()


# task 3

# import random
# import string
#
#
# def generatePasswords(numberOfPasswords, length):
#     for i in range(numberOfPasswords):
#         password = ''
#         for j in range(length):
#             character = random.choice(string.ascii_letters)
#             password += character
#         print('Password ' + str(i+1) + ': ' + password + '\n')
#
#
# def main():
#     n = input('tell me number of passwords you want? \n')
#     length = input('and their length? \n')
#     generatePasswords(int(n), int(length))
#     return
#
#
# main()

# task 4
import math

class Complex:
    def __init__(self, realN, imaginaryN):
        self.realN = realN
        self.imaginaryN = imaginaryN

    def magnitude(self):
        return math.sqrt(self.realN ** 2 + self.imaginaryN ** 2)

    def orientation(self):
        return math.atan2(self.imaginaryN, self.realN)  # angle in radians

    def details(self):
        print(f"Complex Number: {self.realN} + {self.imaginaryN}i")
        print(f"Magnitude: {self.magnitude()}")
        print(f"Orientation: {self.orientation()}")


if __name__ == "__main__":
    real = int(input("Enter the real part of the complex number: "))
    imaginary = int(input("Enter the imaginary part of the complex number: "))

    complexN = Complex(real, imaginary)
    complexN.details()




