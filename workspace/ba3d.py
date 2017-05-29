#!/usr/bin/env python

from ba3a import generate_kmers

def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/rosalind_ba3d.txt') as input_data:
        k = int(input_data.readline().strip())
        text = input_data.readline().strip()
    print(text)
    kmers = generate_kmers(text, k - 1)
    d = {}
    print(kmers)
    for i in range(len(kmers) - 1):
        n = kmers[i]
        m = kmers[i + 1]
        if n in d:
            d[n].append(m)
        else:
            d[n] = [m]
    
    # Print and save the answer.
    print(d)
    with open('output/rosalind_ba3d.txt', 'w') as output_data:
        s = sorted(d.keys())
        for k in s:
            output_data.write(k + " -> " + ",".join(sorted(d[k])) + "\n")

if __name__ == '__main__':
    main()
