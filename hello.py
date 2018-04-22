import sys, os

from numpy import linspace

sys.path.append("/Users/shiftehsherafat/PycharmProjects/Test-/lib/")

from utils import hei


#x = linspace()

hei()

utils_path = '/Users/shiftehsherafat/PycharmProjects/Test-/lib/utils.py'

if not os.path.exists(utils_path):
    os.makedirs()
    print('directory exists')

#print(os.path.(utils_path))

filename, file_extention = os.path.basename(utils_path).split('.')

if file_extention == 'py':
    print('file is : %s' % file_extention)


print('filename : %s, extention: %s' % (filename, file_extention))




# print "Hello,world! What is the weather today? (nice/rainy))"
# var = sys.argv[1]
# if IndexError:
#         response = raw_input("Please provide rainy/nice: ")
#
#         if var == "nice":
#                 print "Then lets go outside and enjoy the weather!"
#
#         print "Lets stay in an read a good book!"
#


