#!/usr/bin/env python


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    d = {}
    with open('data/rosalind_ba3e.txt') as input_data:
        for line in input_data:
            line = line.strip()
            if line[:-1] in d:
                d[line[:-1]].append(line[1:])
            else:
                d[line[:-1]] = [line[1:]]

    
    # Print and save the answer.
    print(d)
    with open('output/rosalind_ba3e.txt', 'w') as output_data:
        s = sorted(d.keys())
        for k in s:
            output_data.write(k + " -> " + ",".join(sorted(d[k])) + "\n")

if __name__ == '__main__':
    main()
