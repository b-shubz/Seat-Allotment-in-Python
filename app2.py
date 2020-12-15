import csv

#Author - shubz -
#Admin login -  name    --- 'admin'
#            - password --- 'admin'
#
#Coordinator - username ---- certerid
#            - password ---- 'admin'
#
#example student username and password --- '4' 'manish'


students=[]
preferences=[]
eligibilities=[]
courses=[]
centers=[]
capacities=[]
degrees=[]

def load_data():
    with open('data-files/students.csv', mode='r') as csv_students:
        csv_read=csv.reader(csv_students, delimiter=',')
        for s in csv_read:
            students.append(s)

    with open('data-files/preferences.csv', mode='r') as csv_pref:
        csv_read=csv.reader(csv_pref, delimiter=',')
        for s in csv_read:
            preferences.append(s)

    with open('data-files/eligibilities.csv', mode='r') as csv_eligib:
        csv_read=csv.reader(csv_eligib, delimiter=',')
        for s in csv_read:
            eligibilities.append(s)

    with open('data-files/courses.csv', mode='r') as csv_courses:
        csv_read=csv.reader(csv_courses, delimiter=',')
        for s in csv_read:
            courses.append(s)

    with open('data-files/centers.csv', mode='r') as csv_centers:
        csv_read=csv.reader(csv_centers, delimiter=',')
        for s in csv_read:
            centers.append(s)

    with open('data-files/capacities.csv', mode='r') as csv_capacities:
        csv_read=csv.reader(csv_capacities, delimiter=',')
        for s in csv_read:
            capacities.append(s)

    with open('data-files/degrees.txt', mode='r') as csv_deg:
        csv_read=csv.reader(csv_deg, delimiter=',')
        for s in csv_read:
            degrees.append(s)


def save_data():
    with open('data-files/students.csv', mode='w') as csv_students:
        csv_write=csv.writer(csv_students, delimiter=',')
        for s in students:
            csv_write.writerow(s)

    with open('data-files/capacities.csv', mode='w') as csv_cap:
        csv_write=csv.writer(csv_cap, delimiter=',')
        for c in capacities:
            csv_write.writerow(c)

    with open('data-files/preferences.csv', mode='w') as csv_prefs:
        csv_write=csv.writer(csv_prefs, delimiter=',')
        for p in preferences:
            csv_write.writerow(p)

def register():
    print()
    formno=1
    for s in students:
        formno=max(int(s[0]),formno)
    number=1
    for i in degrees:
        print(number,*i)
        number=number+1
    print()

    students.append([int(formno)+1,input('Name :'),0,0,0,*degrees[int(input('select from above options :'))-1],int(input('Percentage :')),0,'NA','NA',0,0,'NA'])
    save_data()
    print('Registered successfully\n')

def listcourses_for_admin():

    for i in eligibilities:
        print(*i)
    print()

def listcenters_for_admin():

    for i in capacities:
        print(*i)
    print()

def list_students():
    for e in students:
        print(str(e[0]).ljust(4), str(e[1]).ljust(15), str(e[2]).ljust(4), str(e[3]).ljust(4), str(e[4]).ljust(4),
              str(e[5]).ljust(18), str(e[6]).ljust(6), str(e[7]).ljust(3), str(e[8]).ljust(7), str(e[9]).ljust(5),
              str(e[10]).ljust(9), str(e[11]).ljust(4), str(e[12]).ljust(10))

        #print(*e)
    print()

def update_student_ranks():
    formno=int(input('Enter Formno :'))
    for i in students:
        if int(i[0])==formno:
            if input('Add rank A ? y or N :') == 'y':
                i[2] = int(input('Enter rank A '))
            if input('Add rank B ? y or N :') == 'y':
                i[3] = int(input('Enter rank B '))
            if input('Add rank C ? y or N :') == 'y':
                i[4] = int(input('Enter rank C '))
    save_data()

A=['PG-DGI']
B=['PG-DBDA','PG-DAC','PG-DMC']
C=['PG-DESD']
for i in courses:
    if i[3]=='A':
        A.append(i[1])
    elif i[3]=='B':
        B.append(i[1])
    elif i[3]=='C':
        C.append(i[1])


def allocate1():


    for i in range(1, 11):
        # print(students)
        students.sort(key=lambda x: int(x[2]))
        # print(students)
        for s in students:

            for j in preferences:

                if int(s[2]) > 0 and int(s[0]) == int(j[0]) and int(j[1]) == i and j[2] in A:
                    # if int(s[2]) > 0 and s[0] == j[0] and int(j[1]) == i :

                    coursename = j[2]
                    centerid = j[3]
                    for c in capacities:
                        if c[0] == centerid and c[1] == coursename and int(c[3]) < int(c[2]):
                            s[7] = i
                            s[8] = coursename
                            s[9] = centerid
                            c[3] = int(c[3]) + 1

        # print(students)
        students.sort(key=lambda x: int(x[3]))

        for s in students:
            for j in preferences:
                if int(s[3]) > 0 and s[0] == j[0] and int(j[1]) == i and j[2] in B:
                    # if int(s[3]) > 0 and s[0] == j[0] and int(j[1]) == i:
                    coursename = j[2]
                    centerid = j[3]
                    for c in capacities:
                        if c[0] == centerid and c[1] == coursename and int(c[3]) < int(c[2]):
                            s[7] = i
                            s[8] = coursename
                            s[9] = centerid
                            c[3] = int(c[3]) + 1

        students.sort(key=lambda x: int(x[4]))

        for s in students:
            for j in preferences:
                if int(s[4]) > 0 and s[0] == j[0] and int(j[1]) == i and j[2] in C:
                    # if int(s[4]) > 0 and s[0] == j[0] and int(j[1]) == i:
                    coursename = j[2]
                    centerid = j[3]
                    for c in capacities:
                        if c[0] == centerid and c[1] == coursename and int(c[3]) < int(c[2]):
                            s[7] = i
                            s[8] = coursename
                            s[9] = centerid
                            c[3] = int(c[3]) + 1
	save_data()
        # print(*students)

def allocate2():
    for e in capacities:
        e[3] = 0

    for s in students:
        if s[8] != 'NA' and int(s[10]) != 11800:
            s[10] = -1

    for s in students:
        s[7], s[8], s[9] = 0, 'NA', 'NA'

    for i in range(1, 11):
        # print(students)
        students.sort(key=lambda x: int(x[2]))
        # print(students)
        for s in students:

            for j in preferences:

                if int(s[2]) > 0 and int(s[10]) >= 0 and int(s[0]) == int(j[0]) and int(j[1]) == i and j[2] in A:

                    coursename = j[2]
                    centerid = j[3]
                    for c in capacities:
                        if c[0] == centerid and c[1] == coursename and int(c[3]) < int(c[2]):
                            s[7] = i
                            s[8] = coursename
                            s[9] = centerid
                            c[3] = int(c[3]) + 1

        # print(students)
        students.sort(key=lambda x: int(x[3]))

        for s in students:

            for j in preferences:
                if int(s[3]) > 0 and int(s[10]) >= 0 and int(s[0]) == int(j[0]) and int(j[1]) == i and j[2] in B:
                    coursename = j[2]
                    centerid = j[3]
                    for c in capacities:
                        if c[0] == centerid and c[1] == coursename and int(c[3]) < int(c[2]):
                            s[7] = i
                            s[8] = coursename
                            s[9] = centerid
                            c[3] = int(c[3]) + 1

        students.sort(key=lambda x: int(x[4]))

        for s in students:
            for j in preferences:
                if int(s[4]) > 0 and int(s[10]) >= 0 and int(s[0]) == int(j[0]) and int(j[1]) == i and j[2] in C:
                    coursename = j[2]
                    centerid = j[3]
                    for c in capacities:
                        if c[0] == centerid and c[1] == coursename and int(c[3]) < int(c[2]):
                            s[7] = i
                            s[8] = coursename
                            s[9] = centerid
                            c[3] = int(c[3]) + 1
	save_data()

def list_allocated():

    studbycourse=[]
    for c in sorted(courses, key=lambda x:x[1]):
        li=[]
        for s in students:
            if s[8]==c[1]:
                li.append(s)
        studbycourse.append(li)

    studbycenter=[]
    for course in studbycourse:

        for i in sorted(centers,key=lambda x:x[0]):
            li = []
            for s in course:
                if s[9]==i[0]:
                    li.append(s)
            studbycenter.append(li)

    for b in studbycenter:
        b.sort(key = lambda x : x[1])
        for e in b:
            print(str(e[0]).ljust(4), str(e[1]).ljust(15), str(e[2]).ljust(4), str(e[3]).ljust(4), str(e[4]).ljust(4),
                  str(e[5]).ljust(18), str(e[6]).ljust(6), str(e[7]).ljust(3), str(e[8]).ljust(7), str(e[9]).ljust(5),
                  str(e[10]).ljust(9), str(e[11]).ljust(4), str(e[12]).ljust(10))


def list_paid():

    studbycourse = []
    for c in sorted(courses, key=lambda x: x[1]):
        li = []
        for s in students:
            if s[8] == c[1] and int(s[10])>0:
                li.append(s)
        studbycourse.append(li)

    studbycenter = []
    for course in studbycourse:

        for i in sorted(centers, key=lambda x: x[0]):
            li = []
            for s in course:
                if s[9] == i[0]:
                    li.append(s)
            studbycenter.append(li)

    for b in studbycenter:
        b.sort(key=lambda x: x[1])
        for e in b:
            print(str(e[0]).ljust(4), str(e[1]).ljust(15), str(e[2]).ljust(4), str(e[3]).ljust(4), str(e[4]).ljust(4),
                  str(e[5]).ljust(18), str(e[6]).ljust(6), str(e[7]).ljust(3), str(e[8]).ljust(7), str(e[9]).ljust(5),
                  str(e[10]).ljust(9), str(e[11]).ljust(4), str(e[12]).ljust(10))

def list_reported():
    studbycourse = []
    for c in sorted(courses, key=lambda x: x[1]):
        li = []
        for s in students:
            if int(s[11]) == 1:
                li.append(s)
        studbycourse.append(li)

    studbycenter = []
    for course in studbycourse:

        for i in sorted(centers, key=lambda x: x[0]):
            li = []
            for s in course:
                if s[9] == i[0]:
                    li.append(s)
            studbycenter.append(li)

    for b in studbycenter:
        b.sort(key=lambda x: x[1])
        for e in b:
            print(str(e[0]).ljust(4), str(e[1]).ljust(15), str(e[2]).ljust(4), str(e[3]).ljust(4), str(e[4]).ljust(4),
                  str(e[5]).ljust(18), str(e[6]).ljust(6), str(e[7]).ljust(3), str(e[8]).ljust(7), str(e[9]).ljust(5),
                  str(e[10]).ljust(9), str(e[11]).ljust(4), str(e[12]).ljust(10))


def generate_prn():
    for c in capacities:
        number = 1
        for s in students:
            if c[0] == s[9] and c[1] == s[8] and int(s[10])>0:
                print(c[1] + c[0] + str(number))
                s[12] = c[1] + '_' + c[0] +'_'+ str(number)
                number = number + 1

    save_data()


def list_center_students():
    course=input('Enter Course name :')
    center=input('Enter Course name :')
    cstud=[]
    for s in students:
        if s[8]==course and s[9]==center and int(s[10])>0:

            cstud.append(s)

    cstud.sort(key=lambda x: x[1])
    for e in cstud:
        #print(*c)
        print(str(e[0]).ljust(4), str(e[1]).ljust(15), str(e[2]).ljust(4), str(e[3]).ljust(4), str(e[4]).ljust(4),
              str(e[5]).ljust(18), str(e[6]).ljust(6), str(e[7]).ljust(3), str(e[8]).ljust(7), str(e[9]).ljust(5),
              str(e[10]).ljust(9), str(e[11]).ljust(4), str(e[12]).ljust(10))

def admin():
    while True:
        i = int(input(
            'Enter choice  \n1. list courses \n2.list courses \n3. list students \n4.update student rank \n5.Allocate round 1 \n6.Allocate round 2 \n7.list allocated \n8. list paid \n9.list reported \n10.generate prn \n11.list students of center \n12. Main Menu:'))
        if i == 1:
            listcourses_for_admin()

        elif i == 2:
            listcenters_for_admin()

        elif i == 3:
            list_students()

        elif i == 4:
            update_student_ranks()

        elif i == 5:
            allocate1()

        elif i == 6:
            allocate2()

        elif i == 7:
            list_allocated()

        elif i == 8:
            list_paid()

        elif i == 9:
            list_reported()


        elif i == 10:
            generate_prn()

        elif i == 11:
            list_center_students()

        elif i == 12:
            break


def listcourses_student(degree,marks):
    print()
    for i in eligibilities:
        if i[1]==degree and float(marks)>=float(i[2]):
            print(*i)

    print()

def listcenters():
    print()
    for i in centers:
        print(*i)

    print()

def add_preferences(formno,degree, marks):
    eligible_courses = []
    for i in eligibilities:
        if i[1] == degree and float(marks) >= float(i[2]):
            eligible_courses.append(i[0])
    add_to_pref = []

    for i in capacities:

        for e in eligible_courses:
            if i[1] == e:
                add_to_pref.append([ e, i[0]])
                print( e, i[0])


    for i in range(int(input('Enter number of preferences you want to add.(max 10)\n'))):
        number=1
        for p in add_to_pref:
            print(number,*p)
            number+=1
        pref = int(input('Enter preference number from abve :'))
        pref=pref-1

        preferences.append([formno, i + 1, add_to_pref[pref][0], add_to_pref[pref][1]])
        print()
        print( i + 1, add_to_pref[pref][0], add_to_pref[pref][1])
        print()
        add_to_pref.pop(pref)

    save_data()


def see_allocated(pref,course,center):
    print()
    for i in capacities:
        if i[0]==center:
            print(i[0],i[1])
    print()


def update_payment(formno):
    for s in students:
        if int(s[0])==int(formno) :
            s[10]=11800
            print('update successful\n')
    save_data()

def stud(s):
    while True:
        i = int(input(
            'Enter choice  \n1.list courses \n2.list centers \n3.add preferences \n4.see allocated center \n5.Update Paid \n6.Exit  :'))

        if i == 1:
            listcourses_student(s[5], s[6])

        elif i == 2:
            listcenters()

        elif i == 3:
            add_preferences(s[0], s[5], s[6])

        elif i == 4:
            see_allocated(s[7], s[8], s[9])

        elif i == 5:
            update_payment(s[0])

        elif i == 6:
            break


def listcourses_coordinator(center):
    for i in capacities:
        if i[0]==center:
            print(i[1])

def list_center_students_coord(center):
    course=input('Enter course :')
    cstud=[]
    for s in students:
        if s[9]==center and s[8]==course:
            cstud.append(s)

    cstud.sort(key=lambda x: x[1])
    for e in cstud:
        print(str(e[0]).ljust(4), str(e[1]).ljust(15), str(e[2]).ljust(4), str(e[3]).ljust(4), str(e[4]).ljust(4),
              str(e[5]).ljust(18), str(e[6]).ljust(6), str(e[7]).ljust(3), str(e[8]).ljust(7), str(e[9]).ljust(5),
              str(e[10]).ljust(9), str(e[11]).ljust(4), str(e[12]).ljust(10))
    print()

def update_student_reported(center):
    formno=int(input('Enter Formno:'))
    for s in students:
        if int(s[0])==formno :
            if s[8]!="NA" and s[9]==center:
                s[11]=1
                print('Success ')
            else:
                print('Error student not got any seat allocated')
    save_data()

def list_admitted_students(center):
    course=input('Enter course :')
    cstud=[]
    for s in students:
        if s[8]==course and s[9]==center and s[11]==1:
            cstud.append(s)

    cstud.sort(key=lambda x: x[1])
    for e in cstud:
        print(str(e[0]).ljust(4), str(e[1]).ljust(15), str(e[2]).ljust(4), str(e[3]).ljust(4), str(e[4]).ljust(4),
              str(e[5]).ljust(18), str(e[6]).ljust(6), str(e[7]).ljust(3), str(e[8]).ljust(7), str(e[9]).ljust(5),
              str(e[10]).ljust(9), str(e[11]).ljust(4), str(e[12]).ljust(10))




def coordinator(center):
    while True :
        i = int(input('Enter choice  \n1. list course \n2.list students in center \n3.update students reported \n4.list admitted students \n5. Main Menu:'))
        if i == 1:
            listcourses_coordinator(center[0])

        elif i ==2:
            list_center_students_coord(center[0])

        elif i == 3:
            update_student_reported(center[0])

        elif i == 4:
            list_admitted_students(center[0])

        elif i == 5:
            break





def signin():
    uname=input('Enter username :')
    password=input('Enter password :')

    co = []
    for e in centers:
        co.append(e[0])

    if uname=='admin' and password=='admin':
        admin()

    elif uname in co:
        for i in centers:
            if uname==i[0] and password=='admin':
                coordinator(i)

    else:
        for s in students:
            if s[0]==uname and s[1]==password:
                stud(s)

def main():
    load_data()
    while True:
        i=int(input('Enter choice  \n1.Register \n2.Sign in \n3: Exit:'))
        if i==1:
            register()

        elif i==2:
            signin()

        elif i==3:
            save_data()
            break
main()
