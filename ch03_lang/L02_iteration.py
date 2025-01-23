def main():

    print("Python iteration demo")

    # while True:
    #     name = input("Enter your name: ")

        # if not name:
        #     break
        #
        # print("Hello, " + name + "!")

    nums = [1, 5, 8, 10, 7, 2]
    for n in nums:
        print(f"The next number is {n}")

    print()

    for idx, n in enumerate(nums, start=1):
        print(f"The {idx}th number is {n}")

    for _ in range(1,11):
        print("This time!")

if __name__ == '__main__':
    main()