#!/usr/bin/env python
import itertools
from collections import defaultdict


def skip_lines(input_data, number_of_lines):
    # Skip unneeded lines
    for _ in range(number_of_lines):
        input_data.readline()

        
def get_threshold_columns(threshold, alignment_strings):
    m = len(alignment_strings)
    n = len(alignment_strings[0])
    bad_columns = []
    for i in range(n):
        column = [alignment_strings[x][i] for x in range(m)]
        dels = column.count("-")
        if dels / m >= threshold:
            bad_columns.append(i)
    return bad_columns


def get_alignment_states(alignment_strings, threshold_columns):
    m = len(alignment_strings)
    states = [[] for t in range(m)]
    for i in range(m):
        cur_idx = 0
        for j in range(len(alignment_strings[i])):
            if j in threshold_columns:
                if alignment_strings[i][j] == "-":
                    continue
                states[i].append("I" + str(cur_idx))
                continue
            cur_idx += 1
            if alignment_strings[i][j] == "-":
                states[i].append("D" + str(cur_idx))
            else:
                states[i].append("M" + str(cur_idx))
    return states
        
        
def build_alignment_star(threshold_columns, alignment_strings):
    star = [[] for i in range(len(alignment_strings))]
    for index, string in enumerate(alignment_strings):
        for i in range(len(string)):
            if i in threshold_columns:
                not_del = string[i] != "-"
                if not_del:
                    star[index].append(string[i])
            else:
                star[index].append(string[i])
    return star


def build_transition_table(alphabet, alignment_states, alignment_star, n):
    transition_dict = defaultdict(list)
    m = len(alignment_star)
    for i in range(m):
        ins_count = 0
        transition_dict["S"].append(alignment_states[i][0])
        state_len = len(alignment_states[i])
        for j in range(state_len - 1):
            transition_dict[alignment_states[i][j]].append(alignment_states[i][j + 1])
            if alignment_states[i][j] == "I":
                ins_count += 1
        transition_dict[alignment_states[i][state_len - 1]].append("E")
    num_of_states = 3*(n+1)
    transition_table = [[0] * num_of_states for i in range(num_of_states)]
    print(transition_dict)
    states = get_hmm_states(num_of_states)
    for i in range(num_of_states):
        for j in range(num_of_states):
            state = states[i]
            state_letters = transition_dict[state]
            transition_table[i][j] = state_letters.count(states[j]) / max(1, len(state_letters))
    return transition_table

    

def build_emission_table(alphabet, alignment_states, alignment_star, n):
    emission_dict = defaultdict(list)
    m = len(alignment_star)
    for i in range(m):
        state_len = len(alignment_states[i])
        for j in range(state_len):
            emission_dict[alignment_states[i][j]].append(alignment_star[i][j])
    emission_table = [[0] * len(alphabet) for i in range(3 * (n+1))]
    states = get_hmm_states(3*(n+1))
    for i in range(3 * (n+1)):
        for j in range(len(alphabet)):
            state = states[i]
            state_letters = emission_dict[state]
            emission_table[i][j] = state_letters.count(alphabet[j]) / max(1, len(state_letters))
    return emission_table


def get_hmm_states(number_of_states):
    states = []
    for index in range(number_of_states):
        states.append(get_hmm_state(index, number_of_states))
    return states


def get_hmm_state(index, number_of_states):
    if index < 2:
        if index == 0:
            return "S"
        else:
            return "I0"
    if index == number_of_states - 1:
        return "E"
    index -= 2
    return ["M", "D", "I"][index % 3] + str(index // 3 + 1)

def get_alignment_state(type, index, ins_count):
    if type != "I":
        index += 1 - ins_count
    else:
        index -= ins_count
    return type + str(index)


def print_table(table, rows, columns, output_data):
    output_data.write("\t" + "\t".join(columns) + "\n")
    for i in range(len(rows)):
        output_data.write(rows[i] + "\t")
        values = ["{0:.1f}".format(table[i][j]) for j in range(len(columns))]
        output_data.write("\t".join(values) + "\n")


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/rosalind_ba10e.txt') as input_data:
        threshold = float(input_data.readline().strip())
        skip_lines(input_data, 1)
        alphabet = input_data.readline().strip().split()
        skip_lines(input_data, 1)
        alignment_strings = []
        for line in input_data:
            alignment_strings.append(line.strip())
        print("Strings are:")
        print("\n".join(alignment_strings))
    threshold_columns = get_threshold_columns(threshold, alignment_strings)
    print("Bad columns are:"); print(threshold_columns)
    alignment_star = build_alignment_star(threshold_columns, alignment_strings)
    print("Alignment*:")
    print(alignment_star)
    alignment_states = get_alignment_states(alignment_strings, threshold_columns)
    print("States:")
    print(alignment_states)
    n = len(alignment_strings[0])
    n -= len(threshold_columns)

    hmm_states = get_hmm_states(3*(n+1))
    transition_table = build_transition_table(alphabet, alignment_states, alignment_star, n)
    emission_table = build_emission_table(alphabet, alignment_states, alignment_star, n)
    with open('output/rosalind_ba10e.txt', 'w') as output_data:
        print_table(transition_table, hmm_states, hmm_states, output_data)
        output_data.write("--------" + "\n")
        print_table(emission_table, hmm_states, alphabet, output_data)

if __name__ == '__main__':
    main()
