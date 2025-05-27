import re
import os
os.chdir('Practical7')  # Change to the directory where the input file is located

def extract_tata_genes(input_file, output_file):
    """
    Extract genes containing the TATA box sequence from a FASTA file and write the results to a new FASTA file.

    Args:
        input_file (str): Path to the input .fa file.
        output_file (str): Path to the output .fa file.
    """
    tata_pattern = re.compile(r'TATA[AT][AT]')  # Match the TATAWAW pattern, where W is A or T

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        current_header = None
        current_sequence = []

        for line in infile:
            line = line.strip()
            if not line:
                continue  # Skip empty lines

            if line.startswith('>'):
                # Process the previous sequence
                if current_header is not None:
                    # Join the sequence parts into a single string
                    sequence = ''.join(current_sequence).upper()
                    # Check if the sequence contains the TATA box
                    if tata_pattern.search(sequence):
                        # Write the header and sequence to the output file
                        outfile.write(f">{current_header}\n")
                        # Split the sequence into lines of 80 characters each
                        for i in range(0, len(sequence), 80):
                            outfile.write(sequence[i:i+80] + '\n')

                # Start a new sequence
                # Extract the gene name (up to the first space)
                current_header = line[1:].split()[0]  # Remove '>' and split to get the gene name
                current_sequence = []
            else:
                # Accumulate the sequence parts
                current_sequence.append(line)

        # Process the last sequence
        if current_header is not None:
            sequence = ''.join(current_sequence).upper()
            if tata_pattern.search(sequence):
                outfile.write(f">{current_header}\n")
                for i in range(0, len(sequence), 80):
                    outfile.write(sequence[i:i+80] + '\n')

    print(f"Processing complete! Results saved to {output_file}")



    

if __name__ == "__main__":
    input_fa = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"  # input file path
    output_fa = "tata_genes.fa"  # output file path

    extract_tata_genes(input_fa, output_fa)
#C:/Users/玄青石/Desktop/收藏/IBI_2024-25/IBI1_2024-25/Practical7/