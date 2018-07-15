import os
list_file = os.listdir()
files = [file_name for file_name in list_file if file_name.find('pdf') != -1]
numbers = [element for element in range(1, (len(files)*2)+1, 2)]
[os.rename(file_name, "exploring_english_"+str(numbers[index])+".pdf") for index, file_name in enumerate(files)]