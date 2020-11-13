# Programmers:
# Course: CS151, Dr. Simari
# Date: Thu Apr 23, 2020
# Lab: 11
# Program Inputs:
# Program Outputs:

# declare column index constants for data fields
RELEASE_DATE = 0
TITLE = 1
BUDGET = 2
GROSS = 3

import math


# ------------------------------------------------------------------------------
# Given the name of a file respecting the csv format outlined above, loads the
# data into a list of lists and returns it.
def load_movie_data(filename):

    # start with an empty list for data
    data = []

    try:

        # open the given file in read mode
        f = open(filename, "r")

        # for every line in the file
        line_counter = 0
        for line in f:

            # keep track of current line number
            line_counter += 1

            # split it according to file format (in this case, commas)
            line_entries = line.split(",")

            try:

                # cast/process all fields according to their type
                line_entries[RELEASE_DATE] = line_entries[RELEASE_DATE].strip()
                line_entries[TITLE] = line_entries[TITLE].strip()
                line_entries[BUDGET] = float(line_entries[BUDGET])
                line_entries[GROSS] = float(line_entries[GROSS])

                # append processed row into data (list of lists)
                data.append(line_entries)

            except ValueError:

                print("Error reading from line", line_counter, "in file",
                      filename, ". Encountered bad value. Skipping line.")

    except FileNotFoundError:

        print("Error: file, ", "(", filename, ")", "not found.")

    # return the loaded data
    return data

# ----------------------------------------------------------------------------------------------------------------------

def get_date_by_decade(data):
    line_count = 0

    for line in data:

        # split each date
        new_line = line[RELEASE_DATE].split("/")
        intermediate_line = new_line[2]
        line_number = intermediate_line
        line_number = int(line_number)
        line_number = float(line_number)

        # find decade for each movie
        date = line_number/10
        date = math.floor(date)
        decade  = date * 10

        data[line_count][RELEASE_DATE] = decade

        line_count += 1

    return data
# ----------------------------------------------------------------------------------------------------------------------
def get_decade_counts(data):

    date_counts = {}

    for line in data:

        decade = line[RELEASE_DATE]


        # if decade is listed
        if decade in date_counts:

            date_counts[decade] += 1

        # if decade doesn't exist
        else:
            date_counts[decade] = 1

    return date_counts
# ----------------------------------------------------------------------------------------------------------------------
def print_decade_counts(date_counts):

    # sort list of dates
    dates_sorted = list(date_counts.keys())
    dates_sorted.sort()
    dates_sorted.reverse()

    for decade in dates_sorted:
        print(decade,":", date_counts[decade])


# ------------------------------------------------------------------------------
def main():

    # output purpose
    print("This program will allow you to load a movie data csv file and "
          "output the number of movies represented per decade in "
          "chronological order.")

    # ask user for filename of movie data
    filename_in = input("\nPlease enter the name of movie data csv file you "
                        "would like to load (movies.csv) : ")
    filename_in = filename_in.strip()
    print()

    # load the data from the given file
    print("Loading", filename_in, "...")
    movie_data = load_movie_data(filename_in)

    print("Done:", len(movie_data), "entries loaded.")


    # print yearly data list
    print_dates = get_date_by_decade(movie_data)
    print("\nNow printing the movies in an updated chronological list. ")
    print(print_dates)

    # print dictionary
    dictionary = get_decade_counts(movie_data)
    print("Now printing the amount of movies released in that decade.")
    print(dictionary)

    print("Now printing the final movie count.")
    final_count = print_decade_counts(dictionary)
    print(final_count)

    print("\nThank you for using this program!")



# ==============================================================================
main()
# ==============================================================================
