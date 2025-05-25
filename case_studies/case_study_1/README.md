# Case Study 1: Bacterial Genome-Scale Phylogeny
## Description of Files
This directory contains the following files:

- `*.gb` - example input - a collection of genbank files for bacterial genomes

- `bacteria_alignment.fasta` - example output - the concatenated alignment produced by getphylo

- `bacteria_partition.txt` - example output - the partition produced by getphylo for the above alignment

- `bacteria_tree.tree` - example output - the resulting phylogenetic tree produced by getphylo

- `README.md` - This document!

## Example Command
Try running:
`getphylo -g '*.gb' -ia`
