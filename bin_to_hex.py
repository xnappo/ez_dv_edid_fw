import argparse
import binascii

def binary_to_hex(input_file, output_file):
    """
    Converts a binary file to a formatted hex string, writes it to an output file,
    and prints it to the screen.

    Args:
        input_file (str): The path to the binary file to read.
        output_file (str): The path to the text file where the formatted hex string will be written.
    """
    # Read the binary data from the input file
    with open(input_file, 'rb') as bin_file:
        binary_data = bin_file.read()

    # Convert binary data to hex string
    hex_string = binascii.hexlify(binary_data).decode('ascii')

    # Break hex string into bytes (2 characters per byte)
    byte_list = [hex_string[i:i+2] for i in range(0, len(hex_string), 2)]

    # Group into lines of 16 bytes (i.e., 16 entries per line)
    lines = [' '.join(byte_list[i:i+16]) for i in range(0, len(byte_list), 16)]

    # Join the lines with newlines
    formatted_output = '\n'.join(lines)

    # Write to output file
    with open(output_file, 'w') as text_file:
        text_file.write(formatted_output)

    # Print to screen
    print(formatted_output)
    print(f"\nFormatted hex string successfully written to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert binary file to formatted hex string.")
    parser.add_argument("input_file", help="Path to the input binary file.")
    parser.add_argument("output_file", help="Path to the output hex text file.")

    args = parser.parse_args()
    binary_to_hex(args.input_file, args.output_file)

