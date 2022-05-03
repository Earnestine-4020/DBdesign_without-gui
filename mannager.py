def Menu():
    print('请输入您要完成的操作(输入编号)：')
    print('1.增加信息')
    print('2.删除信息')
    print('3.更改信息')
    print('4.查询信息')
    print('5.更改密码')
    c = int(input())
    if c in (1, 2, 3, 4):
        print('请选择您要操作的表格(输入编号)：')
        print('1.高风险地区表(danger)')
        print('2，学生个人信息表(student)')
        print('3，教师个人信息表(teacher)')
        print('4，辅导员个人信息表(worker)')
        print('5，选课信息表(xuanke)')
        print('6.学生返校审批结果表(result)')
        print('7.登录信息表(login)')
        tab = int(input())
        tab = [c, tab]
    else:
        tab = [c, 0]
    return tab


def Menu2():
    print('按“q”键返回主菜单')
    t = input()
    while t != 'q':
        print('按“q”键返回主菜单')
        t = input()
    tab = Menu()
    return tab


def getuser():
    print('请输入您要操作的账户号')
    iduser = input()
    return iduser


def search(mass):
    print('是否需要按指定账户查询？[y/n]')
    t = input()
    while t == 'y':
        iduser = getuser()
        find = 0
        for i in mass:
            if i[0] == iduser:
                print(i)
                find = 1
        if find == 0:
            print('您输入的账户名不正确！')
        print('是否继续按账户号查询？[y/n]')
        t = input()


def one1():
    flag = True
    while flag:
        print('请输入您要增加的地区')
        loc = input()
        print(loc)
        print('是否确认提交？[提交y/修改n]')
        t = input()
        if t == 'y':
            flag = False
    return loc


def one2():
    flag = True
    while flag:
        print('请依次输入下列学生个人信息（学号，姓名，院系号，联系电话），每输入一项请按回车')
        value = []
        for i in range(0, 4):
            x = input()
            value.append(x)
        print(value)
        print('是否确认提交？[提交y/修改n]')
        t = input()
        if t == 'y':
            flag = False
    return value


def one3():
    flag = True
    while flag:
        print('请依次输入下列教师个人信息（教工号，姓名，联系电话），每输入一项请按回车')
        value = []
        for i in range(0, 3):
            x = input()
            value.append(x)
        print(value)
        print('是否确认提交？[提交y/修改n]')
        t = input()
        if t == 'y':
            flag = False

    return value


def one4():
    flag = True
    while flag:
        print('请依次输入下列辅导员个人信息（职工号，院系号，姓名，联系电话），每输入一项请按回车')
        value = []
        for i in range(0, 4):
            x = input()
            value.append(x)
        print(value)
        print('是否确认提交？[提交y/修改n]')
        t = input()
        if t == 'y':
            flag = False
    return value


def one5():
    flag = True
    while flag:
        print('请依次输入下列选课信息（学号，课程号，教工号），每输入一项请按回车')
        value = []
        for i in range(0, 3):
            x = input()
            value.append(x)
        print(value)
        print('是否确认提交？[提交y/修改n]')
        t = input()
        if t == 'y':
            flag = False
    return value


def one6():
    flag = True
    while flag:
        print('请依次输入下列返校审批结果（学号，院系号，结果），每输入一项请按回车')
        value = []
        for i in range(0, 3):
            x = input()
            value.append(x)
        print(value)
        print('是否确认提交？[提交y/修改n]')
        t = input()
        if t == 'y':
            flag = False
    return value


def one7():
    flag = True
    while flag:
        print('请依次输入下列登录用户信息（用户号，密码，账号名），每输入一项请按回车')
        value = []
        for i in range(0, 3):
            x = input()
            value.append(x)
        print(value)
        print('是否确认提交？[提交y/修改n]')
        t = input()
        if t == 'y':
            flag = False
    return value


def two1(mass):
    flag = True
    while flag:
        find = 0
        while find == 0:
            print('请输入您需要删除的地区')
            loc = input()
            for i in mass:
                if i[0] == loc:
                    find = 1
            if find == 0:
                print('您输入的地区不正确！')
        print(loc)
        print('是否确认提交？[提交y/修改n]')
        t = input()
        if t == 'y':
            flag = False
    return loc


def two2(mass):
    flag = True
    while flag:
        find = 0
        while find == 0:
            print('请输入您要删除的学生的学号')
            idstudent = input()
            for i in mass:
                if i[0] == idstudent:
                    find = 1
            if find == 0:
                print('您输入的学号不正确！')
        print(idstudent)
        print('是否确认提交？[提交y/修改n]')
        t = input()
        if t == 'y':
            flag = False
    return idstudent


def two3(mass):
    flag = True
    while flag:
        find = 0
        while find == 0:
            print('请输入您要删除的教师的职工号')
            idteacher = input()
            for i in mass:
                if i[0] == idteacher:
                    find = 1
            if find == 0:
                print('您输入的职工号不正确！')
        print(idteacher)
        print('是否确认提交？[提交y/修改n]')
        t = input()
        if t == 'y':
            flag = False
    return idteacher


def two4(mass):
    flag = True
    while flag:
        find = 0
        while find == 0:
            print('请输入您要删除的辅导员的职工号')
            idworker = input()
            for i in mass:
                if i[0] == idworker:
                    find = 1
            if find == 0:
                print('您输入的职工号不正确！')
        print(idworker)
        print('是否确认提交？[提交y/修改n]')
        t = input()
        if t == 'y':
            flag = False
    return idworker


def two5(mass):
    find = 0
    while find == 0:
        idstudent = getuser()
        for i in mass:
            if i[0] == idstudent:
                find = 1
        if find == 0:
            print('您输入的学号号不正确！')
    flag = True
    while flag:
        find = 0
        while find == 0:
            print('请输入您要删除的该学生所选的课程号')
            idclass = input()
            for i in mass:
                if i[1] == idclass:
                    find = 1
            if find == 0:
                print('您输入的课程不正确！')
        print(idclass)
        print('是否确认提交？[提交y/修改n]')
        t = input()
        if t == 'y':
            flag = False
    value = [idstudent, idclass]
    return value


def two6(mass):
    flag = True
    while flag:
        find = 0
        while find == 0:
            print('请输入您要删除的审批结果的学生学号')
            res = input()
            for i in mass:
                if i[0] == res:
                    find = 1
            if find == 0:
                print('您输入的学号不正确！')
        print(res)
        print('是否确认提交？[提交y/修改n]')
        t = input()
        if t == 'y':
            flag = False
    return res


def two7(mass):
    flag = True
    while flag:
        find = 0
        while find == 0:
            print('请输入您要删除的登录信息用户号')
            log = input()
            for i in mass:
                if i[0] == log:
                    find = 1
            if find == 0:
                print('您输入的用户不正确！')
        print(log)
        print('是否确认提交？[提交y/修改n]')
        t = input()
        if t == 'y':
            flag = False
    return log


def three2(mass):
    flag = True
    while flag:
        find = 0
        while find == 0:
            print('请输入您要更改的的学生学号')
            temp = input()
            for i in mass:
                if i[0] == temp:
                    find = 1
            if find == 0:
                print('您输入的学号不正确！')
        print('请依次输入下列选课信息（学号，姓名，院系号，联系电话），每输入一项请按回车')
        value = []
        for i in range(0, 4):
            x = input()
            value.append(x)
        print('将' + temp + '处的信息变更为')
        print(value)
        print('是否确认提交？[提交y/修改n]')
        t = input()
        if t == 'y':
            flag = False
        value.append(temp)
    return value


def three3(mass):
    flag = True
    while flag:
        find = 0
        while find == 0:
            print('请输入您要更改的的教师工号')
            temp = input()
            for i in mass:
                if i[0] == temp:
                    find = 1
            if find == 0:
                print('您输入的教师工号不正确！')
        print('请依次输入教师个人信息（工号，姓名，联系电话），每输入一项请按回车')
        value = []
        for i in range(0, 3):
            x = input()
            value.append(x)
        print('将' + temp + '处的信息变更为')
        print(value)
        print('是否确认提交？[提交y/修改n]')
        t = input()
        if t == 'y':
            flag = False
        value.append(temp)
    return value


def three4(mass):
    flag = True
    while flag:
        find = 0
        while find == 0:
            print('请输入您要更改的的辅导员工号')
            temp = input()
            for i in mass:
                if i[0] == temp:
                    find = 1
            if find == 0:
                print('您输入的辅导员工号不正确！')
        print('请依次输入辅导员个人信息（工号，院系号，姓名，联系电话），每输入一项请按回车')
        value = []
        for i in range(0, 4):
            x = input()
            value.append(x)
        print('将' + temp + '处的信息变更为')
        print(value)
        print('是否确认提交？[提交y/修改n]')
        t = input()
        if t == 'y':
            flag = False
        value.append(temp)
    return value


def three5(mass):
    flag = True
    while flag:
        find = 0
        while find == 0:
            print('请输入您要更改的的课程号（如需要更改学生所选课程应直接执行增加/删除操作）')
            temp = input()
            for i in mass:
                if i[1] == temp:
                    find = 1
            if find == 0:
                print('您输入的课程号不正确！')
        print('请依次输入该课程的任课教师职工号')
        value = []
        x = input()
        value.append(x)
        print('将' + temp + '处的任课教师改为')
        print(value)
        print('是否确认提交？[提交y/修改n]')
        t = input()
        if t == 'y':
            flag = False
        value.append(temp)
    return value


def three7(mass):
    flag = True
    while flag:
        find = 0
        while find == 0:
            print('请输入您要更改的的登录账号')
            temp = input()
            for i in mass:
                if i[0] == temp:
                    find = 1
            if find == 0:
                print('您输入的帐号不正确！')
        print('请依次输入账户信息（登录账号，密码，身份号），每输入一项请按回车')
        value = []
        for i in range(0, 3):
            x = input()
            value.append(x)
        print('将' + temp + '处的信息变更为')
        print(value)
        print('是否确认提交？[提交y/修改n]')
        t = input()
        if t == 'y':
            flag = False
        value.append(temp)
    return value
