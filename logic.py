def main():
    ...

def bubble_sort(number):
    loop = True
    steps = 0
    n = len(number)

    while loop:
        loop = False
        for i in range(n - 1):
            if number[i] > number[i + 1]:
                temper = number[i]
                number[i] = number[i + 1]
                number[i + 1] = temper
                steps += 1
                loop = True

    return number, steps

if __name__ == "__main__":
    main()
