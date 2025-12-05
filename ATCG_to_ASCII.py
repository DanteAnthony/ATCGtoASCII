string = str(input("ATCG Segment: "))

def convert_atcg_to_binary(string):
    binary_string = ""
    for char in string:
        if char == 'A':
            binary_string += '0'
        elif char == 'T':
            binary_string += '0'
        elif char == 'C':
            binary_string += '1'
        elif char == 'G':
            binary_string += '1'
        else:
            raise ValueError("Input string must only contain 'A' 'T' 'C' and 'G' characters")
    return binary_string

def convert_binary_to_ascii(binary_string):
    if len(binary_string) % 8 != 0:
        raise ValueError("Binary string length must be multiple of 8")
    
    ascii_characters = []
    for i in range(0, len(binary_string), 8):
        binary_chunk = binary_string[i:i+8]
        decimal_value = int(binary_chunk, 2)
        ascii_character = chr(decimal_value)
        ascii_characters.append(ascii_character)
    return "".join(ascii_characters)

binary_data = convert_atcg_to_binary(string)
print(binary_data)
ascii_result = convert_binary_to_ascii(binary_data)
print(ascii_result)