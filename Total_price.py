
#function for getting the list
def finalprice(product_quantities,prices):
    final_list = []
    for i in range(n):
        item=product_quantities[i]*prices[i]
        final_list.append(item)
    return final_list

#function for adding the elements of the list
def add(p):
    sum=0
    for i in range(len(p)):
        sum=sum+p[i]
    return sum
#taking the input
product_quantities= [13, 5, 6, 10, 11]
prices = [1.2, 6.5, 1.0, 4.8, 5.0]

n=len(product_quantities)#calculagting the length
p=finalprice(product_quantities,prices)
final=add(p)
print("total price is :",final)#printing the final answer