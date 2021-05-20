""" You have a list of integers, and for each index you want to find the product 
of every integer except the integer at that index.

Write a function get_products_of_all_ints_except_at_index() that takes a 
list of integers and returns a list of the products.

For example, given:

  [1, 7, 3, 4]

your function would return:

  [84, 12, 28, 21]

by calculating:

  [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]

Here's the catch: You can't use division in your solution! """

# Start coding from here
def get_products_of_all_ints_except_at_index(main_list):
    total = 1
    for n in main_list:
        total=total* n
    return total
List = [1, 7, 3, 4]
N = len(List)
for i in range(N):
 BaseList=([List[0:i] + List[i+1:N]])
 for a in BaseList:
  products= get_products_of_all_ints_except_at_index(a)
  print(products)
