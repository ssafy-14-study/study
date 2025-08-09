while True:
    try:
        a = input()
        up, low, empty, num = 0, 0, 0, 0
        for str_ in a:
            if str_.isupper():
                    up += 1
            elif str_.islower():
                    low += 1
            elif str_ == " ":
                    empty += 1
            elif str_.isdigit():
                    num += 1
            
        print(low, up, num, empty)
    except EOFError:
          break