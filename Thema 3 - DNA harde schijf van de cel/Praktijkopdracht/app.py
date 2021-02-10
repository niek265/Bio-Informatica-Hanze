#!/usr/bin/env python3

"""
Script for calling different templates on corresponding addresses
"""

from flask import Flask, request, render_template, url_for, redirect
from file_reader import *

__author__ = 'Niek Scholten'

APP = Flask(__name__)


@APP.route('/')
def index():
    """
    The homepage, contains general information
    """
    return render_template('index.html', title='Home', active1='active')


@APP.route('/upload')
def upload():
    """
    Used for selecting the file you want to upload
    """
    return render_template('upload.html', title='Upload', active2='active')


@APP.route('/results', methods=['GET', 'POST'])
def results():
    """
    Will check for an input, if there is a valid one, load the template
    """
    if request.method == 'POST':
        try:
            form_input_file = request.files['file']
            process = FQProcessor(form_input_file)  # Initializes the class
            process.read_file()
            process.get_quality()
            return render_template('results.html', title='Results',
                                   results=process.create_graph(), active3='active')
        except (KeyError, IndexError, UnicodeDecodeError):  # Checks for failures in the reading process
            return render_template('upload.html', active2='active',
                                   message='Please select a valid FASTQ file')
    else:
        return redirect('/upload')


@APP.route('/about')
def about():
    """
    Contains more in depth information about the webapp
    """
    return render_template('about.html', title='About', active4='active')


if __name__ == '__main__':
    APP.run(debug=True)
