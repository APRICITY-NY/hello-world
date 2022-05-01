#1 평균 구하기
scores = [78, 89, 43, 25, 64, 75, 93, 82, 87, 99]

x = 0 #the number of student over than score 80
s = 0 #sum of scores over than 80

for n in scores:
    if n >= 80:
        s = s + n
        x = x + 1
s = s/x

print("80점 이상인 학생은 %d명이고, 평균은 %.1f점이다." % (x, float(s)))