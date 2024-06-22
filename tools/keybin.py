#!/usr/bin/env python3
import sys

def replace_chars_in_bin_file(bin_file_path, chars):
    if len(chars) != 6:
        raise ValueError("Exactly 6 characters are required.")
    
    hex_values = [format(ord(char), '02x') for char in chars]

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
        print("Usage: python script.py <bin_file_path> <char1> <char2> <char3> <char4> <char5> <char6>")
        sys.exit(1)

    bin_file_path = sys.argv[1]
    chars = sys.argv[2:8]

    replace_chars_in_bin_file(bin_file_path, chars)
    print("Bin file has been updated with new ascii characters.")

