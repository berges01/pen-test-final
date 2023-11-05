def number_generator():

    file_path = 'passwords.txt'
    with open(file_path, 'a') as file:
        for i in range(1, 999999):
            formatted_number = f"{i:06d}\n"
            file.write(formatted_number)



number_generator()