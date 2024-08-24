import DateTime as dt
import mysql.connector as conn
import matplotlib.pyplot as plt

tSubs = {1: 'DS', 2: 'CAMP', 3: 'ADE', 4: 'DM', 5: 'DT', 6: 'DBMS'}
lSubs = {7: 'DS LAB', 8: 'DT LAB', 9: 'DBMS LAB'}
total = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
timetable = {'Mon': [1, 3, 6, 5, 4], 'Tue': [9, 4, 5, 2], 'Wed': [7, 6, 3, 1], 'Thu': [9, 3, 2, 6, 1],
             'Fri': [4, 5, 2], 'Sat': [], 'Sun': []}
graph = {}

mydb = conn.connect(
    host="localhost",
    user="hary",
    password="password",
    database="hariee_1"
)

mycursor = mydb.cursor()
# query = "CREATE TABLE IF NOT EXISTS attendance_v1(Subject VARCHAR(255),Present VARCHAR(255),Absent VARCHAR(255),Total VARCHAR(255))"
subs = list(tSubs.values())+list(lSubs.values())

def insertSubs(subject):
    print(subject)
    query = "INSERT INTO attendance_v1(Subject, Present , Absent , Total ) VALUES (%s,%s,%s,%s)"
    mycursor.executemany(query, [(subject, 0, 0, 0)])

def updateAttendance(subject,status):
    if status == 1:
        if subject in tSubs:
            query = "UPDATE attendance_v1 SET Present = Present +1,Total = Total+1 WHERE Subject = "+'"'+subject+'"'
        else:
            query = "UPDATE attendance_v1 SET Present = Present +2,Total = Total+2 WHERE Subject = "+'"'+subject+'"'
        mycursor.execute(query)
    else:
        if subject in lSubs:
            query = "UPDATE attendance_v1 SET Absent = Absent +2,Total = Total+2 WHERE Subject = "+'"'+subject+'"'
        else:
            query = "UPDATE attendance_v1 SET Absent = Absent +2,Total = Total+2 WHERE Subject = "+'"' + subject+'"'
        mycursor.execute(query)
    mydb.commit()

class Tracker:
    def __init__(self):
        print('in constructor')
        Today = dt.DateTime()
        self.day = Today.aDay()
    def update(self):
        print("Today's TimeTable is:" )
        for i in timetable[self.day]:
            if i > 6:
                print(lSubs[i],end='->')
            else:
                print(tSubs[i],end='->')
        print('END\nEnter a list(coma separated) for Attendance as(Present:1/Absent:0):')
        attend = list(map(int,input().split(',')))
        for i in timetable[self.day]:
            if i > 6:
                updateAttendance(lSubs[i],attend[0])
            else:
                updateAttendance(tSubs[i],attend[0])
            attend.pop(0)
    def display(self):
        for i in subs:
            query = "SELECT (Present/Total)*100 AS Percentage FROM Attendance_v1 WHERE Subject = "+'"'+i+'"'
            mycursor.execute(query)
            for j in mycursor.fetchall():
                for k in j:
                    graph[i] = float(k)
        print(graph)
        fig = plt.figure()
        ax = fig.add_subplot(111)
        bars = ax.bar(graph.keys(), graph.values(),width = 0.5)
        plt.title("Attendance vs Subject")
        plt.xlabel("Subjects")
        plt.ylabel("Percentage")
        plt.yticks([0,10,20,30,40,50,60,70,80,90,100])
        for bar in bars:
            plt.text(bar.get_x(),bar.get_height()+0.2,str(int(bar.get_height()))+'%')
        plt.grid(linewidth=0.5, linestyle='--',alpha=0.6,color='grey')

        plt.show()
s1=Tracker()
# s1.update()
s1.display()
mydb.commit()
mydb.close()