def convert_atcg_to_binary(seq: str) -> str:
    mapping = {
        'A': '0',
        'T': '0',
        'C': '1',
        'G': '1'
    }
    try:
        return "".join(mapping[nuc] for nuc in seq.upper())
    except KeyError:
        raise ValueError("Input string must only contain A, T, C, and G.")

def convert_binary_to_ascii(binary_string: str) -> str:
    if len(binary_string) % 8 != 0:
        raise ValueError("Binary string length must be a multiple of 8.")

    chars = [
        chr(int(binary_string[i:i+8], 2))
        for i in range(0, len(binary_string), 8)
    ]
    return "".join(chars)

text = input("ATCG: ").strip()

binary_data = convert_atcg_to_binary(text)
print(f"Binary: {binary_data}")
ascii_result = convert_binary_to_ascii(binary_data)
print(f"ASCII:  {ascii_result}")