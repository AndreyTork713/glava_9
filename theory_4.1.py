def main():
    set1 = set([1, 2, 3, 4, 5, 6])
    set2 = set([2, 4, 6, 8])
    set4 = set([1, 3, 5, 2])
    set3 = set1.intersection(set2)
    print(set3)
    set5 = set3 & set4
    print(set5)

if __name__ == '__main__':
    main()