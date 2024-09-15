import os

l='# Changelog List(Use `>changelog <Version>` to see details.):\n'
files = [f for f in os.listdir(r'changelog') if os.path.isfile(os.path.join(r'changelog', f))]
for i in files:
    l=l+'- '+i[10:16]+'\n'
print(l)

