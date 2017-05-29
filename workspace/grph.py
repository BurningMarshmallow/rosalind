#!/usr/bin/env python

from FASTA import ReadFASTA

def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.

    dna_list = ReadFASTA('data/rosalind_grph.txt')

    overlaps = []
    for i in range(len(dna_list)):
        for j in filter(lambda j: j!=i, range(len(dna_list))):
            if  dna_list[i][1][-3:] == dna_list[j][1][:3]:
                overlaps.append(dna_list[i][0] + ' ' + dna_list[j][0])

    # Print and save the answer.
    print ('\n'.join(overlaps))
    with open('output/012_GRPH.txt', 'w') as output_data:
        output_data.write('\n'.join(overlaps))

if __name__ == '__main__':
    main()
