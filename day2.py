valid_1 = 0
valid_2 = 0

def read_file(fileName):
    my_file = open(fileName, 'r')
    content = my_file.read().split('\n')
    input_list = list(filter(None, content))
    splitted = [i.split(' ', 2) for i in input_list]
    return splitted

def split_number(nr, index):
    return int(nr.split('-',2)[index])

def split_list(listElement):
    first = split_number(listElement[0], 0)
    second = split_number(listElement[0], 1)
    letter = listElement[1][0]
    password = listElement[2]
    return (first, second, letter, password)

def solution(first, second, letter, password):
    global valid_1, valid_2
    check = 0
    counter = 0
    for y in password:
        if y == letter:
            counter += 1
    if counter >= first and counter <= second:
        valid_1 += 1
    if letter == password[first-1]:
        check += 1
    if letter == password[second-1]:
        check += 1
    if check == 1:
        valid_2 += 1

def answer(inputList):
    for x in inputList:
        first, second, letter, password = split_list(x)
        solution(first, second, letter, password)
    print(valid_1, valid_2)

answer(read_file('input-day2.txt'))

