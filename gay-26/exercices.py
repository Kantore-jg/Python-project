numbers = [1,1,2,3,5,8,13,21,34,55]

# squared_numbers = [number*number for number in numbers]

result = [number for number in numbers if number%2==0]


print(result)