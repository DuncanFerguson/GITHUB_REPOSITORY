# Student: Duncan Ferguson
# Student ID: 871-641-260
# Class: COMP-3006-2; Project 6: numpy and pandas
# Date: 3/18/2021
# Teacher: dalton.crutchfield@du.edu
# TA: sunny.shrestha@du.edu

import pandas as pd
import numpy as np


"""Project 6: 

Part 1 (make_matrix): This program uses numpy to generate a 10 column by 1000 row matrix of values. These random values
have been hard coded in as 1 to 40. This matrix of random numbers represents 'snow' fall. The columns for the matrix
are hard coded at the start. (make_csv_file) This Matrix is then saved as a csv file 'Mountains.csv
There are two options for saving. The first uses pandas to save the file. The commented out code is how to save the 
csv file without using pandas. 
 
Part 2 (make_panda): Using pandas, this csv labeled 'Mountains.csv' is then loaded as a data frame. 

Part 3 (mountain_stats): A New panda is created 'my_stats.' This dataframe contains the headers or keys from 
mountain_pandas. The index is then set to the stats required, 'mean', 'St_dev', 'mode' , and 'median'. 
Looping through each column and taking the stats from the index.
  
Part 4 (gen_sum_file): 'Mountain Stats' are saved to the txt file 'Mountain_Stats.txt'
Three Random Rows are chosen for our sample data and then printed to the txt file as well. """


def make_matrix():
    """This function generates a 10 column by 1000 row matrix of values"""
    num_columns = 10
    num_rows = 1000
    matrix = np.random.randint(1, 40, (num_rows, num_columns))  # It will snow a random 1 to 40 inches

    return matrix


def make_csv_file(data_2_save):
    """This function makes a csv file with the matrix created above. This is supposed to represent
    data for inches of snow per month for ten different mountains the last 1000 big storm events. The code turns
    the matrix into a panda first and then saves to 'Mountains.csv' The commented out code accomplishes the same thing
    but does not use pandas. """

    # Creating 10 mountains for column names to try and make sense of random matrix
    column_names = ["Keystone", "Vail", "Beaver_Creek", "A_basin", "Aspen",
                    "Winter Park", "Copper", "Echo_Mountain", "Telluride", "Wolf_Creek"]
    data_2_save = pd.DataFrame(data_2_save)
    data_2_save.columns = column_names
    data_2_save.to_csv("Mountains.csv", index=False)  # Saving to CSV without the index, but with column names
    print("\n\nCreated Matrix: Random into 1-40 inches of snow\n\n", data_2_save)

    # TODO This is an alternate way to save the array to csv not using pandas
    # column_names ="Keystone,Vail,Beaver_Creek,A_basin,Aspen," \
    #                 "Winter_Park,Copper,Echo_Mountain,Telluride,Wolf_Creek\n"
    # # Creating CSV file with data
    # with open("Mountains.csv", mode="w") as f:
    #     f.write(column_names)
    #     for x in data_2_save:
    #         for y in range(len(x)):
    #             f.write(str(x[y])+",")  # Writing row
    #         f.write("\n")  # New row


def make_panda():
    """This function uses pandas to load the file that was just created as a dataframe"""
    df = pd.read_csv("Mountains.csv", header=0, index_col=False)  # Loading in file name
    return df


def mountain_stats(mountain_pandas):
    """This function calculates an array of stats required. The Mean, Stdev, Mode, Median. Being the row index.
    With the columns being the 'not hard coded' column names of  mountain_pandas, which is a panda passed into
    the function."""

    # Creating Panda to record stats
    my_stats = pd.DataFrame(columns=mountain_pandas.columns, index=["Mean", "St_Dev", "Mode", "Median"])

    # Looping through the columns and index to calculate stats and fill dataframe
    for mountain in my_stats.keys():
        for _ in my_stats.index:
            my_stats[mountain][0] = mountain_pandas[mountain].mean()
            my_stats[mountain][1] = mountain_pandas[mountain].std()
            my_stats[mountain][2] = mountain_pandas[mountain].mode()[0]  # Changing Mode to Columns
            my_stats[mountain][3] = mountain_pandas[mountain].median()
    print("\n\nMountain Stats\n\n", my_stats)

    return my_stats


def gen_sum_file(stats, original_data_frame):
    """Generating a text file called "Mountain_Stats.txt" that includes the statistics and 3 random sample rows"""

    # Taking three random sample rows and converting to string
    original_data_frame = original_data_frame.sample(n=3).to_string()
    print("\n\n3 Sample Rows\n\n", original_data_frame)

    # Writing the stats from above to txt file
    stats = stats.to_string()
    with open("Mountain_Stats.txt", mode='w') as f:
        f.write(stats)  # Writing the stats to file
        f.write("\n\nThree Sample Rows\n\n")
        f.write(original_data_frame)  # Writing 3 sample rows into file


def main():
    """This function holds the main code ."""
    mountain_cub = make_matrix()  # Making a 1000 x 10 array
    make_csv_file(mountain_cub)  # Saving Array to csv "Mountains.csv"
    mountain_panda = make_panda()  # Opening "Mountains.csv" and turing it into a dataframe
    stats = mountain_stats(mountain_panda)  # Taking Statistics of that dataframe
    gen_sum_file(stats, mountain_panda)  # Saving Stats to txt file  "Mountain_Stats" and 3 Samples Rows


if __name__ == "__main__":
    main()
