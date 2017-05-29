#!/usr/bin/env python


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    kmers = []
    with open('data/rosalind_ba3c.txt') as input_data:
        for line in input_data:
            kmers.append(line.strip())
    
    d = {}
    print(kmers)
    for n in kmers:
        for m in kmers:
            if n[1:] == m[:-1]:
                d[n] = m
    # Print and save the answer.
    with open('output/rosalind_ba3c.txt', 'w') as output_data:
        for k in d:
            output_data.write(k + " -> " + d[k] + "\n")

if __name__ == '__main__':
    main()
