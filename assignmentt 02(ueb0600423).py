
def to_lowercase(s):
    return s.lower()

def swap_case(s):
    return s.swapcase()

def remove_uppercase(s):
    return ''.join(ch for ch in s if not ch.isupper())

def count_case(s):
    upper = sum(1 for ch in s if ch.isupper())
    lower = sum(1 for ch in s if ch.islower())
    return f"Uppercase: {upper}, Lowercase: {lower}"

def remove_non_letters(s):
    return ''.join(ch for ch in s if ch.isalpha())

def triangle_area(a, b, c):
    # Validate sides first (triangle inequality + positive lengths)
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Sides must be positive numbers.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Invalid triangle: sides do not satisfy triangle inequality.")
    p = (a + b + c) / 2.0
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def format_names(names):
    names = [n.strip() for n in names if n.strip()]
    if not names:
        print("No names provided.")
        return
    width = max(len(n) for n in names) + 4
