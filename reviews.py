data = [] #
count = 0
with open ('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count = count + 1
        if count % 1000 == 0:
            print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')

#加總留言長度
sum_len = 0
for word in data:
    sum_len = sum_len + len(word)

#平均留言長度
print('平均是', sum_len/len(data))

#篩選小於100字的留言
new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '筆留言長度小於100')

#印出長度小於100字的留言中的第一筆
print(new[0])

#篩選所有有good的留言
good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有', len(good), '筆留言提到good')
print(good[0])