
def words_count(string:str) -> int:
    return len(string.split())

def letters_count(string) -> dict:
    letters_dict = {}

    for letter in string.lower():
        if letter.isalpha():
            if letter in letters_dict:
                letters_dict[letter] += 1
            else:
                letters_dict[letter] = 1
    
    return letters_dict

path_to_book = "/books/frankenstein.txt"
with open(f".{path_to_book}") as f:
    file_contents = f.read()
    print(f"--- Begin report of books {path_to_book} ---")
    print(f"{words_count(file_contents)} words found in the document\n")
    
    for c_count in sorted(letters_count(file_contents).items(), key=lambda x:x[1],reverse = True):
        print(f"The '{c_count[0]}' character was found {c_count[1]} times")

    