from Bio import AlignIO
import sys

#read alignment
filename = sys.argv[1] 
alignment = AlignIO.read(filename, "fasta")


#count informative sites
num_sequences = len(alignment)
alignment_length = alignment.get_alignment_length()
informative_sites = 0

for i in range(alignment_length):
    characters = alignment[:, i]
    characters = [
            character for character in characters if character not in ["X","-","?"]
            ]
    if len(set(characters)) > 2: #is there more than 2 sites you can skip the later calculation
        informative_sites += 1
    elif len(set(characters)) > 1: #otherwise check that that the unique character appears more than once
        unique_characters = set(characters)
        characters_informative = []
        for character in unique_characters:
            count = characters.count(character)
            characters_informative.append(count > 2)
            informative_characters = len([value for value in characters_informative if value == True])
            if informative_characters > 1:
                informative_sites +=1

print('The alignment length is %s.' % alignment_length)
print('The number of informative sites is %s.' % informative_sites)

