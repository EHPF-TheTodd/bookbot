def main():
    file_contents = read_book_text("/home/thetodd/workspace/github.com/EHPF-TheTodd/bookbot/books/frankenstein.txt")
    print(file_contents)
    print(f"Word Count: {count_words(file_contents)}")

def read_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(read_contents):
    words = read_contents.split()
    return len(words)

main()