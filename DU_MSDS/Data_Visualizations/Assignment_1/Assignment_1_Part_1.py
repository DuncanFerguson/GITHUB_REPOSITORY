# Student: Duncan Ferguson
# Student Id: 871641260
# Class: Comp 4433
# Assignment: Assignment 1
# Date 6/24/2021

# Part 1
# Reading in CSV file for periodic table
df = pd.read_csv("Periodic_Table.csv")

# Adding in 9th Element
df = df.append({'Name': 'Fluorine', 'Symbol':'F', 'Atomic Number': '9'}, ignore_index=True)

# Adding in 10th Element
df = df.append({'Name': 'Neon', 'Symbol': 'Ne', 'Atomic Number': '10'}, ignore_index=True)

# Adding in Column with Atomic Weights Rounded to the nearest Integer
Atomic_Weights = [1.008, 4.002602, 6.941, 9.012182, 10.8, 12.011, 14.007, 15.999, 18.998403, 20.1797]
df['Atomic Weights'] = Atomic_Weights
df['Atomic Weights'] = df['Atomic Weights'].round(decimals=0).astype(int)
print(df)