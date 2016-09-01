#!/usr/bin/python
##uyenhoangnguyenhoangnguyenhoangnguyenhoangnguyenhoangnguyenhoangnguyenhoangnguyenhoang
"""This scripts contains function that help dealing with file

    Sometimes I have to rename all jpg file to png file, but i don't know how to do it  quickly with bash script,
    then this is my python tool
"""

def write_to_file(lines, file_path):
    """Write each element on the list down to file, appending "\n" as new line character

    """
    fout = open(file_path, 'w')
    for line_i in lines:
        fout.write(line_i + '\n')

def add_full_stop_to_file(file_path):
    """Add full_stop (period) punctuation at the end of line if there isn't

    """
    lines = open(file_path, 'rw')
    new_lines = []
    punctuation = set(['!', '#', '"', '%', '$', "'", '&', ')', '(', '+', '*', '-',
                    ',', '/', '.', ';', ':', '=', '<', '?', '>', '@', '[', ']',
                    '\\', '_', '^', '`', '{', '}', '|', '~'])
    for line_i in lines:
        line_i_stripped = line_i.strip()
        if len(line_i_stripped) >= 1 and line_i_stripped[-1] not in punctuation:
            line_i_stripped += '.'
        new_lines.append(line_i_stripped)

    write_to_file(new_lines, file_path)

def standardize_file_name(folder_path):
    """Standardize all files, directories name in specific folder:
        - change ' ' or '-' into '_'
        - change UPPER_CASE into lower_case

        folder_path does not include path separator at the end
    """
    from glob import glob
    from os.path import isdir, sep
    file_paths = glob(folder_path + sep + '*')
    for fp_i in file_paths:
        if isdir(fp_i):
            standardize_file_name(fp_i)
        rename_file(fp_i, ' ', '_','-', '_','A','a','B','b','C','c','D','d','E','e','F','f',
                'G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O',
                'o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w',
                'X','x','Y','y','Z','z')

def rename_file(file_path, *replacements):
    """Rename existing files

        arg -- replacements: a tuple like ('A', 'a', 'B', 'b') will replace all character A  and B by a and b, respectively
    """
    import os
    from ntpath import split
    parent_folder, file_name = split(file_path)

    num_pair = len(replacements) / 2
    for pair_i in range(0, num_pair):
        file_name = file_name.replace(replacements[pair_i * 2], replacements[pair_i * 2 + 1])

    os.rename(file_path, parent_folder + os.path.sep + file_name)

def rename_files_in_folder(folder_path, *replacements):
    """Rename all file in one folder, like *.png -> *.jpg

    Dont change sub-folder's name"""
    from glob import glob
    from os.path import isfile, sep
    file_paths = glob(folder_path + sep + '*')
    for fp_i in file_paths:
        if isfile(fp_i):
            rename_file(fp_i, *replacements) #note unpacking tuples before transfering to next func

if __name__ == '__main__':
    print "Do not run this script alone"
    print "test"
