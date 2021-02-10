Niek Scholten  
7 april 2019  
Version 1.0

This folder contains a pycharm project.  
The project contains a website using Flask.

## Dependencies:
-Pyhton 3.7  
-Flask 1.0.2  
-Jinja2 2.10  
-matplotlib 2.2.4  
-IO  
-Base64

## Folders:
* [static](static):
    * Contains the vector files for the website's icons,
      and the stylesheet (css) file
* [templates](templates):
    * Contains the html templates used to render the website

## Files:
* [app.py](app.py):
    * Run this script to start the webserver.
* [file_reader.py](file_reader.py):
    * Contains a class used to create the graph displayed on the website.
* [README.md](README.md):
    * This file, contains general information.
* [test_file.fastq](test_file.fastq):
  * Smaller file to test the creation of the graph.

Running the program:
1. Make sure all necessary files and dependencies are installed
2. Run app.py in pycharm
3. Click the link or go to 'http://127.0.0.1:5000/'
4. Go to the 'Upload' tab to select a file