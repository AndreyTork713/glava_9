def main():

    set1 = set([1, 2, 3, 4, 5])
    set2 = {item for item in set1}
    print(set1)
    print(set2)

    set1 = set([10, 20, 30, 40, 50])
    set2 = {item for item in set1 if item > 20}
    print(set2)


if __name__ == '__main__':
    main()