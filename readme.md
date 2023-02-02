This is a Python challenge to download Star Wars API data from :
https://swapi.co/api/people/, save and present in the system. 
Functionality of going through files and counting specific 
homeworlds were provided.

###### Programmers limitations and problems that took time:

- I wasn't able to create 'load more' button
- in views file, one of functions was called 'download', which caused 
an overriding of some other function, generated error and took time to find.

###### Improvements:

- Deleting a file in the system should automatically remove the csv file 
from the place where file is stored - using signals;
- Additional tests should be added for functions in operations.py
- ~~After adding second API call, app slowed, 
improving might be necessary~~ - Fixed in 1.02.2023 Update
- Warning 'DateTimeField Metadata.download_date received a naive datetime 
(2023-01-30 19:32:37.361895) while time zone support is active.' 
should be resolved;
- Data should be stored in a database, in order to have a full access and 
changes tracking - an ETL should be added to check if data exists or 
was changed (ex.: Lookup transformation in SSIS);

###### Instruction of use

All the collections of files are presented in a 'Collections' tab. 
'Download' button saves the newest file to the system, page refreshes and 
displays all saved data. Clicking a filename (ex.: '202330011929541.csv')
takes the user to the page that displays all the rows from downloaded 
csv file. Below there is a table of counting how many times specific 
homeworld occured in a file 'Back' button was added to come back 
to collections page.

###### Warnings:

Pycharm expects imports to be typed in such way:

from .models import Metadata

In order to fully work, removing of dot might be necessary.


###### 31.01.2023 Update

- Added resolving the homeworld field into name
- Added 'homeworld' items count


###### 1.02.2023 Update - AFTER DEADLINE! 
Fixing performance issue with downloading the data.
Get_homeworld function was fixed in the way it checks 
that specific homeworld was already downloaded (stored in dictionary)
If yes, there is no need to download it from API again.
Test results of get_homeworld function:

Before performance fix:
- 50.028223752975464 seconds
- 25.991403579711914 seconds
- 41.56271028518677 seconds

After performance fix:
- 10.732773065567017 seconds
- 9.19198727607727 seconds
- 6.425095558166504 seconds



###### Time:
Planning ~ 1h

Coding ~ 7h 



