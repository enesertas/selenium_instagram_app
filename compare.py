file = open("followers.txt", "r", encoding="UTF-8")
lines = file.readlines()
file2 = open("followings.txt", "r", encoding="UTF-8")
lines2 = file2.readlines()
count = 0
printed = []
for line in lines2:
    if(line not in lines):
        if(line not in printed):
            print(line)
            printed.append(line)
            count += 1
print(count)
print("Total of people don't follow you back.")
