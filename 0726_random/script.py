import random
entrant = int(input('参加者は何名ですか？：'))
humans = {1:'you'}
# 辞書の追加と参加人数が合うようにする
humans[1] = str(input('あなたの名前：'))
x = 2
while  x <= entrant:
    humans[x] = str(input('参加者'+ str(x-1) +'人目の名前：'))
    x += 1
select = random.randint(1,len(humans))
print('今回選ばれたのは' + humans[select] + 'さんです')