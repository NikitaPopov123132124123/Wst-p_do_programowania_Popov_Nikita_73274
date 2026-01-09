def reverse_string(s: str) -> str:
    result = ""
    for char in s:
        result = char + result
    return result

print(reverse_string("Hello"))
