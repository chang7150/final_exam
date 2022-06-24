n = int(input("輸入n值:"))
t = {}
for i in range(n):
    name = input("請輸入姓名:")
    mail = input("請輸入電子郵件:")
    t[name] = mail
select = input("請輸入要查詢電子郵件的姓名:")
print(f"{select} 電子郵件帳號為{t[select]}")