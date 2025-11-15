print("Hello World")
print("Hello the others")
print("new branch")
print("newer branch")
print("again")
# open file for writing
with open(file="text.txt", mode="a") as f:
    while(True):
        user_name = input("Give your name ? ")
        if(not user_name):
            break
        print("Your name is", user_name)
        # write to file
        f.write(user_name)
        f.write("\n")
print("This is the result.")
with open(file="text.txt", mode="r") as f:
    print(f.read())