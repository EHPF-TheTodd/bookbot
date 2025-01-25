def main():
    file_contents = read_book_text("/home/thetodd/workspace/github.com/EHPF-TheTodd/bookbot/books/frankenstein.txt")
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"Word Count: {count_words(file_contents)}\n")
    char_count = count_characters(file_contents)
    sorted_characters = sorting(char_count)
    for i in sorted_characters:
        print(f"The '{i["character"]}' character was found {i["num"]} times")
    print("--- End report ---")

def read_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(read_contents):
    words = read_contents.split()
    return len(words)

def count_characters(read_contents):
    char_count = {}
    for character in read_contents.lower():
        if character in char_count:
            char_count[character] += 1
        else:
            char_count[character] = 1
    return char_count

def sorting(dictionary):
    dict_list = []
    for i in dictionary:
        if i.isalpha() == True:
            dict_list.append({"character": i, "num": dictionary[i]})
    sorted_list = sorted(dict_list, key=lambda d: d["character"])
    return sorted_list

main()