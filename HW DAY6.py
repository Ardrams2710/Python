blog_views=[150,800,2500,600,1200,450,3000]
count=0
sum=0
for x in blog_views:
    if x>1000:
        print("Trending")
        count=count+1
    elif x>500 and x<1000:
        print("Average")
    else:
        print("Low Traffic")
for x in blog_views:
    sum=sum+x
print("total number of views:",sum)
print(count,"trending post")
    

