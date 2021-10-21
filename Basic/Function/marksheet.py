def information():
    name = input("* Student Information * \nName: ")
    classes = input("Semester: ")
    section = input("Section: ")
    reg_no = input("Registration No. : ")
    date = input("Date: ")
    return name, classes, section, reg_no, date

def marks():
    print("\n** Basic Marketing **\n")
    ab = int(input("1st Assignment: "))
    bb = int(input("Internal Examination: "))
    cb = int(input("Attendance: "))
    db = int(input("Quizzes: "))
    eb = int(input("Group Project: "))

    print("\n** Introduction to E-Commerce **\n")
    ai = int(input("1st Assignment: "))
    bi = int(input("Internal Examination: "))
    ci = int(input("Attendance: "))
    di = int(input("Quizzes: "))
    ei = int(input("Group Project: "))

    print("\n** Computer Graphics **\n")
    ac = int(input("1st Assignment: "))
    bc = int(input("Internal Examination: "))
    cc = int(input("Attendance: "))
    dc = int(input("Quizzes: "))
    ec = int(input("Group Project: "))

    print("\n** Mobile Programming **\n")
    am = int(input("1st Assignment: "))
    bm = int(input("Internal Examination: "))
    cm = int(input("Attendance: "))
    dm = int(input("Quizzes: "))
    em = int(input("Group Project: "))

    return ab, bb, cb, db, eb, ai, bi, ci, di, ei, ac, bc, cc, dc, ec, am, bm, cm, dm, em

name, classs, section, reg, date = information()
print("\n***Enter the marks of following Subject in following factor***")
ab, bb, cb, db, eb, ai, bi, ci, di, ei, ac, bc, cc, dc, ec, am, bm, cm, dm, em = marks()

tb = ab+bb+cb+db+eb
ti = ai+bi+ci+di+ei
tc = ac+bc+cc+dc+ec
tm = am+bm+cm+dm+em

#Outer Layout
print(f'''
    ----------------------------------------------------------------------------------------------------------------------------------
    |                                        SUNWAY INTERNATIONAL BUSINESS SCHOOL                                                    |
    |                            Behind Maitidevi Temple, Maitidevi, Kathmandu, Nepal, 01-4431725                                    |
    |                                                                                                                                |
    |                                                PROGRESS REPORT                                                                 |
    |                                        Semester Final Internal Result                                                          |
    |    BCS                                                                                                 ISSUED DATE:{date}  |''')
print("\t----------------------------------------------------------------------------------------------------------------------------------")
print(f'''    |    NAME: {name}                     SEMESTER: {classs}                     SECTION: {section}                       REGD NO.: {reg}   |''')
print(f'''    ----------------------------------------------------------------------------------------------------------------------------------
    |S.N|           Subject              |   1st Assignment  |   Internal Exam   |   Quizzes |   Group Project   |   Marks Obtained  |
    ----------------------------------------------------------------------------------------------------------------------------------
    | 1.| Basic Marketing                |        {ab}          |        {bb}           |    {cb}      |       {db}           |      {tb}           |
    ----------------------------------------------------------------------------------------------------------------------------------
    | 2.| Introduction to E-Commerce     |        {ai}          |        {bi}           |    {ci}      |       {di}           |      {ti}           |
    ----------------------------------------------------------------------------------------------------------------------------------
    | 3.| Computer Graphics              |        {ac}          |        {bc}           |    {cc}      |       {dc}           |      {tc}           |
    ----------------------------------------------------------------------------------------------------------------------------------
    | 4.| Mobile Programming             |        {am}          |        {bm}           |    {cm}      |       {dm}           |      {tm}           |
    ----------------------------------------------------------------------------------------------------------------------------------
    ''')