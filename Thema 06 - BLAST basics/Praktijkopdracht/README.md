# DifficultData

##Folders:
* [Code](/Code): Contains original template code provided.
* [lib](/lib):  Has all modules for the program.
* [RawFiles](/RawFiles): Contains the data files.
* [static](/static): Static web files, such as css and javascript.
* [templates](/templates): HTML templates to render.
* [venv](/venv): Virtual Python environment.

####Code:
* [aligningMain.py](Code/aligningMain.py): Original pipeline script. DISCONTINUED.
* [createDirs.py](Code/createDirs.py): Create the necessary directories. DISCONTINUED.
* [determineGenomeInfo.py](Code/determineGenomeInfo.py): Fetches genome of the target organism. DISCONTINUED.

####lib:
* [alignment.py](lib/alignment.py): Performs alignment using HISAT2.
* [count_matrix.py](lib/count_matrix.py): Creates count matrices.
* [fastqc_analysis_analysis.py](lib/fastqc_analysis_analysis.py): Uses fastqc_function.py to analyze fastqc data.
* [fastqc_function.py](lib/fastqc_function.py): Analyzes and provides feedback.
* [identifier.py](lib/identifier.py): Fetches genome of the target organism.
* [make_dirs.py](lib/make_dirs.py): Create the necessary directories.
* [multiqc_analysis.py](lib/multiqc_analysis.py): Uses fastqc_function.py to analyze multiqc data.
* [preprocessing.py](lib/preprocessing.py): Marks duplicates and creates count files.
* [process_fasta.py](lib/process_fasta.py): Creates sequence dictionaries.
* [process_manager.py](lib/process_fasta.py): DISCONTINUED.
* [quality_check.py](lib/quality_check.py): Runs fastqc on input files.
* [trimmer.py](lib/trimmer.py): Trims the reads.

##Files:
* [.gitignore](/.gitignore): List of files that do not have to be added to git.
* [app.py](/app.py): Used to run and route the Flask app. DISCONTINUED
* [pipeline.py](pipeline.py): Used to run the full program without an interface.
* [config.ini](/config.ini): Config file that contains paths to installed tools.
* [requirements.txt](/requirements.txt): Contains all the required modules.
* [setup.sh](setup.sh): Source to install the necessary tools and modules from requirements.txt.

##Tools:
* [Picard](lib/Picard-2.21.6): Used for SAM and BAM files.
* [Subread](lib/Subread-2.0.0): Used for creation of count matrix.
* [TrimGalore](lib/TrimGalore-0.6.5): Used for trimming.
* MultiQC: Used for performing the quality check.
* FastQC: Used for performing the quality check.
* SAMTools: Used for converting SAM files.
* HISAT2: Contains genome data.
* Cutadapt: Used by TrimGalore.

##Usage:
sh setup.sh  
Change the values in the config.ini to the correct paths.  
python3.7 pipeline.py -d [fastq directory]-o [hg|mm|rn|mmu] -out [out directory] -p (use paired end)    
-c [number of threads] -t [last bp | first and last bp]    

**NOTE:**   
The colorspace format of fastq files (for example the output of SOLiD sequencing) is not supported!   
This is due to the fact that this file format is not supported by the trimming tool and we could not find   
an efficient way of translating these files to letterspace.