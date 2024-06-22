#!/usr/bin/env python3
import sys

def replace_chars_in_bin_file(bin_file_path, values):
    if len(values) != 12:
        raise ValueError("Exactly 12 characters or hex values are required.")
    
    hex_values = []
    for value in values:
        if value.startswith("0x"):
            # If the value starts with "0x", it is assumed to be a hexadecimal value
            hex_value = value[2:]
            if len(hex_value) != 2:
                raise ValueError(f"Invalid hex value: {value}")
        else:
            # Otherwise, it is an ASCII character, convert it to hexadecimal
            hex_value = format(ord(value), '02x')
        
        hex_values.append(hex_value)

    with open(bin_file_path, 'rb+') as bin_file:
        # Read the existing content of the file
        content = bin_file.read()
        
        # Convert the content to a modifiable list of hexadecimal values
        content_hex = content.hex()
        content_hex_list = [content_hex[i:i+2] for i in range(0, len(content_hex), 2)]
        
        # Replace the first 12 bytes with the new hexadecimal values
        for i in range(12):
            content_hex_list[i] = hex_values[i]
        
        # Reconvert the list of hexadecimal values into a string
        new_content_hex = ''.join(content_hex_list)
        
        # Reconvert the hexadecimal string into bytes
        new_content = bytes.fromhex(new_content_hex)
        
        # Write the new content into the file, overwriting the existing content
        bin_file.seek(0)
        bin_file.write(new_content)

if __name__ == "__main__":
    if len(sys.argv) != 14:
        print("Usage: python script.py <bin_file_path> <value1> <value2> <value3> <value4> <value5> <value6> <modifier1> <modifier2> <modifier3> <modifier4> <modifier5> <modifier6>")
        sys.exit(1)

    bin_file_path = sys.argv[1]
    values = sys.argv[2:14]

    replace_chars_in_bin_file(bin_file_path, values)
    print("Success: Bin file has been updated with new ascii characters.")
