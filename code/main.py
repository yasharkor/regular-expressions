from os import listdir
from os.path import isfile, join
import re 
import csv
import sys

# Path of .txt data directory
mypath = sys.argv[1]
# getting the names of all files in the directory
file_name_list = [f for f in listdir(mypath) if isfile(join(mypath, f))]


# remove matches that are copy or smaller
def remove_matches(temp_list):
    # take the span element of each math an put it in tuples
    tuples=[x[4] for x in temp_list]
    indexes=set()
    for j, big in enumerate(tuples):
        for i, small in enumerate(tuples):  
            if(small[0]>=big[0] and small[1]<=big[1] and i!=j):
                indexes.add(i)
    for index in sorted(list(indexes), reverse=True):
        del temp_list[index]         
    return temp_list




##---------------------------------------------------------##
# defining a list for all regesx pattern
regex_list=[]
# defining a list for the type of date expression 
expr_list=[]
# defining a list for the output
out_list=[['article_id','expr_type','value','char_offset','temp']]

##---------------------------------------------------------##
##---------------------------------------------------------##

# Set of all months
months=set([
    'January','February','March','April','May','June','July','August',
    'September','October','November','December',
    'january', 'february', 'march', 'april', 'june', 'july',
    'august', 'september', 'october', 'november', 'december'
])
# creating OR statement between various months
months = '|'.join(months)

# Set of all days
days=set(['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
# creating OR statement between days
days='|'.join(days)

seasons=set(['Fall','Winter','Summer','Spring','Autumn'])
seasons='|'.join(seasons)

numbers=set(['one','two','three','four','five','six','seven','eigth','nine','ten','1st','2nd','3rd'])
numbers='|'.join(numbers)

interval=set(['day','Day','week','Week','Month','month','season','Season','year','Year','hour','minute','Hour','Minute','noon','today','tomorrow','yesterday'])
interval='|'.join(interval)

deictic1=set(['next','prior','last','before','after'])
deictic1='|'.join(deictic1)

deictic2=set(['ago','later'])
deictic2='|'.join(deictic2)

##---------------------------------------------------------##
##---------------------Regex Patterns----------------------##
##---------------------------------------------------------##

##----------------------Pattern 1--------------------------##

# Appending regext pattern to regex_list
regex_list.append(
    re.compile("""
(
\w+    
\s   
((?: {}))[s]?                # interval set                                         
\s?                                  # space                
(?:{})                       # deictic1 set       
\s?                                  # interval set 
((?: {}))[s]?                       
)                          
""".format(interval,deictic1,interval), re.VERBOSE)
) 
# Appending type of date expression to expr_list
expr_list.append('time-deictic1-time')
##----------------------Pattern 2--------------------------##
# Appending regext pattern to regex_list
regex_list.append(
    re.compile("""
(
(?:{})                         # Numbers set                      
\s?                                   # space               
((?: {}))[s]?                 # interval set                 
\s?                                   # space
(?:{}))                       # deictic2 set 
                          
""".format(numbers,interval,deictic2), re.VERBOSE)
) 
# Appending type of date expression to expr_list
expr_list.append('numbers-time-deictic')

##----------------------Pattern 3--------------------------##
# Appending regext pattern to regex_list
regex_list.append(
    re.compile("""
(
(?:half)?                                # optional half to match words like half an hour
\s?                                      # optional space
\w+                                      # one word before interval vocabularies
\s?                                      # optional space
(?:{}))[s,.]?                    # interval set
                          
""".format(interval), re.VERBOSE)
) 
# Appending type of date expression to expr_list
expr_list.append('interval')
##----------------------Pattern 4--------------------------##
# Appending regext pattern to regex_list
regex_list.append(
    re.compile("""
(
(?:\b{}[s,]?\b)                   # deictic1 set
\s?                                       # space
(?: {})                               # days set
)                          
""".format(deictic1,days), re.VERBOSE)
) 
# Appending type of date expression to expr_list
expr_list.append('deictic1')
##----------------------Pattern 5--------------------------##

# Appending regext pattern to regex_list
regex_list.append(
    re.compile("""
(
(?:next)?
\s?
(?:{})                    # Any weekdays
)                          
""".format(days), re.VERBOSE)
) 
# Appending type of date expression to expr_list
expr_list.append('weekday')
##----------------------Pattern 6--------------------------##
# Appending regext pattern to regex_list
regex_list.append(
    re.compile("""
(
(?:[01]?[0-9]|2[0-3])           # up to 0-23 h
:
[0-5][0-9]                      # up to 00-59 min
(?::[0-5][0-9])?                # up to 59 sec optional
)
""",re.VERBOSE)
)
# Appending type of date expression to expr_list
expr_list.append('24hr time')
##----------------------Pattern 7--------------------------##
# Appending regext pattern to regex_list
regex_list.append(
    re.compile("""
(
(?:19|20)\d\d              # 1900-2099 year
[\ .-/]
(?: 0?[1-9]|1[012])           # 0-12 M
[\ .-/]
(?: 0?[1-9]|[12]\d|3[01])   # 0-9 | 10-19, 20-29 | 30,31


)
""",re.VERBOSE)
)
# Appending type of date expression to expr_list
expr_list.append('YYYY/M/D')
##----------------------Pattern 8--------------------------##
# Appending regext pattern to regex_list
regex_list.append(
    re.compile("""
(
(?:0?[1-9]|1[012])?               #optional 0-12 M
[\. -/]
(?:0?[1-9]|[12]\d|3[01])?         #optional  0-9 | 10-19, 20-29 | 30,31
[\. -/]
(?:(?:19|20)\d\d)                # 1900-2099 year
)
""",re.VERBOSE)
)
# Appending type of date expression to expr_list
expr_list.append('M/D/YYYY or MM/DD/YYYY')
##----------------------Pattern 9--------------------------##
# Appending regext pattern to regex_list
regex_list.append(
    re.compile("""
(
(?:0?[1-9]|[12]\d|3[01])?   # 0-9 | 10-19, 20-29 | 30,31
[\. -/]
(0?[1-9]|1[012])?          # optional 0-12 M
[\. -/]
(?:(?:19|20)\d\d)         # 1900-2099 year
)
""",re.VERBOSE)
)
# Appending type of date expression to expr_list
expr_list.append('D/M/YYYY or DD/MM/YYYY')
##----------------------Pattern 10--------------------------##
# Appending regext pattern to regex_list
regex_list.append(
    re.compile("""
(

(?:[12][0-9]{{3}}s?)?             # 1900-2099 year
\s?
(?:{})
\s?
(?:[12][0-9]{{3}}s?)?             # 1900-2099 year
)
""".format(seasons),re.VERBOSE)
)
# Appending type of date expression to expr_list
expr_list.append('Season')
##----------------------Pattern 11--------------------------##
# Appending regext pattern to regex_list
regex_list.append(
    re.compile("""
(
immediately 
)
""",re.VERBOSE)
)
# Appending type of date expression to expr_list
expr_list.append('immediate time')
##----------------------Pattern 12--------------------------##
# Appending regext pattern to regex_list
regex_list.append(
    re.compile("""
(
\w+                   # 1 word before years
\s*                   # space
years?[, .]?          # years, year, year, year.
)
""",re.VERBOSE)
)
# Appending type of date expression to expr_list
expr_list.append('number of years')
##----------------------Pattern 13--------------------------##
# Appending regext pattern to regex_list
regex_list.append(
    re.compile("""
(
(?: {})                    # Months
\s*                              # space
\d{{0,2}}                        # Day 0-99
\s*                              # space
(?:[12][0-9]{{3}}s?)             # Year 1000-2999
 )              
""".format(months),re.VERBOSE)
)
# Appending type of date expression to expr_list
expr_list.append('month dd yyyy')
##----------------------Pattern 14--------------------------##
# Appending regext pattern to regex_list
regex_list.append(
    re.compile("""
(
\d{{0,2}}                        # Day 0-99
\s*                              # space
(?: {})                    # Months
\s*                              # space
(?:[12][0-9]{{3}}s?)             # Year 1000-2999
)              
""".format(months),re.VERBOSE)
)
# Appending type of date expression to expr_list
expr_list.append('dd months yyyy')
##----------------------Pattern 15--------------------------##
# Appending regext pattern to regex_list
regex_list.append( 
    re.compile("""
(
(?: late|early|mid)?                # optional late or early
[\s-]?                             # optional space
[12]                            # 1 or 2
[0-9]{3}                      # any 3 digit number, find years between 1000-2999
s*                              # optional s
)                     
                                 
""",re.VERBOSE)
)
# Appending type of date expression to expr_list
expr_list.append('year')

##----------------------Pattern 16--------------------------##
# Appending regext pattern to regex_list
regex_list.append(
    re.compile("""
({})                        # months
""".format(months), re.VERBOSE)
) 
# Appending type of date expression to expr_list
expr_list.append('month')
##----------------------Pattern 17--------------------------##
# Appending regext pattern to regex_list
regex_list.append(
    re.compile("""
((?:{})-(?:{}))                        # Any combination of months-months
""".format(months,months), re.VERBOSE)
) 
# Appending type of date expression to expr_list
expr_list.append('month-month')

##---------------------------------------------------------##
##-------Read, and find patterns and save into list -------##
##---------------------------------------------------------##


# For loop over all .txt files
for file_name in file_name_list:
    # opening one .txt file
    with open (join(mypath,file_name)) as text_file:
        # Reading the .txt file
        text=text_file.read()
        # text=text.replace('\n', ' ')
        temp_list=[]
        # print(text)
        # For loop over all regext patters in regex_list and enumerating them to assign the associated expr_list
        for i, pattern in enumerate(regex_list):
            # For loop over all matches found by findall
            for m in pattern.finditer(text):
                # Appending to the list (file name, expression type, value, char_offset)
                # print(file_name,m.group(),m.span())
                temp_list.append([file_name,expr_list[i],m.group(),m.start(),m.span()])
          # remove matches that are copy or smaller        
        remove_matches(temp_list)
    # Append the list of matched find in a specific .txt file to the out_list
    out_list.extend(temp_list)

# seleting the first 4 elements of each out put = dropping .span() informtion
out_list=list(map(lambda x:x[0:4],out_list))



##-------------------------------------------------------------
# seleting the first 4 elements of each out put = dropping .span() informtion


# out_list=list(map(lambda x:x[0:3],out_list))

##-----------------save into CSV file-------------------------##
# Writing the output(out_list) in to a csv file(out.csv)

dirPath2 = sys.argv[2]

with open(dirPath2+"out.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(out_list)


print('Successful')
print(len(out_list))