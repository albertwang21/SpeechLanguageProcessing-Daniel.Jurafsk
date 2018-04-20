# -*- coding: utf-8 -*-
"""
Project: Speech and Language Processing
File: DNFiniteStateAutomaton.py
Author: Wang Di
Create_Time: 2018.04.11
"""


# define a Non-Deterministic Finite-State Automaton machine
s = 'stop'
columns = ['a','b','!']
node = [2,3]
my_machine = [[s,1,s],[2,s,s],[node,s,s],[s,s,4],[s,s,s]]


# define a dict of strings for testing
a = 'accept'
r = 'reject'
my_tapes = {'aba!b':r, 'baaaaaa!':a, 'ba!':r, 'baa!':a, 'baaa!':a, 'baa':r}


# The Non-Deterministic Recognizer: non-deterministic algorithm


def accept_state(search_state, tape, machine):
    current_node = search_state['node']
    index = search_state['index']
    if index == len(tape) and list(machine[current_node]) == [s,s,s]:
        return True
    else:
        return False


def generate_new_state(current_state, tape, machine):
    current_node = current_state['node']
    index = current_state['index']
    search_states = []
    if machine[current_node][columns.index(tape[index])] != s:
        if type(machine[current_node][columns.index(tape[index])]) != list:
            new_node = machine[current_node][columns.index(tape[index])]
            search_states += [{'node': new_node, 'index': index+1}]
        else:
            for new_node in machine[current_node][columns.index(tape[index])]:
                search_states += [{'node':new_node, 'index': index+1}]
    return search_states


def nd_recognize(tape, machine):
    agenda = [{'node':0, 'index':0}]
    i = 0
    current_search_state = agenda[i]
    while s == 'stop':
        if accept_state(current_search_state, tape, machine):
            return 'accept'
        elif current_search_state['index'] >= len(tape):
            return 'reject'
        else:
            agenda += generate_new_state(current_search_state, tape, machine)
        if agenda[-1] == current_search_state:
            return 'reject'
        else:
            i += 1
            current_search_state = agenda[i]


# test
tapes = list(my_tapes.keys())
for string in tapes:
    print(nd_recognize(string,my_machine)==my_tapes[string])





