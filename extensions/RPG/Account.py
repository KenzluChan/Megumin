import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
from RPG import Get

def read():
    with open(r"K:\Megumin\extensions\RPG\data\UserData.json","r",encoding='utf-8') as f:
        return json.load(f)

def register(name):
    print(f'Registering...(Account:{name})')
    d = read()  # 從資料庫讀取現有的用戶資料
    print(d, name)
    print(name in d)  # 檢查用戶名是否已存在於資料庫中
    
    if name in d:
        # 如果用戶名已存在，顯示錯誤信息並返回 False
        print('Register fail: Registered')
        print(f'{name}\'s Data: {d[name]}')
        return False
    
    # 如果用戶名不存在，註冊新用戶
    d[name] = Get.StandardUserData()
    write(d)  # 將更新後的資料寫入資料庫
    print('Register done.')
    return True


def write(d):
    with open(r"K:\Megumin\extensions\RPG\data\UserData.json","w",coding='utf-8') as f:
        json.dumps(d,f, indent=4, ensure_ascii=False)