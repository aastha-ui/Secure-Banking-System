import json, hashlib, re

failed = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def strong(password):
    return (len(password)>=8 and
            re.search(r'[A-Z]', password) and
            re.search(r'[a-z]', password) and
            re.search(r'\d', password))

def create_account(file):
    with open(file,'r') as f:
        users=json.load(f)

    u=input('Username: ')
    p=input('Password: ')

    if not strong(p):
        print('Weak password')
        return

    users[u]={'password':hash_password(p),'balance':0,'history':[]}

    with open(file,'w') as f:
        json.dump(users,f,indent=2)

    print('Account created')

def login(file):
    with open(file,'r') as f:
        users=json.load(f)

    u=input('Username: ')
    p=input('Password: ')

    if failed.get(u,0)>=3:
        print('Account locked')
        return None

    if u in users and users[u]['password']==hash_password(p):
        failed[u]=0
        return u

    failed[u]=failed.get(u,0)+1
    print('Invalid credentials')
    return None
