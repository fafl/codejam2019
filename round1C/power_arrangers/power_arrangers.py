import sys


def debug(*s):
    # pass
    print(*s, file=sys.stderr)


def main():
    t, f = map(int, input().split())

    for testcase_number in range(1, t + 1):

        known_letters = [''] * 595

        # Check the first letter of each set, using 119 guesses
        for i in range(0, 595, 5):
            print(i+1, flush=True)
            known_letters[i] = input()

        # One letter appears only 23 times
        first_letter = next(c for c in 'ABCDE' if known_letters.count(c) == 23)

        # Check the second letter, using 23 guesses (142 so far)
        for i in range(1, 595, 5):
            if known_letters[i-1] != first_letter:
                continue
            print(i+1, flush=True)
            known_letters[i] = input()

        # One letter appears only 5 times
        second_letter = next(c for c in 'ABCDE' if known_letters[1::5].count(c) == 5)

        # Check the third letter, using 5 guesses (147 so far)
        for i in range(2, 595, 5):
            if known_letters[i - 2] != first_letter:
                continue
            if known_letters[i - 1] != second_letter:
                continue
            print(i + 1, flush=True)
            known_letters[i] = input()

        # One letter appears only once
        third_letter = next(c for c in 'ABCDE' if known_letters[2::5].count(c) == 1)

        # Check the fourth letter, using 1 guess (148 so far)
        for i in range(3, 595, 5):
            if known_letters[i - 3] != first_letter:
                continue
            if known_letters[i - 2] != second_letter:
                continue
            if known_letters[i - 1] != third_letter:
                continue
            print(i + 1, flush=True)
            fifth_letter = input()  # This fourth letter must be our fifth letter

        # The fourth letter is the only one left
        fourth_letter = (set('ABCDE') - {first_letter, second_letter, third_letter, fifth_letter}).pop()

        print(''.join([first_letter, second_letter, third_letter, fourth_letter, fifth_letter]))

        assert input()


if __name__ == '__main__':
    main()
