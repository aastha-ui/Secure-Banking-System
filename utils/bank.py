import json

def save(users,file):
    with open(file,'w') as f:
        json.dump(users,f,indent=2)

def menu(user,file):
    while True:
        with open(file,'r') as f:
            users=json.load(f)

        print('\n1.Deposit 2.Withdraw 3.Balance 4.History 5.Logout')
        c=input('Choice: ')

        if c=='1':
            amt=float(input('Amount: '))
            users[user]['balance']+=amt
            users[user]['history'].append(f'Deposit {amt}')
            save(users,file)

        elif c=='2':
            amt=float(input('Amount: '))
            if amt<=users[user]['balance']:
                users[user]['balance']-=amt
                users[user]['history'].append(f'Withdraw {amt}')
                save(users,file)

        elif c=='3':
            print('Balance:',users[user]['balance'])

        elif c=='4':
            print(*users[user]['history'],sep='\n')

        elif c=='5':
            break
