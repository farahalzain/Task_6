lst = [30, 75, 9, 97, 50, -4, 59]
lst.sort(reverse=True)
print(lst[0])
print("*"*50)
lst.pop()
print(lst)
print("*"*25)
lst.sort()
print(lst)
print("*"*25)
print(lst[2:])
print("*"*50)

main_lst = [["python", 3], [5, 7.8], ["python", 11], ["python", 1]]
count = 0
for item in main_lst:
    for j in item:
        if j == "python":
            count += 1
print(count)
print("*"*50)

my_lst = ["I", "Love", "GAZa", "sKy", "GEEKs"]
print(' '.join(my_lst))
print("*"*50)


my_list = [12, 3.8, "GSG", ["sky", "zak"]]
new_list = []
for i in my_list:
    new_list.append(i)
print(new_list)
print("*"*50)

my_lst = ["GSG", "Zakaria", 19 , 9.8 ,"Omer"]
X = my_lst[2]
my_lst[2] = my_lst[4]
my_lst[4] = X
print(my_lst)
print("*"*50)

nums = [33, 5.9, 6, -43, 9, 7, 39, 0,-40]
Sum = sum(nums)
print(Sum)
print("*"*50)

tuple1 = (4,"python" , "GSG", [8,3,1])
tuple1 = tuple1 + (9,)
print(tuple1)
print("*"*50)

tuple1 = (4,"python" , "GSG", [8,3,1])
tuple2 = ("java", "C++" ,7.8)
new_tuple = tuple1 +tuple2
print(new_tuple)
print("*"*50)