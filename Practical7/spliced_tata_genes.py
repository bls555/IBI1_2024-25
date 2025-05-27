import re
import os
os.chdir('Practical7')  # Change to the directory where the input file is located

def find_longest_spliced_segment(sequence, splice_start, splice_end):
    """
    Find the longest segment in the sequence that starts with splice_start and ends with splice_end.

    Args:
        sequence (str): The DNA sequence to search in.
        splice_start (str): The first two characters of the splice combination.
        splice_end (str): The last two characters of the splice combination.

    Returns:
        str: The longest segment starting with splice_start and ending with splice_end.
    """
    pattern = re.compile(rf"{splice_start}.*?{splice_end}")
    matches = pattern.findall(sequence)
    
    if not matches:
        return None
    
    # Find the longest match
    longest_segment = max(matches, key=len)
    return longest_segment


def process_spliced_genes(input_file, output_file, splice_combination):
    """
    Process spliced genes to identify those containing TATA boxes in the longest spliced segment and count their occurrences.

    Args:
        input_file (str): Path to the input .fa file.
        output_file (str): Path to the output .fa file.
        splice_combination (str): Splice donor/acceptor combination (4 characters).
    """
    tata_pattern = re.compile(r'TATA[AT][AT]')  # Match TATAWAW pattern
    splice_start = splice_combination[:2]
    splice_end = splice_combination[2:]

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
                    # Find the longest spliced segment
                    longest_segment = find_longest_spliced_segment(sequence, splice_start, splice_end)
                    
                    if longest_segment:
                        # Check if the longest segment contains the TATA box
                        tata_matches = tata_pattern.findall(longest_segment)
                        if tata_matches:
                            # Write the header and sequence to the output file
                            tata_count = len(tata_matches)
                            outfile.write(f">{current_header}_TATA_count:{tata_count}\n")
                            outfile.write(f"{longest_segment}\n")

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
            longest_segment = find_longest_spliced_segment(sequence, splice_start, splice_end)
            
            if longest_segment:
                tata_matches = tata_pattern.findall(longest_segment)
                if tata_matches:
                    tata_count = len(tata_matches)
                    outfile.write(f">{current_header}_TATA_count:{tata_count}\n")
                    outfile.write(f"{longest_segment}\n")

    print(f"Processing complete! Results saved to {output_file}")


def main():
    # Ask the user for the splice combination
    splice_combinations = ['GTAG', 'GCAG', 'ATAC']
    print("Available splice combinations:", ', '.join(splice_combinations))
    user_input = input("Please enter one of the splice combinations (GTAG, GCAG, ATAC): ").strip().upper()

    if user_input not in splice_combinations:
        print("Invalid splice combination. Please enter one of the specified combinations.")
        return

    input_fa = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"  # Input file path
    output_fa = f"{user_input}_spliced_genes.fa"  # Output file path based on user input

    process_spliced_genes(input_fa, output_fa, user_input)

#C:/Users/玄青石/Desktop/收藏/IBI_2024-25/IBI1_2024-25/Practical7/
if __name__ == "__main__":
    main()