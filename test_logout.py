from Individual import *
from Student import *
from Instructor import *
from Admin import *
import sqlite3

# This is a test for the logout function for every individual type

if __name__ == '__main__':

    # Instantiate each of the invdividual type classes and a flag for the output
    S = Student()
    I = Instructor()
    A = Admin()
    flag = False
    # Reset and open the text file
    outfile = open('logout_test_output.txt', 'w')


    outfile.write('User enters yes\n')
    outfile.write('Should return false: \n')
    outfile.write(str(S.logout(confirm="y")) + ', ')
    outfile.write(str(I.logout(confirm='y')) + ', ')
    outfile.write(str(A.logout(confirm='y')) + '.\n\n')

    
    outfile.write('User enters no\n')
    outfile.write("Should return true: \n")
    outfile.write(str(S.logout(confirm='n')) + ', ')
    outfile.write(str(I.logout(confirm='n')) + ', ')
    outfile.write(str(A.logout(confirm='n'))  + '.\n\n') 

    outfile.write('User enters a number\n')
    outfile.write("Should return true: \n")
    outfile.write(str(S.logout(confirm='1')) + ', ')
    outfile.write(str(I.logout(confirm='2')) + ', ')
    outfile.write(str(A.logout(confirm='3'))  + '.\n\n') 
    
    outfile.write('User enters nothing\n')
    outfile.write("Should return true: \n")
    outfile.write(str(S.logout(confirm='')) + ', ')
    outfile.write(str(I.logout(confirm='')) + ', ')
    outfile.write(str(A.logout(confirm=''))  + '.\n\n') 

    outfile.close()