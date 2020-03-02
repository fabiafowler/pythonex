file = open ("newteams.txt","w")
teams = ['England','Wales','Ireland']
for team in teams:
    newfile = "\n".join(teams)
file.write(newfile)