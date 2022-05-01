#2 가장 높은 성적을 낸 학생의 이름과 성적을 출력
scores = [('Tony', 54), ('James', 14), ('Amy', 18), ('Timmy', 99), ('Chris', 87)]

x = 0 #현재 가장 높은 성적을 가지고 있는 학생이 몇 번째에 있는지
s = -1 #몇 번째 아이템을 확인하고 있는지

for n in scores:
  s = s + 1
  if scores[x][1] <= n[1]:
    x = s

print("가장 높은 점수를 받은 학생은 %s이고, 점수는 %d점이다." % scores[x])