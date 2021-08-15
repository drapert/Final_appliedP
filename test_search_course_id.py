from Individual import *
from Student import *
from Instructor import *
from Admin import *
import sqlite3

# This is a test for the login function for every individual type
def check_results(results):
    # Checks length of results (if there is a course found) and outputs data to a txt file
    outfile.write('Output: ')
    if isinstance(results, list):
        outfile.write(results[0] + '\n')
    else:
        outfile.write("Nothing was output.\n")

if __name__ == '__main__':
    
    
    # Instantiate each of the invdividual type classes
    S = Student()
    I = Instructor()
    A = Admin()


    # Reset and open the text file
    outfile = open('course_id_search_test_output.txt', 'w')
    outfile.write('Search a valid course\n')
    outfile.write('SHOULD RETURN THE NAME OF A COURSE (EMBEDDED SENSOR NETWORKS).\n')
    results = S.course_search_id('4050')
    check_results(results)
    results = I.course_search_id('4050')
    check_results(results)
    results = A.course_search_id('4050')
    check_results(results)

    outfile.write('\n\n')


    outfile.write('Search an invalid course ID\n')
    outfile.write('SHOULD RETURN "Nothing was output."\n')
    results = S.course_search_id('40111')
    check_results(results)
    results = I.course_search_id('40111')
    check_results(results)
    results = A.course_search_id('40111')
    check_results(results)

    outfile.write('\n\n')
    
    outfile.write('Search an invalid course ID (not an integer)\n')
    outfile.write('SHOULD RETURN "Nothing was output."\n')
    results = S.course_search_id('Hello')
    check_results(results)
    results = I.course_search_id('Hello')
    check_results(results)
    results = A.course_search_id('Hello')
    check_results(results)

    outfile.write('\n\n')

    outfile.write('Search nothing\n')
    outfile.write('SHOULD RETURN "Nothing was output."\n')
    results = S.course_search_id('')
    check_results(results)
    results = I.course_search_id('')
    check_results(results)
    results = A.course_search_id('')
    check_results(results)
    outfile.close()

