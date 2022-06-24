def dec_to_bin(num):
    i = []
    while True:
        num, reminder = divmod(num, 3)
        i.append(str(reminder))
        if num == 0:
            break
    return "".join(i[::-1])
    
n = int(input("請輸入10進位正數字"))
print(dec_to_bin(n))