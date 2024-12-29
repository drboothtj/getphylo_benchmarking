# Case Study 2: Biosynthetic Gene Cluster Phylogeny
## Description of Files
This directory contains the following files:

- `mibig_bgc_accessions.txt` - a list of accessions from the MiBiG database used in this case study. You can download MiBiG version 3.1, [here](https://dev.mibig.secondarymetabolites.org/download).

- `rsn_BGC.gbk` - example input - the rsn BGC **only**. You will need to download the other accessions from MiBiG to run this case study for youtself. See `mibig_bgc_accessions.txt`.

- `rsn_BGC_alignment.fasta` - example output - the concatenated alignment produced by getphylo

- `rsn_BGC_partition.txt` - example output - the partition produced by getphylo for the above alignment

- `rsn_BGC_tree.tree`  - example output - the resulting phylogenetic tree produced by getphylo

- `README.md` - This document!

## Example Command
Try running:

`getphylo -s rsn.gbk -p 10`

**NOTE:** This Will Only Work if you have downloaded the MiBiG accessions!
