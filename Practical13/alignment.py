import numpy as np
import blosum as bl
import os
os.chdir('Practical13')  # Change to the directory where the FASTA files are located




def read_fasta(file_path):
    """
    Reads a FASTA file and returns the sequence as a string.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()
        sequence = ''.join(line.strip() for line in lines[1:])  # Skip the first line (header)
    return sequence

def default_blosum62():
    matrix = bl.BLOSUM(62)
    return matrix


def blosum_score(seq1, seq2, matrix):
    """
    Calculate the BLOSUM62 score for two sequences.
    """
    edit_distance=	0		
    #set	initial	distance	as	zero	
    for	i	in	range(len(seq1)):	#compare	each	amino	acid	
        if	seq1[i]!=seq2[i]:				
            edit_distance+=	matrix[seq1[i]][seq2[i]]	#add	a	score	1	if	amino	acids	are	 different	
    print	("score:",edit_distance)
    count=0
    for i in range(len(seq1)):
        if	seq1[i]!=seq2[i]:				
            count +=1   #add	a	score	1	if	amino	acids	are	 different	
    print	("percentage:",(len(seq1)-count)/len(seq1)*100.0,"%")	#calculate	the	percentage	of	similarity
seq1=read_fasta("seq1.fasta")
seq2=read_fasta("seq2.fasta")
seq3=read_fasta("seq3(random).fasta")
# 222 Mitochondrion matrix
#83.3 to 100
matrix=default_blosum62()
blosum_score(seq1, seq2, matrix)
blosum_score(seq1, seq3, matrix)
blosum_score(seq2, seq3, matrix)
#the most	closely	related	sequence is	seq1 and seq2,from human and rat.

'''summary:
The length is 222, subcellular location is Mitochondrion matrix
The	range of percentage	identities	in	the	reported online	BLAST, results is 83.3 to 100.

seq1 and seq2:
score: 1.0
percentage: 90.09009009009009 %
seq1 and seq3:
score: -311.0
percentage: 9.45945945945946 %
seq2 and seq3:
score: -311.0
percentage: 9.90990990990991 %

The most closely related sequence is seq1 and seq2,from human and rat.
'''
