
# МНОЖЕСТВА
def main():

    myset1 = set(['один', 'два', 'три'])
    print(myset1)
    print(len(myset1))

    myset2 = set('один два три')
    print(myset2)
    print(len(myset2))

    myset3 = set(['один два три'])
    print(myset3)
    print(len(myset3))

    myset4 = set()
    myset4.add(11)
    myset4.add(21)
    myset4.add(31)
    print(myset4)

    myset4.update([41, 51, 61])
    print(myset4)
    myset4.update(myset1)
    print(myset4)


if __name__ == '__main__':
    main()