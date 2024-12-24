                          #   write a program to find the transpose of a matrix 

# def transpose_matrix(matrix):
#     transposed=[[matrix[i][j]  for i in range(len(matrix)) for j in range(len(matrix))]]
#     return transposed

# matrix=[
        
#     [1,6,5],
#     [3,8,0],
#     [2,4,7]
        
#     ]

# transpose_matrix=transpose_matrix(matrix)
# print("orginal matrix")
# for row in matrix:
#  print(row)
# print("\n transported matrix :")
# for row in transpose_matrix:
#  print(row)    


            #   write a program to demonstrate all bulid-in method of dictionary 


# dict_2={
#     "name":"sidx",
#     "age":30,
#     "Address":"ekm"
# }

# print("key :",dict_2.keys())
# print("values :", dict_2.values())
# print("items :",dict_2.items())

# print("get :",dict_2.get("name"))
# dict_2.update({"Address":"EKM"})
# print(dict_2)
# dict_2.pop("Address")
# print(dict_2)
# dict_2.popitem()
# print(dict_2)


                                # write a python program to sum all the items in a dictionary

# def sum_dict_items(dictionary):
#     total=sum(dictionary.values())
#     return total

# dict={"apple":10,
#       "blackcurrent":5,
#       "cherry":3}
# total_sum=sum_dict_items(dict)
# print(f"Total sum : {total_sum} ")