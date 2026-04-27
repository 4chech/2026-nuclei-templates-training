with open("swollen_username_list.txt", "r") as f:
    lines = f.readlines()


new_lines = []
for line in lines:
    temp = line
    for i in range(1,10):
        new_lines.append(temp)

with open("swollen_username_list.txt", "w") as f:
    f.truncate(0)

with open("swollen_username_list.txt", "w") as f:
    f.writelines(new_lines)