def main():
    name = input("What is your name? ")
    some_method(name)


def some_method(name):
    if name.strip().lower() == "jorge":
        print("Hello Jorge!")
    else:
        print(f"Nice to meet you  {name}")
        print("My name is Python")


if __name__ == '__main__':
    main()