def nbr_of_words(cont):
    print(len(cont.split()))

def char_count(cont):
    myd = {}
    for c in cont:
        c = c.lower()
        if not c.isalpha():
            continue
        if c in myd:
            myd[c] += 1
        else:
            myd[c] = 1
    #print(myd)
    return myd

def report(cont):
    myd = char_count(cont)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{nbr_of_words} words found in the document")
    for key, value in myd.items():
        print(f"The '{key}' character was found {value} times")

    print("--- End report ---")

def main():
    with open("books/frankenstein.txt") as f:
              cont = f.read()
    #print(cont)
    #print(nbr_of_words(cont))
    #char_count(cont)
    report(cont)

if __name__ == "__main__":
    main()
