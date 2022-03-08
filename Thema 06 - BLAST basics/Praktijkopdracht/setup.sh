sudo apt-get install cutadapt;
echo 'installing cutadapt..'
echo 'cutadapt installed, installing fastqc..'
sudo apt-get install fastqc;
echo 'fastq installed, installing hisat2..'
sudo apt-get install hisat2;
echo 'hisat2 installed, installing samtools..'
sudo apt-get install samtools;
echo 'hisat2 installed, installing python packages..'
sudo pip install -r requirements.txt;
echo 'python packages installed, setup complete,'
echo 'pipeline should now be functional'
