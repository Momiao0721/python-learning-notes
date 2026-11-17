# 第17—26课：输入输出、运算符与 if

## 1. 输入与类型转换

```python
age = int(input("请输入年龄："))
price = float(input("请输入价格："))
```

- `input()` 返回字符串
- `int()` 转整数
- `float()` 转小数

## 2. 赋值与比较

```python
a = 10      # 赋值
a == 10     # 判断是否相等
```

- `=` 是赋值
- `==` 是比较

## 3. 算术运算符

```python
+  -  *  /  //  %  **
```

例如：

```python
print(7 // 2)   # 3
print(7 % 2)    # 1
print(2 ** 3)   # 8
```

## 4. 比较与逻辑运算符

```python
>  <  >=  <=  ==  !=
and  or  not
```

## 5. if / elif / else

```python
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 60:
    print("C")
else:
    print("D")
```

从上往下判断，只会执行第一个成立的分支。

## 6. 常见错误

### 成绩 90 分边界

错误：

```python
if score > 90:
```

正确：

```python
if score >= 90:
```

### 区间空档

```python
elif 80 <= score <= 89:
```

会漏掉 89.5 这种小数。  
更稳的写法：

```python
elif score >= 80:
```

### 两个独立的 if 链

错误结构：

```python
if op == "+":
    print("结果")
elif op == "-":
    print("结果")

if op == "/":
    ...
else:
    print("运算符错误")
```

输入 `+` 时，第二个链的 `else` 也可能执行。  
互斥条件必须放进同一个 `if/elif/else` 链。

## 7. 本阶段结论

- 会输入、会转换类型
- 会算术、比较、逻辑运算
- 会写互斥的 if/elif/else
- 下一步：match、while、for
