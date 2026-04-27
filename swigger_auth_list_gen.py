with open('passwords.txt', 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines, start=1):
    new_lines.append(line)
    if i % 2 == 0:
        new_lines.append("peter\n")

with open('passwords.txt', 'w') as f:
    f.writelines(new_lines)

lines = []
for i in range(1, 101):
    lines.append('carlos\n')
    if i % 2 == 0:
        lines.append("wiener\n")

with open('usernames.txt', 'w') as f:
    f.writelines(lines)