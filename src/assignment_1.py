# Importing NLP library
import spacy
nlp = spacy.load("en_core_web_md") # loads the entire model spacy into the variable nlp

# Importing data manipulation library
import pandas as pd
import re

# Importing systems library
import os
import sys
sys.path.append(".")

# Creating functions to be used later 

# Cleaning function
def clean_data(corpus): 
    text = re.sub(r'<.*?>', '', corpus)  # Regexing removing alle places where there are angle brackets in the corpus.
    # sub - replaces the occurrance 
    # . - means all characters
    # * - means zero or more occurances
    # ? - means matching the lowest amount possible
    doc = nlp(text) # use spacy nlp to create and find tokens defined by spacy.

    return doc

# Counting nouns, verbs, adjectives, and adverbs function
def count_words(corpus):
    noun_count =0    # Creating empty variables to store the number of occurances for nouns, verbs, adjectives and adverbs  
    verb_count =0
    adjective_count = 0
    adverb_count = 0

    # For loop that counts the number of times each adj, noun, verb and adv accours, and adds one, by using spacys pos.
    # part of speach 
    for token in corpus: 
        if token.pos_ =="ADJ": # Each time "ADJ" appears
            adjective_count +=1 # add one to empty variable 
        elif token.pos_ == "NOUN":
            noun_count += 1
        elif token.pos_ == "VERB":
            verb_count +=1
        elif token.pos_ == "ADV":
            adverb_count += 1

    return noun_count, verb_count, adjective_count, adverb_count

# Relative frequency function
def relative_frequence(nouns, verbs, adjectives, adverbs, corpus):
    
    relative_freq_ADJ = round((adjectives/len(corpus)) * 10000, 2) # Finding the relative frequence by dividing a specific part of speech with the lenght of the text
    #, multiplying by 10 000, and rounding up to 2 decimal numbers
    relative_freq_NOUN = round((nouns/len(corpus)) * 10000, 2)

    relative_freq_VERB = round((verbs/len(corpus)) * 10000, 2)

    relative_freq_ADV = round((adverbs/len(corpus)) * 10000, 2)

    return relative_freq_ADJ, relative_freq_NOUN, relative_freq_VERB, relative_freq_ADV

# Function to count unique: PER, LOC, ORG
def unique_NERS(corpus):
    # Finding Unique PER; LOC, ORG
    # creating empty lists
    entities_PER = [] 
    entities_LOC = []
    entities_ORG = []

    # for loop that finds each word with either person, loc or org and appends to the matching variable 
    for ent in corpus.ents: # get named entities and add to list
        if ent.label_ == "PERSON": # If "PERSON" appears, append to list 
            entities_PER.append(ent.text)
        elif ent.label_ == "LOC":
            entities_LOC.append(ent.text)
        elif ent.label_ == "ORG":
            entities_ORG.append(ent.text)

    # defining unique only with the set function
    unique_entities_PER = len(set(entities_PER)) # Removing duplicates, and then counting length of the list.
    unique_entities_LOC = len(set(entities_LOC))
    unique_entities_ORG = len(set(entities_ORG))

    return unique_entities_PER, unique_entities_LOC, unique_entities_ORG

# Creating dataframes function
def create_dataframe(all_data, file_name, relative_freq_NOUN, relative_freq_VERB, relative_freq_ADJ, relative_freq_ADV, unique_entities_PER, unique_entities_LOC, unique_entities_ORG):
    # Creating an empty list to store the touples, created below.
    touple_of_data = [] 

    # Appending each variable together as a touple 
    touple_of_data.append((file_name, relative_freq_NOUN, relative_freq_VERB, relative_freq_ADJ, relative_freq_ADV, unique_entities_PER, unique_entities_LOC, unique_entities_ORG))
    # And creating a dataframe out of the list. Specifying columns aswell.
    data = pd.DataFrame(touple_of_data, columns=['Filename', 'Noun Freq', 'Verb Freq', 'Adj Freq', 'Adv Freq', 'Unique PER', 'Unique LOC', 'Unique ORG'])
    
    # Appending each dataframe (which is only one row) into an empty list created in the "get_data function"
    all_data.append(data)

# Function for saving dataframes, as csv
def save_function(all_data, folder_name):
    # concating / appending all dataframes together to create one dataframe for each text.
    final_data = pd.concat(all_data)
    # Saving the dataframe to folder out.
    outpath = os.path.join(".", "out", folder_name + ".csv") 
    final_data.to_csv(outpath, index= False) # index false to not add an index


def get_data(directory): # Making a function called find_attributes with the parameter directory
    # Making a for loop that finds each file and the path to that file, and saves it in a variable folder_path
    # os.listdir makes a list of the specified directory with all the files in the directory.
    # os.path.join joins the "file" to the path for the file.
    for folder_name in os.listdir(directory): 
        folder_path = os.path.join(directory, folder_name)

        # Start by checking if the new variable is a directory, if true it moves on and finds the path to each file in the subfolder.
        if os.path.isdir(folder_path):
            all_data = [] # An empty list to store each dataframe created from function "creating_dataframe".
            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)
                # If statement that checks if the new file_path is a file, if yes it moves on and opens the file encoding it as latin-1 
                # Latin-1 is used here, because the files could not be read with utf8. 
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
                    
                     


def main_function(): # Main function that has the directory path for the data. 
    directory = os.path.join(".", "in", "USEcorpus")
    get_data(directory)
    


if __name__ == "__main__": # If called from terminal run main function 
    main_function()
