from django.db import models


#one to one relationship
class Rollnumber(models.Model):
    roll_number = models.PositiveIntegerField()

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.OneToOneField(Rollnumber , on_delete=models.CASCADE)


# Backward or forward ki process ko samjhan one-to-one field ke case me

# forward ---->
# 1. i want to access the data from child to parent so this process called forward process -
    #  in this model example we can access the student data like (ki jo student ka roll number he vo Rollnumber model se aaraha he to ise ham easily extract kar sakte he kese me dikhata hu)
    
    # Using Queryset ---->
    #                     student_data = Student.objects.all();
    #                     this line get all objects from the models ab ise easily access kar sakte he roll number 
                        
    #                     for i in student_data:
    #                         print(i.name , i.roll.roll_number)

    # Using singal record ---->
    #                     Student_data = Student.objects.get(id=1)
    #                     Student_data.name   # ram
    #                     Student_data.roll.roll_number
    

# Backword ----> jab ham parent table ke through child table ka data get karna chahte he to is process ko backword
#                process bolte he.
                #  ham yaha releated_name or model ke name ka use karke data access kar sakte he 
                # suppose
                # mere pass do model he jo uper dikh rhe he 
                
                # example ---->
                            # using queryset ---->
                            #             roll_table_obj =  Rollnumber.objects.all()
                            #             for i in roll_table_obj:
                            #                 # print(i.roll , i.releated_name.filed_name)
                            #                 print(i.roll , i.ram.name)


                #Note ---->  is senerio me ham set_all() ka use nhi kar sakte he 




