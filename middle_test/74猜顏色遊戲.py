chance = 0
while chance != 10:
    respond = ""
    ans = ["red","blue","red","green"]
    guess = input("開始猜測\n").split()
    for i in range(4):
        if guess[i] in ans:
            if guess[i] == ans[i]:
                respond += "1"
            else:
                respond += "2"
        else:
            respond += "3"
    print(respond)
    if respond == "1111":
        print("挑戰成功")
        exit()
print("挑戰失敗")