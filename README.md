
# Assignment 1 - Extracting linguistic features using spaCy

## Contribution 
- This assignment was made in contribution with fellow students from class, and with inspiration from in-class notebooks. All in-code comments are made by me.
- The assignment uses data gathered by the University of Oxford.

### Data 
- The data from the University of Oxford consits of 1 489 English papers written by 440 Swedish students. The data is split up into 14 folders. The folders are split up in *a, b,* and *c*, each representing a different level of English proficency. There are five folders of A-level essays, eight B-level essays, and one C-level essay. Each folder, representing a group, had a different subject that they wrote about. According to the authors of the data, the average essay length is 820 words. For more information: [University of Oxford, 2003, The Uppsala Student English Corpus (USE), Oxford Text Archive,] (https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2457). 

## Packages 
-	Spacy
    - Is used for Natural language processing (NLP), Part of Speech tagging (POS), and named entity recognition. 
    - I am using the medium version of Spacy, which allows for *part-of-speech tagging* and *named entity recognition.* 
-	Pandas
    - Is used for data manipulation and structuring the data
-	Re
    - Is used to create a regular expression
-	Os
    - Is used to navigate the operating system
-	Sys
    - Is used to navigate the directory
-	Zipfile
    - Is used to extract the zip file
-	Argparse
    - Is used to specify the path to the zip file as a command line argument.

## Repository Contents 
The repository contains:
- assignment_1 
    - This folder contains the virtual environment. 
- data
    - An empty folder where you will place the zip-file 
- out
    - The folder that will contain the output CSV files for each folder
- src
    - The folder that contains the python script
- README.md 
    - The README file 
- requirements.txt 
    - A text file containing the required libraries, that will be installed when you run the setup.sh file.
- setup.sh 
    - The setup file that will create a virtual environment, upgrade pip, and install the nessecary requirements.

## Assignment description 
Written by Ross:
For this exercise, you should write some code that does the following:

- Loop over each text file in the folder
- Extract the following information:
    - Relative frequency of Nouns, Verbs, Adjective, and Adverbs per 10,000 words
    - Total number of *unique* PER, LOC, ORGS
- For each sub-folder (a1, a2, a3, ...) save a table which shows the following information:

|Filename|RelFreq NOUN|RelFreq VERB|RelFreq ADJ|RelFreq ADV|Unique PER|Unique LOC|Unique ORG|
|---|---|---|---|---|---|---|---|
|file1.txt|---|---|---|---|---|---|---|
|file2.txt|---|---|---|---|---|---|---|
|etc|---|---|---|---|---|---|---|

## Methods / What does the code do
The code does the following:
- The script starts by initializing an argparse, which is used to define the path to the zip file. The code than checks if a specific path to the the data exists. If the path does not exist, the zip file is extracted. After extracting the data, functions are created which will be used later. The first function, ```clean_data```, uses regular expression to clean the files. The regular expression, removes all angel brackets and whats is in between the angle brackets. The next function, ```count_words```, uses SpaCys *part-of-speech* (POS) tagging to count each time an adjective, noun, verb, or adverb appears. The function, ```relative_frequence```, uses the count of each (POS) diveded by the length of the file and multiplied by 10000, to find the relative frequency of each POS. The function, ```unique_NERS```, uses SpaCys *named entity recognition* (NER) to count how many unique *person, location,* and *organizations* are used in each text file. The two next functions, *create_dataframe* and *save_function*



- Unzips the zip file. Goes through each text in each folder, removes HTML tags, and uses spacy to get specific linguistic features, such as the relative frequency count of nouns, verbs, adjectives, and adverbs. Counts the number of unique persons, locations, and organizations. All information is then stored in one overall data frame for each folder, containing rows of each text. The data frame is then made into a CSV file and stored in the folder ```out```. In total 14 CSV files are created.

## Future usage of the code
- It is difficult to manually get an overview of what separates the texts into three different levels. However, it could be interesting to cluster the texts together to see how different-level texts may be grouped. It would also be interesting to create a classifier to see how other texts would be classified based on this data.

## Usage 
To run this code follow these steps:
1.	Clone the repository
2.	Get the zip file *USEcorpus.zip* from [here]( https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2457#) and place it in the datafolder
3.	Run ```bash setup.sh``` in the command line. This will install the requirements, and create a virtual environment. 
4.	Run ```source ./assignment_1/bin/activate``` in the command line. This will activate the virtual environment. 
5.	Run ```python3 src/assignment_1.py –-zip_name data/USEcorpus.zip``` in the command line which will run the code. 
6.	The current folder, that is being analyzed will be printed to the command line.
7.	Your output will be stored in the folder ```out```  as 14 csv files
