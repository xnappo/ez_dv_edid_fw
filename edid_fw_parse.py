import re
import sys

try:
    import tkinter
    gui = True
    from tkinter import filedialog
except ImportError:
    gui = False

def check_dolby_vision(ecid_data):
    global dv_count
    if ("EB0146D000" in ecid_data) or ("eb0146d000" in ecid_data):
        dv_count += 1
        print('Dolby Vision Capable')
        print_ecid(ecid)
        print('\n' * 2)  # Two line breaks between EDIDs
        
# Function to format and print the ECID data
def print_ecid(ecid_data):
    for i in range(0, len(ecid_data), 32):
        print(ecid_data[i:i+32])

if (gui == True):
    hex_file = filedialog.askopenfilename(
            filetypes=[("HEX Files", "*.hex")],
            title="Select HEX File:",
    )
else:  # Check if the correct number of command-line arguments is provided
  if len(sys.argv) != 2:
      print("Usage: python script.py <hex_file>")
      sys.exit(1)
  # # Get the filename from the command-line arguments
  hex_file = sys.argv[1]

edid_count = 0
dv_count = 0

# Read the Intel Hex file
with open(hex_file, 'r') as file:
    lines = file.readlines()

# Read the Intel Hex file
with open(hex_file, 'r') as file:
    lines = file.readlines()

ecid_data = ''  # Variable to store ECID data
# start_lines = []

# Iterate through the lines of the hex file
for line in lines:
    data = line[9:-3]  # Extract data portion, excluding address and checksum
    ecid_data += data

# Search for all occurrences of '00ffffffffffff' pattern in the concatenated data (case-insensitive)
matches = re.finditer('00ffffffffffff', ecid_data, re.IGNORECASE)

for match in matches:
    edid_count += 1
    start_index = match.start()
    end_index = start_index + 512
    ecid = ecid_data[start_index:end_index]
    check_dolby_vision(ecid)

print ("Scanned for EDID in file", hex_file)
print ("Total number of EDID header =", edid_count)
print ("Total number of Dolby Vision EDIDs =", dv_count)
