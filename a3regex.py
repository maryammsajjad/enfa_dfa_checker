# Maryam Sajjad
# mas454
# 11285700
# CMPT 364 - Ian McQuillan


from FAdo.fa import *
from FAdo.reex import *
from FAdo.fio import *
import time


def main():
    regex = input("enter your regular expression: ")
    regex_new = str2regexp(regex)
    print(regex_new)
    list_of_strings = input("enter your list of strings, separated by one space: ")
    list_of_strings = list_of_strings.split(" ")
    regex_to_nfa(regex_new, list_of_strings)
    regex_to_dfa(regex_new, list_of_strings)


def regex_to_nfa(regex, list_of_strings):
    # convert to nfa, record time to convert as well
    start_time = time.time()
    nfa = regex.nfaPosition()
    end_time = time.time()
    print("Time to convert to NFA:", end_time - start_time, "seconds")
    # obtain the states in the nfa
    states = len(nfa.States)
    for string in list_of_strings:
        start_time = time.time()
        nfa_acceptance = nfa.evalWordP(string)
        end_time = time.time()
        print("NFA accepts", string, ":", nfa_acceptance, "(Time taken:", end_time - start_time, "seconds)")

    print(states)


def regex_to_dfa(regex, list_of_strings):
    # convert to dfa, record time to convert as well
    start_time = time.time()
    dfa = regex.nfaPosition().toDFA()
    end_time = time.time()
    print("Time to convert to DFA:", end_time - start_time, "seconds")
    # obtain the states in dfa
    states = len(dfa.States)
    for string in list_of_strings:
        start_time = time.time()
        dfa_acceptance = dfa.evalWordP(string)
        end_time = time.time()
        print("DFA accepts", string, ":", dfa_acceptance, "(Time taken:", end_time - start_time, "seconds)")
    print(states)


if __name__ == "__main__":
    main()