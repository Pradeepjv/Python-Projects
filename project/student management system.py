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

highinmarks_maths=0
highinmarks_name=0
for student in student_list:
    if(student.get("maths")>highinmarks_maths):
        highinmarks_maths=student.get("maths")
        highinmarks_name=student.get("name")
print(f"The highest score is {highinmarks_maths} by {highinmarks_name}")