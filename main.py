import random
ap = ['琴','刻晴','迪卢克','莫娜','七七','提纳里','迪希雅']
up5 = "基尼奇"
up4 = ['夏沃蕾','九条裟罗','托马']
p3 = ['飞天御剑','冷刃','沐浴龙血的剑','黑缨枪','讨龙英杰谭','弹弓','鸦羽弓','黎明神剑','以理服人','铁影阔剑','翡玉法球','魔导绪论','神射手之誓']
tmp = ''
op = []
tmp = 0
count = 0
gt4 = 1
def app(t,b):
    if random.randint(0,1) == 1 or t == 2:
        b.append(up5)
    elif random.randint(0,1) == 1:
        b.append("".join(random.choice(ap)))
    else:
        b.append(up5)
for i in range(1000):
    list = []
    pb = [0.06,5.1,100]
    t = 0
    while ("".join(up5) in list) == False:
        tmp = int("".join(random.choices(['0','1','2'],weights=pb)))
        count += 1
        gt4 += 1
        if tmp == 0:
            t += 1
            app(t,list)
            pb[0] = 0.06
            count = 0
        if count > 73:
            pb[0] = 0.06+(count-73)*6
        if tmp == 1:
            list.append(random.choice(up4))
            gt4 = 1
        if tmp == 2:
            list.append(random.choice(p3))
        if gt4 == 9:
            pb[1] = 56
        if gt4 == 10:
            list.append(random.choice(up4))
            gt4 = 1
            pb[1] = 5.1
        if count == 90:
            pb[0] = 0.06
            t += 1
            app(t,list)
            count == 0
    op.append(len(list))
print(sum(op) / len(op))