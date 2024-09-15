import json

with open(r'K:\Megumin\extensions\RPG\data\StandardData.json','r',encoding='utf-8') as f:
    data=json.load(f)

def StandardUserData():
    return data['StandardUserData']