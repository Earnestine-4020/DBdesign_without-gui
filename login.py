import pymysql
import student
import teacher
import mannager
import worker

a = 0
iduser = ''
flag = 0

def open():
    conn = pymysql.connect(host='localhost', user='root', passwd='TMD00544', database='学生返校')
    cur = conn.cursor()
    return conn, cur


def mean():
    print('请选择身份登录(输入编号)')
    print('1.教师')
    print('2.学生')
    print('3.辅导员')
    print('4.数据库管理人员')


def chose():
    global a
    mean()
    global iduser
    a = int(input())
    while a < 1 | a > 5:
        print('身份错误！请选择提供的身份！')
        mean()
        a = int(input())
    print('请输入id')
    iduser = input()


def logjudge():
    global a
    global iduser
    sql = 'select passwd from login where logid=%s and iduser=%s'
    cur = open()[1]
    cur.execute(sql, [a, iduser])
    b = cur.fetchone()
    while b is None:
        print('身份错误，登陆失败')
        chose()
        sql = 'select passwd from login where logid=%s and iduser=%s'
        cur.execute(sql, [a, iduser])
        b = cur.fetchone()
    print('请输入密码')
    key = input()
    k = str(b[0])
    i = 0
    global flag
    while key != k:
        i += 1
        if i < 5:
            print('密码错误！请重新输入密码')
            key = input()
        else:
            print('您的账号已锁定，请您联系管理员查看或更改密码')
            break
    if i < 5:
        flag = 1
    cur.close()


def start():
    chose()
    logjudge()
    return a


def one():
    c = teacher.Menu()
    while c in (1, 2, 3, 4):
        if c == 1:
            conn = open()[0]
            cur = open()[1]
            value = teacher.one()
            value = (value, iduser)
            sql = 'update teacher set phoneteacher=%s where idteacher=%s'
            try:
                cur.execute(sql, value)
                conn.commit()
                print('信息更改成功！')
            except pymysql.Error as e:
                print('更改失败' + str(e))
                conn.rollback()
            cur.close()
            c = teacher.Menu2()
        if c == 2:
            cur = open()[1]
            sql = 'select distinct idclass from xuanke where idteacher=%s'
            cur.execute(sql, iduser)
            result = cur.fetchall()
            for i in result:
                print(i)
            cur.close()
            c = teacher.Menu2()
        if c == 3:
            cur = open()[1]
            idclass = teacher.getclass()
            sql = 'select distinct result.idstudent,result.result,student.phonestudent from xuanke,result,' \
                  'student where result.idstudent=xuanke.idstudent and xuanke.idclass=%s and ' \
                  'student.idstudent=result.idstudent and xuanke.idteacher=%s '
            cur.execute(sql, [idclass, iduser])
            mass = cur.fetchone()
            if mass is None:
                print('没有查询结果！请检查您输入的课程号是否有误')
                c = teacher.Menu2()
                cur.close()
            else:
                mass = cur.fetchall()
                for i in mass:
                    print(i)
                teacher.search(mass)
                c = teacher.Menu2()
                cur.close()
        if c == 4:
            resetpasswd()
            c = teacher.Menu2()




def two():
    c = student.Menu()
    while c in (1, 2, 3, 4, 5):
        if c == 1:
            conn = open()[0]
            cur = open()[1]
            value = student.one()
            value = (value[0], value[1], value[2], iduser)
            sql = 'update student set home=%s,health=%s,phonestudent=%s where idstudent=%s'
            try:
                cur.execute(sql, value)
                conn.commit()
                print('信息更改成功！')
            except pymysql.Error as e:
                print('更改失败' + str(e))
                conn.rollback()
            sql = 'select location from danger'
            cur.execute(sql)
            danger = []
            for i in cur.fetchall():
                danger = danger + [i[0], ]
            def judege(r):
                sql0 = 'update result set result=%s where idstudent=%s'
                try:
                    cur.execute(sql0, [r, iduser])
                    conn.commit()
                    print('已为您提交审批，您可以在主菜单栏选择查看结果.')
                except pymysql.Error as e:
                    print('您的审批似乎遇到了问题，请联系院系辅导员手动审批.' + str(e))
                    conn.rollback()
            if value[1] == 'green':
                if value[0] not in danger:
                    judege('yes')
                else:
                    judege('no')
            else:
                judege('no')
            cur.close()
            c = student.Menu2()
        if c == 2:
            conn = open()[0]
            cur = open()[1]
            sql = 'select result from result where idstudent=%s'
            cur.execute(sql, iduser)
            result = cur.fetchall()
            print(result[0][0])
            cur.close()
            c = student.Menu2()
        if c == 3:
            conn = open()[0]
            cur = open()[1]
            sql = 'select distinct nameworker,phoneworker from student,worker where student.dpid=worker.dpid'
            cur.execute(sql)
            mass = cur.fetchall()
            for i in mass:
                print(i)
            cur.close()
            c = student.Menu2()
        if c == 4:
            conn = open()[0]
            cur = open()[1]
            sql = 'select distinct teacher.idteacher,phoneteacher,idclass from teacher,xuanke where idstudent=%s and ' \
                  'xuanke.idteacher=teacher.idteacher '
            cur.execute(sql, iduser)
            mass = cur.fetchall()
            for i in mass:
                print(i)
            cur.close()
            c = student.Menu2()
        if c == 5:
            resetpasswd()
            c = student.Menu2()

def three():
    c = worker.Menu()
    while c in (1, 2, 3, 4):
        if c == 1:
            conn = open()[0]
            cur = open()[1]
            value = worker.one()
            value = (value, iduser)
            sql = 'update worker set phoneworker=%s where idworker=%s'
            try:
                cur.execute(sql, value)
                conn.commit()
                print('信息更改成功！')
            except pymysql.Error as e:
                print('更改失败' + str(e))
                conn.rollback()
            cur.close()
            c = worker.Menu2()
        if c == 2:
            cur = open()[1]
            sql = 'select distinct student.idstudent,student.namestudent,student.home,student.health,' \
                  'student.phonestudent from student,worker where student.dpid=worker.dpid '
            cur.execute(sql)
            mass = cur.fetchall()
            print('您所在的院系的所有学生的个人信息如下:')
            for i in mass:
                print(i)
            worker.search(mass)
            cur.close()
            c = worker.Menu2()
        if c == 3:
            conn = open()[0]
            cur = open()[1]
            sql = 'select distinct idstudent,result from result,worker where result.dpid=worker.dpid'
            cur.execute(sql)
            mass = cur.fetchall()
            print('您的院系的所有学生返校结果为')
            for i in mass:
                print(i)
            worker.searno(mass)
            print('是否需要更改这些学生的审批结果？[y/n]')
            t = input()
            while t == 'y':
                value = worker.reset(mass)
                sql = 'update result set result=%s where idstudent=%s'
                try:
                    cur.execute(sql, value)
                    conn.commit()
                    print('信息更改成功！')
                except pymysql.Error as e:
                    print('更改失败' + str(e))
                    conn.rollback()
                print('是否继续修改？')
                t = input()
            cur.close()
            c = worker.Menu2()
        if c == 4:
            resetpasswd()
            c = worker.Menu2()


def four():
    tab = mannager.Menu()
    while tab[0] in (1, 2, 3, 4, 5):
        c = tab[0]
        if c == 1:
            conn = open()[0]
            cur = open()[1]
            if tab[1] == 1:
                loc = mannager.one1()
                sql = "insert into danger (location) value (%s)"
                try:
                    cur.execute(sql, loc)
                    conn.commit()
                    print('插入成功！')
                except pymysql.Error as e:
                    conn.rollback()
                    print('插入失败！' + str(e))
                tab = mannager.Menu2()
            if tab[1] == 2:
                value = mannager.one2()
                sql = "insert into student(idstudent,namestudent,dpid,phonestudent) value (%s,%s,%s,%s)"
                try:
                    cur.execute(sql, value)
                    conn.commit()
                    print('插入成功！请记得更新登录信息表！')
                except pymysql.Error as e:
                    conn.rollback()
                    print('插入失败！' + str(e))
                tab = mannager.Menu2()
            if tab[1] == 3:
                value = mannager.one3()
                sql = "insert into teacher value (%s,%s,%s)"
                try:
                    cur.execute(sql, value)
                    conn.commit()
                    print('插入成功！请记得更新登录信息表！')
                except pymysql.Error as e:
                    conn.rollback()
                    print('插入失败！' + str(e))
                tab = mannager.Menu2()
            if tab[1] == 4:
                value = mannager.one4()
                sql = "insert into worker  value (%s,%s,%s,%s)"
                try:
                    cur.execute(sql, value)
                    conn.commit()
                    print('插入成功！请记得更新登录信息表！')
                except pymysql.Error as e:
                    conn.rollback()
                    print('插入失败！' + str(e))
                mannager.Menu2()
            if tab[1] == 5:
                value = mannager.one5()
                sql = "insert into xuanke  value (%s,%s,%s)"
                try:
                    cur.execute(sql, value)
                    conn.commit()
                    print('插入成功！')
                except pymysql.Error as e:
                    conn.rollback()
                    print('插入失败！' + str(e))
                tab = mannager.Menu2()
            if tab[1] == 6:
                value = mannager.one6()
                sql = "insert into result  value (%s,%s,%s)"
                try:
                    cur.execute(sql, value)
                    conn.commit()
                    print('插入成功！')
                except pymysql.Error as e:
                    conn.rollback()
                    print('插入失败！' + str(e))
                tab = mannager.Menu2()
            if tab[1] == 7:
                value = mannager.one7()
                sql = "insert into login  value (%s,%s,%s)"
                try:
                    cur.execute(sql, value)
                    conn.commit()
                    print('插入成功！')
                except pymysql.Error as e:
                    conn.rollback()
                    print('插入失败！' + str(e))
                tab = mannager.Menu2()
            cur.close()
        if c == 2:
            conn = open()[0]
            cur = open()[1]
            if tab[1] == 1:
                sql = 'select * from danger'
                cur.execute(sql)
                mass = cur.fetchall()
                for i in mass:
                    print(i)
                loc = mannager.two1(mass)
                sql = "delete from danger where location=%s"
                try:
                    cur.execute(sql, loc)
                    conn.commit()
                    print('删除成功！')
                except pymysql.Error as e:
                    conn.rollback()
                    print('删除失败!' + str(e))
                tab = mannager.Menu2()
            if tab[1] == 2:
                sql = 'select * from student'
                cur.execute(sql)
                mass = cur.fetchall()
                for i in mass:
                    print(i)
                idstudent = mannager.two2(mass)
                sql = "delete from student where idstudent=%s"
                try:
                    cur.execute(sql, idstudent)
                    conn.commit()
                    print('删除成功！')
                except pymysql.Error as e:
                    conn.rollback()
                    print('删除失败!' + str(e))
                tab = mannager.Menu2()
            if tab[1] == 3:
                sql = 'select * from teacher'
                cur.execute(sql)
                mass = cur.fetchall()
                for i in mass:
                    print(i)
                idteacher = mannager.two3(mass)
                sql = "delete from teacher where idteacher=%s"
                try:
                    cur.execute(sql, idteacher)
                    conn.commit()
                    print('删除成功！')
                except pymysql.Error as e:
                    conn.rollback()
                    print('删除失败!' + str(e))
                tab = mannager.Menu2()
            if tab[1] == 4:
                sql = 'select * from worker'
                cur.execute(sql)
                mass = cur.fetchall()
                for i in mass:
                    print(i)
                idworker = mannager.two4(mass)
                sql = "delete from worker where idworker=%s"
                try:
                    cur.execute(sql, idworker)
                    conn.commit()
                    print('删除成功！')
                except pymysql.Error as e:
                    conn.rollback()
                    print('删除失败!' + str(e))
                tab = mannager.Menu2()
            if tab[1] == 5:
                sql = 'select * from xuanke'
                cur.execute(sql)
                mass = cur.fetchall()
                for i in mass:
                    print(i)
                mannager.search(mass)
                value = mannager.two5(mass)
                sql = "delete from xuanke where idstudent=%s and idclass=%s"
                try:
                    cur.execute(sql, value)
                    conn.commit()
                    print('删除成功！')
                except pymysql.Error as e:
                    conn.rollback()
                    print('删除失败!' + str(e))
                tab = mannager.Menu2()
            if tab[1] == 6:
                sql = 'select * from result'
                cur.execute(sql)
                mass = cur.fetchall()
                for i in mass:
                    print(i)
                res = mannager.two6(mass)
                sql = "delete from result where idstudent=%s"
                try:
                    cur.execute(sql, res)
                    conn.commit()
                    print('删除成功！')
                except pymysql.Error as e:
                    conn.rollback()
                    print('删除失败!' + str(e))
                tab = mannager.Menu2()
            if tab[1] == 7:
                sql = 'select * from login'
                cur.execute(sql)
                mass = cur.fetchall()
                for i in mass:
                    print(i)
                log = mannager.two7(mass)
                sql = "delete from login where iduser=%s"
                try:
                    cur.execute(sql, log)
                    conn.commit()
                    print('删除成功！')
                except pymysql.Error as e:
                    conn.rollback()
                    print('删除失败!' + str(e))
                tab = mannager.Menu2()
            cur.close()
        if c == 3:
            conn = open()[0]
            cur = open()[1]
            if tab[1] == 1:
                print('请您直接对此表执行更新/删除操作！')
                tab = mannager.Menu2()
            if tab[1] == 2:
                sql = 'select * from student'
                cur.execute(sql)
                mass = cur.fetchall()
                for i in mass:
                    print(i)
                value = mannager.three2(mass)
                sql = 'update student set idstudent=%s,namestudent=%s,dpid=%s,phonestudent=%s where ' \
                      'idstudent=%s '
                try:
                    cur.execute(sql, value)
                    conn.commit()
                    print('更新成功！')
                except pymysql.Error as e:
                    conn.rollback()
                    print('更新失败!' + str(e))
                tab = mannager.Menu2()
            if tab[1] == 3:
                sql = 'select * from teacher'
                cur.execute(sql)
                mass = cur.fetchall()
                for i in mass:
                    print(i)
                value = mannager.three3(mass)
                sql = 'update teacher set idteacher=%s,nameteacher=%s,phoneteacher=%s where ' \
                      'idteacher=%s '
                try:
                    cur.execute(sql, value)
                    conn.commit()
                    print('更新成功！')
                except pymysql.Error as e:
                    conn.rollback()
                    print('更新失败!' + str(e))
                tab = mannager.Menu2()
            if tab[1] == 4:
                sql = 'select * from worker'
                cur.execute(sql)
                mass = cur.fetchall()
                for i in mass:
                    print(i)
                value = mannager.three4(mass)
                sql = 'update worker set idworker=%s,dpid=%s,nameworker=%s,phoneworker=%s where ' \
                      'idworker=%s '
                try:
                    cur.execute(sql, value)
                    conn.commit()
                    print('更新成功！')
                except pymysql.Error as e:
                    conn.rollback()
                    print('更新失败!' + str(e))
                tab = mannager.Menu2()
            if tab[1] == 5:
                sql = 'select * from xuanke'
                cur.execute(sql)
                mass = cur.fetchall()
                for i in mass:
                    print(i)
                value = mannager.three5(mass)
                sql = 'update xuanke set idteacher=%s where idclass=%s '
                try:
                    cur.execute(sql, value)
                    conn.commit()
                    print('更新成功！')
                except pymysql.Error as e:
                    conn.rollback()
                    print('更新失败!' + str(e))
                tab = mannager.Menu2()
            if tab[1] == 6:
                print('该表格不需要您的更新！您可以直接进入插入/删除操作来更改该表')
                tab = mannager.Menu2()
            if tab[1] == 7:
                sql = 'select * from login'
                cur.execute(sql)
                mass = cur.fetchall()
                for i in mass:
                    print(i)
                value = mannager.three7(mass)
                sql = 'update login set iduser=%s,passwd=%s,logid=%s where ' \
                      'iduser=%s '
                try:
                    cur.execute(sql, value)
                    conn.commit()
                    print('更新成功！')
                except pymysql.Error as e:
                    conn.rollback()
                    print('更新失败!' + str(e))
                tab = mannager.Menu2()
            cur.close()
        if c == 4:
            cur = open()[1]
            if tab[1] == 1:
                sql = 'select * from danger'
                cur.execute(sql)
                mass = cur.fetchall()
                print('高风险地区如下：')
                for i in mass:
                    print(i)
                tab = mannager.Menu2()
            if tab[1] == 2:
                sql = 'select * from student'
                cur.execute(sql)
                mass = cur.fetchall()
                print('所有学生信息如下：')
                for i in mass:
                    print(i)
                mannager.search(mass)
                tab = mannager.Menu2()
            if tab[1] == 3:
                print('所有教师信息如下：')
                sql = 'select * from teacher'
                cur.execute(sql)
                mass = cur.fetchall()
                for i in mass:
                    print(i)
                mannager.search(mass)
                tab = mannager.Menu2()
            if tab[1] == 4:
                print('所有辅导员信息如下：')
                sql = 'select * from worker'
                cur.execute(sql)
                mass = cur.fetchall()
                for i in mass:
                    print(i)
                mannager.search(mass)
                tab = mannager.Menu2()
            if tab[1] == 5:
                sql = 'select * from xuanke'
                cur.execute(sql)
                mass = cur.fetchall()
                for i in mass:
                    print(i)
                print('指定账户意为指定学生')
                mannager.search(mass)
                tab = mannager.Menu2()
            if tab[1] == 6:
                sql = 'select * from result'
                cur.execute(sql)
                mass = cur.fetchall()
                for i in mass:
                    print(i)
                mannager.search(mass)
                tab = mannager.Menu2()
            if tab[1] == 7:
                sql = 'select * from login'
                cur.execute(sql)
                mass = cur.fetchall()
                print('所有登录信息如下：')
                for i in mass:
                    print(i)
                mannager.search(mass)
                tab = mannager.Menu2()
            cur.close()
        if c == 5:
            resetpasswd()
            tab = mannager.Menu2()


def resetpasswd():
    global iduser
    f = True
    while f:
        print('请输入新的密码')
        passwd = input()
        print(passwd)
        print('是否确认提交？[提交y/修改n]')
        t = input()
        if t == 'y':
            f = False
    sql = 'update login set passwd=%s where iduser=%s'
    conn = open()[0]
    cur = open()[1]
    try:
        cur.execute(sql, [passwd, iduser])
        conn.commit()
        print('更新成功！')
    except pymysql.Error as e:
        conn.rollback()
        print('更新失败!' + str(e))
    cur.close()
