#!/usr/bin/env python


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/rosalind_ba3b.txt') as input_data:
        text = input_data.readline().strip()
        for line in input_data:
            text += line[-2]

    # Print and save the answer.
    print ("+" + text)
    with open('output/rosalind_ba3b.txt', 'w') as output_data:
        output_data.write(text)

if __name__ == '__main__':
    main()
