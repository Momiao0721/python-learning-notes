# 简单计算器（阶段测参考修正版）
one = float(input("请输入第一个数："))
two = float(input("请输入第二个数："))
op = input("请输入运算符（+ - * /）：").strip()

if op == "+":
    print(f"结果：{one + two:g}")
elif op == "-":
    print(f"结果：{one - two:g}")
elif op == "*":
    print(f"结果：{one * two:g}")
elif op == "/":
    if two == 0:
        print("除数不能为0")
    else:
        print(f"结果：{one / two:g}")
else:
    print("运算符错误")
