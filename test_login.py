from Individual import *
from Student import *
from Instructor import *
from Admin import *
import sqlite3

# This is a test for the login function for every individual type

if __name__ == '__main__':
    
    
    # Instantiate each of the invdividual type classes
    S = Student()
    I = Instructor()
    A = Admin()

    flag = False

    # Reset and open the text file
    outfile = open('login_test_output.txt', 'w')
 
    # Try with valid information
    outfile.write('Valid Inputs::')
    outfile.write('EXPECTED RESULT: True\n')
    outfile.write(str(S.login('1112', 'student', '1')) + ',')
    outfile.write(str(I.login('2111', 'instructor', '1')) + ',')
    outfile.write(str(A.login('3111', 'admin', '1')) + '\n\n')

    # Try with invalid passwords
    outfile.write('Invalid Passwords::')
    outfile.write ('EXPECTED RESULT: False\n')
    outfile.write(str(S.login('1111', 'student', '2')) + ',')
    outfile.write(str(I.login('2111', 'instructor', '2')) + ',')
    outfile.write(str(A.login('3111', 'admin', '2')) + '\n\n')

    # Try with characters as the ID\
    outfile.write('Invalid Inputs::')
    outfile.write('EXPECTED RESULT: False\n')
    outfile.write(str(S.login('qwerty', 'student', '1')) + ',')
    outfile.write(str(I.login('asdfg', 'instructor', '1')) + ',')
    outfile.write(str(A.login('hjkl;', 'admin', '1'))  + '\n\n')

    # Try with nothing entered for individual type
    outfile.write('No Individual Type Selected::')
    outfile.write ('EXPECTED RESULT: False\n')
    outfile.write(str(S.login('1111', '', '1')) + ',')
    outfile.write(str(I.login('2111', '', '1')) + ',')
    outfile.write(str(A.login('3111', '', '1')) + '\n\n')

    outfile.close()