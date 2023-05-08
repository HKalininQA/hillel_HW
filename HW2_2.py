casino_blacklist = {'John Doe', 'Mark Hammer', 'Max Mironov', 'Igor Ryabtsev', 'Mark Martsun', 'Vlad Bowser'}
poker_blacklist = {'Mark Martsun', 'Irina Smith', 'Mark Hammer', 'Rebecca Saints', 'Igor Ryabtsev'}
alcohol_blacklist = {'Irina Smith', 'Mark Martsun', 'Rebecca Saints', 'John Doe', 'Mark Hammer'}

#First approach to resolve this task
#blacklist = (set(casino_blacklist) & set(poker_blacklist) & set(alcohol_blacklist))
#print(blacklist)

#Second approach to resolve this task
blacklist = casino_blacklist.intersection(poker_blacklist, alcohol_blacklist)
print(blacklist)

