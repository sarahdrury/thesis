
# script uses a local install of Trimmomatic
# load libraries
import os
import tarfile

seq_dir = 'test_dataset'
trim_out = 'trim_out'
standard1 =' SE -phred33 '
standard2 = ' ILLUMINACLIP:TruSeq3-SE:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36'


file_list = os.listdir(seq_dir)

os.mkdir(trim_out)

for seq in file_list:
   command_trim = 'java -jar ~/masters/lectures/MA5114/FastQC/Trimmomatic-0.39/trimmomatic-0.39.jar' \
+ standard1 + seq_dir + '/' + seq +' ' + trim_out + '/' + seq +'.trimmed' + standard2
   print(command_trim)
   os.system(command_trim)


file_list = os.listdir(".")

with tarfile.open('prac21.tar', 'x') as tar:
	for file in file_list:
		tar.add(file)
