
count= True
while (count):
    print """
    1> Display individual component
    2> Display component average
    3> Display Standard Report
    4> Sort by alternate column
    5> Change Pass/Fail point
    6> Exit"""

    choice= input("Select Menu : ")
    #print choice

    student_tuples=[]
    if(choice == 1):
        comp_name= raw_input("Enter Component Name : ")
        if(comp_name=="A1"):

            with open("a1.txt","r") as f:
                data = f.readline()
                print "A1 grade (", data.rstrip() ,") \n"
                data1=f.readlines()
                for line1 in data1:
                    id=line1.split("|").pop(0)
                    #print(line1)
                    with open("class.txt","r") as f:
                        data=f.readlines()
                        for line in data:
                            if id in line:
                                list=[]
                                list=line.split("|")
                                break
                    print line1.replace("|"," "+list[2].rstrip()+","+list[1].rstrip()+" ")

        if(comp_name=="A2"):

            with open("a2.txt","r") as f:
                data = f.readline()
                print "A2 grade (", data.rstrip() ,") \n"
                data1=f.readlines()
                for line1 in data1:
                    id=line1.split("|").pop(0)
                    #print(line1)
                    with open("class.txt","r") as f:
                        data=f.readlines()
                        for line in data:
                            if id in line:
                                list=[]
                                list=line.split("|")
                                break
                    print line1.replace("|"," "+list[2].rstrip()+","+list[1].rstrip()+" ")

        if(comp_name=="PR"):

            with open("project.txt","r") as f:
                data = f.readline()
                print "Project grade (", data.rstrip() ,") \n"
                data1=f.readlines()
                for line1 in data1:
                    id=line1.split("|").pop(0)
                    #print(line1)
                    with open("class.txt","r") as f:
                        data=f.readlines()
                        for line in data:
                            if id in line:
                                list=[]
                                list=line.split("|")
                                break
                    print line1.replace("|"," "+list[2].rstrip()+","+list[1].rstrip()+" ")

        if(comp_name=="T1"):

         with open("test1.txt","r") as f:
            data = f.readline()
            print "Test1 grade (", data.rstrip() ,") \n"
            data1=f.readlines()
            for line1 in data1:
                id=line1.split("|").pop(0)
                #print(line1)
                with open("class.txt","r") as f:
                    data=f.readlines()
                    for line in data:
                        if id in line:
                            list=[]
                            list=line.split("|")
                            break
                print line1.replace("|"," "+list[2].rstrip()+","+list[1].rstrip()+" ")

        if(comp_name=="T2"):

            with open("test2.txt","r") as f:
                data = f.readline()
                print "Test2 grade (", data.rstrip() ,") \n"
                data1=f.readlines()
                for line1 in data1:
                    id=line1.split("|").pop(0)
                #print(line1)
                    with open("class.txt","r") as f:
                        data=f.readlines()
                        for line in data:
                            if id in line:
                                list=[]
                                list=line.split("|")
                                break
                    print line1.replace("|"," "+list[2].rstrip()+","+list[1].rstrip()+" ")

# menu 2
    if(choice == 2):
        comp_name= raw_input("Enter Component Name : ")

        if(comp_name == "A1"):
            with open("a1.txt","r") as f:
                data = f.readline()
                data1=f.readlines()
                marks=0.0
                count=0
                for line in data1:
                    marks += int(line.split("|").pop(1))
                    count+=1
                print "A1 Average : "+str(marks/count)+"/"+data.rstrip()+"\n"


        if(comp_name == "A2"):
            with open("a2.txt","r") as f:
                data = f.readline()
                data1=f.readlines()
                marks=0.0
                count=0
                for line in data1:
                    marks += int(line.split("|").pop(1))
                    count+=1
                print "A2 Average : "+str(marks/count)+"/"+data.rstrip()+"\n"

        if(comp_name == "PR"):
            with open("project.txt","r") as f:
                data = f.readline()
                data1=f.readlines()
                marks=0.0
                count=0
                for line in data1:
                    marks += int(line.split("|").pop(1))
                    count+=1
                print "PR Average : "+str(marks/count)+"/"+data.rstrip()+"\n"

        if(comp_name == "T1"):
            with open("test1.txt","r") as f:
                data = f.readline()
                data1=f.readlines()
                marks=0.0
                count=0
                for line in data1:
                    marks += int(line.split("|").pop(1))
                    count+=1
                print "T1 Average : "+str(marks/count)+"/"+data.rstrip()+"\n"

        if(comp_name == "T2"):
            with open("test2.txt","r") as f:
                data = f.readline()
                data1=f.readlines()
                marks=0.0
                count=0
                for line in data1:
                    marks += int(line.split("|").pop(1))
                    count+=1
                print "Test2 Average : "+str(marks/count)+"/"+data.rstrip()+"\n"

# menu 2
    if(choice == 3):
        print """ID\tLN\tFN\tA1\tA2\tPR\tT1\tT2\tGR\tFL\n"""


        list=range(10)
        with open("class.txt","r") as f:
            data1=f.readlines()
            for line1 in data1:
                id=line1.rstrip().split("|").pop(0)
                ln=line1.rstrip().split("|").pop(2)
                fn=line1.rstrip().split("|").pop(1)
                list[0]=id
                list[1]=ln
                list[2]=fn





                #print(line1)
                with open("a1.txt","r") as f:
                    atotal1=f.readline().rstrip()
                    data=f.readlines()
                    for line in data:
                        if list[0] in line:
                            list1=[]
                            list1=line.rstrip().split("|")
                            list[3]=line.rstrip().split("|").pop(1)
                            break
                        else:
                            list[3]=0

                with open("a2.txt","r") as f:
                    atotal2=f.readline().rstrip()
                    data=f.readlines()
                    for line in data:
                        if list[0] in line:
                            list1=[]
                            list1=line.rstrip().split("|")
                            list[4]=line.rstrip().split("|").pop(1)
                            break
                        else:
                            list[4]=0

                with open("project.txt","r") as f:
                    ptotal=f.readline().rstrip()
                    data=f.readlines()
                    for line in data:
                        if list[0] in line:
                            list1=[]
                            list1=line.rstrip().split("|")
                            list[5]=line.rstrip().split("|").pop(1)
                            break
                        else:
                            list[5]=0

                with open("test1.txt","r") as f:
                    ttotal1=f.readline().rstrip()
                    data=f.readlines()
                    for line in data:
                        if list[0] in line:
                            list1=[]
                            list1=line.rstrip().split("|")
                            list[6]=line.rstrip().split("|").pop(1)
                            break
                        else:
                            list[6]=0

                with open("test2.txt","r") as f:
                    ttotal2=f.readline().rstrip()
                    data=f.readlines()
                    for line in data:
                        if list[0] in line:
                            list1=[]
                            list1=line.rstrip().split("|")
                            list[7]=line.rstrip().split("|").pop(1)
                            break
                        else:
                            list[7]=0


                #marks/maxmarks*weightage
                list[8]= ((float(list[3])/float(atotal1))*7.5) + ((float(list[4]))/float(atotal2)*7.5) + ((float(list[5])/float(ptotal))*25) +  \
                         ((float(list[6])/float(ttotal1))*30) + ((float(list[7])/float(ttotal2))*30)

                #final

                if (list[8]<50):
                    list[9]="F"
                if ( 50<= list[8] <=58 ):
                    list[9]="C"
                if (59<= list[8] <=65):
                    list[9]="B-"
                if (66<= list[8] <=72):
                    list[9]="B"
                if (73<= list[8] <=79):
                    list[9]="B+"
                if (80<= list[8] <=86):
                    list[9]="A-"
                if (87<= list[8] <=93):
                    list[9]="A"
                if (94<= list[8] <=100):
                    list[9]="A+"



                student_tuples.append(tuple(list))
              #  print '{:5}'.format(list[0])+"\t"+'{:6}'.format(list[1])+"\t"+'{:6}'.format(list[2])+"\t\t"+str(list[3])+\
               #       "\t\t"+str(list[4])+"\t\t"+str(list[5])+"\t\t"+str(list[6])+"\t\t"+str(list[7])+"\t\t"+ str(int(list[8]))+"\t\t"+list[9]+"\n"



        student_tuples1= sorted(student_tuples, key=lambda student: student[0])
        for name in student_tuples1:
            y=name[1]
            #print y
            # print student_tuples
            print '{:5}'.format(name[0])+"\t"+'{:6}'.format(name[1])+"\t"+'{:6}'.format(name[2])+"\t"+str(name[3])+ \
              "\t"+str(name[4])+"\t"+str(name[5])+"\t"+str(name[6])+"\t"+str(name[7])+"\t"+ str(int(name[8]))+"\t"+name[9]+"\n"




# menu 4
    if(choice == 4):
        sort_by= raw_input("Sort by LT (last name) or by GR (numeric grade) : ")

        list=range(10)
        with open("class.txt","r") as f:
                data1=f.readlines()
                for line1 in data1:
                    id=line1.rstrip().split("|").pop(0)
                    ln=line1.rstrip().split("|").pop(2)
                    fn=line1.rstrip().split("|").pop(1)
                    list[0]=id
                    list[1]=ln
                    list[2]=fn





                    #print(line1)
                    with open("a1.txt","r") as f:
                        atotal1=f.readline().rstrip()
                        data=f.readlines()
                        for line in data:
                            if list[0] in line:
                                list1=[]
                                list1=line.rstrip().split("|")
                                list[3]=line.rstrip().split("|").pop(1)
                                break
                            else:
                                list[3]=0

                    with open("a2.txt","r") as f:
                        atotal2=f.readline().rstrip()
                        data=f.readlines()
                        for line in data:
                            if list[0] in line:
                                list1=[]
                                list1=line.rstrip().split("|")
                                list[4]=line.rstrip().split("|").pop(1)
                                break
                            else:
                                list[4]=0

                    with open("project.txt","r") as f:
                        ptotal=f.readline().rstrip()
                        data=f.readlines()
                        for line in data:
                            if list[0] in line:
                                list1=[]
                                list1=line.rstrip().split("|")
                                list[5]=line.rstrip().split("|").pop(1)
                                break
                            else:
                                list[5]=0

                    with open("test1.txt","r") as f:
                        ttotal1=f.readline().rstrip()
                        data=f.readlines()
                        for line in data:
                            if list[0] in line:
                                list1=[]
                                list1=line.rstrip().split("|")
                                list[6]=line.rstrip().split("|").pop(1)
                                break
                            else:
                                list[6]=0

                    with open("test2.txt","r") as f:
                        ttotal2=f.readline().rstrip()
                        data=f.readlines()
                        for line in data:
                            if list[0] in line:
                                list1=[]
                                list1=line.rstrip().split("|")
                                list[7]=line.rstrip().split("|").pop(1)
                                break
                            else:
                                list[7]=0


                    #marks/maxmarks*weightage
                    list[8]= ((float(list[3])/float(atotal1))*7.5) + ((float(list[4]))/float(atotal2)*7.5) + ((float(list[5])/float(ptotal))*25) + \
                             ((float(list[6])/float(ttotal1))*30) + ((float(list[7])/float(ttotal2))*30)

                    #final

                    if (list[8]<50):
                        list[9]="F"
                    if ( 50<= list[8] <=58 ):
                        list[9]="C"
                    if (59<= list[8] <=65):
                        list[9]="B-"
                    if (66<= list[8] <=72):
                        list[9]="B"
                    if (73<= list[8] <=79):
                        list[9]="B+"
                    if (80<= list[8] <=86):
                        list[9]="A-"
                    if (87<= list[8] <=93):
                        list[9]="A"
                    if (94<= list[8] <=100):
                        list[9]="A+"



                    student_tuples.append(tuple(list))
                    #print '{:5}'.format(list[0])+"\t"+'{:6}'.format(list[1])+"\t"+'{:6}'.format(list[2])+"\t\t"+str(list[3])+ \
                    #      "\t\t"+str(list[4])+"\t\t"+str(list[5])+"\t\t"+str(list[6])+"\t\t"+str(list[7])+"\t\t"+ str(int(list[8]))+"\t\t"+list[9]+"\n"


        if(sort_by=="LT"):
            print """ID\tLN\tFN\tA1\tA2\tPR\tT1\tT2\tGR\tFL\n"""



            student_tuples1= sorted(student_tuples, key=lambda student: student[1])
            for name in student_tuples1:
                y=name[1]
                #print y
                # print student_tuples
                print '{:5}'.format(name[0])+"\t"+'{:6}'.format(name[1])+"\t"+'{:6}'.format(name[2])+"\t"+str(name[3])+ \
                  "\t"+str(name[4])+"\t"+str(name[5])+"\t"+str(name[6])+"\t"+str(name[7])+"\t"+ str(int(name[8]))+"\t"+name[9]+"\n"

        if(sort_by=="GR"):
            print """ID\tLN\tFN\tA1\tA2\tPR\tT1\tT2\tGR\tFL\n"""



            student_tuples1= sorted(student_tuples, key=lambda student: student[8])
            for name in student_tuples1:
                y=name[1]
                #print y
                # print student_tuples
                print '{:5}'.format(name[0])+"\t"+'{:6}'.format(name[1])+"\t"+'{:6}'.format(name[2])+"\t"+str(name[3])+ \
                      "\t"+str(name[4])+"\t"+str(name[5])+"\t"+str(name[6])+"\t"+str(name[7])+"\t"+ str(int(name[8]))+"\t"+name[9]+"\n"




            # menu 6

    if(choice == 5):
        point=input("Enter new Pass/Fail point : ")


    if(choice == 6):
        print "Good Bye"
        count=False






