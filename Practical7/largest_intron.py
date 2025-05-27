import re
# This script finds the largest intron in a given DNA sequence.

seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
matches1 = re.finditer('GT', seq)
matches2 = re.finditer('AG', seq)
positions1 = [match.start() for match in matches1]#find the start positions of 'GT'
#print(positions1)
positions2 = [match.start() for match in matches2]#find the start positions of 'AG'
#print(positions2)
print(positions2[len(positions2)-1]-positions1[0]+2)
largest_intron = seq[positions1[0]:positions2[len(positions2)-1]+2]
print(largest_intron)
#seq3='GTGGTGTGTCTGTTCTGAGAG'
#print(len(seq3))