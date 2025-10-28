import messy_project.src.utils.basic_maths_operations as basic_maths_operations
import messy_project.src.utils.get_data_function as get_data_function

print("starting app")

x = input("Enter your name: ")
print("Hello " + x)

result = basic_maths_operations.add(5, 3)
print("Result:", result)

data = get_data_function.getData()
print("Data:", data)
