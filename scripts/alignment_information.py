'''
A script for counting alignment size and informative characters.

Requirements:
	Bio

Usage:
	python3 alignment_information.py myalignment.fasta
'''
import sys
from Bio import AlignIO

#1. Read the alignment from the file
filename = sys.argv[1]
alignment = AlignIO.read(filename, "fasta")

#2. Count informative sites
num_sequences = len(alignment)
alignment_length = alignment.get_alignment_length()
informative_sites = 0

#For each column in the alignment...
for i in range(alignment_length):
    characters = alignment[:, i]
    #...discard gaps and missing data...
    characters = [
            character for character in characters if character not in ["X","-","?"]
            ]
    #...if there is more than one difference the site is informative...
    if len(set(characters)) > 2:
        informative_sites += 1
    #..if there are only two characters...
    elif len(set(characters)) > 1:
        unique_characters = set(characters)
        characters_informative = []
        for character in unique_characters:
            count = characters.count(character)
            characters_informative.append(count > 2)
            informative_characters = len(
                [value for value in characters_informative if value is True])
            #...they are only informative if they appear more than once...
            if informative_characters > 1:
                informative_sites +=1

#3. Print the alignment information
print('This is an alignment of %s sequences.' % num_sequences)
print('The alignment length is %s.' % alignment_length)
print('The number of informative sites is %s.' % informative_sites)
