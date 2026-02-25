# Defining main function
def main():

    test = LinkedList(1000)
    test.traverse()

    for i in range(0, 2147):
        test.push(i)
    test.traverse()

    for i in range(0, 2147):
        test.pop()
    test.traverse()


# Using the special variable 
# __name__
if __name__=="__main__":
    main()
