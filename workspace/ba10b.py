#!/usr/bin/env python

from ba3a import generate_kmers

def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    emission_table = {}
    with open('data/rosalind_ba10b.txt') as input_data:
        string = input_data.readline().strip()
        for i in range(3):
            input_data.readline() # Skip unneeded lines
        path = input_data.readline().strip()
        transitions = generate_kmers(path, 2)
        for i in range(4):
            input_data.readline() # Skip unneeded lines
        ax, ay, az = map(float, input_data.readline().strip().split()[1:])
        bx, by, bz = map(float, input_data.readline().strip().split()[1:])
        emission_table["Ax"] = ax
        emission_table["Ay"] = ay
        emission_table["Bx"] = bx
        emission_table["By"] = by
        emission_table["Az"] = az
        emission_table["Bz"] = bz
    print(emission_table)
    pairs = zip(path, string)
    cond_prob = 1
    for pair in pairs:
        path_symbol = "".join(pair)
        cond_prob *= emission_table[path_symbol]
    # Print and save the answer.
    print(cond_prob)
    with open('output/rosalind_ba10b.txt', 'w') as output_data:
        output_data.write(str(cond_prob))

if __name__ == '__main__':
    main()
