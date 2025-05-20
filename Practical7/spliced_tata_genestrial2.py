import re

def process_spliced_genes(input_file, output_file, splice_combination):
    """
    Process spliced genes to identify those containing TATA boxes and count their occurrences.

    Args:
        input_file (str): Path to the input .fa file.
        output_file (str): Path to the output .fa file.
        splice_combination (str): Splice donor/acceptor combination.
    """
    tata_pattern = re.compile(r'TATA[AT][AT]')  # Match TATAWAW pattern

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        current_header = []
        current_sequence = []
        for line in infile:
            line = line.strip()
            if not line:  
                continue  # Skip empty lines
            if line.startswith('>'):
                #sequence = ''.join(current_sequence).upper()               
                # Start a new sequence
                # Extract the gene name (up to the first space)
                current_header.append( line[1:].split()[0] ) # Remove '>' and split to get the gene name
                current_sequence = []
            else:
                # Accumulate the sequence parts
                current_sequence.append(line)
        for i in range(len(current_sequence)):
                fir=0
                las=9999
                if((splice_combination[0:2] not in current_sequence[i]) or (splice_combination[2:4] not in current_sequence[i])):
                    continue
                fir = current_sequence[i].finditer(splice_combination[0:2])[0]
                
                las = current_sequence[i].finditer(splice_combination[2:4])[len(current_sequence[i].find(splice_combination[2:4]))+2] 
                tata_matches = tata_pattern.finditer(current_sequence[i][fir:las])
                if tata_matches:
                        # Write the header and sequence to the output file
                        tata_count = len(tata_matches)
                        outfile.write(f">{current_header[i]}_TATA_count:{tata_count}\n")
                        outfile.write(f"{current_sequence[i]}\n")

        
        
    print(f"Processing complete! Results saved to {output_file}")

def main():
    # Ask the user for the splice combination
    splice_combinations = ['GTAG', 'GCAG', 'ATAC']
    print("Available splice combinations:", ', '.join(splice_combinations))
    user_input = input("Please enter one of the splice combinations (GTAG, GCAG, ATAC): ").strip().upper()

    if user_input not in splice_combinations:
        print("Invalid splice combination. Please enter one of the specified combinations.")
        return

    input_fa = "C:/Users/玄青石/Desktop/收藏/IBI_2024-25/IBI1_2024-25/Practical7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"  # Input file path
    output_fa = f"C:/Users/玄青石/Desktop/收藏/IBI_2024-25/IBI1_2024-25/Practical7/{user_input}_spliced_genes.fa"  # Output file path based on user input

    process_spliced_genes(input_fa, output_fa, user_input)


if __name__ == "__main__":
    main()