capacity = int(input())
command = input()
messages = {}
while command != 'Statistics':
    command = command.split('=')
    if 'Add' in command:
        username = command[1]
        sent = int(command[2])
        received = int(command[3])
        if username not in messages:
            messages[username] = []
            messages[username].append(sent)
            messages[username].append(received)
    elif 'Message' in command:
        sender = command[1]
        receiver = command[2]
        if sender in messages and receiver in messages:
            messages[sender][0] += 1
            messages[receiver][1] += 1
            if messages[sender][0] + messages[sender][1] >= capacity:
                messages.pop(sender)
                print(f"{sender} reached the capacity!")
            if messages[receiver][1] + messages[receiver][0] >= capacity:
                messages.pop(receiver)
                print(f"{receiver} reached the capacity!")
    elif 'Empty' in command:
        username = command[1]
        if username == 'All':
            messages = {}
        elif username in messages:
            messages.pop(username)
    command = input()

print(f'Users count: {len(messages)}')
if len(messages) >0:
    for username in messages:
        print(f'{username} - {messages[username][0]+messages[username][1]}')