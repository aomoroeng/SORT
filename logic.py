def main():
    ...

def bubble_sort(array):
    loop = True
    steps = []
    n = len(array)

    while loop:
        loop = False
        for i in range(n - 1):
            if array[i] > array[i + 1]:
                temper = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temper
                steps.append(array)
                loop = True

    return array, steps

if __name__ == "__main__":
    main()
