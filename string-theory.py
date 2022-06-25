import string


def is_palindrome(text):
    text = clear_text(text)
    # for i in range(0,len(text)//2):
    #     if text[i] != text[-i-1]:
    #         return False
    # return True
    # backwards = text[::-1]
    return text[::-1] == text



def clear_text(text):
    # check = ["a", "b", "c"]
    text = text.lower()
    letters = []
    for char in text:
        if char in string.ascii_lowercase:
            letters.append(char)
    
    return letters    

def is_isogram(text):
    """
    >>> is_isogram('uncopyrightables')
    True
    """
    pass


def is_pangram(text):
    """
    >>> is_pangram('The quick brown fox jumps over the lazy dog')
    True
    """
    pass


def is_anagram(text1, text2):
    """
    >>> is_anagram('Justin Timberlake', "I'm a jerk but listen")
    True
    """
    pass


def is_blanagram(text1, text2):
    """
    >>> is_blanagram('Justin Timberlake', "I'm a berk but listen")
    True
    """
    pass
text = "Mr. Owl ate my metal worma"
print(is_palindrome(text))   