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






# many to one relationship
 
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE , related_name='auth')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

# Explation of many to one relationship

# Forward  ----> Forward is same like a one to one relationship we can directly access parent property
           
           
            # single record
            # ---------------


            # >>> a = Album.objects.filter(name="Ramayan")
            # >>> a
            #     <Album: ramayan>
            # >>> # now i use forward relation to access author first name jo album me he
            # >>> a.artist.first_name
            #     'Vijay'



            # Queryset ---->
            # ---------------


            # >>> for i in Album.objects.all():
            # ...  print(i.name , i.artist.first_name)



# Backward ---->
# ------------------
    # Jab ham parent model se child ki property ko extract karna chahte he to ham backward relation use karte he
    # ham yah do tariko se kar sakte he 
    
    # first ----> using set.all()
    # second -----> using releate_name



    # so lets discuss first approch
    # using set.all()
         
        #  using single record ---->
        # --------------------------

                    # >>> a = Musician.objects.get(first_name='Vijay')
                    # >>> a
                    # <Musician: Vijay>
                    # >>> a1 = a.album_set.all()
                    # >>> a1
                    # <QuerySet [<Album: ramayan>, <Album: mahabharat>, <Album: Bhagwat>]>
                    # >>> 
        
        #   using queryset ----->
        # -----------------------

                # >>> for i in Musician.objects.all():
                # ...  print( i.first_name , i.last_name ,i.album_set.all())
                # ... 
                # Vijay Goyal <QuerySet [<Album: ramayan>, <Album: mahabharat>, <Album: Bhagwat>]>
                # Arijit Singh <QuerySet [<Album: Pyari samjh gyi>, <Album: Geetanjali>]>
                # Ramesh Jain <QuerySet [<Album: All Is well>, <Album: Bhagwat1>]>
                # Raju Yadav <QuerySet [<Album: Shivayam>, <Album: Ganesha>, <Album: Radhe-Shyam>]>
                # Mohan Pal <QuerySet [<Album: Prakasham>]>
                # Surendra Parjapat <QuerySet []>



     # Using related_name

    #             >>> a = Musician.objects.get(first_name='Vijay')
    #             >>> a
    #             <Musician: Vijay>
    #             >>> a1 = a.auth.all()
    #             >>> a1
    #             <QuerySet [<Album: ramayan>, <Album: mahabharat>, <Album: Bhagwat>]>