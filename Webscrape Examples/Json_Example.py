f = open('nyt2.json',mode='r', encoding='UTF-8')
lines = f.readlines()
print(lines)

dict = {}
for line in lines:
    keyIndex = line.find('$oid":"')
    key = line[keyIndex+7:line.find('"}', keyIndex+1)]
    innerDict ={}
    index = line.find(',',line.find('"}', keyIndex+1))
    while index > 0:
        innerKey = line[index+2:line.find(':}',index+1)]
        valIndex = line.find(':',index+1)
        value = line[valIndex+1:line.find('}',valIndex+1)]
        innerDict.update({innerKey:value})
        index = line.find(',', index+1)
    dict.update({key:innerDict})
print(dict)

