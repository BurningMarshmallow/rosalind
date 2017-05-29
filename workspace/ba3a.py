#!/usr/bin/env python



def generate_kmers(text, k):
    kmers = []
    for i in range(len(text)-k + 1):
        kmers.append(text[i:i+k])

    return kmers


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/rosalind_ba3a.txt') as input_data:
        k = int(input_data.readline())
        text = input_data.readline()

    kmers = generate_kmers(text, k)

    # Print and save the answer.

    with open('output/rosalind_ba3a.txt', 'w') as output_data:
        output_data.write("\n".join(kmers))

if __name__ == '__main__':
    main()
