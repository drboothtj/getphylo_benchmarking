# Case Study 4: Fungal Genome-Scale Phylogeny from proteomes
## Description of Files
This directory contains the following files:

`strains.txt` - a list of the strains whose proteomes were downloaded from the NCBI

`eurotiomycete_alignment.fasta` - example output - the concatenated alignment produced by getphylo

`eurotiomycete_partition.txt` - example output - the partition produced by getphylo for the above alignment

`eurotiomycete_tree.tree` - example output - the resulting phylogenetic tree produced by getphylo

`README.md` - This document!

## Example Command
Try running:

`getphylo -c 8 -cp FASTA_EXTRACTED -g 'output/fasta/*.fasta' –-maxloci 100 -r 111`

**NOTE:** This will only work if you have downloaded the proteomes from the NCBI.
