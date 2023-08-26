#create a new environment for protview
conda create -n protview_environment
conda activate protview_environment

#install protview
pip install protview
protview setup_commands

#input sanitation
ProtView fasta_input_sanitation at1g66610.fasta

#digest
rpg -i at1g66610.fasta -o at1g66610_rpg.fasta -e 1 15 28 42 -q

#peptide processing
#default parameters
rpg_output_processing at1g66610_rpg.fasta
#example with miscleavage <2, max len = 40
rpg_output_processing at1g66610_rpg.fasta -mc=2 -max=40

#proteomic summary statistics
ProtView summary_stats -fasta at1g66610.fasta -u at1g66610_rpg.csv -f at1g66610_rpg_len_7_35.csv -o at1g66610_summary.csv -r C S K

#coding sequence extraction
ProtView cds_extraction at1g66610.gff3

#genomic coordinate conversion
gen_coords at1g66610_rpg_len_7_35.csv at1g66610_+_cdsdf.csv at1g66610_-_cdsdf.csv

#identification of junction covering peptides
ProtView junction_peptides at1g66610_rpg_len_7_35.csv at1g66610_+_cdsdf.csv at1g66610_-_cdsdf.csv at1g66610_junction_pept.csv

#proteogenomic summary statistics
ProtView junction_summary -pept at1g66610_junction_pept_-_.csv -cds at1g66610_+_cdsdf.csv at1g66610_-_cdsdf.csv -out at1g66610_junction_summary.csv 

#add unique peptide column to the proteogenomic summary table
ProtView unique_count at1g66610_junction_summary.csv at1g66610_rpg_len_7_35.csv
