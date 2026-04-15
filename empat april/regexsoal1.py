# You can use Regex - Optional
import re
def sorting_string(paragraph):
    paragraph = paragraph.replace(" ", "")
    
    capital_letter = ""
    small_letter = ""
    number = ""
    
    for char in paragraph:
        if char.isupper():
            capital_letter += char
        elif char.islower():
            small_letter += char
        elif char.isdigit():
            number += char
    
    return small_letter + capital_letter + number
# Write your function and logic there

if __name__ == "__main__":
    stript = str(input())
    print(sorting_string(stript))