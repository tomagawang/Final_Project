def multiple_choice():
    answer = input("Please enter a choice between A or B:").lower()
    if answer == 'a':
        return 0
    elif answer == 'b':
        return 1
    else:
        print('You have entered a choice outside of the choices.')
        multiple_choice()

def main():
    multiple_choice()


if __name__ == '__main__':

    main()