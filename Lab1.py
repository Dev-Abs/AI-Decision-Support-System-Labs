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
# import math
#
#
# class Complex:
#     def __init__(self, realN, imaginaryN):
#         self.realN = realN
#         self.imaginaryN = imaginaryN
#
#     def magnitude(self):
#         return math.sqrt(self.realN ** 2 + self.imaginaryN ** 2)
#
#     def orientation(self):
#         return math.atan2(self.imaginaryN, self.realN)  # angle in radians
#
#     def details(self):
#         print(f"Complex Number: {self.realN} + {self.imaginaryN}i")
#         print(f"Magnitude: {self.magnitude()}")
#         print(f"Orientation: {self.orientation()}")
#
#
# if __name__ == "__main__":
#     real = int(input("Enter the real part of the complex number: "))
#     imaginary = int(input("Enter the imaginary part of the complex number: "))
#
#     complexN = Complex(real, imaginary)
#     complexN.details()

# task 5

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        return root

    def search(self, root, key):
        if root is None or root.val == key:
            return root

        if key > root.val:
            return self.search(root.right, key)

        return self.search(root.left, key)


def create_tree():
    bst = BST()
    root = None

    keys = [15, 10, 20, 8, 12, 16, 25, 13]

    for key in keys:
        root = bst.insert(root, key)

    return bst, root


def search_for_13(bst, root):
    search_key = 13
    result = bst.search(root, search_key)

    if result is not None:
        print(f"Node {search_key} found in the tree.")
    else:
        print(f"Node {search_key} not found in the tree.")


if __name__ == "__main__":
    BST, ROOT = create_tree()
    search_for_13(BST, ROOT)