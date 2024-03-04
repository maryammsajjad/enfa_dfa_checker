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
    nfa_dfa_dict = dict()
    list_of_strings = input("enter your list of strings, separated by one space: ")
    list_of_strings = list_of_strings.split(" ")
    regex_to_nfa(regex_new, list_of_strings, nfa_dfa_dict)
    regex_to_dfa(regex_new, list_of_strings, nfa_dfa_dict)
    print("{:<8} {:<15} {:<25} {:<15} {:<25}".format('String', 'Accepted by NFA', 'Time', 'Accepted by DFA', 'Time'))
    for k, v in nfa_dfa_dict.items():
        enfa, time1, dfa, time2 = v
        print("{:<8} {:<15} {:<25} {:<15} {:<25}".format(k, enfa, time1, dfa, time2))


def regex_to_nfa(regex, list_of_strings, nfa_dfa_dict):
    # convert to nfa, record time to convert as well
    start_time = time.time()
    nfa = regex.nfaPosition()
    end_time = time.time()
    print("---------------------------------------------------------------")
    print("Time to convert to NFA:", end_time - start_time, "seconds")
    # obtain the states in the nfa
    print("Number of states:", len(nfa.States))
    print("---------------------------------------------------------------")
    for string in list_of_strings:
        start_time = time.time()
        nfa_acceptance = nfa.evalWordP(string)
        end_time = time.time()
        nfa_dfa_dict[string] = [nfa_acceptance, end_time - start_time]
        print("NFA accepts", string, ":", nfa_acceptance, "(Time taken:", end_time - start_time, "seconds)")
    print("---------------------------------------------------------------")
    return nfa_dfa_dict


def regex_to_dfa(regex, list_of_strings, nfa_dfa_dict):
    # convert to dfa, record time to convert as well
    start_time = time.time()
    dfa = regex.nfaPosition().toDFA()
    end_time = time.time()
    print("---------------------------------------------------------------")
    print("Time to convert to DFA:", end_time - start_time, "seconds")
    # obtain the states in dfa
    print("Number of states:", len(dfa.States))
    print("---------------------------------------------------------------")
    for string in list_of_strings:
        start_time = time.time()
        dfa_acceptance = dfa.evalWordP(string)
        end_time = time.time()
        nfa_dfa_dict[string] += [dfa_acceptance, end_time - start_time]
        print("DFA accepts", string, ":", dfa_acceptance, "(Time taken:", end_time - start_time, "seconds)")
    print("---------------------------------------------------------------")


if __name__ == "__main__":
    main()
