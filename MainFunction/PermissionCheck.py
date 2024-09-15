import json
from MainFunction import SetUp

with open(r'K:\Megumin\data\Memberpermissions.json', 'r',encoding='utf-8') as file:
    Memberpermissions = json.load(file)

def check(Category, Options, role, user):
    if SetUp.CheckValue(Category, Options):
        return role in Memberpermissions.get(user, [])
    return True

def checkrole(role,user):
    if role in Memberpermissions[user]:
        return True
    else:
        return False
