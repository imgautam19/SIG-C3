def merge_the_tools(string, k): 
    x = len(string)
    lst = []
    g = []
    for i in range(0,x,k):
        a = ""
        for j in range(k):
            a = a + string[i+j]
        lst.append(a)
        
    for word in lst:
        b = ""
        for j in range(k):
            if word[j] not in b:
                b = b + word[j]
        print(b)