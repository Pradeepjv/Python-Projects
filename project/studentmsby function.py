def calculate_highinmarks_social(student_list):
 highinmarks_social=0
 highinmarks_name=''
 for student in student_list:
    if(student.get("social") > highinmarks_social):
        highinmarks_social=student.get("social")
        highinmarks_name=student.get("name")
 print(f"The highest score is {highinmarks_social} by {highinmarks_name}")

student1={
    "maths":45,
    "social":75,
    "science":96,
    "name":'Virat'
}
student2={
    "maths":65,
    "social":85,
    "science":76,
    "name":'brat'
}

student_list=[student1,student2]

calculate_highinmarks_social(student_list)