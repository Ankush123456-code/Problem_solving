def my_gen(ls):
    print("hi")
    for i in ls:
        if i % 2 == 0:
            yield i


ls = [20, 58, 97, 12]
for i in my_gen(ls):
    print(i)
