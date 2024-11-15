def word_count(file):
    count = 0
    current_words = []

    try:
        for line in file.splitlines():
            if (line.find("*** START") == -1):
                continue 
            elif (line.isspace() == True):
                continue
            elif (line.find("*** END") == -1):
                pass
            else:
                break


    except Exception as e:
        print(e)


    return count

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
        print(file_contents)
        print(f"There are {word_count(file_contents)} words in the book")

main()
