#!/usr/bin/env python3
import sys

def replace_chars_in_bin_file(bin_file_path, values):
    if len(values) != 6:
        raise ValueError("Exactly 6 characters or hex values are required.")
    
    hex_values = []
    for value in values:
        if value.startswith("0x"):
            # Si la valeur commence par "0x", on suppose que c'est une valeur hexadécimale
            hex_value = value[2:]
            if len(hex_value) != 2:
                raise ValueError(f"Invalid hex value: {value}")
        else:
            # Sinon, c'est un caractère ASCII, on le convertit en hexadécimal
            hex_value = format(ord(value), '02x')
        
        hex_values.append(hex_value)

    with open(bin_file_path, 'rb+') as bin_file:
        # Lire le contenu existant du fichier
        content = bin_file.read()
        
        # Convertir le contenu en une liste modifiable de valeurs hexadécimales
        content_hex = content.hex()
        content_hex_list = [content_hex[i:i+2] for i in range(0, len(content_hex), 2)]
        
        # Remplacer les 6 premiers octets par les nouvelles valeurs hexadécimales
        for i in range(6):
            content_hex_list[i] = hex_values[i]
        
        # Reconvertir la liste de valeurs hexadécimales en une chaîne de caractères
        new_content_hex = ''.join(content_hex_list)
        
        # Reconvertir la chaîne de caractères hexadécimaux en bytes
        new_content = bytes.fromhex(new_content_hex)
        
        # Écrire le nouveau contenu dans le fichier en écrasant le contenu existant
        bin_file.seek(0)
        bin_file.write(new_content)

if __name__ == "__main__":
    if len(sys.argv) != 8:
        print("Usage: python script.py <bin_file_path> <value1> <value2> <value3> <value4> <value5> <value6>")
        sys.exit(1)

    bin_file_path = sys.argv[1]
    values = sys.argv[2:8]

    replace_chars_in_bin_file(bin_file_path, values)
    print("Success: Bin file has been updated with new ascii characters.")
