MA5114 practical 20/ 21
Name: Sarah Drury
Date: 15/12/2020

fastqc_script.py runs FastQC on each .fastq file in the "test_dataset" directory,
creates a directory called "fastqc_out" and places the output (one .html and .zip
file per .fastqc file) into that directory.

trimm_script.py runs Trimmomatic on each .fastq file in the "test_dataset"
directory, creates a directory called "trim_out" and places the output files in 
that directory. It then makes a .zip file called "prac21.tar" containing every file
in the directory it is located.
