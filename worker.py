def Menu():
    print('请输入您要完成的操作(输入编号)：')
    print('1.更改个人联系方式')
    print('2.查看本院的学生个人信息')
    print('3.查询/更改学生返校审批结果')
    print('4.更改密码')
    c = int(input())
    return c


def Menu2():
    print('按“q”键返回主菜单')
    t = input()
    while t != 'q':
        print('按“q”键返回主菜单')
        t = input()
    c = Menu()
    return c


def one():
    flag = True
    while flag:
        print('请输入您的联系方式')
        phone = input()
        print('联系方式：' + phone)
        print('是否确认提交？[提交y/修改n]')
        t = input()
        if t == 'y':
            flag = False
    return phone


def getstuent():
    print('请输入您要操作的学生学号')
    idstudent = input()
    return idstudent


def search(mass):
    print('是否需要按指定学号查询？[y/n]')
    t = input()
    while t == 'y':
        idstudent = getstuent()
        find = 0
        for i in mass:
            if i[0] == idstudent:
                print(i)
                find = 1
        if find == 0:
            print('您输入的学号不正确！')
        print('是否继续按学号查询？[y/n]')
        t = input()
    return


def searno(mass):
    print('是否需要我们为您筛选出未返校的学生？[y/n]')
    t = input()
    if t == 'y':
        for i in mass:
            if i[1] == 'no':
                print(i)


def reset(mass):
    find = 0
    while find == 0:
        print('请输入您需要更改的学生学号')
        idstudent = input()
        for i in mass:
            if i[0] == idstudent:
                find = 1
        if find == 0:
            print('您输入的学号不正确！')
    print('您希望将结果修改为？[yes/no]')
    result = input()
    return result, idstudent
