import random

def convert_ascii_to_binary(text):
    binary_string = ""
    for char in text:
        ascii_value = ord(char)
        binary_chunk = format(ascii_value, '08b')  # 8-bit binary
        binary_string += binary_chunk
    return binary_string

def convert_binary_to_atcg(binary_string):
    if any(bit not in '01' for bit in binary_string):
        raise ValueError("Binary string must contain only 0s and 1s")

    atcg_string = ""
    for bit in binary_string:
        if bit == '0':
            atcg_string += random.choice(['A', 'T'])
        elif bit == '1':
            atcg_string += random.choice(['C', 'G'])
    return atcg_string

text = input("ASCII Text: ").strip()

binary_data = convert_ascii_to_binary(text)
print(f"Binary: {binary_data}")
atcg_result = convert_binary_to_atcg(binary_data)
print(f"ATCG: {atcg_result}")