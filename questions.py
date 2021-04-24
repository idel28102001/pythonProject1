def return_input(inp):
    return int(inp)


def question():
    answer = None
    while answer != 1799:
        answer = return_input(input('Когда родился А.С. Пушкин? -'))  # When A. S. Pushkin was born
    while answer != 6:
        answer = return_input(input('А в какой день? -'))  # Could you tell me the day of the born
    print('Верно')  # That's right, keep up the good work
