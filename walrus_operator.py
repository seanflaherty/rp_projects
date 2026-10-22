
"""module docstring"""
def analyze_text(text: str) -> dict:
    """function docstring"""
    details: dict = {'words': (words := text.split()),
                     'amount': len(words),
                     'chars': len(''.join(words)),
                     'reversed': words[::-1]}
    return details

user_input: str = "Hello there!"

if (text := len(user_input)) > 5:
    print(text, 'All good.')
else:
    print(text, 'Please enter more text.')

def get_value():
    """function docstring"""
    return None

if var := get_value():
    print(var)
else:
    print('No value.')

print(analyze_text('Hi all, what\'s up?'))
