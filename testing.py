
def example1_1():
    """
    Demo readline().  Read the first two names from a text file names.txt and print them out
    :return: None
    """

    namesfile = open("test.txt", 'r')

    name1 = namesfile.readline()
    name2 = namesfile.readline()

    print(name1)
    print(name2)

example1_1()
