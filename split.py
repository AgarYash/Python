def split(a,b):
    word = ""
    num = 0
    a += b
    l = len(a)
    substr_list = []
    for i in range(l):
        if (a[i] != b):
            word += a[i]
        else:
            if (len(word) != 0):
                substr_list.append(word)
            word = ""
    return substr_list
if __name__ == '__main__':
    str = "YASH-AGARWAL-MCA-D2010"
    c = '-'
    res = split(str, c)
    for x in range(len(res)):
        print(res[x])
