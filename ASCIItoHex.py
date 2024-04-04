def ascii_to_hex(ascii_string):
 """
 Converts a string of ASCII characters to a space-separated hexadecimal string.

 Args:
     ascii_string: The string of ASCII characters to convert.

 Returns:
     A space-separated hexadecimal string representation of the ASCII characters.
 """

 hex_string = []
 for char in ascii_string:
   # Get the integer value of the ASCII character
   char_int = ord(char)
   # Convert the integer to lowercase hexadecimal string
   hex_char = hex(char_int).lower()[2:]
   # Add padding if necessary
   hex_char = hex_char.zfill(2)
   hex_string.append(hex_char)
 return " ".join(hex_string)

# Example usage
string = "Hello, world!"
hex_string = ascii_to_hex(string)
print(hex_string) 
