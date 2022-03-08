from flask import Flask, render_template, redirect, request, url_for
from flask_socketio import SocketIO
from werkzeug.utils import secure_filename
import jinja2
from lib.quality_check import RunFastqc
from pipeline import check_path_or_file
from os import path

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',
                           title='Home',
                           current0='mdl-navigation__link--current')


@app.route('/SortSam')
def sort_sam():
    return render_template('sortsam.html',
                           title='SortSam',
                           current1='mdl-navigation__link--current')


@app.route('/AddOrReplaceReadGroups')
def aor_groups():
    return render_template('addorreplacereadgroups.html',
                           title='AddOrReplaceReadGroups',
                           current2='mdl-navigation__link--current')


@app.route('/FixMateInformation')
def fix_mate_info():
    return render_template('fixmateinformation.html',
                           title='FixMateInformation',
                           current3='mdl-navigation__link--current')


@app.route('/MergeSamFiles')
def merge_sam():
    return render_template('mergesamfiles.html',
                           title='MergeSamFiles',
                           current4='mdl-navigation__link--current')


@app.route('/MarkDuplicates')
def mark_dups():
    return render_template('markduplicates.html',
                           title='MarkDuplicates',
                           current5='mdl-navigation__link--current')


@app.route('/Results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        try:
            form_input_file = request.files['file']
            file_path = path.join('Uploads', secure_filename(form_input_file.filename))
            form_input_file.save(file_path)
            file_list = check_path_or_file(file_path)
            quality = RunFastqc('./lib/SiteOutput')

            quality.multi_run(file_list)
            print(quality)
            return render_template('results.html',
                                   title='MarkDuplicates',
                                   current5='mdl-navigation__link--current',
                                   result=f'{secure_filename(form_input_file.filename.replace(".fastq.gz", ""))}_fastqc.html')
        except (KeyError, IndexError, UnicodeDecodeError):  # Checks for failures in the reading process
            return render_template('index.html', active2='active',
                                   message='Please select a valid FASTQ file')
    else:
        return redirect('/')


@app.route('/Results/<result>', methods=['GET', 'POST'], )
def fqresult(result):
    return render_template(result)


if __name__ == '__main__':
    my_loader = jinja2.ChoiceLoader([
        app.jinja_loader,
        jinja2.FileSystemLoader(['/difficultdata/SiteOutput/Results/Fastqc',
                                 '/difficultdata/templates']),
    ])
    app.jinja_loader = my_loader
    socketio = SocketIO(app)
    socketio.run(app)
