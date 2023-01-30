This is a Python challenge to download Star Wars API data from :
https://swapi.co/api/people/, save and present in the system. 
Functionality of going through files with data is provided.

###### Programmers limitations and problems that took time:

- in views file, one of functions was called 'download', which caused 
an overriding of some other function, generated error and took time to find.

###### Improvements:

- Deleting a file in the system should automatically remove the csv file 
from the place where file is stored - using signals;
- Warning 'DateTimeField Metadata.download_date received a naive datetime 
- (2023-01-30 19:32:37.361895) while time zone support is active.' 
should be resolved;
- Data should be stored in a database, in order to have a full access and 
changes tracking - an ETL should be added to check if data exists or 
was changed (ex.: Lookup transformation in SSIS);

###### Instruction of use

All the collections of files are presented in a 'Collections' tab. 
'Download' button saves the newest file to the system, page refreshes and 
displays all saved data. Clicking a filename (ex.: '202330011929541.csv')
takes the user to the page that displays all the rows from downloaded 
csv file. 'Back' button was added to come back to collections page.

###### Warnings:

Pycharm expects imports to be typed in such way:

from .models import Metadata

In order to fully work, dot might be necessary to remove.

###### Time:
Planning ~ 1h

Coding ~ 5h 

