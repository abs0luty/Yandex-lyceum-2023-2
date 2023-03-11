url = input()
for i in url.split('/'):
    if '#' in i:
        print(i[:i.find('#')])
