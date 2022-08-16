import pandas as pd
import numpy as np

# opening the file in read mode
my_file = open("input.txt", "r") 
# reading the file
data = my_file.read() 
# replacing end splitting the text 
# when newline ('\n') is seen.
input_list = data.split("\n")
my_file.close()

zipped = zip(input_list, input_list[1:])
# print(f"zipped: {set(zipped)}")

# list comprehension which 
increased = ["increase" for first, second in zipped if second > first]
# print(f"input list from 1st enrty: {input_list}")
# print(f"input list from 2nd enrty: {input_list[1:]}")
# print(set(zip(input_list, input_list[1:])))


print(f"Number of increases: {len(increased)}")
