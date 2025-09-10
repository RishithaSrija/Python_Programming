def high_marks(record):
    max_record = record[0]
    for rec in record[1:]:
        if rec[2] > max_record[2]: 
            max_record = rec
    
    print(f"Highest marks : Student roll no {max_record[0]} Student name {max_record[1]} Student marks {max_record[2]}")

def marks_75(record):
     print("Student with marks>75: ")
     for rec in record:
        if rec[2] > 75: 
           print(f"Highest marks : Student roll no {rec[0]} Student name {rec[1]} Student marks {rec[2]}")
     if not found:
            print("No student has marks above 75.")


def stu_records():
    record=()
    for _ in range(5):
        roll_no=input("Enter roll no: ")
        name=input("Enter name: ")
        marks=(int,input("Enter marks "))
        record.append(roll_no,name,marks) 
    high_marks(record)
    marks_75(record)      

stu_records()
