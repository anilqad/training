word = str(input("enter  the  word "))
ic = str(input("enter the char need to change"))
char = str(input("enter replace char"))
n_str=''
for i in range(len(word)):
    if word[i] == ic:
        n_str = n_str + char
    else:
        n_str = n_str + word[i]
print(n_str)
