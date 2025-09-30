import json

with open(r'data\SetUp.json', 'r', encoding='utf-8') as file:
    SetUp = json.load(file)

def CheckValue(Category, Options):
    try:
        return SetUp[Category][Options]
    except Exception:
        return None

def ChangeValue(Category, Options, Value):
    if Category not in SetUp:
        return f"[Error] Category '{Category}' not found in SetUp."
    
    if Options not in SetUp[Category]:
        return f"[Error] Option '{Options}' not found in Category '{Category}'."
    
    previous = SetUp[Category][Options]
    changed = False

    if Value=="True":
        SetUp[Category][Options] = True
        changed = True
    elif Value=="False":
        SetUp[Category][Options] = False
        changed = True
    else:
        try:
            Value = float(Value)
            if isinstance(SetUp[Category][Options], float):
                SetUp[Category][Options] = Value
                changed = True
        except ValueError:
            if isinstance(SetUp[Category][Options], str):
                SetUp[Category][Options] = Value
                changed = True
    if changed:
        with open(r'data\SetUp.json', 'w', encoding='utf-8') as file:
            json.dump(SetUp, file, indent=4)
        message = f"The Value of {Options} in {Category} is changed to {Value}. (Original value: {previous})"
    else:
        message = f"[TypeError] Change failed!\nThe Value of {Options} in {Category} is {type(SetUp[Category][Options])}, not {type(Value)}."
    return message

def list():
    setuplist='# Available Setup Value:\n'
    setuphelp=open(r'data\setuphelp.txt', 'r', encoding='utf-8')
    for i in SetUp:
        setuplist+='## '+i+':\n'
        for j in SetUp[i]:
            setuplist+='### '+j+f'(Current Value:{CheckValue(i,j)})'+':\n'
            setuplist+=setuphelp.readline()+'\n'
    setuphelp.close()

    return setuplist

