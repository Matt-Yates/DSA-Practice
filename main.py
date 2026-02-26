from random import randint
from linkedlist import *
from dynamicarray import *
# Defining main function
def main():

    test = LinkedList(1000)
    test.traverse()

    for i in range(0, 214):
        test.push(i)
    test.traverse()

    for i in range(0, 214):
        test.pop()
    test.traverse()

    test_array = DynamicArray()
    for i in range(100):
        test_array.pushback(randint(1, 1000))
    test_array.print()

    for i in range(95):
        test_array.popback()
    test_array.print()
    

# Using the special variable 
# __name__
if __name__=="__main__":
    main()
