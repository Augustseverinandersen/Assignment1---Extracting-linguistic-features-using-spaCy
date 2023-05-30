# 1. Assignment 1 - Extracting linguistic features using spaCy
## 1.1 Assignment description

Written by Ross: 
For this exercise, you should write some code that does the following: Loop over each text file in the folder and extract the following information:
- Relative frequency of _Nouns, Verbs, Adjective, and Adverbs_ per 10,000 words
- Total number of _unique PER, LOC, ORGS_
For each sub-folder (a1, a2, a3, ...) save a table which shows the following information:

|Filename|RelFreq NOUN|RelFreq VERB|RelFreq ADJ|RelFreq ADV|Unique PER|Unique LOC|Unique ORG|
|---|---|---|---|---|---|---|---|
|file1.txt|---|---|---|---|---|---|---|
|file2.txt|---|---|---|---|---|---|---|
|etc|---|---|---|---|---|---|---|
## 1.2 Machine Specifications and My Usage

All the computation done for this project was performed on the UCloud interactive HPC system, which is managed by the eScience Center at the University of Southern Denmark. The script was run on Coder Python 1.76.1 and Python version 3.9.2. I ran the script with 8 CPUs, and it took nine minutes to complete.
### 1.2.1 Perquisites

To run the script, make sure to have Bash and Python3 installed on your device. The script has only been tested on Ucloud.
## 1.3 Contribution

This assignment was made in contribution with fellow students from class, in-code comments are made by me. The assignment uses data gathered by the [University of Oxford](https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2457).
### 1.3.1 Data

The data, created by the University of Oxford, consists of 1,489 English papers written by 440 Swedish students, studying English. The dataset has 14 folders, each folder is labelled a, b, or c, followed by a number. The letters represent different levels of English proficiency. There are five folders of A-level essays, eight B-level essays, and one C-level essay. Each folder, representing a group, had a different subject that they wrote about. The subjects were either _personal essays about English, argumentation essays, reflections, literature course assignments, or culture course assignments_ – [source](http://icame.uib.no/ij24/use.pdf). 
According to the authors, Margareta Westergren Axelsson and Ylva Berglund, the corpus consists of 1,221,265 words averaging an essay length of 820 words. [University of Oxford, 2003, The Uppsala Student English Corpus (USE), Oxford Text Archive](https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2457).
## 1.4 Packages

The following are the packages used in the scripts:
- **SpaCy (version 3.1.3)** is used for Natural Language Processing (NLP), Part of Speech Tagging (POS), and Named Entity Recognition (NER). I am using the medium version of SpaCy.
- **Pandas (version 1.5.3)** is used for data manipulation and structuring data. I am using it to read the data and create data frames.
- **Re** is used to create a regular expression in the script to clean the texts.
- **Os** is used to navigate across operating systems.
- **Sys** is used to navigate the directory.
- **Zipfile** is used to unpack the zip file.
- **argparse** is used to create command-line arguments.
## 1.5 Repository Contents

The repository contains the following folders and files:
- ***data*** is an empty folder where the zip file will be placed.
- ***out*** is the folder that contains the output created in the script, a CSV file for each folder.
- ***src*** is the folder that contains the Python script.
- ***utils*** is the folder that contains a script with functions used in the main script.
- ***README.md*** is the README file.
- ***requirements.txt*** is the text file that contains the packages that are needed to run the script.
- ***setup.sh*** is the file that creates a virtual environment, upgrades pip, installs SpaCy, and installs the packages in the requirements.txt.
## 1.6 Methods 

The script does the following:
-	After importing the necessary packages and functions the script initializes an argparse, which is used to define the path to the zip file.
-	The code that checks if a specific path to the data exists. If not, the zip file is extracted. 
-	The ``get_data`` function is then created. This function finds the path to each folder using _os.listdir_ if the path is a directory, _os.listdir_ is then used again to find the path to each file in each folder. Each path is then checked to see if it is a file and if it is, the file is then opened and encoded as _Latin-1_ (_utf-8_ did not work). 
-	Each file is then processed using functions from the script ``helper_function.py`` located in the folder _utils_. 
-	The first function, ``clean_data``, takes the file and cleans the file by removing angle brackets and its contents. The cleaned file is then tokenized using SpaCys _nlp_ function.
-	The function ``count_words uses`` SpaCys _POS_ to count the occurrence of _adjectives, nouns, verbs, and adverbs_. 
-	The function ``relative_frequence`` uses the count of each _POS_ to get the relative frequency of each _POS_. This is done by dividing the _POS_ with the length of the file and multiplying by 10,000. 
-	Using SpaCys _NER_, the function ``unique_NERS``, finds each occurrence of a _person, location, and organization_, and counts the unique occurrence of each. 
-	Lastly, the functions, ``create_dataframe`` and ``save_function``, are used to create a data frame for each file, append the data frames together for each folder, and save the data frame as a CSV file in the folder _out_.
## 1.7 Discussion
By using natural language processing, it is possible to get a unique understanding of how different levels of English proficiency write. POS tagging gives insight into the distribution of adjectives, nouns, verbs, and adverbs which can be used to see how different levels of English proficiency construct sentences. NER gives insight into how different levels of English proficiency use named entities, this can be particularly interesting to see which kind of written task uses the most named entities. Relative frequency gives insight into how different POS are used in the text compared to the length of the text, this can be used to compare the texts equally.
### 1.7.1 Future usage of the code
It is difficult to get an overview of what separates the texts into three different levels. However, it could be interesting to cluster the texts together to see how different-level texts may be grouped. It would also be interesting to create a classifier to see which levels other texts would be classified to based on this data.
## 1.8 Usage
To run the script, follow these steps:
- Clone the repository.
- Navigate to the correct directory.
- Get the zip file, _USEcorpus.zip_, from [here](https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2457) and place it in the data folder (you might need to rename the zip file).
- Run ``bash setup.sh`` in the command line. This will install the requirements and create virtual environment.
- Run ``source ./assignment_1/bin/activate`` in the command line. This will activate the virtual environment.
- Run ``python3 src/assignment_1.py --zip_name data/USEcorpus.zip`` in the command line. This will run the script.
    - The argparse ``--zip_name`` takes a string as input. Here you should define the path to your zip file. The path should be ``data/THE_ZIP_FILE.zip``
- The CSV files for each folder will be saved to the folder out.
