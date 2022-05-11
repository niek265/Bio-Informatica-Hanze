#!/usr/bin/perl
use strict;
use warnings;
use Getopt::Long;
use IPC::Open3;
use File::Spec;
use File::Basename;
use Cwd;

## This program is Copyright (C) 2012-19, Felix Krueger (felix.krueger@babraham.ac.uk)
## Edited by Frankie James (github.com/fjames003) for multi-core support

## This program is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.

## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with this program. If not, see <http://www.gnu.org/licenses/>.


## This script is taking in FastQ sequences and trims them using Cutadapt

## last modified on 07 11 2019

my $DOWARN = 1; # print on screen warning and text by default
BEGIN { $SIG{'__WARN__'} = sub { warn $_[0] if $DOWARN } };

my $trimmer_version = '0.6.4_dev';
my $cutadapt_version;
my $python_version;

my ($compression_path,$cores,$cutoff,$adapter,$stringency,$rrbs,$length_cutoff,$keep,$fastqc,$non_directional,$phred_encoding,$fastqc_args,$trim,$gzip,$validate,$retain,$length_read_1,$length_read_2,$a2,$error_rate,$output_dir,$no_report_file,$dont_gzip,$clip_r1,$clip_r2,$three_prime_clip_r1,$three_prime_clip_r2,$nextera,$small_rna,$path_to_cutadapt,$illumina,$max_length,$maxn,$trim_n,$hardtrim5,$clock,$polyA,$hardtrim3,$nextseq,$basename,$consider_already_trimmed) = process_commandline();
my $report_message; # stores result of adapter auto-detection

my @filenames = @ARGV;
die "\nPlease provide the filename(s) of one or more FastQ file(s) to launch Trim Galore!\n
USAGE:  'trim_galore [options] <filename(s)>'    or    'trim_galore --help'    for more options\n\n" unless (@filenames);
file_sanity_check($filenames[0]);

if (defined $hardtrim5){
    warn "Hard-trimming from the 3'-end selected. File(s) will be trimmed to leave the leftmost $hardtrim5 bp on the 5'-end, and Trim Galore will then exit.\n\n";
    foreach my $file(@filenames){
		hardtrim_to_5prime_end($file);
    }
    exit;
}

if (defined $hardtrim3){
    warn "Hard-trimming from 5'-end selected. File(s) will be trimmed to leave the rightmost $hardtrim3 bp on the 3'-end, and Trim Galore will then exit.\n\n";
    foreach my $file(@filenames){
		hardtrim_to_3prime_end($file);
    }
    exit;
}

if ($clock){
    warn "\nIT'S TIME FOR CLOCK PROCESSING!!!\t\t\t\t\t\t\t\t\t[pun intended]\n\n";

    while (@ARGV){
		my $in1 = shift @ARGV;
		my $in2 = shift @ARGV;
		clockwork($in1,$in2);
    }
    warn "\nPre-processing finished...\n\nPlease run Trim Galore again to remove adapters, poor quality bases as well as UMI/fixed sequences from the 3'-end of the reads.\nA sample command for this is:\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\ntrim_galore --paired --three_prime_clip_R1 15 --three_prime_clip_R2 15 *.clock_UMI.R1.fq.gz *.clock_UMI.R2.fq.gz\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nTrim Galore Epigenetic Clock processing complete.\n\n";
    exit;
}

sub clockwork{

    ### FILEHANDLES
    my ($in1_fh,$in2_fh); # input filehandles
    my ($read1_fh,$read2_fh); # output filehandles

    ### INPUT FILES
    my ($in1,$in2) = @_;
    if ($in1 =~ /\.gz$/){
		open ($in1_fh,"$compression_path -d -c $in1 |") or die "Failed to read from file $in1: $!";
    }
    else{
		open ($in1_fh,$in1) or die "Failed to read from file $in1: $!";
    }
    if ($in2 =~ /\.gz$/){
		open ($in2_fh,"$compression_path -d -c $in2 |") or die "Failed to read from file $in2: $!";
    }
    else{
		open ($in2_fh,$in2) or die "Failed to read from file $in2: $!";
    }
    # warn " Input file name 1: $in1\n";
    # warn " Input file name 2: $in2\n";

    ### OUTPUT FILES
    my $out1 = (split (/\//,$in1))[-1];
    my $out2 = (split (/\//,$in2))[-1];

    $out1 =~ s/(\.fastq$|\.fastq\.gz$)//;
    $out1 =~ s/(\.fq$|\.fq\.gz$)//;
    $out1 .= '.clock_UMI.R1.fq'; # appending to the end

    $out2 =~ s/(\.fastq$|\.fastq\.gz$)//;
    $out2 =~ s/(\.fq$|\.fq\.gz$)//;
    $out2 .= '.clock_UMI.R2.fq'; # appending to the end


    ### READ 1
    if ($gzip or $in1 =~ /\.gz$/){
		if ($dont_gzip){
			open ($read1_fh,'>',$output_dir.$out1) or die "Can't open '$out1': $!\n";
		}
		else{
			$out1 .= '.gz';
			open ($read1_fh,"| $compression_path -c - > ${output_dir}${out1}") or die "Can't write to '$out1': $!\n";
		}
    }
    else{
		open ($read1_fh,'>',$output_dir.$out1) or die "Can't open '$out1': $!\n";
    }
    warn "Writing dual trimmed version of the input file '$in1' to '$out1'\n";

    ### READ 2
    if ($gzip or $in2 =~ /\.gz$/){
		if ($dont_gzip){
			open ($read2_fh,'>',$output_dir.$out2) or die "Can't open '$out2': $!\n";
		}
		else{
			$out2 .= '.gz';
			open ($read2_fh,"| $compression_path -c - > ${output_dir}${out2}") or die "Can't write to '$out2': $!\n";
		}
    }
    else{
		open ($read2_fh,'>',$output_dir.$out2) or die "Can't open '$out2': $!\n";
    }
    warn "Writing dual trimmed version of the input file '$in2' to '$out2'\n                 ---\n";
    # warn "Output file name 1: $out1\n";
    # warn "Output file name 2: $out2\n";


    my %freqs;
    my $umi_1;
    my $umi_2;

    # open ($out2,"| $compression_path -c - > $out1") or die $!;
    # open (OUT2,"| $compression_path -c - > $out2") or die $!;

    # print "Processing files $in1 and $in2\n";
    my %r1; # storing the barcodes for R1
    my %r2; # storing the barcodes for R2

    my %fix1; # storing the fixed sequence (CAGT + A from A-tailing) of R1
    my %fix2; # storing the fixed sequence (CAGT + A from A-tailing) of R2

    my $count = 0;
    my $filtered_count = 0;
    my $r1_contains_rc = 0;

	ORANGE: while (1){

		my $one1 = <$in1_fh>;
		my $one2 = <$in1_fh>;
		my $one3 = <$in1_fh>;
		my $one4 = <$in1_fh>;

		my $two1 = <$in2_fh>;
		my $two2 = <$in2_fh>;
		my $two3 = <$in2_fh>;
		my $two4 = <$in2_fh>;

		last unless  ($one4 and $two4);
		chomp $one2; # sequence
		chomp $two2; # sequence

		chomp $one1; # read ID, need to append UMIs to the read ID
		chomp $two1; # read ID, need to append UMIs to the read ID

		chomp $one4; # quality
		chomp $two4; # quality

		++$count; # sequence count

		if ($count % 1000000 ==0){
			warn "Processed $count sequences so far...\n";
		}
		my $r1_barcode;
		my $r2_barcode;
		my $r1_fix;
		my $r2_fix;


		$r1_barcode = substr($one2,0,8);
		$r2_barcode = substr($two2,0,8);
		$r1_fix = substr($one2,8,4);
		$r2_fix = substr($two2,8,4);
		# warn "$one2\n$two2\n$r1_barcode\t$r1_fix\n$r2_barcode\t$r2_fix\n\n";sleep(1);

		# this part of code simply counts the different types of sequence that occurred at the constant region where we expected
		# to read CAGT in both reads. Both R1 and R2 are taken into account at the same time
		unless ($r1_fix eq 'CAGT' and $r2_fix eq 'CAGT'){
			$freqs{$r1_fix}++;
			$freqs{$r2_fix}++;
			$filtered_count++;
		}

		### BOTH READ1 AND READ2 should look like this:

		# 0        8    12 13                                    INDEX position
		# UUUUUUUU CAGT A  FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF   SEQUENCE

		# where:
		#    U = UMI base
		# CAGT = fixed sequence
		#    A = A-tail
		# FFFF = RRBS-fragment to be aligned

		### Capturing the sequence after the A from A-tailing (FFFFFFFFFFFFFF...)

		my $seq1 = substr($one2,13); # truncated sequence without UMIs or fixed sequence
		my $seq2 = substr($two2,13);

		my $qual1 = substr($one4,13); # truncated quality string without barcode or fixed sequence
		my $qual2 = substr($two4,13);

		# warn "$one1\n";
		$one1 .= ":R1:${r1_barcode}:R2:${r2_barcode}:F1:${r1_fix}:F2:${r2_fix}";
		#warn "$one1\n";

		#warn "$two1\n";
		$two1 .= ":R1:${r1_barcode}:R2:${r2_barcode}:F1:${r1_fix}:F2:${r2_fix}";
		#warn "$two1\n";
		#   warn "$one2\n          $seq1\n$one4\n          $qual1\n~~\n$two2\n          $seq2\n$two4\n          $qual2\n\n";sleep(1);

		print ${read1_fh} "$one1\n";
		print ${read1_fh} "$seq1\n";
		print ${read1_fh} "+\n";      # replacing this with a + for space and format reasons
		print ${read1_fh} "$qual1\n";

		print ${read2_fh} "$two1\n";
		print ${read2_fh} "$seq2\n";
		print ${read2_fh} "+\n";      # replacing this with a + for space and format reasons
		print ${read2_fh} "$qual2\n";

		# sleep(1);

		$r1{$r1_barcode}++;
		$r2{$r2_barcode}++;

		$fix1{$r1_fix}++;
		$fix2{$r2_fix}++;
    }

    my $perc;
    if ($count){
		$perc = sprintf("%.2f",$filtered_count/$count * 100);
    }
    else{
		$perc = 'N/A';
    }

    warn "Sequences processed in total: $count\nthereof had fixed sequence CAGT in both R1 and R2:\t $filtered_count ($perc%)\n     ~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n";
}

sub rc{
    my $string = shift;
    $string = reverse($string);
    $string =~ tr/GATC/CTAG/;
    return $string;
}


########################################################################


my $path_to_fastqc = 'fastqc';


########################################################################




### SETTING DEFAULTS UNLESS THEY WERE SPECIFIED
unless (defined $cutoff){
	unless ($nextseq){
       $cutoff = 20;
    }
}

my $phred_score_cutoff = $cutoff; # only relevant for report
my $adapter_name = '';
unless (defined $adapter){
    if ($nextera){
		$adapter = 'CTGTCTCTTATA';
		$adapter_name = 'Nextera Transposase sequence; user defined';
    }
    elsif($small_rna){
		$adapter = 'TGGAATTCTCGG';
		$adapter_name = 'Illumina small RNA adapter; user defined';
    }
    elsif($illumina){
		$adapter = 'AGATCGGAAGAGC';
		$adapter_name = 'Illumina TruSeq, Sanger iPCR; user defined';
    }
    else{ # default
		### If other -a and/or -a2 were given
		if ($polyA){ # specialised PolyA trimming
			($adapter,$adapter_name) = autodetect_polyA_type();

			if ($validate){ # we need to select -a2 as the reverse complement to -a
				if ($adapter =~ /A+/){
					$adapter =  extend_adapter_sequence("A",20);  # defaulting to 20
					$a2 = extend_adapter_sequence("T",150); # defaulting to 150 bp
				}
				elsif($adapter =~ /T+/){
					$adapter =  extend_adapter_sequence("T",20);  # defaulting to 20
					$a2 = extend_adapter_sequence("A",150);
				}
				else{
					die "Something unexpected happened with the Poly-A autodetection, please check\n";
				}
				# warn "Paired-end Poly-A detection, set the following parameters:\n";
				# warn " -a: $adapter\n-a2: $a2\n   ~~~~~~~~~~ \n\n";sleep(1);
			}
			else{
				# Single end
				if ($adapter =~ /A+/){
					$adapter =  extend_adapter_sequence("A",20);  # defaulting to 20
				}
				elsif($adapter =~ /T+/){
					$adapter =  extend_adapter_sequence("T",20);  # defaulting to 20
				}
				else{
					die "Something unexpected happened with the Poly-A autodetection, please check\n";
				}
			}
		}
		else{ # ADAPTER TRIMMING; DEFAULT
			($adapter,$adapter_name,$report_message) = autodetect_adapter_type();
		}
    }
}
else{
    $adapter_name = 'user defined';
}

### For smallRNA adapters we are reducing the sequence length cutoff before a sequences gets thrown out entirely to 18bp. We are doing this because some 20-23bp long smallRNAs
### may be removed if T, TG, or TGG etc gets trimmed off the end (changed b ack up from 16 to 18bp to remove noise from alignment files, 18 11 2015)
if ($adapter eq 'TGGAATTCTCGG'){
    unless (defined $length_cutoff){ # user defined length cutoff wins over auto-detection
		$length_cutoff = 18;
		warn "Reducing length cutoff to 18bp for small RNA-Seq reads because a cutoff of 20bp may remove some short species of small RNAs if they had been trimmed by 1,2 or 3bp\n";
    }

    ### If the file is a smallRNA library and paired-end we set the Illumina 5' adapter as the $a2 sequence
    if ($validate){
		unless (defined $a2){
			$a2 = 'GATCGTCGGACT';
			warn "Setting the Illumina smallRNA 5' adapter as adapter 2: 'GATCGTCGGACT'\n";
		}
    }
}

unless (defined $length_cutoff){
    $length_cutoff = 20; # non small RNA length cutoff
}


unless (defined $a2){ # optional adapter for the second read in a pair. Only works for --paired trimming
	$a2 = '';
}

unless (defined $stringency){
	$stringency = 1;
}

if ($phred_encoding == 64){
    $cutoff += 31;
}


my $file_1;
my $file_2;

foreach my $filename (@ARGV){
    trim ($filename);
}


sub trim{
    my $filename = shift;

    my $output_filename = (split (/\//,$filename))[-1];

    my $report = $output_filename;
    $report =~ s/$/_trimming_report.txt/;


	if ($no_report_file) {
		$report = File::Spec->devnull;
		open (REPORT,'>',$report) or die "Failed to write to file '$report': $!\n";
		# warn "Redirecting report output to /dev/null\n";
	}
    else{
		open (REPORT,'>',$output_dir.$report) or die "Failed to write to file '$report': $!\n";
		warn "Writing report to '$output_dir$report'\n";
    }

    warn "\nSUMMARISING RUN PARAMETERS\n==========================\nInput filename: $filename\n";
    print REPORT "\nSUMMARISING RUN PARAMETERS\n==========================\nInput filename: $filename\n";

    if ($validate){ # paired-end mode
		warn "Trimming mode: paired-end\n";
		print REPORT "Trimming mode: paired-end\n";
    }
    else{
		warn "Trimming mode: single-end\n";
		print REPORT "Trimming mode: single-end\n";
    }

    warn "Trim Galore version: $trimmer_version\n";
    print REPORT "Trim Galore version: $trimmer_version\n";

    warn "Cutadapt version: $cutadapt_version\n";
    print REPORT "Cutadapt version: $cutadapt_version\n";

	if (defined $python_version){
		warn "Python version: $python_version\n";
		print REPORT "Python version: $python_version\n";
	}

    if (defined $cores){
		my $temp = $cores;
		$temp =~ s/-j //;
        warn "Number of cores used for trimming: $temp\n";
		print REPORT "Number of cores used for trimming: $temp\n";
    }
	
    if (defined $phred_score_cutoff){
        warn "Quality Phred score cutoff: $phred_score_cutoff\n";
		print REPORT "Quality Phred score cutoff: $phred_score_cutoff\n";
    }


    warn "Quality encoding type selected: ASCII+$phred_encoding\n";
    print REPORT "Quality encoding type selected: ASCII+$phred_encoding\n";

    if ($report_message){
    	# warn "adding Auto-detection statement\n";
    	print REPORT $report_message;
    }

    warn "Adapter sequence: '$adapter' ($adapter_name)\n";
    print REPORT "Adapter sequence: '$adapter' ($adapter_name)\n";

    if ($error_rate == 0.1){
        warn "Maximum trimming error rate: $error_rate (default)\n";
    }
    else{
        warn "Maximum trimming error rate: $error_rate\n";
    }

    if (defined $maxn){
        warn "Maximum number of tolerated Ns: $maxn\n";
    }

    if ($nextseq){
        warn "2-colour high quality G-trimming enabled, with quality cutoff: $nextseq\n";
        print REPORT "2-colour high quality G-trimming enabled, with quality cutoff: $nextseq\n";
    }

    print REPORT "Maximum trimming error rate: $error_rate";
	if ($error_rate == 0.1){
		print REPORT " (default)\n";
    }
    else{
		print REPORT "\n";
    }

    if ($a2){
        warn "Optional adapter 2 sequence (only used for read 2 of paired-end files): '$a2'\n";
        print REPORT "Optional adapter 2 sequence (only used for read 2 of paired-end files): '$a2'\n";
    }

    warn "Minimum required adapter overlap (stringency): $stringency bp\n";
    print REPORT "Minimum required adapter overlap (stringency): $stringency bp\n";


    if (defined $consider_already_trimmed){
    	warn "During adapter auto-detection, files are considered already adapter-trimmed if the highest found adapter was found equal to or lower than: $consider_already_trimmed\n";
	    print REPORT "During adapter auto-detection, files are considered already adapter-trimmed if the highest found adapter was found equal to or lower than: $consider_already_trimmed\n";
    }

    if ($validate){
        warn "Minimum required sequence length for both reads before a sequence pair gets removed: $length_cutoff bp\n";
        print REPORT "Minimum required sequence length for both reads before a sequence pair gets removed: $length_cutoff bp\n";
    }
    else{
        warn "Minimum required sequence length before a sequence gets removed: $length_cutoff bp\n";
        print REPORT "Minimum required sequence length before a sequence gets removed: $length_cutoff bp\n";
    }

    if ($max_length){
        warn "Maxiumum tolerated read length after trimming (for smallRNA trimming): $max_length bp\n";
        print REPORT "Maxiumum tolerated read length after trimming (for smallRNA trimming): $max_length bp\n";
    }

    if ($trim_n){
        warn "Removing Ns from the start and end of reads\n";
        print REPORT "Removing Ns from the start and end of reads\n";
    }


    if ($validate){ # only for paired-end files

        if ($retain){ # keeping single-end reads if only one end is long enough

            if ($length_read_1 == 35){
                warn "Length cut-off for read 1: $length_read_1 bp (default)\n";
                print REPORT "Length cut-off for read 1: $length_read_1 bp (default)\n";
            }
            else{
                warn "Length cut-off for read 1: $length_read_1 bp\n";
                print REPORT "Length cut-off for read 1: $length_read_1 bp\n";
            }

            if ($length_read_2 == 35){
                warn "Length cut-off for read 2: $length_read_2 bb (default)\n";
                print REPORT "Length cut-off for read 2: $length_read_2 bp (default)\n";
            }
            else{
                warn "Length cut-off for read 2: $length_read_2 bp\n";
                print REPORT "Length cut-off for read 2: $length_read_2 bp\n";
            }
        }
    }

    if ($rrbs){
        warn "File was specified to be an MspI-digested RRBS sample. Read 1 sequences with adapter contamination will be trimmed a further 2 bp from their 3' end, and Read 2 sequences will be trimmed by 2 bp from their 5' end to remove potential methylation-biased bases from the end-repair reaction\n";
        print REPORT "File was specified to be an MspI-digested RRBS sample. Read 1 sequences with adapter contamination will be trimmed a further 2 bp from their 3' end, and Read 2 sequences will be trimmed by 2 bp from their 5' end to remove potential methylation-biased bases from the end-repair reaction\n";
    }

    if ($non_directional){
        warn "File was specified to be a non-directional MspI-digested RRBS sample. Sequences starting with either 'CAA' or 'CGA' will have the first 2 bp trimmed off to remove potential methylation-biased bases from the end-repair reaction\n";
        print REPORT "File was specified to be a non-directional MspI-digested RRBS sample. Sequences starting with either 'CAA' or 'CGA' will have the first 2 bp trimmed off to remove potential methylation-biased bases from the end-repair reaction\n";
    }

    if ($trim){
        warn "All sequences will be trimmed by 1 bp on their 3' end to avoid problems with invalid paired-end alignments with Bowtie 1\n";
        print REPORT "All sequences will be trimmed by 1 bp on their 3' end to avoid problems with invalid paired-end alignments with Bowtie 1\n";
    }

    if ($clip_r1){
    warn "All Read 1 sequences will be trimmed by $clip_r1 bp from their 5' end to avoid poor qualities or biases\n";
    print REPORT "All Read 1 sequences will be trimmed by $clip_r1 bp from their 5' end to avoid poor qualities or biases\n";
    }
    if ($clip_r2){
		warn "All Read 2 sequences will be trimmed by $clip_r2 bp from their 5' end to avoid poor qualities or biases (e.g. M-bias for BS-Seq applications)\n";
		print REPORT "All Read 2 sequences will be trimmed by $clip_r2 bp from their 5' end to avoid poor qualities or biases (e.g. M-bias for BS-Seq applications)\n";
	}

    if ($three_prime_clip_r1){
		warn "All Read 1 sequences will be trimmed by $three_prime_clip_r1 bp from their 3' end to avoid poor qualities or biases\n";
		print REPORT "All Read 1 sequences will be trimmed by $three_prime_clip_r1 bp from their 3' end to avoid poor qualities or biases\n";
    }
    if ($three_prime_clip_r2){
		warn "All Read 2 sequences will be trimmed by $three_prime_clip_r2 bp from their 3' end to avoid poor qualities or biases\n";
		print REPORT "All Read 2 sequences will be trimmed by $three_prime_clip_r2 bp from their 3' end to avoid poor qualities or biases\n";
    }

    if ($fastqc){
        warn "Running FastQC on the data once trimming has completed\n";
        print REPORT "Running FastQC on the data once trimming has completed\n";

        if ($fastqc_args){
            warn "Running FastQC with the following extra arguments: '$fastqc_args'\n";
            print REPORT  "Running FastQC with the following extra arguments: $fastqc_args\n";
        }
    }

    if ($keep and $rrbs){
        warn "Keeping quality trimmed (but not yet adapter trimmed) intermediate FastQ file\n";
        print REPORT "Keeping quality trimmed (but not yet adapter trimmed) intermediate FastQ file\n";
    }


    if ($gzip or $filename =~ /\.gz$/){
        $gzip = 1;
        unless ($dont_gzip){
            warn "Output file(s) will be GZIP compressed\n";
            print REPORT "Output file will be GZIP compressed\n";
        }
    }


    warn "\n";
    print REPORT "\n";
    # sleep (3);

    my $temp;

	### We need to make sure that Cutadapt still runs if users use a fairly old version of Cutadapt, as multi-core handling is only supported sincce
	### Cutadapt version 1.15. Edited on 08 03 2019
	# if the Cutadapt version has more . in the version, we discard the second one.
	# warn "Version was: $cutadapt_version\n";
	if ($cutadapt_version =~ /(\d+\.\d+)\.\d+/){
		$cutadapt_version = $1;
	}
	# warn "Version now is: $cutadapt_version\n"; 
	my ($major_version,$sub_version) = ($1,$2) if ($cutadapt_version =~ /^(\d+)\.(\d+)$/);
	# warn "Major: $major_version\nSub version: $sub_version\n";
	# sleep(3);
	if ($major_version == 1){ # versions prior to 1.15 did not support the -j option
		if ($sub_version < 15){
			if ($cores > 1){
				die "I'm sorry but your version of Cutadapt is too old to support multi-core trimming. Please update Cutadapt, and try again\n\n";
			}
			else{ #default single-core prcessing with old version of Cutadapt
				warn "Your version of Cutadapt is fairly old (detected v$cutadapt_version), please consider updating Cutadapt!\n";
				$cores = ""; # need to delete -j entirely as Cutadapt 	
			}	
		}
		else{
			warn "Cutadapt seems to be reasonably up-to-date. Setting -j $cores\n";
			unless ($cores =~ /^-j \d+$/){ # if it was set before, don't change it again
				$cores = "-j $cores";
			}
		}
	}
	elsif ($major_version > 1){
		warn "Cutadapt seems to be fairly up-to-date (version $cutadapt_version). Setting -j $cores\n";
		unless ($cores =~ /^-j \d+$/){ # if it was set before, don't change it again
			$cores = "-j $cores";
		}
	}
	else{
		die "Cutadapt major version was not 1 or higher. Simply too old...\n";
	}

    ### Proceeding differently for RRBS and other type of libraries
    if ($rrbs){
      
		### Skipping quality filtering for RRBS libraries if a quality cutoff of 0 was specified
		if ($cutoff == 0){
			warn "Quality cutoff selected was 0    -    Skipping quality trimming altogether\n\n";
			# sleep (3);
		}
		else{
	  
			$temp = $filename;
			$temp =~ s/^.*\///; # replacing optional file path information
			$temp =~ s/$/_qual_trimmed.fastq/;
			open (TEMP,'>',$output_dir.$temp) or die "Can't write to '$temp': $!";
	  
			warn "  >>> Now performing adaptive quality trimming with a Phred-score cutoff of: $cutoff <<<\n\n";
			# sleep (1);
		  
			open (QUAL,"$path_to_cutadapt  $cores -e $error_rate -q $cutoff -a X $filename |") or die "Can't open pipe to Cutadapt: $!";

			my $qual_count = 0;
		  
			while (1){
				my $l1 = <QUAL>;
				my $seq = <QUAL>;
				my $l3 = <QUAL>;
				my $qual = <QUAL>;
				last unless (defined $qual);
		
				$qual_count++;
				if ($qual_count%10000000 == 0){
					warn "$qual_count sequences processed\n";
				}
				print TEMP "$l1$seq$l3$qual";
			}
		  
			warn "\n  >>> Quality trimming completed <<<\n$qual_count sequences processed in total\n\n";
			close QUAL or die "Unable to close QUAL filehandle: $!\n";
		  
		}	
	}
  
  
	if ($output_filename =~ /\.fastq$/){
		$output_filename =~ s/\.fastq$/_trimmed.fq/;
	}
	elsif ($output_filename =~ /\.fastq\.gz$/){
		$output_filename =~ s/\.fastq\.gz$/_trimmed.fq/;
	}
	elsif ($output_filename =~ /\.fq$/){
		$output_filename =~ s/\.fq$/_trimmed.fq/;
	}
	elsif ($output_filename =~ /\.fq\.gz$/){
		$output_filename =~ s/\.fq\.gz$/_trimmed.fq/;
	}
	else{
		$output_filename =~ s/$/_trimmed.fq/;
	}
  
	if ($gzip or $filename =~ /\.gz$/){
		if ($dont_gzip){
			open (OUT,'>',$output_dir.$output_filename) or die "Can't open '$output_filename': $!\n"; # don't need to gzip intermediate file
		}
		else{
			### 6 Jan 2014: had a request to also gzip intermediate files to save disk space
			#  if ($validate){
			# open (OUT,'>',$output_dir.$output_filename) or die "Can't open '$output_filename': $!\n"; # don't need to gzip intermediate file
			# }
			$output_filename .= '.gz';
			open (OUT,"| $compression_path -c - > ${output_dir}${output_filename}") or die "Can't write to '$output_filename': $!\n";
		}
	}
	else{
		open (OUT,'>',$output_dir.$output_filename) or die "Can't open '$output_filename': $!\n";
	}
	warn "Writing final adapter and quality trimmed output to $output_filename\n\n";
  
	my $count = 0;
	my $too_short = 0;
	my $too_long = 0;
	my $too_many_n = 0;
	my $quality_trimmed = 0;
	my $rrbs_trimmed = 0;
	my $rrbs_trimmed_start = 0;
	my $CAA = 0;
	my $CGA = 0;
  
	my $pid;
  
	if ($rrbs and $cutoff != 0){
     
		### optionally using 2 different adapters for read 1 and read 2
		if ($validate and $a2){
			### Figure out whether current file counts as read 1 or read 2 of paired-end files
			if ( scalar(@filenames)%2 == 0){ # this is read 1 of a pair
				warn "\n  >>> Now performing adapter trimming for the adapter sequence: '$adapter' from file $temp <<< \n";
				#sleep (1);
				$pid = open3 (\*WRITER, \*TRIM, \*ERROR,"$path_to_cutadapt  $cores -e $error_rate -O $stringency -a $adapter $output_dir$temp") or die "Failed to launch Cutadapt: $!\n";
			}
			else{                            # this is read 2 of a pair
				warn "\n  >>> Now performing adapter trimming for the adapter sequence: '$a2' from file $temp <<< \n";
				#sleep (1);
				$pid = open3 (\*WRITER, \*TRIM, \*ERROR,"$path_to_cutadapt  $cores -e $error_rate -O $stringency -a $a2 $output_dir$temp") or die "Failed to launch Cutadapt: $!\n";
			}
		}
		### Using the same adapter for both read 1 and read 2
		else{
			warn "\n  >>> Now performing adapter trimming for the adapter sequence: '$adapter' from file $temp <<< \n";
			# sleep (3);
			$pid = open3 (\*WRITER, \*TRIM, \*ERROR,"$path_to_cutadapt  $cores -e $error_rate -O $stringency -a $adapter $output_dir$temp") or die "Failed to launch Cutadapt: $!\n";
		}
      
		close WRITER or die $!; # not needed
      
		open (QUAL,"$output_dir$temp") or die $!; # quality trimmed file
      
		if ($filename =~ /\.gz$/){
			open (IN,"gunzip -c $filename |") or die $!; # original, untrimmed file
		}
		else{
			open (IN,$filename) or die $!; # original, untrimmed file
		}
      
		while (1){
	  
			# we can process the output from Cutadapt and the original input 1 by 1 to decide if the adapter has been removed or not
			my $l1 = <TRIM>;
			my $seq = <TRIM>; # adapter trimmed sequence
			my $l3 = <TRIM>;
			my $qual = <TRIM>;
	  
			$_ = <IN>;   # irrelevant
			my $original_seq = <IN>;
			$_ = <IN>;   # irrelevant
			$_ = <IN>;   # irrelevant
	  
			$_ = <QUAL>; # irrelevant
			my $qual_trimmed_seq = <QUAL>;
			$_ = <QUAL>; # irrelevant
			my $qual_trimmed_qual = <QUAL>;		

			last unless (defined $qual and defined $qual_trimmed_qual); # could be empty strings

			$count++;
			if ($count%10000000 == 0){
				warn "$count sequences processed\n";
			}
	  
			chomp $seq;
			chomp $qual;
			chomp $qual_trimmed_seq;
			chomp $original_seq;
	  
			my $quality_trimmed_seq_length = length $qual_trimmed_seq;
	  
			if (length $original_seq > length $qual_trimmed_seq){
				++$quality_trimmed;
			}
	  
			my $nd = 0;
	  
			### NON-DIRECTIONAL RRBS
			if ($non_directional){
				$nd = 1;
				if (length$seq > 2){ # only doing something if the read is longer than 2bp
					
					# only trimming Read 1 of a pair for a further 2bp from their 3' end
					if ($seq =~ /^CAA/){ # this might be a non-directional sequence
						++$CAA;
						$seq = substr ($seq,2,length($seq)-2);
						$qual = substr ($qual,2,length($qual)-2);
						++$rrbs_trimmed_start;
					}
					elsif ($seq =~ /^CGA/){ # this might be a non-directional sequence
						$seq = substr ($seq,2,length($seq)-2);
						$qual = substr ($qual,2,length($qual)-2);
						++$CGA;
						++$rrbs_trimmed_start;
					}
					else{ 							
						# If the reads look like standard OT/OB sequences (CGG/TGG) 
						# we need to trim in the same way as for directional sequences
						if (length$seq < $quality_trimmed_seq_length){
							$seq = substr ($seq,0,length($seq)-2);
							$qual = substr ($qual,0,length($qual)-2);
							++$rrbs_trimmed;
						}
					}							
				}
				else{
					# read is too short anyway (so it will probably not survive the length filtering step
				}
			}
	  
			### directional read
			unless ($nd == 1){
				# only trimming Read 1 of a pair for a further 2bp from their 3' end
				if ($validate){ # paired end
					if ( scalar(@filenames)%2 == 0){ # this is read 1 of a pair
						if (length $seq >= 2 and length$seq < $quality_trimmed_seq_length){
							$seq = substr ($seq,0,length($seq)-2);
							$qual = substr ($qual,0,length($qual)-2);
							++$rrbs_trimmed;
						}
					}
					else{
						# this is read 2 of a pair. We do not trim further from the 3' end but rather trim R2 from the 5' end later
					}
				}
				else{ # single-end reads will be trimmed from their 3' end
					if (length $seq >= 2 and length$seq < $quality_trimmed_seq_length){                                                                                                                   
						$seq = substr ($seq,0,length($seq)-2);                                                                                                                                            
						$qual = substr ($qual,0,length($qual)-2);                                                                                                                                         
						++$rrbs_trimmed;                                                                                                                                                                  
					}                                  
				}
			}

			### Shortening all sequences by 1 bp on the 3' end 
			# 28 02 2019: This was really only required for Bowtie 1 paired-end alignments, maybe we should drop this option in soon
			if ($trim){
				$seq = substr($seq,0,length($seq)-1);
				$qual = substr($qual,0,length($qual)-1);
			}
	  
			### PRINTING (POTENTIALLY TRIMMED) SEQUENCE
			if ($validate){ # printing the sequence without performing a length check (this is performed for the read pair separately later)
				print OUT "$l1$seq\n$l3$qual\n";
			}
			else{ # single end
	      
				if ($clip_r1){
					if (length $seq > $clip_r1){  # sequences that are already too short won't be clipped again
						$seq = substr($seq,$clip_r1); # starting after the sequences to be trimmed until the end of the sequence
						$qual = substr($qual,$clip_r1);
					}
				}
	      
				if ($three_prime_clip_r1){
					if (length $seq > $three_prime_clip_r1){  # sequences that are already too short won't be clipped again
					# warn	 "seq/qual before/after trimming:\n$seq\n$qual\n";
						$seq = substr($seq,0,(length($seq) - $three_prime_clip_r1)); # starting after the sequences to be trimmed until the end of the sequence
						$qual = substr($qual,0,(length($qual) - $three_prime_clip_r1 ));
						# warn "$seq\n$qual\n";
					}
				}
	      
				if (defined $maxn){
					my $n_count = Ncounter($seq);
					# warn "Checking for Ns: Found $n_count\n";
					if ($n_count > $maxn){
						++$too_many_n;
						next;
					}
				}	
		  
				if (length $seq < $length_cutoff){
					++$too_short;
					next;
				}
				elsif($max_length and length$seq > $max_length){
					++$too_long;
					next; # sequence is too long
				}
				else{
					print OUT "$l1$seq\n$l3$qual\n";
				}
			}
		}
      
		print REPORT "\n";
		while (<ERROR>){
			warn $_;
			print REPORT $_;
		}
		
		close IN or die "Unable to close IN filehandle: $!";
		close QUAL or die "Unable to close QUAL filehandle: $!";
		close TRIM or die "Unable to close TRIM filehandle: $!";
		close OUT or die  "Unable to close OUT filehandle: $!";
      
	}
    ############################################################################################################

    elsif($polyA){ # PolyA trimming
	
		warn "POLY-A TRIMMING MODE; EXPERIMENTAL!!\n";
		my $isR2 = 0;
	
		# For the moment we set the temp file name back to $filename
		$temp = $filename;

		### optionally using 2 different adapters for read 1 and read 2
		if ($validate and $a2){
			### Figure out whether current file counts as read 1 or read 2 of paired-end files
			if ( scalar(@filenames)%2 == 0){ # this is read 1 of a pair
				warn "\n  >>> Now performing Poly-A trimming for the adapter sequence: '$adapter' from file $temp <<< \n";
				$pid = open3 (\*WRITER, \*TRIM, \*ERROR,"$path_to_cutadapt  $cores -e $error_rate -O $stringency -a $adapter $output_dir$temp") or die "Failed to launch Cutadapt: $!\n";
			}
			else{                            # this is read 2 of a pair
				$isR2 = 1;
				warn "\n  >>> Now performing Poly-A trimming for the adapter sequence: '$a2' from file $temp <<< \n";	
				# For Read 2 we need to trim the PolyT (or PolyA) from the 5' end instead! Hence -g $a2 and not -a! 
				$pid = open3 (\*WRITER, \*TRIM, \*ERROR,"$path_to_cutadapt  $cores -e $error_rate -O $stringency -g $a2 $output_dir$temp") or die "Failed to launch Cutadapt: $!\n";
			}
		}
		### Using the same adapter for both read 1 and read 2 - Single end will use the same adapters are Read 1s for paired-end files
		else{
			warn "\n  >>> Now performing single-end Poly-A trimming for with the sequence: '$adapter' from file $temp <<< \n";
			# sleep (3);
			$pid = open3 (\*WRITER, \*TRIM, \*ERROR,"$path_to_cutadapt  $cores -e $error_rate -O $stringency -a $adapter $output_dir$temp") or die "Failed to launch Cutadapt: $!\n";
		}
		
		close WRITER or die $!; # not needed

		# This is the Illumina adapter trimmed file
		if ($temp =~ /\.gz$/){
			open (QUAL,"gunzip -c $output_dir$temp |") or die $!; # quality trimmed file
		}
		else{
			open (QUAL,"$output_dir$temp") or die $!; # quality trimmed file
		}
	  
		while(1){
			# we can process the output from Cutadapt and the original input 1 by 1 to decide if the adapter has been removed or not
			my $l1 = <TRIM>;
			my $seq = <TRIM>; # adapter trimmed sequence
			my $l3 = <TRIM>;
			my $qual = <TRIM>;
		  
			#   $_ = <IN>;   # irrelevant
			#   my $original_seq = <IN>;
			#   $_ = <IN>;   # irrelevant
			#   $_ = <IN>;   # irrelevant
			
			$_ = <QUAL>; # irrelevant
			my $qual_trimmed_seq = <QUAL>;
			$_ = <QUAL>; # irrelevant
			my $qual_trimmed_qual = <QUAL>;
			
			last unless (defined $qual and defined $qual_trimmed_qual); # could be empty strings
			
			$count++;
			if ($count%10000000 == 0){
				warn "$count sequences processed\n";
			}
			chomp $l1;
			chomp $seq;
			chomp $qual;
			chomp $qual_trimmed_seq;
			# chomp $original_seq;
			
			my $quality_trimmed_seq_length = length $qual_trimmed_seq;
			
			#    if (length $original_seq > length $qual_trimmed_seq){
			#		++$quality_trimmed;
			#	     }
			
			my $diff = length($qual_trimmed_seq) - length($seq);

			### CHANGING THE readID to remove white spaces and adding PolyA trimming information
			$l1 =~ s/\s+/_/g; # removing white spaces from readID
			if ($diff > 0){ # only adding the PolyA removal tag if some A's were really removed, so we can filter these out later if desired
				# warn "$l1\n";
				$l1 =~ s/\@/\@${diff}:A:/; # also adding the PolyA trimmed reads to the start of the read in the format
				# "trimmed_bases:A:" as this is the current Way Thermo Fisher are handling it
				$l1 .= "_PolyA:$diff";
				# warn "$l1\n~~~~~~~~~~~~~\n"; sleep(1);
			}
			
			### Shortening all sequences by 1 bp on the 3' end - This is probably no longer needed since we have stopped using Bowtie (1)
			if ($trim){
				$seq = substr($seq,0,length($seq)-1);
				$qual = substr($qual,0,length($qual)-1);
			}
			
			### PRINTING (POTENTIALLY TRIMMED) SEQUENCE
			if ($validate){ # printing the sequence without performing a length check (this is performed for the read pair separately later)
				if ($isR2){
					#print "$l1\n$qual_trimmed_seq\n$seq\n$l3$qual_trimmed_qual\n$qual\n~~~~~\n";
				   # print "length original: ",length($qual_trimmed_seq) , "\nlength trimmed:  ", length($seq) , "\nDifference: $diff bp\n   ~~~\n\n"; sleep(1);
				}
				print OUT "$l1\n$seq\n$l3$qual\n";
			}
			else{ # single end
			
				if ($clip_r1){
					if (length $seq > $clip_r1){  # sequences that are already too short won't be clipped again
						$seq = substr($seq,$clip_r1); # starting after the sequences to be trimmed until the end of the sequence
						$qual = substr($qual,$clip_r1);
					}
				}
				
				if ($three_prime_clip_r1){
					if (length $seq > $three_prime_clip_r1){  # sequences that are already too short won't be clipped again
						# warn "seq/qual before/after trimming:\n$seq\n$qual\n";
						$seq = substr($seq,0,(length($seq) - $three_prime_clip_r1)); # starting after the sequences to be trimmed until the end of the sequence
						$qual = substr($qual,0,(length($qual) - $three_prime_clip_r1 ));
						# warn "$seq\n$qual\n";
					}
				}
			
				if (length $seq < $length_cutoff){
					++$too_short;
					next;
				}
				elsif($max_length and length$seq > $max_length){
					++$too_long;
					next; # sequence is too long
				}
				else{
					print OUT "$l1\n$seq\n$l3$qual\n";
				}
			}
		}
	
		print REPORT "\n";
		while (<ERROR>){
			warn $_;
			print REPORT $_;
		}
	
		close QUAL or die "Unable to close QUAL filehandle: $!";
		close TRIM or die "Unable to close TRIM filehandle: $!";
		close OUT or die  "Unable to close OUT filehandle: $!";
    }
    
    ############################################################################################################  
    else{ # non-RRBS mode. default

    	my $quality_cutoff;

		if ($nextseq){
      		$quality_cutoff = $nextseq;
      	}
      	else{
      		$quality_cutoff = "-q $cutoff";
      	}

		### optionally using 2 different adapters for read 1 and read 2
		if ($validate and $a2){
     
			### Figure out whether current file counts as read 1 or read 2 of paired-end files
			if ( scalar(@filenames)%2 == 0){ # this is read 1 of a pair
				warn "\n  >>> Now performing quality (cutoff '$quality_cutoff') and adapter trimming in a single pass for the adapter sequence: '$adapter' from file $filename <<< \n";
				#sleep (1);
				$pid = open3 (\*WRITER, \*TRIM, \*ERROR, "$path_to_cutadapt  $cores -e $error_rate $quality_cutoff -O $stringency $trim_n -a $adapter $filename") or die "Failed to launch Cutadapt: $!";
			}
			else{                            # this is read 2 of a pair
				warn "\n  >>> Now performing quality (cutoff '$quality_cutoff') and adapter trimming in a single pass for the adapter sequence: '$a2' from file $filename <<< \n";
				#sleep (1);
				$pid = open3 (\*WRITER, \*TRIM, \*ERROR, "$path_to_cutadapt  $cores -e $error_rate $quality_cutoff -O $stringency $trim_n -a $a2 $filename") or die "Failed to launch Cutadapt: $!";
			}
		}
		### Using the same adapter for both read 1 and read 2
		else{
			warn "\n  >>> Now performing quality (cutoff '$quality_cutoff') and adapter trimming in a single pass for the adapter sequence: '$adapter' from file $filename <<< \n";
			#sleep (1);
			$pid = open3 (\*WRITER, \*TRIM, \*ERROR, "$path_to_cutadapt  $cores -e $error_rate $quality_cutoff -O $stringency $trim_n -a $adapter $filename") or die "Failed to launch Cutadapt: $!";
		}
      
		close WRITER or die $!; # not needed
    
		while (1){
	  
			my $l1 = <TRIM>;
			my $seq = <TRIM>; # quality and/or adapter trimmed sequence
			my $l3 = <TRIM>;
			my $qual = <TRIM>;
			# print "$l1$seq\n$l3$qual\n";
			last unless (defined $qual); # could be an empty string
	  
			$count++;
			if ($count%10000000 == 0){
				warn "$count sequences processed\n";
			}
	  
			chomp $seq;
			chomp $qual;

			### Shortening all sequences by 1 bp on the 3' end
			if ($trim){
				$seq = substr($seq,0,length($seq)-1);
				$qual = substr($qual,0,length($qual)-1);
			}
	  
			### PRINTING (POTENTIALLY TRIMMED) SEQUENCE
			if ($validate){ # printing the sequence without performing a length check (this is performed for the read pair separately later)
				print OUT "$l1$seq\n$l3$qual\n";
			}
			else{ # single end
			  
				if ($clip_r1){
					if (length $seq > $clip_r1){ # sequences that are already too short won't be clipped again
						$seq = substr($seq,$clip_r1); # starting after the sequences to be trimmed until the end of the sequence
						$qual = substr($qual,$clip_r1);
					}
				}
			  
				if ($three_prime_clip_r1){
					if (length $seq > $three_prime_clip_r1){  # sequences that are already too short won't be clipped again
						# warn "seq/qual before/after trimming:\n$seq\n$qual\n";
						$seq = substr($seq,0,(length($seq) - $three_prime_clip_r1)); # starting after the sequences to be trimmed until the end of the sequence
						$qual = substr($qual,0,(length($qual) - $three_prime_clip_r1));
						# warn "$seq\n$qual\n";sleep(1);
					}
				}

				if (defined $maxn){
					my $n_count = Ncounter($seq);
					# warn "Checking for Ns: Found $n_count\n";
					if ($n_count > $maxn){
						++$too_many_n;
						next;
					}
				}	
	      
				if (length $seq < $length_cutoff){
					++$too_short;
					next;
				}
				elsif ($max_length and length$seq > $max_length){
					++$too_long;
					next; # sequence is too long
				}
				else{
					print OUT "$l1$seq\n$l3$qual\n";
				}
			}
		}
      
		print REPORT "\n";
		while (<ERROR>){
			warn $_;
			print REPORT $_;
		}	
      
		close TRIM or die "Unable to close TRIM filehandle: $!\n";
		close ERROR or die "Unable to close ERROR filehandle: $!\n";
		close OUT or die  "Unable to close OUT filehandle: $!\n";
      
	}
  
  
	if ($rrbs){
		unless ($keep){ # keeping the quality trimmed intermediate file for RRBS files
	  
			# deleting temporary quality trimmed file
			my $deleted = unlink "$output_dir$temp";
		  
			if ($deleted){
				warn "Successfully deleted temporary file $temp\n\n";
			}
			else{
				warn "Could not delete temporary file $temp";
			}
		}
	}
  
	### Wait and reap the child process (Cutadapt) so that it doesn't become a zombie process
	waitpid $pid, 0;
	unless ($? == 0){
		die "\n\nCutadapt terminated with exit signal: '$?'.\nTerminating Trim Galore run, please check error message(s) to get an idea what went wrong...\n\n";
	}
  
	warn "\nRUN STATISTICS FOR INPUT FILE: $filename\n";
	print REPORT "\nRUN STATISTICS FOR INPUT FILE: $filename\n";
  
	warn "="x 45,"\n";
	print REPORT "="x 45,"\n";
  
	warn "$count sequences processed in total\n";
	print REPORT "$count sequences processed in total\n";
  
	###  only reporting this separately if quality and adapter trimming were performed separately
	if ($rrbs){
		my $percentage_shortened;
		if ($count){
			$percentage_shortened = sprintf ("%.1f",$quality_trimmed/$count*100);
			warn "Sequences were truncated to a varying degree because of deteriorating qualities (Phred score quality cutoff: $cutoff):\t$quality_trimmed ($percentage_shortened%)\n";
			print REPORT "Sequences were truncated to a varying degree because of deteriorating qualities (Phred score quality cutoff: $cutoff):\t$quality_trimmed ($percentage_shortened%)\n";
		}
		else{
			warn "Unable to determine percentage of reads that were shortened because 0 lines were processed\n\n";
			print REPORT "Unable to determine percentage of reads that were shortened because 0 lines were processed\n\n";
		}
	}
  
	my $percentage_too_short;
	my $percentage_too_long;
	my $percentage_too_many_n;
	if ($count){
		$percentage_too_short  = sprintf ("%.1f",$too_short/$count*100);
		$percentage_too_long   = sprintf ("%.1f",$too_long/$count*100);
		$percentage_too_many_n = sprintf ("%.1f",$too_many_n/$count*100);
	}
	else{
		$percentage_too_short = 'N/A';
		$percentage_too_long = 'N/A';
		$percentage_too_many_n = 'N/A';
	}
  
  
  
  if ($validate){ ### only for paired-end files
      warn "The length threshold of paired-end sequences gets evaluated later on (in the validation step)\n";
  }
  else{           ### Single-end file
      warn "Sequences removed because they became shorter than the length cutoff of $length_cutoff bp:\t$too_short ($percentage_too_short%)\n";
      print REPORT "Sequences removed because they became shorter than the length cutoff of $length_cutoff bp:\t$too_short ($percentage_too_short%)\n";
      if (defined $maxn){
      warn "Sequences removed because they contained more Ns than the cutoff of $maxn:\t$too_many_n ($percentage_too_many_n%)\n";
      print REPORT "Sequences removed because they contained more Ns than the cutoff of $maxn:\t$too_many_n ($percentage_too_many_n%)\n";
      }
      if ($max_length){
        warn "Sequences removed because after trimming they were longer than the maximum length cutoff of $max_length bp:\t$too_long ($percentage_too_long%)\n";
      print REPORT "Sequences removed because after trimming they were longer than the maximum length cutoff of $max_length bp:\t$too_long ($percentage_too_long%)\n";
      }
  }

  if ($rrbs){
      my $percentage_rrbs_trimmed = sprintf ("%.1f",$rrbs_trimmed/$count*100);
      warn "RRBS reads trimmed by additional 2 bp when adapter contamination was detected:\t$rrbs_trimmed ($percentage_rrbs_trimmed%)\n";
      print REPORT "RRBS reads trimmed by additional 2 bp when adapter contamination was detected:\t$rrbs_trimmed ($percentage_rrbs_trimmed%)\n";
  }

  if ($non_directional){
      my $percentage_rrbs_trimmed_at_start = sprintf ("%.1f",$rrbs_trimmed_start/$count*100);
      warn "RRBS reads trimmed by 2 bp at the start when read started with CAA ($CAA) or CGA ($CGA) in total:\t$rrbs_trimmed_start ($percentage_rrbs_trimmed_at_start%)\n";
      print REPORT "RRBS reads trimmed by 2 bp at the start when read started with CAA ($CAA) or CGA ($CGA) in total:\t$rrbs_trimmed_start ($percentage_rrbs_trimmed_at_start%)\n";
  }

  warn "\n";
  print REPORT "\n";

    ### RUNNING FASTQC unless we are dealing with paired-end files
    unless($validate){

        # File renaming requested in Issue #17 (https://github.com/FelixKrueger/TrimGalore/issues/17)
        ### FILE RENAMING
        if ($basename){
            warn "Now renaming the output file $output_filename\n\n";
            my $tempname = "${basename}$1" if ($output_filename =~ /(_trimmed.*)$/);
            warn "ORIGINAL FILE 1: >>$output_filename<<\tRENAMING TO:>>$tempname<<\n";

            rename "${output_dir}$output_filename", "${output_dir}$tempname";
            $output_filename = $tempname;
        }

        if ($fastqc){
            warn "\n  >>> Now running FastQC on the data <<<\n\n";
            # sleep (1);
            if ($fastqc_args){
                system ("$path_to_fastqc $fastqc_args $output_dir$output_filename");
            }
            else{
                system ("$path_to_fastqc $output_dir$output_filename");
            }
        }
    }

    ### VALIDATE PAIRED-END FILES
    if ($validate){
        ### Figure out whether current file counts as read 1 or read 2 of paired-end files

        if ( scalar(@filenames)%2 == 0){ # this is read 1 of a pair
            $file_1 = $output_filename;
            shift @filenames;
            # warn "This is read 1: $file_1\n\n";
        }
        else{                            # this is read 2 of a pair
            $file_2 = $output_filename;
            shift @filenames;
            # warn "This is read 2: $file_2\n\n";
        }

        if ($file_1 and $file_2){
            warn "Validate paired-end files $file_1 and $file_2\n";

            # File renaming requested in Issue #17 (https://github.com/FelixKrueger/TrimGalore/issues/17)
            ### FILE RENAMING
            if ($basename){
                warn "Now renaming the output files\n\n";
                my $tempname_1 = "${basename}_R1$1" if ($file_1 =~ /(_trimmed.*)$/);
                my $tempname_2 = "${basename}_R2$1" if ($file_2 =~ /(_trimmed.*)$/);
                warn "ORIGINAL FILE 1: >>$file_1<<\tRENAMING TO:>>$tempname_1<<\n";
                warn "ORIGINAL FILE 2: >>$file_2<<\tRENAMING TO:>>$tempname_2<<\n";

                rename "${output_dir}${file_1}","${output_dir}$tempname_1";
                rename "${output_dir}${file_2}","${output_dir}$tempname_2";
                $file_1 = $tempname_1;
                $file_2 = $tempname_2;
			
            }
            # sleep (1);

        my ($val_1,$val_2,$un_1,$un_2) = validate_paired_end_files($file_1,$file_2);

        ### RUNNING FASTQC
        if ($fastqc){

            warn "\n  >>> Now running FastQC on the validated data $val_1<<<\n\n";

        if ($fastqc_args){
            system ("$path_to_fastqc $fastqc_args $output_dir$val_1");
        }
        else{
            system ("$path_to_fastqc $output_dir$val_1");
        }

        warn "\n  >>> Now running FastQC on the validated data $val_2<<<\n\n";
        #sleep (3);

        if ($fastqc_args){
        system ("$path_to_fastqc $fastqc_args $output_dir$val_2");
        }
        else{
        system ("$path_to_fastqc $output_dir$val_2");
        }

      }

      warn "Deleting both intermediate output files $file_1 and $file_2\n";
      unlink "$output_dir$file_1";
      unlink "$output_dir$file_2";

      warn "\n",'='x100,"\n\n";
      # sleep (1);

      $file_1 = undef; # setting file_1 and file_2 to undef once validation is completed
      $file_2 = undef;
      }
  }
  close REPORT or warn "Failed to close filehandle REPORT: $!\n";
}

sub hardtrim_to_5prime_end{

    my $filename = shift;
    warn "Input file name:  $filename\n";

    my $in; # filehandle
    my $hardtrim_5; # filehandle

    if ($filename =~ /gz$/){
    open ($in,"$compression_path -d -c $filename |") or die "Couldn't read from file $!";
    }
    else{
    open ($in,$filename) or die "Couldn't read from file $!";
    }

    ### OUTPUT FILE
    my $output_filename = (split (/\//,$filename))[-1];
    # warn "Output file name: $output_filename\n";

    if ($output_filename =~ /\.fastq$/){
    $output_filename =~ s/\.fastq$/.${hardtrim5}bp_5prime.fq/;
    }
    elsif ($output_filename =~ /\.fastq\.gz$/){
    $output_filename =~ s/\.fastq\.gz$/.${hardtrim5}bp_5prime.fq/;
    }
    elsif ($output_filename =~ /\.fq$/){
    $output_filename =~ s/\.fq$/.${hardtrim5}bp_5prime.fq/;
    }
    elsif ($output_filename =~ /\.fq\.gz$/){
    $output_filename =~ s/\.fq\.gz$/.${hardtrim5}bp_5prime.fq/;
    }
    else{
    $output_filename =~ s/$/.${hardtrim5}bp_5prime.fq/;
    }

    if ($gzip or $filename =~ /\.gz$/){
    if ($dont_gzip){
        open ($hardtrim_5,'>',$output_dir.$output_filename) or die "Can't open '$output_filename': $!\n"; # don't need to gzip intermediate file
    }
    else{
        $output_filename .= '.gz';
        open ($hardtrim_5,"| $compression_path -c - > ${output_dir}${output_filename}") or die "Can't write to '$output_filename': $!\n";
    }
    }
    else{
    open ($hardtrim_5,'>',$output_dir.$output_filename) or die "Can't open '$output_filename': $!\n";
    }
    warn "Writing trimmed version (using the first $hardtrim5 bp only) of the input file '$filename' to '$output_filename'\n";

    my $count = 0;

    while (1){
    my $identifier = <$in>;
    my $sequence = <$in>;
    my $identifier2 = <$in>;
    my $quality_score = <$in>;

    last unless ($identifier and $sequence and $identifier2 and $quality_score);
    ++$count;

    $sequence      =~ s/\r|\n//g; # cross-platform line ending trimming
    $quality_score =~ s/\r|\n//g;
           $identifier    =~ s/\r|\n//g;
    $identifier2   =~ s/\r|\n//g;

    my $trimmed_sequence = substr($sequence,0,$hardtrim5);           # from the start to the $hardtrim5
    my $trimmed_quality_score = substr($quality_score,0,$hardtrim5); # from the start to the $hardtrim5

    print {$hardtrim_5} join ("\n",$identifier,$trimmed_sequence,$identifier2,$trimmed_quality_score),"\n";

    }
    close $in or warn "Failed to close filehandle for $filename";
    close $hardtrim_5 or die "Failed to close out-filehandle hardtrim_5: $!";

    warn "\nFinished writing out converted version of the FastQ file $filename ($count sequences in total)\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n";

}

sub hardtrim_to_3prime_end{

    my $filename = shift;
    warn "Input file name:  $filename\n";

    my $in;         # filehandle
    my $hardtrim_3; # filehandle

    if ($filename =~ /gz$/){
    open ($in,"$compression_path -d -c $filename |") or die "Couldn't read from file $!";
    }
    else{
    open ($in,$filename) or die "Couldn't read from file $!";
    }

    ### OUTPUT FILE
    my $output_filename = (split (/\//,$filename))[-1];
    # warn "Output file name: $output_filename\n";

    if ($output_filename =~ /\.fastq$/){
    	$output_filename =~ s/\.fastq$/.${hardtrim3}bp_3prime.fq/;
    }
    elsif ($output_filename =~ /\.fastq\.gz$/){
    	$output_filename =~ s/\.fastq\.gz$/.${hardtrim3}bp_3prime.fq/;
    }
    elsif ($output_filename =~ /\.fq$/){
   		$output_filename =~ s/\.fq$/.${hardtrim3}bp_3prime.fq/;
    }
    elsif ($output_filename =~ /\.fq\.gz$/){
    	$output_filename =~ s/\.fq\.gz$/.${hardtrim3}bp_3prime.fq/;
    }
    else{
    	$output_filename =~ s/$/.${hardtrim3}bp_3prime.fq/;
    }

    if ($gzip or $filename =~ /\.gz$/){
    if ($dont_gzip){
        open ($hardtrim_3,'>',$output_dir.$output_filename) or die "Can't open '$output_filename': $!\n"; # don't need to gzip intermediate file
    }
    else{
        $output_filename .= '.gz';
        open ($hardtrim_3,"| $compression_path -c - > ${output_dir}${output_filename}") or die "Can't write to '$output_filename': $!\n";
    }
    }
    else{
    open ($hardtrim_3,'>',$output_dir.$output_filename) or die "Can't open '$output_filename': $!\n";
    }
    warn "Writing trimmed version (using the last $hardtrim3 bp only) of the input file '$filename' to '$output_filename'\n";

    my $count = 0;

    while (1){
    my $identifier = <$in>;
    my $sequence = <$in>;
    my $identifier2 = <$in>;
    my $quality_score = <$in>;

    last unless ($identifier and $sequence and $identifier2 and $quality_score);
    ++$count;

    $sequence      =~ s/\r|\n//g; # cross-platform line ending trimming
    $quality_score =~ s/\r|\n//g;
    $identifier    =~ s/\r|\n//g;
    $identifier2   =~ s/\r|\n//g;

    my $trimmed_sequence = substr($sequence,-$hardtrim3,$hardtrim3);           # $hardtrim3 bp from the end
    my $trimmed_quality_score = substr($quality_score,-$hardtrim3,$hardtrim3); # $hardtrim3 bp from the end

    print {$hardtrim_3} join ("\n",$identifier,$trimmed_sequence,$identifier2,$trimmed_quality_score),"\n";

    }
    close $in or warn "Failed to close filehandle for $filename";
    close $hardtrim_3 or die "Failed to close out-filehandle hardtrim_3: $!";

    warn "\nFinished writing out converted version of the FastQ file $filename ($count sequences in total)\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n";

}


sub validate_paired_end_files{

    my $file_1 = shift;
    my $file_2 = shift;

    warn "file_1: $file_1, file_2: $file_2\n\n";
    
   

  if ($file_1 =~ /\.gz$/){
      open (IN1,"$compression_path -d -c $output_dir$file_1 |") or die "Couldn't read from file $file_1: $!\n";
  }
  else{
      open (IN1, "$output_dir$file_1") or die "Couldn't read from file $file_1: $!\n";
  }

  if ($file_2 =~ /\.gz$/){
      open (IN2,"$compression_path -d -c $output_dir$file_2 |") or die "Couldn't read from file $file_2: $!\n";
  }
  else{
      open (IN2, "$output_dir$file_2") or die "Couldn't read from file $file_2: $!\n";
  }

  warn "\n>>>>> Now validing the length of the 2 paired-end infiles: $file_1 and $file_2 <<<<<\n";

    my $out_1 = $file_1;
    my $out_2 = $file_2;

    if ($out_1 =~ /gz$/){
        $out_1 =~ s/trimmed\.fq\.gz$/val_1.fq/;
    }
    else{
        $out_1 =~ s/trimmed\.fq$/val_1.fq/;
    }

    if ($out_2 =~ /gz$/){
        $out_2 =~ s/trimmed\.fq\.gz$/val_2.fq/;
    }
    else{
        $out_2 =~ s/trimmed\.fq$/val_2.fq/;
    }

    if ($basename){
        ### FILE RENAMING
        warn "Renaming the output files (AGAIN).\n";
        # warn "ORIGINAL FILE 1: >>$out_1<<\n";
        $out_1 =~ s/_R1_val_1.fq$/_val_1.fq/;
        # warn "ORIGINAL FILE 1: >>$out_1<<\n";

        # warn "ORIGINAL FILE 2: >>$out_2<<\n";
        $out_2 =~ s/_R2_val_2.fq$/_val_2.fq/;
        # warn "ORIGINAL FILE 2: >>$out_2<<\n";
    }

  if ($gzip){
      if ($dont_gzip){
      open (R1,'>',$output_dir.$out_1) or die "Couldn't write to $out_1 $!\n";
      }
      else{
      $out_1 .= '.gz';
      open (R1,"| $compression_path -c - > ${output_dir}${out_1}") or die "Can't write to $out_1: $!\n";
      }
  }
  else{
      open (R1,'>',$output_dir.$out_1) or die "Couldn't write to $out_1 $!\n";
  }

  if ($gzip){
      if ($dont_gzip){
      open (R2,'>',$output_dir.$out_2) or die "Couldn't write to $out_2 $!\n";
    }
      else{
      $out_2 .= '.gz';
      open (R2,"| $compression_path -c - > ${output_dir}${out_2}") or die "Can't write to $out_2: $!\n";
      }
  }
  else{
      open (R2,'>',$output_dir.$out_2) or die "Couldn't write to $out_2 $!\n";
  }

  warn "Writing validated paired-end Read 1 reads to $out_1\n";
  warn "Writing validated paired-end Read 2 reads to $out_2\n\n";

  my $unpaired_1;
  my $unpaired_2;

  if ($retain){

      $unpaired_1 = $file_1;
      $unpaired_2 = $file_2;

      if ($unpaired_1 =~ /gz$/){
      $unpaired_1 =~ s/trimmed\.fq\.gz$/unpaired_1.fq/;
      }
      else{
      $unpaired_1 =~ s/trimmed\.fq$/unpaired_1.fq/;
      }

      if ($unpaired_2 =~ /gz$/){
      $unpaired_2 =~ s/trimmed\.fq\.gz$/unpaired_2.fq/;
      }
      else{
      $unpaired_2 =~ s/trimmed\.fq$/unpaired_2.fq/;
      }

      if ($gzip){
      if ($dont_gzip){
          open (UNPAIRED1,'>',$output_dir.$unpaired_1) or die "Couldn't write to $unpaired_1: $!\n";
      }
      else{
          $unpaired_1 .= '.gz';
          open (UNPAIRED1,"| $compression_path -c - > ${output_dir}${unpaired_1}") or die "Can't write to $unpaired_1: $!\n";
      }
      }
      else{
      open (UNPAIRED1,'>',$output_dir.$unpaired_1) or die "Couldn't write to $unpaired_1: $!\n";
      }

      if ($gzip){
      if ($dont_gzip){
          open (UNPAIRED2,'>',$output_dir.$unpaired_2) or die "Couldn't write to $unpaired_2: $!\n";
      }
      else{
          $unpaired_2 .= '.gz';
          open (UNPAIRED2,"| $compression_path -c - > ${output_dir}${unpaired_2}") or die "Can't write to $unpaired_2: $!\n";
      }
      }
      else{
      open (UNPAIRED2,'>',$output_dir.$unpaired_2) or die "Couldn't write to $unpaired_2: $!\n";
      }

      warn "Writing unpaired read 1 reads to $unpaired_1\n";
      warn "Writing unpaired read 2 reads to $unpaired_2\n\n";
  }

  my $sequence_pairs_removed = 0;
  my $too_many_N_pairs = 0;
  my $read_1_printed = 0;
  my $read_2_printed = 0;

  my $count = 0;

  while (1){
      my $id_1   = <IN1>;
      my $seq_1  = <IN1>;
      my $l3_1   = <IN1>;
      my $qual_1 = <IN1>;

      my $id_2   = <IN2>;
      my $seq_2  = <IN2>;
      my $l3_2   = <IN2>;
      my $qual_2 = <IN2>;

      if ($id_1 and $seq_1 and $l3_1 and $qual_1 and $id_2 and $seq_2 and $l3_2 and $qual_2){
      # all good, got a read from both files
      }
      elsif( !($id_1 and $seq_1 and $l3_1 and $qual_1) and ($id_2 and $seq_2 and $l3_2 and $qual_2)){
      die "Read 1 output is truncated at sequence count: $count, please check your paired-end input files! Terminating...\n\n";
      }
      elsif( !($id_2 and $seq_2 and $l3_2 and $qual_2) and ($id_1 and $seq_1 and $l3_1 and $qual_1)){
      die "Read 2 output is truncated at sequence count: $count, please check your paired-end input files! Terminating...\n\n";
      }
      else{
      last unless ($id_1 and $seq_1 and $l3_1 and $qual_1);
      last unless ($id_2 and $seq_2 and $l3_2 and $qual_2);
      }
      ++$count;

      ## small check if the sequence files appear to be FastQ files
      if ($count == 1){ # performed just once
      if ($id_1 !~ /^\@/ or $l3_1 !~ /^\+/){
          die "Input file doesn't seem to be in FastQ format at sequence $count\n";
      }
      if ($id_2 !~ /^\@/ or $l3_2 !~ /^\+/){
          die "Input file doesn't seem to be in FastQ format at sequence $count\n";
      }
      }

      chomp $seq_1;
      chomp $seq_2;
      chomp $qual_1;
      chomp $qual_2;

      if ($clip_r1){
      if (length $seq_1 > $clip_r1){ # sequences that are already too short won't be trimmed again
          $seq_1 = substr($seq_1,$clip_r1); # starting after the sequences to be trimmed until the end of the sequence
          $qual_1 = substr($qual_1,$clip_r1);
      }
      }
      if ($clip_r2){
      if (length $seq_2 > $clip_r2){ # sequences that are already too short won't be trimmed again
          $seq_2 = substr($seq_2,$clip_r2); # starting after the sequences to be trimmed until the end of the sequence
          $qual_2 = substr($qual_2,$clip_r2);
      }
      }

      if ($three_prime_clip_r1){
      if (length $seq_1 > $three_prime_clip_r1){  # sequences that are already too short won't be clipped again
          $seq_1 = substr($seq_1,0,(length($seq_1) - $three_prime_clip_r1)); # starting after the sequences to be trimmed until the end of the sequence
          $qual_1 = substr($qual_1,0,(length($qual_1) - $three_prime_clip_r1));
      }
      }
      if ($three_prime_clip_r2){
      if (length $seq_2 > $three_prime_clip_r2){  # sequences that are already too short won't be clipped again
          $seq_2 = substr($seq_2,0,(length($seq_2) - $three_prime_clip_r2)); # starting after the sequences to be trimmed until the end of the sequence
          $qual_2 = substr($qual_2,0,(length($qual_2) - $three_prime_clip_r2));
      }
      }

      if (defined $maxn){

      # Read 1
      my $n_count = Ncounter($seq_1);
      # warn "Checking Read 1 for Ns: Found $n_count\n";
      if ($n_count > $maxn){
          ++$too_many_N_pairs;
          ++$sequence_pairs_removed;
          next; # bailing straight away
      }

      # Read 2
      $n_count = Ncounter($seq_2);
      # warn "Checking Read 2 for Ns: Found $n_count\n";
      if ($n_count > $maxn){
          ++$too_many_N_pairs;
          ++$sequence_pairs_removed;
          next;
      }
      }

      ### making sure that the reads do have a sensible length
      if ( (length($seq_1) < $length_cutoff) or (length($seq_2) < $length_cutoff) ){
      ++$sequence_pairs_removed;
      if ($retain){ # writing out single-end reads if they are longer than the cutoff

          if ( length($seq_1) >= $length_read_1){ # read 1 is long enough
          print UNPAIRED1 $id_1;
          print UNPAIRED1 "$seq_1\n";
          print UNPAIRED1 $l3_1;
          print UNPAIRED1 "$qual_1\n";
          ++$read_1_printed;
          }

          if ( length($seq_2) >= $length_read_2){ # read 2 is long enough
          print UNPAIRED2 $id_2;
          print UNPAIRED2 "$seq_2\n";
          print UNPAIRED2 $l3_2;
          print UNPAIRED2 "$qual_2\n";
          ++$read_2_printed;
          }

      }
      }
      else{
      print R1 $id_1;
      print R1 "$seq_1\n";
      print R1 $l3_1;
      print R1 "$qual_1\n";

      print R2 $id_2;
      print R2 "$seq_2\n";
      print R2 $l3_2;
      print R2 "$qual_2\n";
      }

  }


  my $percentage;
  my $percentage_Ns;

  if ($count){
    $percentage = sprintf("%.2f",$sequence_pairs_removed/$count*100);
    $percentage_Ns = sprintf("%.2f",$too_many_N_pairs/$count*100);
  }
  else{
      $percentage = 'N/A';
      $percentage_Ns = 'N/A';
  }

  warn "Total number of sequences analysed: $count\n\n";
  warn "Number of sequence pairs removed because at least one read was shorter than the length cutoff ($length_cutoff bp): $sequence_pairs_removed ($percentage%)\n";
  if (defined $maxn){
      warn "Number of sequence pairs removed because at least one read contained more N(s) than the specified limit of $maxn: $too_many_N_pairs ($percentage_Ns%)\n";
      print REPORT "Number of sequence pairs removed because at least one read contained more N(s) than the specified limit of $maxn: $too_many_N_pairs ($percentage_Ns%)\n";
  }

  print REPORT "Total number of sequences analysed for the sequence pair length validation: $count\n\n";
  print REPORT "Number of sequence pairs removed because at least one read was shorter than the length cutoff ($length_cutoff bp): $sequence_pairs_removed ($percentage%)\n";

  if ($keep){
      warn "Number of unpaired read 1 reads printed: $read_1_printed\n";
      warn "Number of unpaired read 2 reads printed: $read_2_printed\n";
  }

  close R1 or die $!;
  close R2 or die $!;

  if ($retain){
      close UNPAIRED1 or die $!;
      close UNPAIRED2 or die $!;
  }

  warn "\n";
  if ($retain){
      return ($out_1,$out_2,$unpaired_1,$unpaired_2);
  }
  else{
      return ($out_1,$out_2);
  }
}


sub file_sanity_check{

  my $file = shift;
  if ($file =~ /gz$/){
      open (SANITY,"$compression_path -d -c $file |") or die "Failed to read from file '$file' to perform sanity check: $!\n";
  }
  else{
      open (SANITY,$file) or die "Failed to read from file '$file' to perform sanity check: $!\n";
  }

  # just processing a single FastQ entry
  my $id    = <SANITY>;
  my $seq   = <SANITY>;
  my $three = <SANITY>;
  my $qual  = <SANITY>;

  unless ($id and $seq and $three and $qual){
      die "Input file '$file' seems to be completely empty. Consider respecifying!\n\n";
  }

  chomp $seq;

  # testing if the file is a colorspace file in which case we bail
  if ($seq =~ /\d+/){
      die "File seems to be in SOLiD colorspace format which is not supported by Trim Galore (sequence is: '$seq')! Please use Cutadapt on colorspace files separately and check its documentation!\n\n";
  }

  close SANITY;

}



### ADAPTER AUTO-DETECTION

sub autodetect_adapter_type{
  warn "\n\nAUTO-DETECTING ADAPTER TYPE\n===========================\n";
  warn "Attempting to auto-detect adapter type from the first 1 million sequences of the first file (>> $ARGV[0] <<)\n\n";

  if ($ARGV[0] =~ /gz$/){
    open (AUTODETECT,"$compression_path -d -c $ARGV[0] |") or die "Failed to read from file $ARGV[0]\n";
  }
  else{
    open (AUTODETECT,$ARGV[0]) or die "Failed to read from file $ARGV[0]\n";
  }

  my %adapters;

  $adapters{'Illumina'} -> {seq}  = 'AGATCGGAAGAGC';
  $adapters{'Illumina'} -> {count}= 0;
  $adapters{'Illumina'} -> {name}= 'Illumina TruSeq, Sanger iPCR; auto-detected';

  $adapters{'Nextera'}  -> {seq}  = 'CTGTCTCTTATA';
  $adapters{'Nextera'}  -> {count}= 0;
  $adapters{'Nextera'}  -> {name}= 'Nextera Transposase sequence; auto-detected';

  $adapters{'smallRNA'} -> {seq}  = 'TGGAATTCTCGG';
  $adapters{'smallRNA'} -> {count}= 0;
  $adapters{'smallRNA'} -> {name}= 'Illumina small RNA adapter; auto-detected';


  # we will read the first 1 million sequences, or until the end of the file whatever comes first, and then use the adapter that for trimming which was found to occcur most often
  my $count = 0;
  while (1){

    my $line1 = <AUTODETECT>;
    my $line2 = <AUTODETECT>;
    my $line3 = <AUTODETECT>;
    my $line4 = <AUTODETECT>;
    last unless ($line4);
    $count++;
    last if ($count == 1000000);

    chomp $line2;
    $adapters{'Illumina'}->{count}++ unless (index($line2,'AGATCGGAAGAGC')== -1);
    $adapters{'Nextera'} ->{count}++ unless (index($line2,'CTGTCTCTTATA') == -1);
    $adapters{'smallRNA'}->{count}++ unless (index($line2,'TGGAATTCTCGG') == -1);

  }

  my $highest;
  my $third;
  my $second;
  my $seq;
  my $adapter_name;
  my $report_message;

  	warn "Found perfect matches for the following adapter sequences:\nAdapter type\tCount\tSequence\tSequences analysed\tPercentage\n";
  	foreach my $adapter (sort {$adapters{$b}->{count}<=>$adapters{$a}->{count}} keys %adapters){

    	my $percentage = sprintf("%.2f",$adapters{$adapter}->{count}/$count*100);

    	warn "$adapter\t$adapters{$adapter}->{count}\t$adapters{$adapter}->{seq}\t$count\t$percentage\n";

	    unless (defined $highest){
		    $highest = $adapter;
		    $seq = $adapters{$adapter}->{seq};
	      	$adapter_name = $adapters{$adapter}->{name};
	      	next;
	    }
	    unless (defined $second){
	      	$second = $adapter;
	      	next;
	    }
 		unless (defined $third){
	      	$third = $adapter;
	      	next;
	    }
  }

	
  	if ($adapters{$highest}->{count} == $adapters{$second}->{count} and $adapters{$highest}->{count} == $adapters{$third}->{count}){
    	warn "Unable to auto-detect most prominent adapter from the first specified file (count $highest: $adapters{$highest}->{count}, count $second: $adapters{$second}->{count}, count $third: $adapters{$third}->{count})\n";
    	$report_message .= "Unable to auto-detect most prominent adapter from the first specified file (count $highest: $adapters{$highest}->{count}, count $second: $adapters{$second}->{count}, count $third: $adapters{$third}->{count})\n";

  		if (defined $consider_already_trimmed){
  			if ($adapters{$highest}->{count} <= $consider_already_trimmed ){
  				warn "No auto-detected adapter sequence exceeded the user-specified 'already adapter-trimmed' limit ($consider_already_trimmed). Setting adapter sequence to -a X\n";
  				$report_message .= "No auto-detected adapter sequence exceeded the user-specified 'already adapter-trimmed' limit ($consider_already_trimmed). Setting adapter sequence to -a X\n";
  				$adapter_name = 'No adapter trimming [suppressed by user]';
  				$seq = 'X'; 
			}
			else{
  				warn "Defaulting to Illumina universal adapter ( AGATCGGAAGAGC ). Specify -a SEQUENCE to avoid this behavior).\n\n";
  				$report_message .= "Defaulting to Illumina universal adapter ( AGATCGGAAGAGC ). Specify -a SEQUENCE to avoid this behavior).\n";
  				$adapter_name = 'Illumina TruSeq, Sanger iPCR; default (inconclusive auto-detection)';
  				$seq = 'AGATCGGAAGAGC';  
    		}
	  	}
  		else{
  			warn "Defaulting to Illumina universal adapter ( AGATCGGAAGAGC ). Specify -a SEQUENCE to avoid this behavior).\n\n";
  			$report_message .= "Defaulting to Illumina universal adapter ( AGATCGGAAGAGC ). Specify -a SEQUENCE to avoid this behavior).\n";
  			$adapter_name = 'Illumina TruSeq, Sanger iPCR; default (inconclusive auto-detection)';
  			$seq = 'AGATCGGAAGAGC';  
    	}
    }
    elsif ($adapters{$highest}->{count} == $adapters{$second}->{count} ){
		warn "Unable to auto-detect most prominent adapter from the first specified file (count $highest: $adapters{$highest}->{count}, count $second: $adapters{$second}->{count}, count $third: $adapters{$third}->{count})\n";
    	$report_message .= "Unable to auto-detect most prominent adapter from the first specified file (count $highest: $adapters{$highest}->{count}, count $second: $adapters{$second}->{count}, count $third: $adapters{$third}->{count})\n";
    
    	if (defined $consider_already_trimmed){
  			if ($adapters{$highest}->{count} <= $consider_already_trimmed ){
  				warn "The highest auto-detected adapter sequence did not exceed the user-specified 'already adapter-trimmed' limit ($consider_already_trimmed). Setting adapter sequence to -a X\n";
  				$report_message .= "The highest auto-detected adapter sequence did not exceed the user-specified 'already adapter-trimmed' limit ($consider_already_trimmed). Setting adapter sequence to -a X\n";
  				$adapter_name = 'No adapter trimming [suppressed by user]';
  				$seq = 'X'; 
			}
			else{
				# If one of the highest contaminants was the Illumina adapter, we set that one and print a warning		
		    	if ( ($highest eq 'Illumina') or ($second eq 'Illumina')) {
		    		warn "Defaulting to Illumina universal adapter ( AGATCGGAAGAGC ). Specify -a SEQUENCE to avoid this behavior).\n\n";
		      		$report_message .= "Defaulting to Illumina universal adapter ( AGATCGGAAGAGC ). Specify -a SEQUENCE to avoid this behavior.\n";
		      		$adapter_name = 'Illumina TruSeq, Sanger iPCR; default (inconclusive auto-detection)';
		      		$seq = 'AGATCGGAAGAGC';
		    	}
		    	else{
		    		warn "Defaulting to Nextera adapter as next best option ( CTGTCTCTTATA ). Specify -a SEQUENCE to avoid this behavior).\n";
		      		$report_message .= "Defaulting to Nextera adapter as next best option ( CTGTCTCTTATA ). Specify -a SEQUENCE to avoid this behavior.\n";
		      		$adapter_name = 'Nextera; (assigned because of inconclusive auto-detection)';
		      		$seq = 'CTGTCTCTTATA';	
		      	}
		    }
		}
		else{
			# If one of the highest contaminants was the Illumina adapter, we set that one and print a warning		
	    	if ( ($highest eq 'Illumina') or ($second eq 'Illumina')) {
	    		warn "Defaulting to Illumina universal adapter ( AGATCGGAAGAGC ). Specify -a SEQUENCE to avoid this behavior).\n\n";
	      		$report_message .= "Defaulting to Illumina universal adapter ( AGATCGGAAGAGC ). Specify -a SEQUENCE to avoid this behavior.\n";
	      		$adapter_name = 'Illumina TruSeq, Sanger iPCR; default (inconclusive auto-detection)';
	      		$seq = 'AGATCGGAAGAGC';
	    	}
	    	else{
	    		warn "Defaulting to Nextera adapter as next best option ( CTGTCTCTTATA ). Specify -a SEQUENCE to avoid this behavior).\n";
	      		$report_message .= "Defaulting to Nextera adapter as next best option ( CTGTCTCTTATA ). Specify -a SEQUENCE to avoid this behavior.\n";
	      		$adapter_name = 'Nextera; (assigned because of inconclusive auto-detection)';
	      		$seq = 'CTGTCTCTTATA';	
	      	}
	    }
  	}
  	else{
  		if (defined $consider_already_trimmed){
  			if ($adapters{$highest}->{count} <= $consider_already_trimmed ){
  				warn "The highest auto-detected adapter sequence did not exceed the user-specified 'already adapter-trimmed' limit ($consider_already_trimmed). Setting adapter sequence to -a X\n";
  				$report_message .= "The highest auto-detected adapter sequence did not exceed the user-specified 'already adapter-trimmed' limit ($consider_already_trimmed). Setting adapter sequence to -a X\n";
  				$adapter_name = 'No adapter trimming [suppressed by user]';
  				$seq = 'X'; 
			}
			else{
				# using the highest occurrence as adapter to look out for
    			$report_message .= "Using $highest adapter for trimming (count: $adapters{$highest}->{count}). Second best hit was $second (count: $adapters{$second}->{count})\n";
    			warn "Using $highest adapter for trimming (count: $adapters{$highest}->{count}). Second best hit was $second (count: $adapters{$second}->{count})\n\n";
  			}
  		}
  		else{
			# using the highest occurrence as adapter to look out for
    		$report_message .= "Using $highest adapter for trimming (count: $adapters{$highest}->{count}). Second best hit was $second (count: $adapters{$second}->{count})\n";
    		warn "Using $highest adapter for trimming (count: $adapters{$highest}->{count}). Second best hit was $second (count: $adapters{$second}->{count})\n\n";
  		}
  	}

  close AUTODETECT;

  return ($seq,$adapter_name,$report_message);

}

sub autodetect_polyA_type{

    warn "\n\nAUTO-DETECTING POLY-A TYPE\n===========================\n";
    warn "Attempting to auto-detect PolyA type from the first 1 million sequences of the first file (>> $ARGV[0] <<)\n\n";

    if ($ARGV[0] =~ /gz$/){
    open (AUTODETECT,"$compression_path -d -c $ARGV[0] |") or die "Failed to read from file $ARGV[0]\n";
    }
    else{
    open (AUTODETECT,$ARGV[0]) or die "Failed to read from file $ARGV[0]\n";
    }

  my %adapters;

    $adapters{'PolyA'} -> {seq}  = 'AAAAAAAAAA';
    $adapters{'PolyA'} -> {count}= 0;
    $adapters{'PolyA'} -> {name}= 'Poly-A Read 1; auto-detected';

    $adapters{'PolyT'}  -> {seq}  = 'TTTTTTTTTT';
    $adapters{'PolyT'}  -> {count}= 0;
    $adapters{'PolyT'}  -> {name}= 'Poly-T Read 1; auto-detected';


    # we will read the first 1 million sequences, or until the end of the file whatever comes first, and then use the adapter that for trimming which was found to occcur most often
    my $count = 0;
    while (1){

    my $line1 = <AUTODETECT>;
    my $line2 = <AUTODETECT>;
    my $line3 = <AUTODETECT>;
    my $line4 = <AUTODETECT>;
    last unless ($line4);
    $count++;
    last if ($count == 1000000);

    chomp $line2;
    $adapters{'PolyA'}->{count}++ unless (index($line2,'AAAAAAAAAA')== -1);
    $adapters{'PolyT'} ->{count}++ unless (index($line2,'TTTTTTTTTT') == -1);

    }

    my $highest;
    my $second;
    my $seq;
    my $adapter_name;

    warn "Found perfect matches for the following mono-polymer sequences:\nPoly-nucleotide type\tCount\tSequence\tSequences analysed\tPercentage\n";
    foreach my $adapter (sort {$adapters{$b}->{count}<=>$adapters{$a}->{count}} keys %adapters){

    my $percentage = sprintf("%.2f",$adapters{$adapter}->{count}/$count*100);

    warn "$adapter\t$adapters{$adapter}->{count}\t$adapters{$adapter}->{seq}\t$count\t$percentage\n";

    unless (defined $highest){
        $highest = $adapter;
        $seq = $adapters{$adapter}->{seq};
        $adapter_name = $adapters{$adapter}->{name};
        next;
    }
    unless (defined $second){
        $second = $adapter;
    }
    }


    # using the highest occurrence as adapter to look out for
    if ($adapters{$highest}->{count} == $adapters{$second}->{count}){
    warn "Unable to auto-detect most prominent mono-polymer from the first specified file (count $highest: $adapters{$highest}->{count}, count $second: $adapters{$second}->{count})\n";

    if ($adapters{$highest}->{count} == 0){
        warn "Defaulting to Poly-A. Specify -a SEQUENCE to avoid this behavior).\n\n";
        $adapter_name = 'Poly-A (inconclusive auto-detection)';
        $seq = extend_adapter_sequence ('A',20);
    }
    else{
        warn "Using $highest poly-monomer for trimming (count: $adapters{$highest}->{count}). Second best hit was $second (count: $adapters{$second}->{count})\n\n";
    }
    }
    else{
    warn "Using $highest Polymer for trimming (count: $adapters{$highest}->{count}). Second best hit was $second (count: $adapters{$second}->{count})\n\n";
    }

    close AUTODETECT;

    return ($seq,$adapter_name);

}


###########################################################################

sub process_commandline{
  my $help;
  my $quality;
  my $adapter;
  my $adapter2;
  my $stringency;
  my $report;
  my $version;
  my $rrbs;
  my $length_cutoff;
  my $keep;
  my $fastqc;
  my $non_directional;
  my $phred33;
  my $phred64;
  my $fastqc_args;
  my $trim;
  my $gzip;
  my $validate;
  my $retain;
  my $length_read_1;
  my $length_read_2;
  my $error_rate;
  my $output_dir;
  my $no_report_file;
  my $suppress_warn;
  my $dont_gzip;
  my $clip_r1;
  my $clip_r2;
  my $three_prime_clip_r1;
  my $three_prime_clip_r2;
  my $nextera;
  my $small_rna;
  my $illumina;
  my $path_to_cutadapt;
  my $max_length;
  my $maxn;
    my $trimn;
    my $hardtrim5;
    my $hardtrim3;
    my $clock;
    my $polyA;
    my $nextseq;
    my $basename;
    my $cores;
    my $compression_path;
    my $consider_already_trimmed;

    my $command_line = GetOptions ('help|man' => \$help,
                 'q|quality=i' => \$quality,
                 'a|adapter=s' => \$adapter,
                 'a2|adapter2=s' => \$adapter2,
                 'report' => \$report,
                 'version' => \$version,
                 'stringency=i' => \$stringency,
                 'fastqc' => \$fastqc,
                 'RRBS' => \$rrbs,
                 'keep' => \$keep,
                 'length=i' => \$length_cutoff,
                 'non_directional' => \$non_directional,
                 'phred33' => \$phred33,
                 'phred64' => \$phred64,
                 'fastqc_args=s' => \$fastqc_args,
                 'trim1' => \$trim,
                 'gzip' => \$gzip,
                 'paired_end' => \$validate,
                 'retain_unpaired' => \$retain,
                 'length_1|r1=i' => \$length_read_1,
                 'length_2|r2=i' => \$length_read_2,
                 'e|error_rate=s' => \$error_rate,
                 'o|output_dir=s' => \$output_dir,
                 'no_report_file' => \$no_report_file,
                 'suppress_warn' => \$suppress_warn,
                 'dont_gzip' => \$dont_gzip,
                 'clip_R1=i' => \$clip_r1,
                 'clip_R2=i' => \$clip_r2,
                 'three_prime_clip_R1=i' => \$three_prime_clip_r1,
                 'three_prime_clip_R2=i' => \$three_prime_clip_r2,
                 'illumina' => \$illumina,
                 'nextera' => \$nextera,
                 'small_rna' => \$small_rna,
                 'path_to_cutadapt=s' => \$path_to_cutadapt,
                 'max_length=i' => \$max_length,
                 'max_n=i'      => \$maxn,
                 'trim-n'      => \$trimn,
                 'hardtrim5=i'      => \$hardtrim5,
                 'hardtrim3=i'      => \$hardtrim3,
                 'clock|casio|breitling' => \$clock,
                 'polyA' => \$polyA,
                 '2colour|nextseq=i' => \$nextseq,
                 'basename=s' => \$basename,
                 'j|cores=i' => \$cores,
                 'consider_already_trimmed=i' => \$consider_already_trimmed,
      );

	### EXIT ON ERROR if there were errors with any of the supplied options
	unless ($command_line){
		die "Please respecify command line options\n";
	}

	### HELPFILE
	if ($help){
		print_helpfile();
		exit;
	}





  if ($version){
    print << "VERSION";

                        Quality-/Adapter-/RRBS-/Speciality-Trimming
                                [powered by Cutadapt]
                                  version $trimmer_version

                               Last update: 24 09 2019

VERSION
    exit;
  }

    # testing whether the filenames contain white space. This can only ever be the case if passed within "quotes"
    foreach my $filename (@ARGV){
        if ($filename =~ /\s+/){
            die "\n[FATAL ERROR]: Input file names ('$filename') supplied with whitespace(s). Please move to directory containing the input file(s),
               and/or avoid using whitespace(s) at all costs (e.g. consider using '_' instead), and try again.\n\n";
        }
    }

	# NUMBER OF CORES
	if (defined $cores){
		if ($cores < 1){
			die "Please a use a positive integer for the number of cores to be used, and re-specify!\n\n";
		}
		elsif($cores == 1){
			warn "Proceeding with single-core trimming (user-defined)\n";
		}
		elsif($cores >= 8){
			warn "Using an excessive number of cores has a diminishing return! It is recommended not to exceed 8 cores per trimming process (you asked for $cores cores). Please consider re-specifying\n"; sleep(2);
		}
	}
	else {
		warn "Multicore support not enabled. Proceeding with single-core trimming.\n";
		$compression_path = "gzip";
		$cores = 1;
	}
	
	
	# Before we start let's have quick look if Cutadapt seems to be working with the path information provided
	# To change the path to Cutadapt use --path_to_cutadapt /full/path/to/the/Cutadapt/executable

	if(defined $path_to_cutadapt){
		warn "Path to Cutadapt set as: '$path_to_cutadapt' (user defined)\n";
		# we'll simply use this
	}
	else{
		$path_to_cutadapt = 'cutadapt'; # default, assuming it is in the PATH
		warn "Path to Cutadapt set as: '$path_to_cutadapt' (default)\n";
	}
	
	
	my $return = system "$path_to_cutadapt --version 2>&1 > /dev/null ";
	if ($return == 0){
		warn "Cutadapt seems to be working fine (tested command '$path_to_cutadapt --version')\n";
		$cutadapt_version = `$path_to_cutadapt --version`;
		chomp $cutadapt_version;	
		warn "Cutadapt version: $cutadapt_version\n";
	}
	else{
		die "Failed to execute Cutadapt porperly. Please install Cutadapt first and make sure it is in the PATH, or specify the path to the Cutadapt executable using --path_to_cutadapt /path/to/cutadapt\n\n";
	}




	# We only need to test for pigz if the user asked for multi-core processing
	if ($cores > 1){
	
		## Check Python  Version
		# warn "Let's also find out the Python version used. $path_to_cutadapt\n";
		my $location_of_cutadapt = `which $path_to_cutadapt`;
		#warn "Location is: $location_of_cutadapt\n";
		
		# Reading the first line of the cutadapt executable, since this tends to contain the python version it is using
		open (my $first_line,$location_of_cutadapt) or die "Failed to read the first line of the Cutadapt executable: $!";
		my $shebang = <$first_line>;
		chomp $shebang;
		# warn "This is the first line:\n>>>$shebang<<<\n";
		close $first_line;
		
		# the shebang line seems to contain a path to Python
		if ($shebang =~ /python/i){
			if ($shebang =~ /\#!/){
				# warn "Found a shebangline: >>>$_<<<\n";
				$shebang =~ s/\#!//; 
				# warn "Truncated shebangline: >>>$_<<<\n";
			}
	
			my $python_return = `$shebang --version 2>&1`;
			chomp $python_return;
			# warn "Python return: $python_return\n";
		
			if ($python_return =~ /Python 3.*/){
				warn "Cutadapt seems to be using Python 3! Proceeding with multi-core enabled Cutadapt using $cores cores\n";
			}
			elsif ($python_return =~ /Python 2.*/){
				warn "Python 2 found, multi-core not supported. Proceeding with Cutadapt in single-core mode\n";
				$cores = 1;
			}
			else{
				die "No Python detected. Python required to run Cutadapt!\n\n";
			}
			
			$python_version = $python_return;
			$python_version =~ s/^Python //;
		}
		else{
			# the shebang line doesn't seem to contain a path to Python. Instead, someone edited the Cutadapt executable to look differently.
			# An example for this is the latest version of Miniconda:
			### #!/bin/sh
			### '''exec' /long/path/to/conda/envs/deepsv/bin/python "$0" "$@"
			### ' '''
			### # -*- coding: utf-8 -*-
			### ...
			
			### interestingly, Anacondo does not seem to do this
			warn "Could not detect version of Python used by Cutadapt from the first line of Cutadapt (but found this: >>>$shebang<<<)\n";
			$python_version = 'could not detect';
			warn "Letting the (modified) Cutadapt deal with the Python version instead\n";
		}
		
		### only proceeding if $cores is still > 1, i.e. if Python 3 was found
		if ($cores > 1){
			
			### Test if pigz is installed
			my $pigz_return = system ("pigz --version 2> /dev/null");
			# warn "PIGZ returned: $pigz_return\n";
			if ($pigz_return == 0) {
				warn "Parallel gzip (pigz) detected. Proceeding with multicore (de)compression using $cores cores\n\n";
				$compression_path = "pigz -p $cores";
			} 
			else {
				warn "Proceeding with 'gzip' for compression. PLEASE NOTE: Using multi-cores for trimming with 'gzip' only has only very limited effect! (see here: https://github.com/FelixKrueger/TrimGalore/issues/16#issuecomment-458557103)\n";
				warn "To increase performance, please install 'pigz' and run again\n\n";
				$compression_path = "gzip";
			}
		} 
	}
	else{
		warn "single-core operation.\n"
	}
	unless (defined $compression_path){
		$compression_path = "gzip"; # fall-back option
	}

	### SUPRESS WARNINGS
	if (defined $suppress_warn){
		$DOWARN = 0;
	}

	### QUALITY SCORES
	my $phred_encoding;
	if ($phred33){
		if ($phred64){
			die "Please specify only a single quality encoding type (--phred33 or --phred64)\n\n";
		}
		$phred_encoding = 33;
	}
	elsif ($phred64){
		$phred_encoding = 64;
	}
  unless ($phred33 or $phred64){
      unless (defined $hardtrim5 or $hardtrim3 or $clock){   # we don't need warnings if we simply hard-trim or Clock-trim a file
      warn "No quality encoding type selected. Assuming that the data provided uses Sanger encoded Phred scores (default)\n\n";
      }
      $phred_encoding = 33;
  }

      ### ILLUMINA 2-COLOUR CHEMISTRY SPEICIFC HIGH QUALITY G-TRIMMING
      if (defined $nextseq){
          if (defined $quality){
              die "The options '-quality INT' and '--nextseq INT' are mutually exclusive. Please decide which trimming mode you would like to apply!\n\n";
          }
          #	warn "OK, let's deal with 2-colour issues\n\n";
        unless ( ($nextseq > 0) and $nextseq < 200){
            die "Please select a sensible value for 2-colour specific trimming (currently allowed range is between 1 and 200 Gs). Please respecify!\n";
        }
        $nextseq = "--nextseq-trim=$nextseq";
      }
      else{
          $nextseq = '';
      }

	### NON-DIRECTIONAL RRBS
	if ($non_directional){
		unless ($rrbs){
			die "Option '--non_directional' requires '--rrbs' to be specified as well. Please re-specify!\n";
		}
	}
	else{
		$non_directional = 0;
	}

  if ($fastqc_args){
    $fastqc = 1; # specifying fastqc extra arguments automatically means that FastQC will be executed
  }
  else{
    $fastqc_args = 0;
  }

  ### CUSTOM ERROR RATE
  if (defined $error_rate){
    # make sure that the error rate is between 0 and 1
    unless ($error_rate >= 0 and $error_rate <= 1){
      die "Please specify an error rate between 0 and 1 (the default is 0.1)\n";
    }
  }
  else{
    $error_rate = 0.1; # (default)
  }

 
  if ($nextera and $small_rna or $nextera and $illumina or $illumina and $small_rna ){
    die "You can't use several different adapter types at the same time. Make your choice or consider using -a and -a2\n\n";
  }

  ### ENSURE USERS ARE USING THE POLY-A AUTODETECTION, OR SPECIFY SEQUENCES FOR BOTH -a AND -a2
  if ($polyA){
      if (defined $adapter){
      if ($validate){# paired-end
          unless (defined $adapter2){
          die "Please use either the PolyA auto-detection (defaults to -a \"A{20}\" -a2 \"T{150}\" (or the other way round)), or specify both -a and -a2. Now try again...\n\n";
          }
      }
      }
      if (defined $adapter2){
      if ($validate){# paired-end
          unless (defined $adapter){
          die "Please use either the PolyA auto-detection (defaults to -a \"A{20}\" -a2 \"T{150}\" (or the other way round)), or specify both -a and -a2. Now try again...\n\n";
          }
      }
      }
  }


  if (defined $adapter){

      # The adapter may be given as a single base that occurs a number of times
      # in the form BASE{number of times}, e.g. "-a A{10}"
      if ($adapter =~ /^([ACTGN]){(\d+)}$/){
      # warn "Base: $1\n# repeats: $2\n";


      my $tmp_adapter = extend_adapter_sequence(uc$1,$2);
      warn "Adapter sequence given as >$adapter< expanded to: >$tmp_adapter<\n";
      $adapter = $tmp_adapter;
      }
      else{
      unless ($adapter =~ /^[ACTGNXactgnx]+$/){
          die "Adapter sequence must contain DNA characters only (A,C,T,G or N)!\n";
      }
      }
      $adapter = uc$adapter;

      if ($illumina){
      die "You can't supply an adapter sequence AND use the Illumina universal adapter sequence. Make your choice.\n\n";
      }
      if ($nextera){
      die "You can't supply an adapter sequence AND use the Nextera transposase adapter sequence. Make your choice.\n\n";
      }
      if ($small_rna){
      die "You can't supply an adapter sequence AND use the Illumina small RNA adapter sequence. Make your choice.\n\n";
      }
  }

  if (defined $adapter2){
      unless ($validate){
      die "An optional adapter for read 2 of paired-end files requires '--paired' to be specified as well! Please re-specify\n";
      }

      # The adapter may be given as a single base that occurs a number of times
      # in the form BASE{number of times}, e.g. "-a2 A{10}"
      if ($adapter2 =~ /^([ACTGN]){(\d+)}$/){
      # warn "Base: $1\n# repeats: $2\n";
      my $tmp_adapter2 = extend_adapter_sequence(uc$1,$2);

      warn "Adapter2 sequence given as >$adapter2< expanded to: >$tmp_adapter2<\n";
      $adapter2 = $tmp_adapter2;
      }
      else{
      unless ($adapter2 =~ /^[ACTGNactgn]+$/){
          die "Optional adapter 2 sequence must contain DNA characters only (A,C,T,G or N)!\n";
      }
      }
      $adapter2 = uc$adapter2;
  }

  ### LENGTH CUTOFF
  # this gets set right at the start after the adapter auto-detection has been concluded

  ### MAXIMUM LENGTH CUTOFF - this is intended for smallRNA-libraries to remove sequences that are longer than a certain cutoff and thus problably not small RNA species
  if (defined $max_length){
    if ($validate){
      die "Maximum length filtering works currently only in single-end mode (which is more sensible for smallRNA-sequencing anyway...)\n\n";
    }
    warn "Maximum length cutoff set to >> $max_length bp <<; sequences longer than this threshold will be removed (only advised for smallRNA-trimming!)\n\n";
  }
  else{
    $max_length = 0;
  }

  ### files are supposed to be paired-end files
  if ($validate){

    # making sure that an even number of reads has been supplied
    unless ((scalar@ARGV)%2 == 0){
      die "Please provide an even number of input files for paired-end FastQ trimming! Aborting ...\n";
    }

    ### Ensuring pairs of R1 and R2 are not the very same file
    my $index = 0;
    while ($index <= $#ARGV){
        # warn "File 1: $ARGV[$index]\n";
        # warn "File 2: $ARGV[$index+1]\n~~~~~~~~~~\n\n"; sleep(1);
        if ($ARGV[$index] eq $ARGV[$index+1]){
            die "[FATAL:] Read 1 ($ARGV[$index]) and Read 2 ($ARGV[$index+1]) files appear to be the very same file. This probably happened inadvertently, so please re-specify!\nExiting...\n\n";
        }
        $index += 2;
    }

    ## CUTOFF FOR VALIDATED READ-PAIRS
    if (defined $length_read_1 or defined $length_read_2){

      unless ($retain){
    die "Please specify --keep_unpaired to alter the unpaired single-end read length cut off(s)\n\n";
      }

      if (defined $length_read_1){
    unless ($length_read_1 >= 15 and $length_read_1 <= 100){
      die "Please select a sensible cutoff for when a read pair should be filtered out due to short length (allowed range: 15-100 bp)\n\n";
    }
    unless ($length_read_1 > $length_cutoff){
      die "The single-end unpaired read length needs to be longer than the paired-end cut-off value ($length_cutoff bp)\n\n";
    }
      }

      if (defined $length_read_2){
    unless ($length_read_2 >= 15 and $length_read_2 <= 100){
      die "Please select a sensible cutoff for when a read pair should be filtered out due to short length (allowed range: 15-100 bp)\n\n";
    }
    unless ($length_read_2 > $length_cutoff){
      die "The single-end unpaired read length needs to be longer than the paired-end cut-off value ($length_cutoff bp)\n\n";
    }
      }
    }

    if ($retain){
      $length_read_1 = 35 unless (defined $length_read_1);
      $length_read_2 = 35 unless (defined $length_read_2);
    }
  }


    unless ($no_report_file){
        $no_report_file = 0;
    }

    ### PARENT DIRECTORY
    my $parent_dir = getcwd();
    unless ($parent_dir =~ /\/$/){
        $parent_dir =~ s/$/\//;
    }

    ### OUTPUT DIR PATH
    if (defined $output_dir){

        if ($output_dir =~ /\s+/){
            die "\n[FATAL OPTION]: Output directory name (>>$output_dir<<) contained whitespace(s). Please replace whitespace(s) with '_' and try again.\n\n";
        }

        unless ($output_dir eq ''){
            unless ($output_dir =~ /\/$/){
                $output_dir =~ s/$/\//;
            }

            if (chdir $output_dir){
                $output_dir = getcwd(); #  making the path absolute
                unless ($output_dir =~ /\/$/){
                    $output_dir =~ s/$/\//;
                }
            }
            else{
                mkdir $output_dir or die "Unable to create directory $output_dir $!\n";
                warn "Output directory $output_dir doesn't exist, creating it for you...\n\n"; sleep(1);
                chdir $output_dir or die "Failed to move to $output_dir\n";
                $output_dir = getcwd(); #  making the path absolute
                unless ($output_dir =~ /\/$/){
                        $output_dir =~ s/$/\//;
                }
            }
            warn "Output will be written into the directory: $output_dir\n";
        }
    }
    else{
        $output_dir = '';
    }
    # Changing back to parent directory
    chdir $parent_dir or die "Failed to move to $parent_dir\n";


  ### Trimming at the 5' end
  if (defined $clip_r2){ # trimming 5' bases of read 2
      die "Clipping the 5' end of read 2 is only allowed for paired-end files (--paired)\n" unless ($validate);
  }

  if (defined $clip_r1){ # trimming 5' bases of read 1
      unless ($clip_r1 > 0 and $clip_r1 < 100){
      die "The 5' clipping value for read 1 should have a sensible value (> 0 and < read length)\n\n";
      }
  }

  if (defined $clip_r2){ # trimming 5' bases of read 2
      unless ($clip_r2 > 0 and $clip_r2 < 100){
      die "The 5' clipping value for read 2 should have a sensible value (> 0 and < read length)\n\n";
      }
  }

  ### Trimming at the 3' end
  if (defined $three_prime_clip_r1){ # trimming 3' bases of read 1
      unless ($three_prime_clip_r1 > 0 and $three_prime_clip_r1 < 100){
      die "The 3' clipping value for read 1 should have a sensible value (> 0 and < read length)\n\n";
      }
  }

  if (defined $three_prime_clip_r2){ # trimming 3' bases of read 2
      unless ($three_prime_clip_r2 > 0 and $three_prime_clip_r2 < 100){
      die "The 3' clipping value for read 2 should have a sensible value (> 0 and < read length)\n\n";
      }
  }


  if (defined $maxn){
      unless ($maxn >= 0 and $maxn <= 100){
      die "--max_n needs to be an integer between 0 and 100\nPlease respecify...\n\n";
      }
  }

  my $trim_n;
  if ($trimn){
      $trim_n = '--trim-n';
  }
  else{
      $trim_n = '';
  }

	### RRBS
	if ($rrbs){
		unless ($non_directional){ # only setting this for directional mode
			if ($validate){
				unless (defined $clip_r2){ # user specified R2 clipping overrides the default setting of --clip_r2 2  # added 07 Dec 2016
					warn "Setting the option '--clip_r2 2' (to remove methylation bias from the start of Read 2)\n"; # sleep(1);
					$clip_r2 = 2;
				}
			}
		}
	}
	else{
		$rrbs = 0;
	}

  if (defined $hardtrim5){
      unless ($hardtrim5 > 0 and $hardtrim5 < 1000){
      die "Hard-trim from 3'-end selected: >$hardtrim5< bp. Please ensure a hard-trimming range between 1 and 999 bp. Please try again...\n\n~~~~~~~~~~~~~~~~~~~~~~\n"
      }
  }
  if (defined $hardtrim3){
      unless ($hardtrim3 > 0 and $hardtrim3 < 1000){
      die "Hard-trim from 5'-end selected: >$hardtrim3< bp. Please ensure a hard-trimming range between 1 and 999 bp. Please try again...\n\n~~~~~~~~~~~~~~~~~~~~~~\n"
      }
  }

  ### The
  if ($clock){
      if ($validate){ # already selected as paired-end mode
      # Fine. Currently, the Clock protocol requires paired-end reads with dual UMIs
      }
      else{
      die "\nOption --clock selected, but the processing is still set to single-end mode. The current clock protocol requires paired-end sequencing with dual unique molecular identifiers (UMIs) though. Please respecify...\n\n";
      }
  }

    if (defined $basename){
        warn "Using user-specified basename (>>$basename<<) instead of deriving the filename from the input file(s)\n";

        if ($basename =~ /\//){
            die "Please make sure the name specified with --basename does not contain file path information! ($basename)";
        }
        $basename =~ s/[ !%\$\*&£]/_/g; # replacing weird symbols or spaces

        if (scalar @ARGV > 2){
            die "[FATAL ERROR]: Number of files supplied can be 1 (single-end mode), or 2 (paired-end mode), but was: ",scalar @ARGV,". Please respecify!\n\n";
        }
        else{
            if (scalar @ARGV == 2){
                if ($validate){
                    # fine, this is paired-end
                }
                else{
                    die "[FATAL ERROR]: Number of files supplied was 2, but single-end mode was selected as well. Please respecify!\n\n";
                }
            }
        }
    }

    if (defined $consider_already_trimmed){
    	# making sure the range is sensible
    	unless ($consider_already_trimmed >= 0 and $consider_already_trimmed <= 10000){
    		die "Please select a threshold for when a sample should not be adapter trimmed at all (--consider_already_trimmed) in the range of [0-1000] (inclusive)\n";
    	}
    	if ($nextera or $small_rna or $illumina){
    		die "The threshold for --consider_already_trimmed [INT] only works in conjunction with adapter auto-detection. Make your choice and try again\n\n";
  		}
  		warn "During the adapter auto-detection, any counts equal to or lower than >$consider_already_trimmed< will be considered as 'file was already adapter-trimmed'. Only quality trimming will be carried out (setting -a X)\n"; sleep(1);
    }

    return ($compression_path,$cores,$quality,$adapter,$stringency,$rrbs,$length_cutoff,$keep,$fastqc,$non_directional,$phred_encoding,$fastqc_args,$trim,$gzip,$validate,$retain,$length_read_1,$length_read_2,$adapter2,$error_rate,$output_dir,$no_report_file,$dont_gzip,$clip_r1,$clip_r2,$three_prime_clip_r1,$three_prime_clip_r2,$nextera,$small_rna,$path_to_cutadapt,$illumina,$max_length,$maxn,$trim_n,$hardtrim5,$clock,$polyA,$hardtrim3,$nextseq,$basename,$consider_already_trimmed);
}

sub Ncounter{
  my $seq = shift;
  my $ncount = 0;
  while($seq =~ /N/g){
    ++$ncount;
  }
  return $ncount;
}

sub extend_adapter_sequence{
    my ($letter,$number) = @_;
    return (${letter}x$number);
}



sub print_helpfile{
  print << "HELP";

 USAGE:

trim_galore [options] <filename(s)>


-h/--help               Print this help message and exits.

-v/--version            Print the version information and exits.

-q/--quality <INT>      Trim low-quality ends from reads in addition to adapter removal. For
                        RRBS samples, quality trimming will be performed first, and adapter
                        trimming is carried in a second round. Other files are quality and adapter
                        trimmed in a single pass. The algorithm is the same as the one used by BWA
                        (Subtract INT from all qualities; compute partial sums from all indices
                        to the end of the sequence; cut sequence at the index at which the sum is
                        minimal). Default Phred score: 20.

--phred33               Instructs Cutadapt to use ASCII+33 quality scores as Phred scores
                        (Sanger/Illumina 1.9+ encoding) for quality trimming. Default: ON.

--phred64               Instructs Cutadapt to use ASCII+64 quality scores as Phred scores
                        (Illumina 1.5 encoding) for quality trimming.

--fastqc                Run FastQC in the default mode on the FastQ file once trimming is complete.

--fastqc_args "<ARGS>"  Passes extra arguments to FastQC. If more than one argument is to be passed
                        to FastQC they must be in the form "arg1 arg2 etc.". An example would be:
                        --fastqc_args "--nogroup --outdir /home/". Passing extra arguments will
                        automatically invoke FastQC, so --fastqc does not have to be specified
                        separately.

-a/--adapter <STRING>   Adapter sequence to be trimmed. If not specified explicitly, Trim Galore will
                        try to auto-detect whether the Illumina universal, Nextera transposase or Illumina
                        small RNA adapter sequence was used. Also see '--illumina', '--nextera' and
                        '--small_rna'. If no adapter can be detected within the first 1 million sequences
                        of the first file specified or if there is a tie between several adapter sequences,
                        Trim Galore defaults to '--illumina' (as long as the Illumina adapter was one of the
                        options, else '--nextera' is the default). A single base
                        may also be given as e.g. -a A{10}, to be expanded to -a AAAAAAAAAA.

-a2/--adapter2 <STRING> Optional adapter sequence to be trimmed off read 2 of paired-end files. This
                        option requires '--paired' to be specified as well. If the libraries to be trimmed
                        are smallRNA then a2 will be set to the Illumina small RNA 5' adapter automatically
                        (GATCGTCGGACT). A single base may also be given as e.g. -a2 A{10}, to be expanded
                        to -a2 AAAAAAAAAA.

--illumina              Adapter sequence to be trimmed is the first 13bp of the Illumina universal adapter
                        'AGATCGGAAGAGC' instead of the default auto-detection of adapter sequence.

--nextera               Adapter sequence to be trimmed is the first 12bp of the Nextera adapter
                        'CTGTCTCTTATA' instead of the default auto-detection of adapter sequence.

--small_rna             Adapter sequence to be trimmed is the first 12bp of the Illumina Small RNA 3' Adapter
                        'TGGAATTCTCGG' instead of the default auto-detection of adapter sequence. Selecting
                        to trim smallRNA adapters will also lower the --length value to 18bp. If the smallRNA
                        libraries are paired-end then a2 will be set to the Illumina small RNA 5' adapter
                        automatically (GATCGTCGGACT) unless -a 2 had been defined explicitly.

--consider_already_trimmed <INT>     During adapter auto-detection, the limit set by <INT> allows the user to 
                        set a threshold up to which the file is considered already adapter-trimmed. If no adapter
                        sequence exceeds this threshold, no additional adapter trimming will be performed (technically,
                        the adapter is set to '-a X'). Quality trimming is still performed as usual.
                        Default: NOT SELECTED (i.e. normal auto-detection precedence rules apply).                     

--max_length <INT>      Discard reads that are longer than <INT> bp after trimming. This is only advised for
                        smallRNA sequencing to remove non-small RNA sequences.


--stringency <INT>      Overlap with adapter sequence required to trim a sequence. Defaults to a
                        very stringent setting of 1, i.e. even a single bp of overlapping sequence
                        will be trimmed off from the 3' end of any read.

-e <ERROR RATE>         Maximum allowed error rate (no. of errors divided by the length of the matching
                        region) (default: 0.1)

--gzip                  Compress the output file with GZIP. If the input files are GZIP-compressed
                        the output files will automatically be GZIP compressed as well. As of v0.2.8 the
                        compression will take place on the fly.

--dont_gzip             Output files won't be compressed with GZIP. This option overrides --gzip.

--length <INT>          Discard reads that became shorter than length INT because of either
                        quality or adapter trimming. A value of '0' effectively disables
                        this behaviour. Default: 20 bp.

                        For paired-end files, both reads of a read-pair need to be longer than
                        <INT> bp to be printed out to validated paired-end files (see option --paired).
                        If only one read became too short there is the possibility of keeping such
                        unpaired single-end reads (see --retain_unpaired). Default pair-cutoff: 20 bp.

--max_n COUNT           The total number of Ns (as integer) a read may contain before it will be removed altogether.
                        In a paired-end setting, either read exceeding this limit will result in the entire
                        pair being removed from the trimmed output files.

--trim-n                Removes Ns from either side of the read. This option does currently not work in RRBS mode.

-o/--output_dir <DIR>   If specified all output will be written to this directory instead of the current
                        directory. If the directory doesn't exist it will be created for you.

--no_report_file        If specified no report file will be generated.

--suppress_warn         If specified any output to STDOUT or STDERR will be suppressed.

--clip_R1 <int>         Instructs Trim Galore to remove <int> bp from the 5' end of read 1 (or single-end
                        reads). This may be useful if the qualities were very poor, or if there is some
                        sort of unwanted bias at the 5' end. Default: OFF.

--clip_R2 <int>         Instructs Trim Galore to remove <int> bp from the 5' end of read 2 (paired-end reads
                        only). This may be useful if the qualities were very poor, or if there is some sort
                        of unwanted bias at the 5' end. For paired-end BS-Seq, it is recommended to remove
                        the first few bp because the end-repair reaction may introduce a bias towards low
                        methylation. Please refer to the M-bias plot section in the Bismark User Guide for
                        some examples. Default: OFF.

--three_prime_clip_R1 <int>     Instructs Trim Galore to remove <int> bp from the 3' end of read 1 (or single-end
                        reads) AFTER adapter/quality trimming has been performed. This may remove some unwanted
                        bias from the 3' end that is not directly related to adapter sequence or basecall quality.
                        Default: OFF.

--three_prime_clip_R2 <int>     Instructs Trim Galore to remove <int> bp from the 3' end of read 2 AFTER
                        adapter/quality trimming has been performed. This may remove some unwanted bias from
                        the 3' end that is not directly related to adapter sequence or basecall quality.
                        Default: OFF.

--2colour/--nextseq INT This enables the option '--nextseq-trim=3'CUTOFF' within Cutadapt, which will set a quality
                        cutoff (that is normally given with -q instead), but qualities of G bases are ignored.
                        This trimming is in common for the NextSeq- and NovaSeq-platforms, where basecalls without
                        any signal are called as high-quality G bases. This is mutually exlusive with '-q INT'.


--path_to_cutadapt </path/to/cutadapt>     You may use this option to specify a path to the Cutadapt executable,
                        e.g. /my/home/cutadapt-1.7.1/bin/cutadapt. Else it is assumed that Cutadapt is in
                        the PATH.

--basename <PREFERRED_NAME>	Use PREFERRED_NAME as the basename for output files, instead of deriving the filenames from
                        the input files. Single-end data would be called PREFERRED_NAME_trimmed.fq(.gz), or
                        PREFERRED_NAME_val_1.fq(.gz) and PREFERRED_NAME_val_2.fq(.gz) for paired-end data. --basename
                        only works when 1 file (single-end) or 2 files (paired-end) are specified, but not for longer lists.

-j/--cores INT          Number of cores to be used for trimming [default: 1]. For Cutadapt to work with multiple cores, it
                        requires Python 3 as well as parallel gzip (pigz) installed on the system. The version of Python used 
                        is detected from the shebang line of the Cutadapt executable (either 'cutadapt', or a specified path).
                        If Python 2 is detected, --cores is set to 1.
                        If pigz cannot be detected on your system, Trim Galore reverts to using gzip compression. Please note
                        that gzip compression will slow down multi-core processes so much that it is hardly worthwhile, please 
                        see: https://github.com/FelixKrueger/TrimGalore/issues/16#issuecomment-458557103 for more info).
						
                        Actual core usage: It should be mentioned that the actual number of cores used is a little convoluted.
                        Assuming that Python 3 is used and pigz is installed, --cores 2 would use 2 cores to read the input
                        (probably not at a high usage though), 2 cores to write to the output (at moderately high usage), and 
                        2 cores for Cutadapt itself + 2 additional cores for Cutadapt (not sure what they are used for) + 1 core
                        for Trim Galore itself. So this can be up to 9 cores, even though most of them won't be used at 100% for
                        most of the time. Paired-end processing uses twice as many cores for the validation (= writing out) step.
                        --cores 4 would then be: 4 (read) + 4 (write) + 4 (Cutadapt) + 2 (extra Cutadapt) +	1 (Trim Galore) = 15.

                        It seems that --cores 4 could be a sweet spot, anything above has diminishing returns.
			


SPECIFIC TRIMMING - without adapter/quality trimming

--hardtrim5 <int>       Instead of performing adapter-/quality trimming, this option will simply hard-trim sequences
                        to <int> bp at the 5'-end. Once hard-trimming of files is complete, Trim Galore will exit.
                        Hard-trimmed output files will end in .<int>_5prime.fq(.gz). Here is an example:

                        before:         CCTAAGGAAACAAGTACACTCCACACATGCATAAAGGAAATCAAATGTTATTTTTAAGAAAATGGAAAAT
                        --hardtrim5 20: CCTAAGGAAACAAGTACACT

--hardtrim3 <int>       Instead of performing adapter-/quality trimming, this option will simply hard-trim sequences
                        to <int> bp at the 3'-end. Once hard-trimming of files is complete, Trim Galore will exit.
                        Hard-trimmed output files will end in .<int>_3prime.fq(.gz). Here is an example:

                        before:         CCTAAGGAAACAAGTACACTCCACACATGCATAAAGGAAATCAAATGTTATTTTTAAGAAAATGGAAAAT
                        --hardtrim3 20:                                                   TTTTTAAGAAAATGGAAAAT

--clock                 In this mode, reads are trimmed in a specific way that is currently used for the Mouse
                        Epigenetic Clock (see here: Multi-tissue DNA methylation age predictor in mouse, Stubbs et al.,
                        Genome Biology, 2017 18:68 https://doi.org/10.1186/s13059-017-1203-5). Following this, Trim Galore
                        will exit.

                        In it's current implementation, the dual-UMI RRBS reads come in the following format:

                        Read 1  5' UUUUUUUU CAGTA FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF TACTG UUUUUUUU 3'
                        Read 2  3' UUUUUUUU GTCAT FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF ATGAC UUUUUUUU 5'

                        Where UUUUUUUU is a random 8-mer unique molecular identifier (UMI), CAGTA is a constant region,
                        and FFFFFFF... is the actual RRBS-Fragment to be sequenced. The UMIs for Read 1 (R1) and
                        Read 2 (R2), as well as the fixed sequences (F1 or F2), are written into the read ID and
                        removed from the actual sequence. Here is an example:

                        R1: \@HWI-D00436:407:CCAETANXX:1:1101:4105:1905 1:N:0: CGATGTTT
                            ATCTAGTTCAGTACGGTGTTTTCGAATTAGAAAAATATGTATAGAGGAAATAGATATAAAGGCGTATTCGTTATTG
                        R2: \@HWI-D00436:407:CCAETANXX:1:1101:4105:1905 3:N:0: CGATGTTT
                            CAATTTTGCAGTACAAAAATAATACCTCCTCTATTTATCCAAAATCACAAAAAACCACCCACTTAACTTTCCCTAA

                        R1: \@HWI-D00436:407:CCAETANXX:1:1101:4105:1905 1:N:0: CGATGTTT:R1:ATCTAGTT:R2:CAATTTTG:F1:CAGT:F2:CAGT
                                         CGGTGTTTTCGAATTAGAAAAATATGTATAGAGGAAATAGATATAAAGGCGTATTCGTTATTG
                        R2: \@HWI-D00436:407:CCAETANXX:1:1101:4105:1905 3:N:0: CGATGTTT:R1:ATCTAGTT:R2:CAATTTTG:F1:CAGT:F2:CAGT
                                         CAAAAATAATACCTCCTCTATTTATCCAAAATCACAAAAAACCACCCACTTAACTTTCCCTAA

                        Following clock trimming, the resulting files (.clock_UMI.R1.fq(.gz) and .clock_UMI.R2.fq(.gz))
                        should be adapter- and quality trimmed with Trim Galore as usual. In addition, reads need to be trimmed
                        by 15bp from their 3' end to get rid of potential UMI and fixed sequences. The command is:

                        trim_galore --paired --three_prime_clip_R1 15 --three_prime_clip_R2 15 *.clock_UMI.R1.fq.gz *.clock_UMI.R2.fq.gz

                        Following this, reads should be aligned with Bismark and deduplicated with UmiBam
                        in '--dual_index' mode (see here: https://github.com/FelixKrueger/Umi-Grinder). UmiBam recognises
                        the UMIs within this pattern: R1:(ATCTAGTT):R2:(CAATTTTG): as (UMI R1) and (UMI R2).

--polyA                 This is a new, still experimental, trimming mode to identify and remove poly-A tails from sequences.
                        When --polyA is selected, Trim Galore attempts to identify from the first supplied sample whether
                        sequences contain more often a stretch of either 'AAAAAAAAAA' or 'TTTTTTTTTT'. This determines
                        if Read 1 of a paired-end end file, or single-end files, are trimmed for PolyA or PolyT. In case of
                        paired-end sequencing, Read2 is trimmed for the complementary base from the start of the reads. The
                        auto-detection uses a default of A{20} for Read1 (3'-end trimming) and T{150} for Read2 (5'-end trimming).
                        These values may be changed manually using the options -a and -a2.

                        In addition to trimming the sequences, white spaces are replaced with _ and it records in the read ID
                        how many bases were trimmed so it can later be used to identify PolyA trimmed sequences. This is currently done
                        by writing tags to both the start ("32:A:") and end ("_PolyA:32") of the reads in the following example:

                        \@READ-ID:1:1102:22039:36996 1:N:0:CCTAATCC
                        GCCTAAGGAAACAAGTACACTCCACACATGCATAAAGGAAATCAAATGTTATTTTTAAGAAAATGGAAAATAAAAACTTTATAAACACCAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

                        \@32:A:READ-ID:1:1102:22039:36996_1:N:0:CCTAATCC_PolyA:32
                        GCCTAAGGAAACAAGTACACTCCACACATGCATAAAGGAAATCAAATGTTATTTTTAAGAAAATGGAAAATAAAAACTTTATAAACACC

                        PLEASE NOTE: The poly-A trimming mode expects that sequences were both adapter and quality trimmed
                        before looking for Poly-A tails, and it is the user's responsibility to carry out an initial round of
                        trimming. The following sequence:
 
                        1) trim_galore file.fastq.gz
                        2) trim_galore --polyA file_trimmed.fq.gz
                        3) zcat file_trimmed_trimmed.fq.gz | grep -A 3 PolyA | grep -v ^-- > PolyA_trimmed.fastq

                        Will 1) trim qualities and Illumina adapter contamination, 2) find and remove PolyA contamination.
                        Finally, if desired, 3) will specifically find PolyA trimmed sequences to a specific FastQ file of your choice.


RRBS-specific options (MspI digested material):

--rrbs                  Specifies that the input file was an MspI digested RRBS sample (recognition
                        site: CCGG). Single-end or Read 1 sequences (paired-end) which were adapter-trimmed
                        will have a further 2 bp removed from their 3' end. Sequences which were merely
                        trimmed because of poor quality will not be shortened further. Read 2 of paired-end
                        libraries will in addition have the first 2 bp removed from the 5' end (by setting
                        '--clip_r2 2'). This is to avoid using artificial methylation calls from the filled-in
                        cytosine positions close to the 3' MspI site in sequenced fragments.
                        This option is not recommended for users of the NuGEN ovation RRBS System 1-16
                        kit (see below).

--non_directional       Selecting this option for non-directional RRBS libraries will screen
                        quality-trimmed sequences for 'CAA' or 'CGA' at the start of the read
                        and, if found, removes the first two basepairs. Like with the option
                        '--rrbs' this avoids using cytosine positions that were filled-in
                        during the end-repair step. '--non_directional' requires '--rrbs' to
                        be specified as well. Note that this option does not set '--clip_r2 2' in
                        paired-end mode.

--keep                  Keep the quality trimmed intermediate file. Default: off, which means
                        the temporary file is being deleted after adapter trimming. Only has
                        an effect for RRBS samples since other FastQ files are not trimmed
                        for poor qualities separately.


Note for RRBS using the NuGEN Ovation RRBS System 1-16 kit:

Owing to the fact that the NuGEN Ovation kit attaches a varying number of nucleotides (0-3) after each MspI
site Trim Galore should be run WITHOUT the option --rrbs. This trimming is accomplished in a subsequent
diversity trimming step afterwards (see their manual).



Note for RRBS using MseI:

If your DNA material was digested with MseI (recognition motif: TTAA) instead of MspI it is NOT necessary
to specify --rrbs or --non_directional since virtually all reads should start with the sequence
'TAA', and this holds true for both directional and non-directional libraries. As the end-repair of 'TAA'
restricted sites does not involve any cytosines it does not need to be treated especially. Instead, simply
run Trim Galore! in the standard (i.e. non-RRBS) mode.




Paired-end specific options:

--paired                This option performs length trimming of quality/adapter/RRBS trimmed reads for
                        paired-end files. To pass the validation test, both sequences of a sequence pair
                        are required to have a certain minimum length which is governed by the option
                        --length (see above). If only one read passes this length threshold the
                        other read can be rescued (see option --retain_unpaired). Using this option lets
                        you discard too short read pairs without disturbing the sequence-by-sequence order
                        of FastQ files which is required by many aligners.

                        Trim Galore! expects paired-end files to be supplied in a pairwise fashion, e.g.
                        file1_1.fq file1_2.fq SRR2_1.fq.gz SRR2_2.fq.gz ... .

-t/--trim1              Trims 1 bp off every read from its 3' end. This may be needed for FastQ files that
                        are to be aligned as paired-end data with Bowtie. This is because Bowtie (1) regards
                        alignments like this:

                          R1 --------------------------->     or this:    ----------------------->  R1
                          R2 <---------------------------                       <-----------------  R2

                        as invalid (whenever a start/end coordinate is contained within the other read).
                        NOTE: If you are planning to use Bowtie2, BWA etc. you don't need to specify this option.

--retain_unpaired       If only one of the two paired-end reads became too short, the longer
                        read will be written to either '.unpaired_1.fq' or '.unpaired_2.fq'
                        output files. The length cutoff for unpaired single-end reads is
                        governed by the parameters -r1/--length_1 and -r2/--length_2. Default: OFF.

-r1/--length_1 <INT>    Unpaired single-end read length cutoff needed for read 1 to be written to
                        '.unpaired_1.fq' output file. These reads may be mapped in single-end mode.
                        Default: 35 bp.

-r2/--length_2 <INT>    Unpaired single-end read length cutoff needed for read 2 to be written to
                        '.unpaired_2.fq' output file. These reads may be mapped in single-end mode.
                        Default: 35 bp.

Last modified on 07 November 2019.

HELP
  exit;
}