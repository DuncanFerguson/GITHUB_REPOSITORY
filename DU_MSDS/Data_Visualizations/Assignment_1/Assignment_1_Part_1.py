# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4433
# Assignment: Assignment 1
# Date 6/24/2021

"""
• Assignment 1, Part 1: Construct a CSV file with the first eight elements of the
periodic table. Include columns for name, symbol, and atomic number. Read that
into a pandas DataFrame. Inside the program, add a ninth and 10th element, and
then add a column with the atomic weights rounded to the nearest integer.
"""
import pandas as pd

# Part 1
# Construct a CSV file with the first eight elements of the periodic table.

# Include columns for name, symbol, and atomic number.
P_Name = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen"]  # Names
P_Symbol = ["H", "He", "Li", "Be", "B", "C", "N", "O"]  # Symbols
AtomicNumber = [i for i in range(1, len(P_Name)+1)]  # Fancy way of 1-8

# Turning lists into a data frame and saving to csv
first_eight = pd.DataFrame(list(zip(P_Name, P_Symbol, AtomicNumber)), columns=["Name", "Symbol", "Atomic_Number"])
first_eight.to_csv("Periodic_Table.csv", index=False, header=True)

# Reading in CSV file for periodic table
df = pd.read_csv("Periodic_Table.csv")

# Adding in 9th Element
df = df.append({'Name': 'Fluorine', 'Symbol': 'F', 'Atomic_Number': 9}, ignore_index=True)

# Adding in 10th Element
df = df.append({'Name': 'Neon', 'Symbol': 'Ne', 'Atomic_Number': 10}, ignore_index=True)

# Adding in Column with Atomic Weights
df['Atomic_Weights'] = [1.008, 4.002602, 6.941, 9.012182, 10.8, 12.011, 14.007, 15.999, 18.998403, 20.1797]

# Rounding Weights to nearest Integer
df['Atomic_Weights'] = df['Atomic_Weights'].round(decimals=0).astype(int)

print(df.to_string(index=False))