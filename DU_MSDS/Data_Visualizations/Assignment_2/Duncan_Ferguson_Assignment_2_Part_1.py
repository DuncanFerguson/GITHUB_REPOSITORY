# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4433
# Assignment: Assignment 2
# Date 7/8/2021

"""Assignment 2, Part 1: Create a list of the atomic weights of the first six elements of the
periodic table, each rounded to the nearest integer. Provide two pie charts as follows: (1)
each slice annotated with a percentage of the whole and (2) each slice annotated with its
atomic weight. Explode a different element with each chart.
"""

import pandas as pd

P_Name = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon"]  # Adding Element Name
P_Symbol = ["H", "He", "Li", "Be", "B", "C"]  # Symbols
AtomicNumber = [i for i in range(1, len(P_Name)+1)]  # Adding in element number

first_six = pd.DataFrame(list(zip(P_Name, P_Symbol, AtomicNumber)), columns=["Name", "Symbol", "Atomic_Number"])
first_six['Atomic_Weights'] = [1.008, 4.002602, 6.941, 9.012182, 10.8, 12.011].round(decimals=0).astype(int)

print(first_six)

