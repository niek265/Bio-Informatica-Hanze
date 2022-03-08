# databases2

## Deelopdracht 2

### Requirements
Python version 3.6 or higher
* astroid==2.3.3  
* isort==4.3.21  
* lazy-object-proxy==1.4.3  
* mccabe==0.6.1  
* mysql-connector==2.2.9  
* pylint==2.4.4  
* six==1.13.0  
* typed-ast==1.4.0  
* wrapt==1.11.2  

### Descriptions
[Opdracht 1](opdracht_1.py):  
Uses objects to display database information in an orderly way.  
SQL injections have been made impossible and the script can parse a .cnf file to automatically connect with the given credentials.  
Usage:
```shell script
python opdracht_1.py [-u username -s host -d database -s host -n name -p password -c config_file]
```
If a name is given, the exam information will be printed.  
The standard location of the cnf file is the root of the folder.  
If no arguments are given, it will attempt to load my.cnf.