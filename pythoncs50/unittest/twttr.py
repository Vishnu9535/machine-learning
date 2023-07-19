def main():
    name=str(input("Input: "))
    output=shorten(name)
    print(output)

def shorten(word):
    
    vovels="aeiouAEIOU"
    output=""
    for i in word:
        if i not in vovels:
            output=output+i
    return output


if __name__ == "__main__":
    main()