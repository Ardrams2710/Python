receipt_header=""" Saroja Bookstall Kilimanoor 
Mobile Number:9795647585"""
Book1title="Python Basics"
Book1Price=450
Book2title="Data Science Intro"
Book2Price=600
Book1=f"Book{Book1title}Price{Book1Price}"
Book2=f"Book{Book2title}Price{Book2Price}"
print(Book1)
print(Book2)
total=Book1Price+Book2Price
total_book=f"total price{total}"
thank_you="thank you for shopping!"
receipt=receipt_header+"\n"+Book1+"\t"+Book2+"\n"+ total_book+"\n"+thank_you
print(receipt)
print(receipt.upper())
