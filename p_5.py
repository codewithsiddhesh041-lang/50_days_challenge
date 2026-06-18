try:
    file = open("p_5.txt", "r")
    content = file.read()
    print(content)
    file.close()

except FileNotFoundError:
    print("Error: File not found!")

except PermissionError:
    print("Error: Permission denied!")

except Exception as e:
    print("An unexpected error occurred:", e)