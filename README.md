# Intro to NLP - Assignment 1


This is a solution to Assignment 1 for CMPUT 501 - Intro to NLP at the University of Alberta, created during the Fall 2020 semester.


## Installation and Execution Instructions
- Clone the repository
- Using a terminal navigate to the "code" subdirectory (regular-expressions/code as on github)
- No extra python libraries needed outside of standard library (re, sys, os, math, csv)
- From the terminal run the command ```python3 .\main.py <train data path> <output path>```
- The train data path should be a relative path to a directory containing the text files you will implement regular expressions
- The output path is where the csv files will be created after implementing regular expression

## example
```bash
python main.py ../data/dev/ ../output/ 

```

## Data

The assignment's development data can be found inside [data/dev](data/dev).



## Introduction
Your first assignment will explore the use of regular expressions to extract information from written text. This method has been widely applied in information retrieval, and it is used in text processing applications and research.

A regular expression is a notation used to match strings in a text. It works like the CTRL+F search feature in browsers, but it has the added bonus of allowing the use of special characters to count, exclude, and group specific strings. Like in a language, regular expressions have a set of characters with predefined functions, and these characters can be used to create search patterns. For example, the character + means one or more occurrences. The regular expression /e+/ searches for strings of one or more “e”s. In the string “Feed the Birds”, this regular expression would match “ee”.
## Task
In this assignment you are going to use regular expressions to search for date expressions in news texts. We are interested in two types of date expressions for this assignment. The first one is simple date expressions, strings like “14 June 2019” and “Fall 2020” which represent absolute points in time and are independent of when you are reading them. The second type is deictic date expressions, dates that are relative to the current time, for example, “the day before yesterday”, “next Friday”, and “two weeks prior”.
## Input: news articles
News is a genre that makes use of dates to convey more information about when an event took place and to help the readers place future and past occurrences in time. This first assignment’s input dataset is a collection of news articles that discusses several topics, such as politics, tech, and business. 

Article 265 in this dataset has sentences like this:

“Pipa conducted the poll from 15 November 2004 to 3 January 2005 across 22 countries in face-to-face or telephone interviews.”
## Output: CSV file, code, and documentation
## CSV file
As mentioned before, news articles usually have a lot of time references, and we want you to search for those references in the input data. The output of your search should be a CSV file with all of the dates expressions found. The file should contain at least four columns, one column for the id of the article, one for the type of date expression found, one for the date expression itself, and one for the offset in characters from the beginning of the file to the beginning of the date expression, that is the position of the first character of the date expression in the file. You should name the type of date expression as you wish, making sure that their types reflect the expressions they represent.

- For the excerpt above a valid output is 
- article_id, expr_type, value, char_offset
- 265.txt, date, 15 November 2004, 30
- 265.txt, date, 3 January 2005, 50

You should also extract the entire date expression at once. For example, for the string “June 2019” there should be a single row on the output file, as opposed to one entry for the year and one for the month. You should always extract the longest consecutive date expression possible, there will be no marks for partially extracted expressions.
## Code
You must also submit the code you wrote to extract the date expressions from the text. This code will be graded and executed by the TAs. It is important to point out that the TAs will run your code on a different set of input news articles and some part of the marks will be based on how well your code captures date expressions in novel text. 

With that, you should be discouraged from creating regular expressions specifically tailored for the input data you receive, for example searching for the year 2002 explicitly, as that might hinder your algorithm’s performance on unseen text.
## Documentation
Another very important deliverable is your code’s documentation. You need to explain how to execute your code and communicate which steps are necessary to do so. This is important for the TAs who will be running your code later. You should let them know how to set up a folder as the input folder, which libraries are needed to run your project, how to run your Python script, and where to look for the output file. You can do all that in a README file and put it inside your project’s folder. For more tips on how to write a clear and helpful README file follow this link.
# Suggestions

## Code suggestions
- Create different functions to tackle different parts of the task, e.g., one function to read the input files, one function to split the input text into smaller chunks, one function to apply regular expressions.
- List all possible date expression structures, e.g., day month year, month day, season year, etc.
- Focus on a single date expression structure to search at a time. Write a regular expression for it and then move on to the next structure.
- Add comments after each regular expression definition indicating which date structure they extract so that the TAs can better understand your code.
- Consider a long for-loop structure for your program in which you test every sentence against every regular expression until you find matches.
- Create your own test file, with many hand-crafted expressions for which you know what the correct extraction should be. 
## Useful links
- [This website](https://www.w3schools.com/python/python_regex.asp) has a good overview of the library Python RegEx. It lists the library functions available and regular expression’s metacharacters along with their uses.
- [This post](https://medium.com/factory-mind/regex-tutorial-a-simple-cheatsheet-by-examples-649dc1c3f285) is very useful to look for metacharacters and their applications.
- You may want to test your regular expression before embedding them to your code. [This website](https://regex101.com/) is perfect for that. 
- You may also want to improve the readability of your code by adding comments within a regular expression. The VERBOSE mode in Python provides such functionality, as described [here](https://docs.python.org/3.5/library/re.html#re.X). 

# More information
- Book Chapter: [Chapter 2](https://web.stanford.edu/~jurafsky/slp3/2.pdf)

- Learning Objectives : Learn how to use regular expressions to extract information from text.
