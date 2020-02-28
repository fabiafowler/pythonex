for i in range (10,20,1):
    print(i)

for i in range (20,10,-1):
    print(i)

front_row = ['osman','paul', 'mark','mike','alex','julie']
middle_row = ['gene','catherine','john','salem'] 

 
group = [front_row, middle_row]
for name in front_row:
    print(name)

front_row[3]="Tim"
print(list(front_row))

front_row.append("fabia")
print(list(front_row))

for name in front_row:
    print(name)

for name in group:
    print(name)