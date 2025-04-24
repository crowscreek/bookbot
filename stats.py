


def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count ={}

    for char in text:
        char = char.lower()

        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count
def sorted_list(char_count):
    result = []

    for char, count in char_count.items():
        char_dict = {"char": char, "num": count}
        result.append(char_dict)
    result.sort(reverse=True, key =lambda d: d["num"])
    return result
