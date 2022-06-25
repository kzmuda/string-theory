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
    return len(clear_text(text)) == len(set(clear_text(text)))
    # 4
    # original_string = clear_text(text)
    # distinct_letters = set(original_string)
    # return len(original_string) == len(distinct_letters)
    # 3
    # distinct_letters = set()
    # for element in original_string:
    #     distinct_letters.add(element)
    # return len(original_string) == len(distinct_letters)

    # 2
    # used_letters = []
    # for element in original_string:
    #     if element in used_letters:
    #         return False
    #     used_letters.append(element)
    # return True
    # 1
    # for t in original_string:
    #     if original_string.count(t) > 1:
    #         return False
    # return True

    # 0
    # for i in original_string:
    #     counter = 0
    #     for x in original_string:
    #         if i == x:
    #             counter += 1
    #     if counter > 1:
    #         return False
    # return True

    # """
    # >>> is_isogram('uncopyrightables')
    # True
    # """


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