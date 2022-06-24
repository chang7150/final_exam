s1 = "紅豆生南國，春來發幾枝？願君多采擷，此物最相思。"
s2 = "春眠不覺曉，處處聞啼鳥。夜來風雨聲，花落知多少。"
res = set()
for i in range(len(s1)):
    if s1[i] in s2 and s1[i] != '，' and s1[i] != '。':
        res.add(s1[i])
print(res)