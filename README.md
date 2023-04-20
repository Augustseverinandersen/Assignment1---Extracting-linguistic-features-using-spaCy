[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10189937&assignment_repo_type=AssignmentRepo)

# ASsignment 1 - Extracting linguistic features using spaCy

## Contribution 
- This assignment was made in contribution with fellow students from class, and with inspiration from in class notebooks. All in code comments are made by me. 
- The assignment uses data gathered by the Univeristy of Oxford. The data consists of 14 folders of english papers written by Swedish students. There is in total 1,489 essays divided into three different levels. Their are five folders of A level essays, eight B level essays, and one C level essay. Each group had a different subject that they wrote about. The link to the data can be found [Here](https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2457). 

## Assignment description 
For this exercise, you should write some code which does the following:

- Loop over each text file in the folder called ```in```
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
- - Goes through each text in each folder, removes HTML tags, uses spacy to get specific linguistic features, such as the relative frequency count of noun, verb, adjective, and adverb. Counts the number of unique persons, locations, and organizations. All information is than stored in one overall dataframe for each folder, containing rows of each text. The dataframe is than made into a csv file and stored in folder out. In total 14 csv files are created.

## Future usage of the code
- It is difficult to manually get an overview of what seperates the texts into three different levels. However, it could be interesting to cluster the texts together to see how different level texts may be grouped together. It would also be interesting to create a classifier to see how other texts would be classified based on this data.

## Usage 
To run this code follow these steps:
1. Clone the repository
2. Run ```bash setup.sh``` in the command line. This will install the nessercary requiriments, and create a virtual environment. 
3. Run ```source ./assignment_1/bin/activate``` in the command line. This will activate the virtural enviroment. 
4. Run ```python3 src/assignment_1.py``` in the command line which will run the code. The current folder, that is being analysed will be printed to the command line.






This assignment concerns using ```spaCy``` to extract linguistic information from a corpus of texts.

The corpus is an interesting one: *The Uppsala Student English Corpus (USE)*. All of the data is included in the folder called ```in``` but you can access more documentation via [this link](https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/2457).




## Objective

This assignment is designed to test that you can:

1. Work with multiple input data arranged hierarchically in folders;
2. Use ```spaCy``` to extract linguistic information from text data;
3. Save those results in a clear way which can be shared or used for future analysis

## Some notes

- The data is arranged in various subfolders related to their content (see the [README](in/README.md) for more info). You'll need to think a little bit about how to do this. You should be able do it using a combination of things we've already looked at, such as ```os.listdir()```, ```os.path.join()```, and for loops.
- The text files contain some extra information that such as document ID and other metadata that occurs between pointed brackets ```<>```. Make sure to remove these as part of your preprocessing steps!
- There are 14 subfolders (a1, a2, a3, etc), so when completed the folder ```out``` should have 14 CSV files.

## Additional comments

Your code should include functions that you have written wherever possible. Try to break your code down into smaller self-contained parts, rather than having it as one long set of instructions.

For this assignment, you are welcome to submit your code either as a Jupyter Notebook, or as ```.py``` script. If you do not know how to write ```.py``` scripts, don't worry - we're working towards that!

Lastly, you are welcome to edit this README file to contain whatever informatio you like. Remember - documentation is important!
