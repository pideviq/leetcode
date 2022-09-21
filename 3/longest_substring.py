def longest_substring(s: str) -> int:
    substr: str = ''
    max_length: int = 0
    for char in s:
        if char not in substr:
            substr += char
        else:
            max_length = max(max_length, len(substr))
            duplicate_index = substr.index(char)
            substr = substr[duplicate_index + 1:] + char
    return max(max_length, len(substr))
