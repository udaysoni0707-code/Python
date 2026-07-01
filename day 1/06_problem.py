# enter mrp of a book and discount per and print 
# discount and net price
mrp = int(input("Enter the MRP of book :"))
discount = int(input("Enter the discount :"))

disc = (mrp*discount)/100
print(f"The discount of book :{disc}")

final_price = mrp-disc
print(f"the finall price of book :{final_price}")
