#-------------------------------------------------------------------------------
# Name:        Logic Problem Generator Parser
# Purpose:
#
# Author:      Sehktel
#
# Created:     18.01.2024
# Copyright:   (c) Sehktel 2024
# Licence:     MIT
#-------------------------------------------------------------------------------

import re

import os
import numpy as np

# Function to read author names from namelist.txt
def get_author_names(group):
    with open(group+'_namelist.txt', 'r') as file:
        return file.read().strip().splitlines()

# Function to read group names from grouplist.txt
def get_group_names():
    with open('grouplist.txt', 'r') as file:
        return file.read().strip().splitlines()

def generate_and_save_documents():
    group_names = get_group_names()

    for group in group_names:
        author_names = get_author_names(group)
        for author in author_names:
            document_name = f"./{group}/{author}.tex"
            author_name = author
            # Generate random matrices
            matric_a = np.random.randint(2, size=(2, 4))
            matric_b = np.random.randint(2, size=(4, 2))
            matric_c = np.random.randint(2, size=(4, 4))
            matric_d = np.random.randint(2, size=(8, 4))
            matric_f = np.random.randint(2, size=(8, 8))


            # Read the content from the input file
            with open(document_name, 'r') as file:
                content = file.read()

            # Define the replacement dictionary
            replacements = {
                'author_name' : author_name,
                'a1': str(matric_a[0,0]),
                'a2': str(matric_a[0,1]),
                'a3': str(matric_a[0,2]),
                'a4': str(matric_a[0,3]),
                'a5': str(matric_a[1,0]),
                'a6': str(matric_a[1,1]),
                'a7': str(matric_a[1,2]),
                'a8': str(matric_a[1,3]),

                'b1': str(matric_b[0,0]),
                'b2': str(matric_b[0,1]),
                'b3': str(matric_b[1,0]),
                'b4': str(matric_b[1,1]),
                'b5': str(matric_b[2,0]),
                'b6': str(matric_b[2,1]),
                'b7': str(matric_b[3,0]),
                'b8': str(matric_b[3,1]),

                'c01': str(matric_c[0,0]),
                'c02': str(matric_c[0,1]),
                'c03': str(matric_c[0,2]),
                'c04': str(matric_c[0,3]),
                'c05': str(matric_c[1,0]),
                'c06': str(matric_c[1,1]),
                'c07': str(matric_c[1,2]),
                'c08': str(matric_c[1,3]),
                'c09': str(matric_c[2,0]),
                'c10': str(matric_c[2,1]),
                'c11': str(matric_c[2,2]),
                'c12': str(matric_c[2,3]),
                'c13': str(matric_c[3,0]),
                'c14': str(matric_c[3,1]),
                'c15': str(matric_c[3,2]),
                'c16': str(matric_c[3,3]),


                'd01': str(matric_d[0,0]),
                'd02': str(matric_d[0,1]),
                'd03': str(matric_d[0,2]),
                'd04': str(matric_d[0,3]),
                'd05': str(matric_d[1,0]),
                'd06': str(matric_d[1,1]),
                'd07': str(matric_d[1,2]),
                'd08': str(matric_d[1,3]),
                'd09': str(matric_d[2,0]),
                'd10': str(matric_d[2,1]),
                'd11': str(matric_d[2,2]),
                'd12': str(matric_d[2,3]),
                'd13': str(matric_d[3,0]),
                'd14': str(matric_d[3,1]),
                'd15': str(matric_d[3,2]),
                'd16': str(matric_d[3,3]),

                'd17': str(matric_d[4,0]),
                'd18': str(matric_d[4,1]),
                'd19': str(matric_d[4,2]),
                'd20': str(matric_d[4,3]),
                'd21': str(matric_d[5,0]),
                'd22': str(matric_d[5,1]),
                'd23': str(matric_d[5,2]),
                'd24': str(matric_d[5,3]),
                'd25': str(matric_d[6,0]),
                'd26': str(matric_d[6,1]),
                'd27': str(matric_d[6,2]),
                'd28': str(matric_d[6,3]),
                'd29': str(matric_d[7,0]),
                'd30': str(matric_d[7,1]),
                'd31': str(matric_d[7,2]),
                'd32': str(matric_d[7,3]),

                'f01': str(matric_f[0,0]),
                'f02': str(matric_f[0,1]),
                'f03': str(matric_f[0,2]),
                'f04': str(matric_f[0,3]),
                'f05': str(matric_f[1,0]),
                'f06': str(matric_f[1,1]),
                'f07': str(matric_f[1,2]),
                'f08': str(matric_f[1,3]),
                'f09': str(matric_f[2,0]),
                'f10': str(matric_f[2,1]),
                'f11': str(matric_f[2,2]),
                'f12': str(matric_f[2,3]),
                'f13': str(matric_f[3,0]),
                'f14': str(matric_f[3,1]),
                'f15': str(matric_f[3,2]),
                'f16': str(matric_f[3,3]),

                'f17': str(matric_f[4,0]),
                'f18': str(matric_f[4,1]),
                'f19': str(matric_f[4,2]),
                'f20': str(matric_f[4,3]),
                'f21': str(matric_f[5,0]),
                'f22': str(matric_f[5,1]),
                'f23': str(matric_f[5,2]),
                'f24': str(matric_f[5,3]),
                'f25': str(matric_f[6,0]),
                'f26': str(matric_f[6,1]),
                'f27': str(matric_f[6,2]),
                'f28': str(matric_f[6,3]),
                'f29': str(matric_f[7,0]),
                'f30': str(matric_f[7,1]),
                'f31': str(matric_f[7,2]),
                'f32': str(matric_f[7,3]),

                'f33': str(matric_f[0,4]),
                'f34': str(matric_f[0,5]),
                'f35': str(matric_f[0,6]),
                'f36': str(matric_f[0,7]),
                'f37': str(matric_f[1,4]),
                'f38': str(matric_f[1,5]),
                'f39': str(matric_f[1,6]),
                'f40': str(matric_f[1,7]),
                'f41': str(matric_f[2,4]),
                'f42': str(matric_f[2,5]),
                'f43': str(matric_f[2,6]),
                'f44': str(matric_f[2,7]),
                'f45': str(matric_f[3,4]),
                'f46': str(matric_f[3,5]),
                'f47': str(matric_f[3,6]),
                'f48': str(matric_f[3,7]),

                'f49': str(matric_f[4,4]),
                'f50': str(matric_f[4,5]),
                'f51': str(matric_f[4,6]),
                'f52': str(matric_f[4,7]),
                'f53': str(matric_f[5,4]),
                'f54': str(matric_f[5,5]),
                'f55': str(matric_f[5,6]),
                'f56': str(matric_f[5,7]),
                'f57': str(matric_f[6,4]),
                'f58': str(matric_f[6,5]),
                'f59': str(matric_f[6,6]),
                'f60': str(matric_f[6,7]),
                'f61': str(matric_f[7,4]),
                'f62': str(matric_f[7,5]),
                'f63': str(matric_f[7,6]),
                'f64': str(matric_f[7,7])        }

            # Perform the replacements using regular expressions
            for pattern, replacement in replacements.items():
                content = re.sub(r'\b{}\b'.format(re.escape(pattern)), replacement, content)

            # Write the modified content back to the file
            document_name_out = f"./{group}/{group} {author}.tex"
            with open(document_name_out, 'w') as file:
                file.write(content)

            file_path = document_name
            if os.path.exists(file_path):
                os.remove(file_path)
            else:
                print("File not found.")


generate_and_save_documents()