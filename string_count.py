test_str = "yash06101999@gmail.com"
freq = {}
for i in test_str:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print ("Count of all characters in yash06101999@gmail.com is :\n "
+ str(freq))

