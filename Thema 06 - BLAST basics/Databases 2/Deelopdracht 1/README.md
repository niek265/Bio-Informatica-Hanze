# databases2

## Deelopdracht 1

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
Contains a class for usage with [Opdracht 2/3](opdracht_2_2.py) or standalone.  
Uses string formatting to return the variables in an orderly way.  
Usage:   
```shell script
python opdracht_1.py-s student -v vak -d datum -c cijfer
```

[Opdracht 2/3](opdracht_2_3.py):  
Uses [Opdracht 1](opdracht_1.py) to display database information in an orderly way.  
Usage:
```shell script
python opdracht_2_3.py -u username -s host -d database [-s host -n name -p password]
```
If no password argument is given, a prompt will appear that securely asks fot the password.  
If a name is given, the exam information will be printed.  
The standard host is "mariadb.bin" if you wish to use another, use -s.

The functionality of assignment 3 is added into assignment 2.