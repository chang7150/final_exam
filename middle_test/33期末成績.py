subject = ["國文", "英文", "微積分", "體育", "程式設計"]
score = [int(input("國文：")), int(input("英文：")), int(input("微積分：")), int(input("體育：")), int(input("程式設計："))]
maxnum = max(score)
minnum = min(score)
avg = sum(score)/5
print("平均分數：%.2f"%avg)
print(f"最高分科目：{subject[score.index(maxnum)]}{maxnum}分")
print(f"最低分科目：{subject[score.index(minnum)]}{minnum}分")