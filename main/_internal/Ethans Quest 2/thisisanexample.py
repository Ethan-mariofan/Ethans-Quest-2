def parse_string(input: str) -> [str, str]:
    out = input.split(' ')
    return out[0], out[1]

a, b = parse_string('this is ham')
print(a)
print(b)
