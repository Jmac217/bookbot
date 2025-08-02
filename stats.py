def get_num_words(book_text):
    return len(book_text.split())

def get_letter_frequency(book_text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    count = {}
    for letter in alphabet:
        count[letter] = 0
    
    for char in book_text:
        lower_case = char.lower()
        if lower_case in alphabet:
            count[lower_case] += 1
    return count

def sort_letter_frequency(count_dict, decending=True):
    result = []
    for letter in count_dict:
        count = count_dict[letter]
        result.append({"char": letter, "num": count})
    def sort_on(items):
        return items["num"]
    result.sort(key=sort_on, reverse=decending)
    return result
