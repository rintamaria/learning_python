speed={'jan':47,'feb':52,'march':47,'april':44,'may':52,'june':53,'july':54,'sept':54}
print("dictionary values",speed.values())
speedlist=list()
for i in speed.values():
    if i not in speedlist:
        speedlist.append(i)
print(speedlist)