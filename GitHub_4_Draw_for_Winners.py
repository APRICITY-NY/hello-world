#4 random함수를 사용하여 당첨자 뽑기

from random import *
users = range(1,21)
users = list(users)
shuffle(users)
winners = sample(users, 4)
print("A 당첨자 : {0}".format(winners[0]))
print("B 당첨자 : {0}".format(winners[1:]))