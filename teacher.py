def Menu():
    print('请输入您要完成的操作(输入编号)：')
    print('1.更改个人联系方式')
    print('2.查看个人教授的课程')
    print('3.查看选择课程的学生返校情况及联系方式')
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


def getclass():
    print('请输入您要查询的课程号')
    idclass = input()
    return idclass


def search(mass):
    print('是否需要我们为您筛选出未返校的学生？[y/n]')
    t = input()
    if t == 'y':
        for i in mass:
            if i[1] == 'no':
                print(i)

