import urllib.request, json

with urllib.request.urlopen("https://2bqueue.info/queue") as url:
    queueCount = json.loads(url.read().decode())

with urllib.request.urlopen("https://2bqueue.info/players") as url:
    playerNames = json.loads(url.read().decode())

print('1: Queue Length')
print('2: Players in Queue')
print('3: Players in Server')
input = input('What would you like to do?')
if input == '1':
    print('Priority Queue Length: ' + str(queueCount['prio']))
    print('Regular Queue Length: ' + str(queueCount['regular']))
    print('Total Players in Queue: ' + str(queueCount['total']))
elif input == '2':
    print('Players in Regular Queue: ' + str(playerNames['queue']))
elif input == '3':
    print('Players in Server: ' + str(playerNames['server']))
else:
    print('That is not an option!')