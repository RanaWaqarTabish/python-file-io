import re

def find_heritability(input_file, output_file):
    # Open the input and output files
    with open(input_file, 'r') as input_file, open(output_file, 'w') as output_file:
        # Loop through the input file line by line
        for line_num, line in enumerate(input_file, 1):
            # Define the regular expression pattern
            pattern = r'\b(heritability|heritable|heritably|heritableness|inheritance|inherited|inherently)\b'

            # Search for the pattern in the current line
            matches = re.findall(pattern, line)

            # If there are matches, write them to the output file on separate lines
            if matches:
                for match in matches:
                    output_file.write(f"{line_num}\t{match}\n")

if __name__ == '__main__':
    find_heritability('origin.txt', 'output.txt')