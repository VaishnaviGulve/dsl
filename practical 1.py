"""
Write a python program to store marks scored in subject Fundamental of
Data Structure by N students in the class. Write functions to compute following:
a)	The average score of class 
b)	Highest score and lowest score of class 
c)	Count of students who were absent for the test
d)	Display mark with highest frequency

"""

def accept_marks(A):   
   n = int(input("Enter the total no. of student : "))
   for i in range(n) :
      while True :
         x = input("Enter the marks scored in FDS for student %d : "%(i+1))
         if(x == "AB"):
            x = -1   # indicates Absent students
            break
         x = int(x)
         if(x >= 0 and x <= 30) :
            break
         else :
            print("Plz enter valid marks out of 30")      
      A.append(x)
   print("Marks accepted & stored successfully");

def display_marks(A) :
   print("\nMarks Scored in FDS")
   for i in range(len(A)):
      if(A[i] == -1) :
         print("\tStudent %d : AB"%(i+1))
      else :
         print("\tStudent %d : %d"%(i+1,A[i]))
      
def search_set(A,X) :
    n = len(A)
    for i in range(n):
       if(A[i] == X) :
          return (1)
    return (0)

def find_average_score_of_class(A) :
   sum = 0
   for i in range(len(A)) :
      if(A[i] != -1) :
         sum = sum + A[i]
   avg = sum / len(A)
   display_marks(A)
   print("\nAverage score of class is %.2f\n\n"%avg)
   
def find_highest_and_lowest_score_of_class(A) :
   max = -1
   min = 31
   for i in range(1,len(A)) :
      if(max < A[i]) :
         max = A[i]
         max_ind = i
      if(min > A[i] and A[i] != -1) :
         min = A[i]
         min_ind = i
   display_marks(A)
   print("Highest Mark Score of class is %d scored by student %d"%(max,max_ind+1))
   print("Lowest Mark Score of class is %d scored by student %d"%(min,min_ind+1))        
   
def find_count_of_absent_students(A) :
   count = 0
   for i in range(len(A)):
      if(A[i] == -1) :
         count += 1
   display_marks(A)
   print("\tAbsent Student Count = %d"%count)
      
def display_mark_with_highest_frequency(A) :
   freq = 0
   for i in range(len(A)) :
      count = 0
      if(A[i] != -1) :
         for j in range(len(A)):
            if(A[i] == A[j]) :
               count += 1
      if(freq < count) :
         Marks = A[i]
         freq = count
   display_marks(A)
   print("\nMarks with highest frequency is %d (%d)"%(Marks,freq))
   
def main():
   FDS_Marks = []
   while True :
      print ("\t\t1 : Accept FDS Marks")
      print ("\t\t2 : Average score of class")
      print ("\t\t3 : Highest score and lowest score of class")
      print ("\t\t4 : Count of students who were absent for the test")
      print ("\t\t5 : Display mark with highest frequency")
      print ("\t\t6 : Exit")
      ch = int(input("Enter your choice : "))
      if (ch == 6):
         print ("End of Program")
         quit()
      elif (ch == 1) :
         accept_marks(FDS_Marks)
         display_marks(FDS_Marks)
      elif (ch == 2) :
         find_average_score_of_class(FDS_Marks)
      elif (ch == 3) :
         find_highest_and_lowest_score_of_class(FDS_Marks)
      elif (ch == 4) :
         find_count_of_absent_students(FDS_Marks)
      elif (ch == 5) :
         display_mark_with_highest_frequency(FDS_Marks)
      else :
         print ("Wrong choice entered !! Try again")

main()
