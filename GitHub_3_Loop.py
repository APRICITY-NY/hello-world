#3-1 사용자가 입력한 숫자보다 작은 숫자로 리스트 만들기

# (a) 리스트 a가 [1,2,1,8,9,4,2,5,1,3]로 초기화 되어 있습니다.
# (b) 사용자로부터 정수 하나를 입력받습니다.
# (c) 리스트 a의 아이템 중 사용자가 입력한 숫자보다 작은 숫자를 모두 출력하는 프로그램을 구현합니다.
# (d) 이때, 출력할 숫자를 하나씩 출력하지 말고, 해당되는 숫자들을 모아 새로운 list를 만들어서 그 list를 출력하게 만듭니다. 

a = [1,2,1,8,9,4,2,5,1,3]
b = []

userInt = int(input("Enter the integer: "))

for i in a:
    if userInt > i:
        b.append(i)

print(b)

#3-2 두 개의 리스트 병합하여 중복된 아이템이 없는 새로운 리스트 만들기

# (a) 두 개의 list a와 b를 다음과 같이 정의합니다.
# (b) a = [1,1,2,3,5,8,13,24,34,55]
# (c) b = [1,1,2,3,4,5,6,7,8,9,10,11,12]
# (d) 두 list에 모두 포함되는 요소(element)를 모아서, 중복되는 요소가 없는 새로운 리스트 c를 만든 후, 결과를 출력합니다.

lista = [1,1,2,3,5,8,13,24,34,55]
listb = [1,1,2,3,4,5,6,7,8,9,10,11,12]
listc = []

for item_a in lista:
    if item_a not in listc:
        listc.append(item_a)
    
for item_b in listb:
    if item_b not in listc:
        listc.append(item_b)

print(listc)