from random import randint, choice, shuffle


def copy_to_clipboard(window, text):
    window.clipboard_clear()
    window.clipboard_append(text)
    window.update()


def generate_password(window):
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")

    password_letters = [choice(letters) for _ in range(randint(4, 8))]

    password_symbols = [choice(symbols) for _ in range(randint(4, 8))]

    password_numbers = [choice(numbers) for _ in range(randint(4, 8))]

    password = password_letters + password_symbols + password_numbers

    shuffle(password)

    password = "".join(password)

    copy_to_clipboard(window, password)
