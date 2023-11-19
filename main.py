from yacc import parser


def main():
    while True:
        try:
            expression = input('Enter expression: ')
        except EOFError:
            break
        if expression.lower() == "exit":
            print('end')
            break
        if not expression:
            print('You need to enter something')
            continue
        result = parser.parse(expression)
        print(result)


if __name__ == "__main__":
    main()
