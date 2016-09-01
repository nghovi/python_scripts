#!/usr/bin/python
"""This python scripts is designed for daily task which should be done quickly

        It's supposed to be my first-add tool
        Here is some note: new tupe = tuple + tuple. Eg: viet = (1,) + viet
"""

##uyenhoangnguyenhoangnguyenhoangnguyenhoangnguyenhoangnguyenhoangnguyenhoangnguyenhoang
from file_manager import write_to_file, add_full_stop_to_file, standardize_file_name, rename_file, rename_files_in_folder
from number import fib, is_prime
import sqlite3_api
import task
import time
import datetime
import sys
import re


#todo: <string name="sdfs">sfjsf
# </string>
def qk_localize_text(file_en, file_jp):
    """Copy text from strings.xml to ja/strings.xml

    """
    fin = open(file_en, 'r')
    fin_ja = open(file_jp, 'r+')
    list_japanese_string = fin_ja.readlines()
    copy = []
    for line_i in fin:
        new_line = line_i
        if  re.search('<string', line_i): #if it's not comment line
            occurance = 0
            key = line_i[line_i.index('name="') + 6 : line_i.index('">')]
            #print "english key:" + key
            for japanese_string in list_japanese_string:
                if  re.search('<string', japanese_string): #if it's not comment line
                    ja_key = japanese_string[japanese_string.index('name="') + 6 : japanese_string.index('">')]
                    if key == ja_key:
                        occurance += 1
                        print japanese_string

                        ja_values = japanese_string[japanese_string.index('">') + 2 : japanese_string.index('</string>')]
                        new_line = line_i[:line_i.index('">') + 2] + ja_values + line_i[line_i.index('</stri'):]
                        #print "new line:" + new_line
            if occurance >= 2:
                pass
                #print "Duplicate string: " + line_i
        copy.append(new_line)

    #Write:
    fin_ja.seek(0)
    for li in copy:
        fin_ja.write(li)

    fin.close()
    fin_ja.close()

#todo: if string has some special character like ",', !, @, etc...
# def qk_generate_string(file_xml, file_str):
#     """Generate string id from xml file into strings.xml
#         for both en, jp

#     """
#     fin_xml = open(file_xml, 'r+')
#     fin_str = open(file_str, 'r+')
#     list_xml_string = fin_xml.readlines()
#     new_strings = []
#     base = 0
#     for line_i in list_xml_string:
#         if  re.search('android:text="', line_i) && not re.search('text="@':, line_i): #search string that hasn't got string id yet
#             str_value = line_i[line_i.index('text="') + 6 : line_i.index('"')]
#             base++
#             new_string = _create_str_key_val(base, file_xml, str_value)
#             new_strings.append(new_string)
    
#     while(str_key = fin_str.readline()):
#         if (re.search('</resource>')):
#             for new_string in new_strings:
#                 fin_str.write(new_string)
#             break

#     fin_xml.close
#     fin_str.close


# return something like
# todo better suffix
# <string name="k1101_txt_btn"></string>
def _create_str_key_val(base, file_xml, str_value):
    suffix = base + int(time.time())
    return '<string name="' + file_xml + '_' + suffix + '">' + str_value + '</string>'

def replace_text(folder_path):
    from glob import glob
    from os.path import isfile, sep
    file_paths = glob(folder_path + sep + '*')
    for fp_i in file_paths:
        if not isfile(fp_i):
            replace_text(fp_i) #if this is folder, then recursive
        else:
            if re.search(r'.xml', fp_i): #if this is xml file
                #read and replace each line
                with open(fp_i,'r') as f:
                    newlines = []
                    for line in f.readlines():
                        # new_line = re.sub(r'"(\d+sp)"', r'"@dimen/quicker_\1"', line)
                        new_line = re.sub(r'mLsv', r'mLst', line)
                        # if re.search('margin', line):
                        #     new_line = re.sub(r'"(\d+dp)"', r'"@dimen/margin_\1"', line)
                        # else:
                        #     new_line = re.sub(r'"(\d+dp)"', r'"@dimen/quicker_\1"', line)
                        newlines.append(new_line)

                #write
                with open(fp_i, 'w') as f:
                    for line in newlines:
                        f.write(line)

def qk_standardize_dimens():
    # folder_path = r'D:\projects\Quicker-adr\quicker-cl-adr\src\main\res'
    folder_path = r'D:\projects\Quicker-adr\quicker-cs-adr\src\main\java'
    replace_text(folder_path)

def show_services():
    choice = 1
    while choice:
        print '################Please chose our service#############'
        print '0: Exit'
        print '1: Manage Task'
        print '2: Rename files in folder'
        print '3: Standardize file name'
        print '4. Add full stop to file'
        choice = int(raw_input().strip())
        if choice == 0:
            print 'Goodbye, sir'
            break
        elif choice == 1:
            task.manage_task()
        elif choice == 2:
            rename_files_in_folder(sys.argv[1], sys.argv[1:])
        elif choice == 3 :
            standardize_file_name(sys.argv[1])
        elif choice == 4 :
             add_full_stop_to_file(sys.argv[1])
        else:
            print 'Your choice is  in database!'

if __name__ == '__main__':
     show_services()
    # qk_localize_text('D:\projects\Quicker-adr\quicker-cl-adr\src\main\\res\\values\strings.xml', 'D:\projects\Quicker-adr\quicker-cl-adr\src\main\\res\\values-ja\strings.xml')
    # qk_localize_text('D:\projects\Quicker-adr\quicker-cs-adr\src\main\\res\\values\strings.xml', 'D:\projects\Quicker-adr\quicker-cs-adr\src\main\\res\\values-ja\strings.xml')
    # qk_localize_text_cs()
    # qk_standardize_dimens()