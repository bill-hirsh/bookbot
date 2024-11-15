def word_count(file):
    count = 0

    try:
        for line in file:
            if (line.isspace() == True):
                continue
            else:

                words = line.split(" ")
                print(words)
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
        
        # for line in file_contents:
        #     print(line)

        print(f"There are {word_count(file_contents)} words in the book")

main()
