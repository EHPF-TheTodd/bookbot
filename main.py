def count_words(read_contents):
    words = read_contents.split()
    total = 0
    for word in words:
        total += 1
    return total

def main():
    with open("/home/thetodd/workspace/github.com/EHPF-TheTodd/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)
    print(f"Word Count: {count_words(file_contents)}")

main()