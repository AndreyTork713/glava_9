import pickle


def main():

    phonebook = {'Крис': '555-1111',
                 'Кэти': '555-2222',
                 'Джоанна': '555-333'}

    output_file = open('phonebook.dat', 'wb')
    pickle.dump(phonebook, output_file)

    output_file.close()
    print(output_file)


if __name__ == '__main__':
    main()


