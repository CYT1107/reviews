data = [] #
count = 0
with open ('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count = count + 1
        if count % 1000 == 0:
            print(len(data))
print(len(data)) #印出留言筆數
print(data[0]) #印出第一筆