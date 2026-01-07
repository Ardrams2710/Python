items=["milk","bread","eggs"]
def add_items(items):
    items.append("salad")
    print(items)
add_items(items)
def remove_last_item(items):
    items.pop()
    print(items)
remove_last_item(items)
x=lambda a:[print("item:",a)for a in items]
x(items)
def count_characters(items):
    if items==[]:
        return 0
    return len(items[0])+count_characters(items[1:])
print(count_characters(items))

