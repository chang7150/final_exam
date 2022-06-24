data = {
    "-----":"0",
    ".----":"1",
    "..---":"2",
    "...--":"3",
    "....-":"4",
    ".....":"5",
    "-....":"6",
    "--...":"7",
    "---..":"8",
    "----.":"9",
}
judge = str(input("請輸入摩斯密碼")).split()

ans = ""
i = 0

while i <= len(judge) - 1:
    str_ = judge[i]
    print(str_)
    ans += data[str_]
    
    i += 1
print(ans)

