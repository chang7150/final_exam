str1 = input("輸入單字")
str2 = input("輸入單字")
ans = []
Aans = ""
for i in str1:
    if i in ans:
        continue
    elif i in str2:
        ans.append(i)
if ans == "":
    ans.append("N")
    
Aans = "".join(sorted(ans))

print(f"重複的字母有{Aans}")