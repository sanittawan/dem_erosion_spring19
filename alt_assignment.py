'''
Code for assigning students based on their ranked preferences

Author: Sanittawan Tan (Nikki)
'''
import pandas as pd
import numpy as np
from random import shuffle

FIRSTNAME = 'first name'
LASTNAME = 'last name'
PREF = [FIRST, SECOND, THIRD, FOURTH, FIFTH]

def read_process_spreadsheet(filename):
    ID = 'id'
    FIRST = 'first choice'
    SECOND = 'second choice'
    THIRD = 'third choice'
    FOURTH = 'fourth choice'
    FIFTH = 'fifth choice'

    students_df = pd.read_csv(filename)
    students_df.drop(columns=['Timestamp'], inplace=True)
    students_df.columns = ['email', FIRSTNAME, LASTNAME, ID, FIRST, 
                           SECOND, THIRD, FOURTH, FIFTH]
    return students_df

def read_country_spreadsheet(filename):
    country_df = pd.read_csv(filename)
    country_df.set_index(['country'], inplace=True)
    country_df['student'] = 0

    return country_df

def assign():
    allocated_students = set()
    rounds = 5
    students_df = read_process_spreadsheet('survey.csv')
    cp_students_df = students_df.copy()
    assigned_df = read_country_spreadsheet('countries.csv')

    for i in range(rounds):
        if i > 0:
            shuffle(order) 
        else:
            order = list(np.random.permutation(
                            np.arange(0, cp_students_df.shape[0])))
        print(order)
        cp_order = order.copy()
        for j in cp_order:
            cur_student = students_df.iloc[j]
            cur_choice = cur_student[PREF[i]]
            if not cur_choice:
                continue
            if (assigned_df.loc[cur_choice]['student'] == 0) and\
                cp_students_df[cp_students_df[PREF[i]] == cur_choice].shape[0] == 1:
                assigned_df.loc[cur_choice] = cur_student[LASTNAME]
                allocated_students.add(cur_student[LASTNAME])
                order.remove(j)
                cp_students_df = cp_students_df.drop([j])
    print(cp_students_df)
    print(assigned_df)
    # deal with students who were not allocated any countries so far
    unallocated_students = list(cp_students_df[LASTNAME].values)
    avail_countries = assigned_df[assigned_df['student'] == 0]

    i = 0
    for ind, _ in avail_countries.iterrows():
        assigned_df.loc[ind] = unallocated_students[i]
        i += 1
    print(assigned_df)





