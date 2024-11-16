def letter_count(file):
    letter_dict = {}

    try:
        for line in file:
            if (line.isspace() == True):
                continue
            else:
                for letter in line:
                    if(letter.isalpha() == True):
                        letter = letter.lower()
                        x = letter_dict.get(letter, 0)
                        letter_dict[letter] = x + 1
                    else:
                        continue

    except Exception as e:
        print(e)

    return letter_dict

def word_count(file):
    count = 0

    try:
        for line in file:
            if (line.isspace() == True):
                continue
            else:

                words = line.split(" ")
                for word in words:
                        if (word == ""):
                            continue
                        count += 1

    except Exception as e:
        print(e)


    return count

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.readlines()

        print(f"There are {word_count(file_contents)} words in the book")
        
        for letter, count in letter_count(file_contents).items():
            print(f"The {letter} character was found {count} times")

main()
