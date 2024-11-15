def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        
        for line in file_contents.splitlines():
            print(line)

main()
