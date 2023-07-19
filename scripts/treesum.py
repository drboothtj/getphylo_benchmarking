import sys
from Bio import Phylo

#get path and read tree
filename = sys.argv[1]
max_support = float(sys.argv[2])
tree = Phylo.read(filename, "newick")

#draw the tree to confirm correct parsing
Phylo.draw_ascii(tree)

#get a list of support values
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
            if support_value == max_support:
                supported_clades += 1

#sum values and calculate average
sum_of_values = sum(all_support_values)
average_support = sum_of_values / number_of_clades
proportion_supported = (supported_clades / number_of_clades) * 100

#print data
print('%s has %s total branches.' % (filename, number_of_clades))
print('%s has %s supported branches.' % (filename, supported_clades))
print('%s has an total support of: %s' % (filename, sum_of_values))
print('%s has an average support of %s' % (filename, average_support))
print('%s has %s percent of supported branches.' % (filename, proportion_supported))

