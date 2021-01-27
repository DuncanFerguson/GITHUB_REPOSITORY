from urllib.request import Request, urlopen

url = "https://www.worldometers.info/coronavirus/"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
web_byte = urlopen(req).read()

webpage = web_byte.decode('utf-8')
print(webpage)

# item name starts at v-offer-click= ends at </a>
# price starts at <strong> ends at </strong>

dict = {}
itemIndex = webpage.find('v-offer-click=\'{"')
while itemIndex != -1:
    item = webpage[webpage.find('>',itemIndex+1)+1:
                   webpage.find('</a>', itemIndex)]
    print(item)
    amount = webpage[webpage.find('strong>$', itemIndex + 1) + 7:
                   webpage.find('</strong>', itemIndex+1)]
    print(amount)
    itemIndex = webpage.find('v-offer-click=\'{"', itemIndex+1)
    if len(item)>0 and len(amount)>0:
        dict[item] = amount
print(dict)