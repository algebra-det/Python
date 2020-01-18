def add():
    print("from add "+__name__)

def sub():
    print("from sub")

def main():
    print("From calc main")
    add()
    sub()

if __name__=="__main__":
    main()