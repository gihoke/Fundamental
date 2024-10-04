widget_sales = [
    
    {'name' : 'widget1' , 'sales': 10},
    {'name' : 'widget2' , 'sales': 5},
    {'name' : 'widget3' , 'sales': 0}
    
    ]


sales_by_widget = {}

for widget in widget_sales:
    name = widget['name']
    sales = widget['sales']
    sales_by_widget[name] = sales
    
print(sales_by_widget)

print("-"*20)

sales_by_widget = {widget['name'] : widget['sales'] for widget in widget_sales}
print(sales_by_widget)

print("-"*20)

sbw = {}

for d in widget_sales:
    if d['sales'] > 0:
        name = d['name']
        sales = d['sales']
        sbw[name] = sales
    
    
print(sbw)

print("-"*20)

sbw = {d['name']:d['sales'] for d in widget_sales if d['sales'] > 0 }
print(sbw)