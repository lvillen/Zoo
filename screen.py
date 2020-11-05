def clear():
    print("\033[2J")

def locate(line, column):
    print("\033[{};{}H".format(line, column), end="")
    
if __name__ == '__main__':    
    clear()
    locate(5, 4)
    print("*")

    