import argparse
import binascii

def hex_to_binary(hex_input, output_file):
    """
    Converts a hex string to a binary file.

    Args:
        hex_input (str): The hex string input, with or without spaces or line breaks between bytes.
        output_file (str): The name of the output binary file.
    """
    # Remove all whitespace (including line breaks) from the hex input
    cleaned_hex = ''.join(hex_input.split())

    # Validate that the cleaned input is a valid hex string
    if len(cleaned_hex) % 2 != 0:
        raise ValueError("Hex input must have an even number of characters.")

    try:
        binary_data = binascii.unhexlify(cleaned_hex)
    except binascii.Error as e:
        raise ValueError("Invalid hex input.") from e

    # Write the binary data to the output file
    with open(output_file, 'wb') as bin_file:
        bin_file.write(binary_data)

    print(f"Binary data successfully written to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert a hex string to a binary file.")
    parser.add_argument("hex_input", type=argparse.FileType('r'), help="The file containing the hex string input (spaces and line breaks optional).")
    parser.add_argument("output_file", type=str, help="The name of the output binary file.")

    args = parser.parse_args()

    try:
        # Read the entire content of the input file
        hex_content = args.hex_input.read()
        hex_to_binary(hex_content, args.output_file)
    except ValueError as e:
        print(f"Error: {e}")
