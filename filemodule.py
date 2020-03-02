file = open("teams.txt","r")

for i in range(5):
    line = file.readline()
    if i == 0:
        print(line)
    if i == 3:
        print(line)

file = open("teams.txt","r+")

newfile= []
for i in range(5):
    if i != 0:
        newfile.append(file.readline())
    else:
        file.readline()
print(newfile)
newfile="".join(newfile)

file = open("teams.txt", "w")
file.write(newfile)
file.close()