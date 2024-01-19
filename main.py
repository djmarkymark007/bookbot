def main():
    file_name = "books/frankenstein.txt"
    try:
        with open(file_name) as f:
            file_contents = f.read()
            word_count = get_count_word(file_contents)
            letter_count = get_letter_count(file_contents)
            print_report(file_name, word_count, letter_count)

    except Exception as e:
        print(e)

def get_count_word(text):
    words = text.split()
    return len(words) 

def get_letter_count(text):
    lower_text = text.lower()
    letter_count = {}
    for letter in lower_text:
        if letter_count.get(letter):
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

def print_report(file_name, word_count , letter_count):
    print(f"--- Begin report of {file_name} ---")
    print(f"{word_count} words found in the document\n")
    
    sorted_letters = list(letter_count)
    sorted_letters.sort()
    for letter in sorted_letters:
        if letter.isalpha():
            print(f"The '{letter}' character was found {letter_count[letter]} times")
    
    print("--- End report ---")


if __name__ == '__main__':
    main()