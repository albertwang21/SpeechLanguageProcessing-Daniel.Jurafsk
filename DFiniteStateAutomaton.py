# -*- coding: utf-8 -*-
"""
Project: Speech and Language Processing
File: DFiniteStateAutomaton.py
Author: Wang Di
Create_Time: 2018.04.11
"""

import numpy as np


# define a Deterministic Finite-State Automaton machine
s = 'stop'
columns = ['a','b','!']
my_machine = np.array([[s,1,s],[2,s,s],[3,s,s],[3,s,4],[s,s,s]])


# define a dict of strings for testing
a = 'accept'
r = 'reject'
my_tapes = {'aba!b':r, 'baaaaaa!':a, 'ba!':r, 'baa!':a, 'baaa!':a, 'baa':r}


# The Deterministic Recognizer: deterministic algorithm
def d_recognize(tape, machine):
    index = 0
    machine_state = 0
    while s == 'stop':
        if index == len(tape):
            if list(machine[machine_state]) == [s,s,s]:
                return 'accept'
            else:
                return 'reject'
        elif machine[machine_state,columns.index(tape[index])] == s:
            return 'reject'
        else:
            machine_state = int(machine[machine_state,columns.index(tape[index])])
            index = int(index + 1)


# test
tapes = list(my_tapes.keys())
for string in tapes:
    print(d_recognize(string,my_machine) == my_tapes[string])




