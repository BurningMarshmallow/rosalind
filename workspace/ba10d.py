#!/usr/bin/env python
import itertools


def build_transition_table(input_data, states):
    transition_table = {}
    m = len(states)
    transitions = get_pairs(states, states)
    for i in range(m):
        values = map(float, input_data.readline().strip().split()[1:])
        for j, value in enumerate(values):
            transition_table[transitions[i * len(states) + j]] = value
    return transition_table

def build_emission_table(input_data, states):
    emission_table = {}
    alphabet = ["x", "y", "z"]
    m = len(states)
    n = len(alphabet)
    emissions = get_pairs(states, alphabet)
    for i in range(m):
        values = map(float, input_data.readline().strip().split()[1:])
        for j, value in enumerate(values):
            emission_table[emissions[i * len(alphabet) + j]] = value
    # print(emission_table)
    return emission_table


def get_max_and_maxpos(iterable):
    m = max(iterable)
    for pos, elem in enumerate(iterable):
        if elem == m:
            return (elem, pos)


def get_pairs(first, second):
    return ["".join(s) for s in itertools.product(first, second)]


def likelihood_algo(string, transition_table, emission_table, states):
    path = ""
    transitions = get_pairs(states, states)
    n = len(string)
    m = len(states)
    s = [[0 for j in range(m)] for i in range(n)]
    # Fill first column
    for j in range(m):
        s[0][j] = emission_table[states[j] + string[0]] / m
    # Fill other columns
    for i in range(1, n):
        for j in range(m):
            em_prob = emission_table[states[j] + string[i]]
            prev_s = [s[i - 1][x] * transition_table[transitions[x * m + j]] * em_prob for x in range(m)]
            s[i][j] = sum(prev_s)
    prob = sum([s[-1][x] for x in range(m)])
    return str(prob)

def skip_lines(input_data, number_of_lines):
    # Skip unneeded lines
    for _ in range(number_of_lines):
        input_data.readline()


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/rosalind_ba10d.txt') as input_data:
        string = input_data.readline().strip()
        skip_lines(input_data, 3)
        states = input_data.readline().strip().split()
        skip_lines(input_data, 2)
        transition_table = build_transition_table(input_data, states)
        skip_lines(input_data, 2)
        emission_table = build_emission_table(input_data, states)
    prob = likelihood_algo(string, transition_table, emission_table, states)
    # Print and save the answer.
    print(prob)
    with open('output/rosalind_ba10d.txt', 'w') as output_data:
        output_data.write(prob)

if __name__ == '__main__':
    main()
1