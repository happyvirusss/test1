menus = {
    'bottle': [110, 30],
    'glass': [60, 35],
    'book': [310, 23],
    'phone': [90, 33],
    'dice': [155, 38],
    'mouse':[200, 45],
    'keyboard'[298, 65]:,
    'fan': [300, 36],


}
#obj_detected = {'bottle': [110, 30], 'glass': [60, 35], 'book': [310, 23], 'phone': [90, 33], 'dice': [155, 38], 'mouse':
[200, 45], 'keyboard': [298, 65], 'fan': [300, 36]}
menus.items()
sort_by_key = sorted(menus.items(), key=lambda x: x[0], reverse=False)
sort_by_key
from collections import OrderedDict

menus_by_name = OrderedDict(sort_by_key)
print(menus_by_name)
for k, v in menus_by_name.items():
    print(k, v)
menus.items()
sort_by_value = sorted(menus.items(), key=lambda x: x[1], reverse=False)
sort_by_value
menus_by_orders = OrderedDict(sort_by_value)
print(menus_by_orders)