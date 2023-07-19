'''
A script for reporting support information about phylogenetic trees.

Requirements:
	Bio

Usage:
	python3 treesum.py FILENAME MAX_SUPPORT

Arguments:
    FILENAME: The path to the tree (newick format).
    MAX_SUPPORT: An float reprisenting the maximum possible support value (typically 1 or 100)
'''
import sys
from Bio import Phylo

#1. Read the tree
FILENAME = sys.argv[1]
MAX_SUPPORT = float(sys.argv[2])
tree = Phylo.read(FILENAME, "newick")

#2. Draw the tree for quick visual confirmation
Phylo.draw_ascii(tree)

#3. Get a list of all the support values
all_support_values = []
number_of_clades = 0
supported_clades = 0

for clade in tree.find_clades():
    if clade.branch_length:
        support_value = clade.confidence
        if support_value is None:
            pass
        else:
            all_support_values.append(support_value)
            number_of_clades += 1
            if support_value == MAX_SUPPORT:
                supported_clades += 1

#4. Sum the values and calculate averages
sum_of_values = sum(all_support_values)
average_support = sum_of_values / number_of_clades
proportion_supported = (supported_clades / number_of_clades) * 100

#5. Print data
print('%s has %s total branches.' % (FILENAME, number_of_clades))
print('%s has %s supported branches.' % (FILENAME, supported_clades))
print('%s has an total support of: %s' % (FILENAME, sum_of_values))
print('%s has an average support of %s' % (FILENAME, average_support))
print('%s has %s percent of supported branches.' % (FILENAME, proportion_supported))
