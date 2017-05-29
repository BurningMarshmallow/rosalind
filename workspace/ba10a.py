#!/usr/bin/env python

from ba3a import generate_kmers

def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    transition_table = {}
    with open('data/rosalind_ba10a.txt') as input_data:
        path = input_data.readline().strip()
        transitions = generate_kmers(path, 2)
        for i in range(4):
            input_data.readline() # Skip unneeded lines
        aa, ab = map(float, input_data.readline().strip().split()[1:])
        ba, bb = map(float, input_data.readline().strip().split()[1:])
        transition_table["AA"] = aa
        transition_table["AB"] = ab
        transition_table["BA"] = ba
        transition_table["BB"] = bb
    prob = 0.5
    for trans in transitions:
        prob *= transition_table[trans]
    # Print and save the answer.
    with open('output/rosalind_ba10a.txt', 'w') as output_data:
        output_data.write(str(prob))

if __name__ == '__main__':
    main()
