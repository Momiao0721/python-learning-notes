# 成绩等级（阶段测参考修正版）
score = float(input("请输入成绩："))

if score < 0 or score > 100:
    print("成绩不在0—100范围")
else:
    if score >= 90:
        print("等级：A")
    elif score >= 80:
        print("等级：B")
    elif score >= 60:
        print("等级：C")
    else:
        print("等级：D")
