import random

u_case = "QWERTYUOPASDFGHJKLZXCVBNM"
l_case = u_case.lower()+"i"
digit = "0123456789"
symbols = "!'+%&/()=?-_${[]}"
total = u_case + l_case + digit + symbols


length = int(input("Please enter the password length(max78): "))
password = "".join(random.sample(total,length))
print(password)


### CONTROLLER

# control = len(total)
# length = int(input("Please enter the password length(max78): "))
# if length > control:
#     print("range error (max 78 case)")
#     exit()
# elif length < 0:
#     print("negative value error!")
#     exit()
# else:
#     password = "".join(random.sample(total,length))
#     print(password)