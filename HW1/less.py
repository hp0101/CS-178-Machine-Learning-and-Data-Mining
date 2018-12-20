def test(a,b):
    if b == 0:
        return 0
    return test(a,b-1) + a

if __name__ == "__main__":
    while(True):
        a = int(raw_input())
        b = int(raw_input())
        print(test(a,b))
    
