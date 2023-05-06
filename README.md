
# Assignment 1 - Extracting linguistic features using spaCy

## Contribution 
- This assignment was made in contribution with fellow students from class, and with inspiration from in-class notebooks. All in-code comments are made by me. 
- The assignment uses data gathered by the University of Oxford. The data consists of 14 folders. Each folder contains English papers written by Swedish students. There are in total 1,489 essays divided into three different levels. There are five folders of A-level essays, eight B-level essays, and one C-level essay. Each group had a different subject that they wrote about. The link to the data can be found [Here](https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2457). 
## Packages 
-	Spacy
    - Is used for Natural language processing (NLP), Part of Speech tagging (POS), and named entity recognition. 
    - I am using the medium version of Spacy
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
- The code does the following:
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
