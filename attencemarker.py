import csv
import qrcode
from datetime import date
import cv2
#list of students
students={
    "1":"Afre Shreya",
    "2":"Aryan Vijay",
    "3":"Budye Seher",
    "4":"Chalwadi Parshuram",
    "5":"Chouhan Bhawna",
    "6":"Dange Zaheer",
    "7":"Fernandes Abrelicia",
    "8":"Gazi Hani",
    "9":"Gupta Sanjana",
    "12":"Khan Hala",
    "13":"Khan Kabir",
    "14":"Kohari Maryam",
    "15":"Mahato Ayush",
    "16":"Masish Simon",
    "17":"Mirgal Sharvari",
    "18":"Mishra Shweta",
    "19":"More Trupti",
    "20":"Nimane Mitali",
    "21":"Pal Devesh",
    "22":"Patekar Krupa",
    "23":"Patil Gauri",
    "24":"Pau Arpita",
    "25":"Poojary Chirag",
    "26":"Prasad Yashraj",
    "27":"Rathore Anjali",
    "28":"Salunke Parth",
    "29":"Shaikh Abdur Rehman",
    "30":"Shaikh Maryam",
    "31":"Sharma Chanchal",
    "32":"Shekhavat Diya",
    "33":"Sukate Gayatri",
    "34":"Tiwari Anuj",
    "35":"Umbarkar Rhujuta",
    "36":"Yadav Khushi",
    "37":"Kalagate Prathammesh",
    "38":"Kale Pranav",
    "39":"Tiwari Harsh",
    "40":"Tuppadol Shraddha",
    "41":"Farid Haadi Qais Nida",
    "42":"Kadam Prathamesh",
    "43":"Paikrao Shreya",
    "44":"Vohra Satnam",
    "45":"Yadav Namisha",
    "46":"Asrani Roma",
    "47":"Behrani Rahul",
    "48":"Kadam Atharav",
    "49":"Mahadeshwar Yashika",
    "50":"Mishra Manas",
    "51":"Pal Dharmendrakumar",
    "54":"Shekhawat Govind",
    "55":"Tiwari Adarsh",
    "57":"Mohite Prachi",
    "58":"Vishwakarma Amrita",
    "59":"Molke Prathmesh",
    "60":"Madiwal Kirti",
    "61":"Gupta Hariom",
    "62":"Suryawanshi Suryaraj"
}
for sid,name in students.items():
    qr=qrcode.make(sid)
    qr.save(f"{name}_{sid}.png")


#logging of teacher
def logging_teacher():
    prof=input("Enter your Name :")
    password=input("Enter Password :")#password=Prof_secure
    if password=="Prof_secure":
        Print("Welcome ",prof)
        scanned_ids = []   # create empty list before scanning

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            for qr in decode(frame):
                sid = qr.data.decode('utf-8')

                if sid not in scanned_ids:   # avoid duplicates
                    scanned_ids.append(sid)
                    print("Scanned ID added:", sid)   # shows in console

            cv2.imshow("QR Attendance Scanner", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

        print("Final scanned IDs:", scanned_ids)
        ids_input = input("Enter scanned IDs (comma separated): ")

        attendance={}
        for sid,name in students.items():
            if sid in scanned_ids:
                attendance[sid]="Present"
            else:
                attendance[sid]="absent"
        today=date.today().strftime("%Y-%m-%d")
        filename=f"attendance_{today}.csv"

        with open(filename,"w",newline="") as f:
            writer=csv.writer(f)
            writer.writerow(["Student_ID","Name","Status"])
            for sid,status in attendance.items():
                writer.writerow([sid,students[sid],status])
        print(f"Attendance saved in {filename}")

    else:
            print("incorrect password!")
