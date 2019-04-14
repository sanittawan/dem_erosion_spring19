'''
Code for assigning students based on their ranked preferences

Author: Sanittawan Tan (Nikki)
'''
import pandas as pd
import numpy as np
from random import shuffle

FIRSTNAME = 'first name'
LASTNAME = 'last name'
FIRST = 'first choice'
SECOND = 'second choice'
THIRD = 'third choice'
FOURTH = 'fourth choice'
FIFTH = 'fifth choice'
PREF = [FIRST, SECOND, THIRD, FOURTH, FIFTH]
STUDENT = 'student'

def read_process_spreadsheet(filename):
    ID = 'id'
    TIME = 'Timestamp'
    EMAIL = 'email'
    students_df = pd.read_csv(filename)
    students_df.drop(columns=[TIME], inplace=True)
    students_df.columns = [EMAIL, FIRSTNAME, LASTNAME, ID, FIRST, 
                           SECOND, THIRD, FOURTH, FIFTH]
    return students_df

def read_country_spreadsheet(filename):
    country_df = pd.read_csv(filename)
    country_df.set_index(['country'], inplace=True)
    country_df[STUDENT] = 0

    return country_df

def assign():
    allocated_students = set()
    rounds = 5
    students_df = read_process_spreadsheet('test_students.csv')
    cp_students_df = students_df.copy()
    assigned_df = read_country_spreadsheet('test_countries_small.csv')

    # allocate countries to students based on their preferences
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
            if not cur_choice or pd.isna(cur_choice):
                continue
            if (assigned_df.loc[cur_choice][STUDENT] == 0) and\
                (cp_students_df[cp_students_df[PREF[i]] == cur_choice].shape[0] == 1):
                assigned_df.loc[cur_choice] = cur_student[LASTNAME]
                allocated_students.add(cur_student[LASTNAME])
                order.remove(j)
                cp_students_df = cp_students_df.drop([j])
    print(cp_students_df)
    print(assigned_df)
    
    # deal with students who were not allocated any countries so far
    unallocated_students = list(cp_students_df[LASTNAME].values)
    avail_countries = assigned_df[assigned_df[STUDENT] == 0]
    for i, student in enumerate(unallocated_students):
        assigned_df.iloc[i] = student
    print(assigned_df)

if __name__ == '__main__':
    assign()





