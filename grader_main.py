###########################################
##### FIND THE SCORE FOR THE STUDENT ######
###########################################


##### DEFINE GRADE RANGES ####
grade       = ""
modifyScale = 0
n           = 1
aPlusBottom = 97.0001
aTop        = 97.0
aBottom     = 90.0
bPlusTop    = 89.9999
bPlusBottom = 87.0
bTop        = 86.9999
bBottom     = 80.0
cPlusTop    = 79.9999
CPlusBottom = 77.0
cTop        = 76.9999
cBottom     = 70.0
dPlusTop    = 69.9999
dPlusBottom = 67.0
dTop        = 69.9999
dBottom     = 60.0
failgrade   = 59.9999


#####################################
####### MODIFY SCALE ################
#####################################

#####################################
#FUTURE DEV- ADJUST GRADE SCALE###
'''
while (n == 1):
  modifyScale = 0
  modifyScale = int(input("Would you like to modify the grading scale?\n Please type 1 for yes or 2 for no, then press enter:"))
  if modifyScale == 1:
    aPlusBottom = input("Please define the lowest grade for an A+")
    break
  elif modifyScale == 2:
    print ("no")
    break
  else:
    print ("Sorry, didn't get that.  Please try again.")
    n = 1
'''
#####################################  

score = input("Enter score: ")
score = int(score)

if (score >= aPlusBottom):
    grade = "A+"
elif (score >= aBottom and score <= aTop):
    grade = 'A'
elif (score >= bBottom and score <= bTop):
    grade = 'B'
elif (score >= cBottom and score <= cTop):
    grade = 'C'
elif (score >= dBottom and score <= dTop): 
    grade = 'D'
elif (score <= failgrade):
    grade = 'F'

print ("\n\n Grade is: ", grade)
print ("")
