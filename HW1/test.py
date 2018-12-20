if __name__ == "__main__":
    while(True):
        num = int(raw_input())
        if num == -999:
            break
        l = 1
        for x in range(1,num+1):
            l = l * x
        print "answer = " + str(l)
        print


