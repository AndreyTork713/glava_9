import pickle


def main():

    input_file = open('phonebook.dat', 'rb')
    pb = pickle.load(input_file)
    print(pb)

    input_file.close()


if __name__ == '__main__':
    main()