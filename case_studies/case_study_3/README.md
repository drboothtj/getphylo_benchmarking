# Case Study 3: Primate Phylogeny
## Description of Files
This directory contains the following files:

- `accessions.txt` - list of accessions for the primate genomes used in this case study
  
- `primate_combined_alignment.fasta` example output - the concatenated alignment produced by getphylo
  
- `primate_partition.txt` - example output - the partition produced by getphylo for the above alignment
  
- `primate_tree.tree` - example output - the resulting phylogenetic tree produced by getphylo
  
- `README.md` - This document!

## Example Command
Try running:

`getphylo -ia -l DEBUG -t protein_id -c 8`

**NOTE:** This will only work if you have downloaded the accessions form the NCBI.
