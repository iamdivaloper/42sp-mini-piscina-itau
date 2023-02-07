def my_numbers():
    file = open('numbers.txt', 'r')

    for line in file:
        print(line.replace(',', '\n'))


if __name__ == '__main__':
    my_numbers()
