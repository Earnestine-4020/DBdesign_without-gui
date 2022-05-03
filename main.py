import login

a = login.start()
while login.flag == 1:
    if a == 1:
        login.one()
    if a == 2:
        login.two()
    if a == 3:
        login.three()
    if a == 4:
        login.four()