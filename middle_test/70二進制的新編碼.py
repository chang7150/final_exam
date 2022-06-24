data = input("請輸入要解密的數字")
judge = (len(data) - 2) * 2 
binary = 0
for i in data:
    i = int(i)
    if judge != 0:
        if i == 1:
            binary += judge
        judge -= 2   
    else:
        data = data[::-1]
        if data[0] == 0:
            pass
        else:
            binary + 1
ABC = {
    1:"D",
    2:"E",
    3:"F",
    4:"G",
    5:"H",
    6:"I",
    7:"J",
    8:"K",
    9:"L",
    10:"M",
    11:"N",
    12:"O",
    13:"P",
    14:"Q",
    15:"R",
    16:"S",
    17:"T",
    18:"U",
    19:"V",
    20:"W",
    21:"X",
    22:"Y",
    23:"Z",
    24:"A",
    25:"B",
    26:"C"
}
print(ABC[binary])