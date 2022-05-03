def Menu():
    print('请输入您要完成的操作(输入编号)：')
    print('1.更改个人返校审批信息')
    print('2.查看个人返校审批结果')
    print('3.查看院系辅导员联系方式')
    print('4.查看任课教师联系方式')
    print('5.更改密码')
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
        print('请输入您的居住地（到省份即可）')
        home = input()
        print('请输入您的健康码颜色[green/yellow/red],请如实填写！')
        health = input()
        print('请输入您的联系方式')
        phone = input()
        print('居住地：' + home)
        print('健康码：' + health)
        print('联系方式：' + phone)
        print('是否确认提交？[提交y/修改n]')
        t = input()
        if t == 'y':
            flag = False
    return home, health, phone
