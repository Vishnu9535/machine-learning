from test import square

def main():
    test_square()

def test_square():
    # if square(2) == 4:
    #     print("it was right")
    # if square(4) != 16:
    #     print("even this was wrong ")
    try:
        assert square(2) != 4
    except AssertionError:
        print("2 squared is 4")
    try:
        assert square(3) == 9
    except:
        print("3 squard is not 9")

    try:
        assert square(4) == 14
    except:
        print("4 square is not 14")


if __name__== "__main__":
    main()
