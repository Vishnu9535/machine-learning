import re
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if(len(s) < 2 or len(s) > 6 or s[0:2].isdigit()):
        return False
    pattern = r"(?=.*[a-zA-Z])(?=.*\d)"
    if(re.search(pattern, s)):
        if(s[-1].isalpha()):
            return False
        for i in s:
            if(i.isdigit()):
                if(i == "0"):
                   return False
                break
    if(s.isalnum()):
        return True
    else:
        return False

main()