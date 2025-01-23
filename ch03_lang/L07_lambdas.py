def main():
    nums = [55, 987, 89, -233, 8, 13, -377, 3, 1, -34, 610, 144, 5, 21, 2, 1 ]

    nums.sort(key=lambda n: abs(n) )
    print(nums)

    doubled = (2*n for n in nums)
    print(list(doubled))

if __name__ == '__main__':
    main()