# Importing NLP library

# Importing data manipulation library
import pandas as pd

# Importing systems library
import os
import sys
sys.path.append("utils")
import zipfile 
import argparse

# Funtions from utils folder 
from helper_functions import clean_data, count_words, relative_frequence, unique_NERS, create_dataframe, save_function

def input_parse():
    # initialize the parser
    parser = argparse.ArgumentParser()
    parser.add_argument("--zip_name", type=str, help = "The path to the zip file etc data/USEcorpus.zip")
    # parse the arguments from command line
    args = parser.parse_args()
    return args


def unzip(args):
    folder_path = os.path.join("data", "USEcorpus") # Defining the folder_path to the data.
    directory = folder_path # Saving the path in a new variable to be used later
    if not os.path.exists(folder_path): # If the folder path does not exist, unzip the folder, if it exists do nothing 
        print("Unzipping file")
        path_to_zip = args.zip_name # Defining the path to the zip file
        zip_destination = os.path.join("data") # defining the output destination

        with zipfile.ZipFile(path_to_zip,"r") as zip_ref: # using the package from zipfile, to un zip the zip file
            zip_ref.extractall(zip_destination) # Unzipping
    print("The files are unzipped")
    return directory



def get_data(directory): # Making a function called get_data with the parameter directory
    # Making a for loop that finds each file and the path to that file, and saves it in a variable folder_path
    # os.listdir makes a list of the specified directory with all the files in the directory.
    # os.path.join joins the "file" to the path for the file.
    for folder_name in os.listdir(directory): 
        print("Going through folder: " + folder_name)
        folder_path = os.path.join(directory, folder_name)

        # Start by checking if the new variable is a directory, if true it moves on and finds the path to each file in the subfolder.
        if os.path.isdir(folder_path):
            all_data = [] # An empty list to store each dataframe created from function "creating_dataframe".
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)
                # If statement that checks if the new file_path is a file, if yes it moves on and opens the file encoding it as latin-1 
                # Latin-1 is used here, because the files could not be read with utf-8. 
                # the read file is placed in a new variable called text.
                if os.path.isfile(file_path):
                    with open(file_path, 'r', encoding="latin-1") as file:
                        text = file.read()
                    
                    # Below are all functions created before. 
                    # Each file in each folder, goes through the code, and a csv file is created for that folder. Each row in
                    # That csv file is a text.
                    doc = clean_data(text)
                    noun_count, verb_count, adjective_count, adverb_count = count_words(doc)
                    relative_freq_ADJ, relative_freq_NOUN, relative_freq_VERB, relative_freq_ADV = relative_frequence(noun_count, verb_count, adjective_count, adverb_count, doc)
                    unique_entities_PER, unique_entities_LOC, unique_entities_ORG = unique_NERS(doc)
                    create_dataframe(all_data, file_name, relative_freq_NOUN, relative_freq_VERB, relative_freq_ADJ, relative_freq_ADV, unique_entities_PER, unique_entities_LOC, unique_entities_ORG)
                    save_function(all_data, folder_name)
                    
                     
def main_function(): # Main function  
    args = input_parse() # Command line arguments
    directory = unzip(args) # Unzipping the file and saving the directory path to the data
    get_data(directory) # Function containg the other functions
    

if __name__ == "__main__": # If called from terminal run main function 
    main_function()
