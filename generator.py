#-------------------------------------------------------------------------------
# Name:        Logic Problem Generator
# Purpose:
#
# Author:      Sehktel
#
# Created:     18.01.2024
# Copyright:   (c) Sehktel 2024
# Licence:     MIT
#-------------------------------------------------------------------------------

import numpy as np
import os

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

    for folder in group_names:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Created folder: {folder}")
        else:
            print(f"Folder already exists: {folder}")

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

            # Write the LaTeX document with styled tables and author
            with open(document_name, "w") as file:
                file.write(
f"""\\documentclass[12pt,a4paper,final,notitlepage]{{article}}
\\usepackage[utf8]{{inputenc}}
\\usepackage[english, russian]{{babel}}
\\usepackage{{amsmath}}
\\usepackage[T2A]{{fontenc}}
\\usepackage{{amsfonts}}
\\usepackage{{amssymb}}
\\usepackage{{graphicx}}
\\usepackage[left=2cm,right=2cm,top=2cm,bottom=2cm]{{geometry}}
\\author{{autor}}
\\title{{Logic Tables}}
\\usepackage{{tablefootnote}}
\\usepackage[symbol*]{{footmisc}}
\\usepackage{{indentfirst}}
\\setlength\\parindent{{1.5em}}
\\begin{{document}}

  \\centering
  \\LARGE Упрощение логических функций \\\\[1.5em]
  \\large author_name \\\\[1em]
  \\normalsize

Произвести упрощение следующих функций, заданных картой Карно.

\\begin{{table}}[htbp]
\\begin{{minipage}}{{\\textwidth}}
\\centering
\\setlength{{\\tabcolsep}}{{10pt}}
\\begin{{tabular}}{{cccccccccccc}}
\\multicolumn{{12}}{{c}}{{Базовое задание. Получить СДНФ, СКНФ, ДНФ, КНФ}} \\\\
 &
   &
   &
   &
   &
   &
   &
   &
   &
   &
   &
   \\\\ \\cline{{1-4}} \\cline{{6-7}} \\cline{{9-12}}
\\multicolumn{{1}}{{|c|}}{{a1}} &
  \\multicolumn{{1}}{{c|}}{{a2}} &
  \\multicolumn{{1}}{{c|}}{{a3}} &
  \\multicolumn{{1}}{{c|}}{{a4}} &
  \\multicolumn{{1}}{{c|}}{{}} &
  \\multicolumn{{1}}{{c|}}{{b1}} &
  \\multicolumn{{1}}{{c|}}{{b2}} &
  \\multicolumn{{1}}{{c|}}{{}} &
  \\multicolumn{{1}}{{c|}}{{c01}} &
  \\multicolumn{{1}}{{c|}}{{c02}} &
  \\multicolumn{{1}}{{c|}}{{c03}} &
  \\multicolumn{{1}}{{c|}}{{c04}} \\\\ \\cline{{1-4}} \\cline{{6-7}} \\cline{{9-12}}
\\multicolumn{{1}}{{|c|}}{{a5}} &
  \\multicolumn{{1}}{{c|}}{{a6}} &
  \\multicolumn{{1}}{{c|}}{{a7}} &
  \\multicolumn{{1}}{{c|}}{{a8}} &
  \\multicolumn{{1}}{{c|}}{{}} &
  \\multicolumn{{1}}{{c|}}{{b3}} &
  \\multicolumn{{1}}{{c|}}{{b4}} &
  \\multicolumn{{1}}{{c|}}{{}} &
  \\multicolumn{{1}}{{c|}}{{c05}} &
  \\multicolumn{{1}}{{c|}}{{c06}} &
  \\multicolumn{{1}}{{c|}}{{c07}} &
  \\multicolumn{{1}}{{c|}}{{c08}} \\\\ \\cline{{1-4}} \\cline{{6-7}} \\cline{{9-12}}
 &
   &
   &
   &
  \\multicolumn{{1}}{{c|}}{{}} &
  \\multicolumn{{1}}{{c|}}{{b5}} &
  \\multicolumn{{1}}{{c|}}{{b6}} &
  \\multicolumn{{1}}{{c|}}{{}} &
  \\multicolumn{{1}}{{c|}}{{c09}} &
  \\multicolumn{{1}}{{c|}}{{c10}} &
  \\multicolumn{{1}}{{c|}}{{c11}} &
  \\multicolumn{{1}}{{c|}}{{c12}} \\\\ \\cline{{6-7}} \\cline{{9-12}}
 &
   &
   &
   &
  \\multicolumn{{1}}{{c|}}{{}} &
  \\multicolumn{{1}}{{c|}}{{b7}} &
  \\multicolumn{{1}}{{c|}}{{b8}} &
  \\multicolumn{{1}}{{c|}}{{}} &
  \\multicolumn{{1}}{{c|}}{{c13}} &
  \\multicolumn{{1}}{{c|}}{{c14}} &
  \\multicolumn{{1}}{{c|}}{{c15}} &
  \\multicolumn{{1}}{{c|}}{{c16}} \\\\ \\cline{{6-7}} \\cline{{9-12}}
 &
   &
   &
   &
   &
   &
   &
   &
   &
   &
   &
   \\\\
\\multicolumn{{12}}{{c}}{{\\begin{{tabular}}[c]{{@{{}}c@{{}}}}Задание повышенной сложности. \\footnotetext{{* +1/4 баллов}}{{*}}\\\\ Функция от 5 переменных f(A, B, C, D, E)\\end{{tabular}}}} \\\\
 &
   &
   &
   &
   &
   &
   &
   &
   &
   &
   &
   \\\\ \\cline{{3-10}}
 &
  \\multicolumn{{1}}{{c|}}{{}} &
  \\multicolumn{{1}}{{c|}}{{d01}} &
  \\multicolumn{{1}}{{c|}}{{d02}} &
  \\multicolumn{{1}}{{c|}}{{d03}} &
  \\multicolumn{{1}}{{c|}}{{d04}} &
  \\multicolumn{{1}}{{c|}}{{d05}} &
  \\multicolumn{{1}}{{c|}}{{d06}} &
  \\multicolumn{{1}}{{c|}}{{d07}} &
  \\multicolumn{{1}}{{c|}}{{d08}} &
   &
   \\\\ \\cline{{3-10}}
 &
  \\multicolumn{{1}}{{c|}}{{}} &
  \\multicolumn{{1}}{{c|}}{{d09}} &
  \\multicolumn{{1}}{{c|}}{{d10}} &
  \\multicolumn{{1}}{{c|}}{{d11}} &
  \\multicolumn{{1}}{{c|}}{{d12}} &
  \\multicolumn{{1}}{{c|}}{{d13}} &
  \\multicolumn{{1}}{{c|}}{{d14}} &
  \\multicolumn{{1}}{{c|}}{{d15}} &
  \\multicolumn{{1}}{{c|}}{{d16}} &
   &
   \\\\ \\cline{{3-10}}
 &
  \\multicolumn{{1}}{{c|}}{{}} &
  \\multicolumn{{1}}{{c|}}{{d17}} &
  \\multicolumn{{1}}{{c|}}{{d18}} &
  \\multicolumn{{1}}{{c|}}{{d19}} &
  \\multicolumn{{1}}{{c|}}{{d20}} &
  \\multicolumn{{1}}{{c|}}{{d21}} &
  \\multicolumn{{1}}{{c|}}{{d22}} &
  \\multicolumn{{1}}{{c|}}{{d23}} &
  \\multicolumn{{1}}{{c|}}{{d24}} &
   &
   \\\\ \\cline{{3-10}}
 &
  \\multicolumn{{1}}{{c|}}{{}} &
  \\multicolumn{{1}}{{c|}}{{d25}} &
  \\multicolumn{{1}}{{c|}}{{d26}} &
  \\multicolumn{{1}}{{c|}}{{d27}} &
  \\multicolumn{{1}}{{c|}}{{d28}} &
  \\multicolumn{{1}}{{c|}}{{d29}} &
  \\multicolumn{{1}}{{c|}}{{d30}} &
  \\multicolumn{{1}}{{c|}}{{d31}} &
  \\multicolumn{{1}}{{c|}}{{d32}} &
   &
   \\\\ \\cline{{3-10}}
 &
   &
   &
   &
   &
   &
   &
   &
   &
   &
   &
   \\\\
\\multicolumn{{12}}{{c}}{{\\begin{{tabular}}[c]{{@{{}}c@{{}}}}Задание повышенной сложности.  \\footnotetext{{** Удвоение баллов}}{{**}} \\\\ Функция от 6 переменных f (A, B, C, D, E, G)\\end{{tabular}}}} \\\\
 &
   &
   &
   &
   &
   &
   &
   &
   &
   &
   &
   \\\\ \\cline{{3-10}}
 &
  \\multicolumn{{1}}{{c|}}{{}} &
  \\multicolumn{{1}}{{c|}}{{f01}} &
  \\multicolumn{{1}}{{c|}}{{f02}} &
  \\multicolumn{{1}}{{c|}}{{f03}} &
  \\multicolumn{{1}}{{c|}}{{f04}} &
  \\multicolumn{{1}}{{c|}}{{f05}} &
  \\multicolumn{{1}}{{c|}}{{f06}} &
  \\multicolumn{{1}}{{c|}}{{f07}} &
  \\multicolumn{{1}}{{c|}}{{f08}} &
   &
   \\\\ \\cline{{3-10}}
 &
  \\multicolumn{{1}}{{c|}}{{}} &
  \\multicolumn{{1}}{{c|}}{{f09}} &
  \\multicolumn{{1}}{{c|}}{{f10}} &
  \\multicolumn{{1}}{{c|}}{{f11}} &
  \\multicolumn{{1}}{{c|}}{{f12}} &
  \\multicolumn{{1}}{{c|}}{{f13}} &
  \\multicolumn{{1}}{{c|}}{{f14}} &
  \\multicolumn{{1}}{{c|}}{{f15}} &
  \\multicolumn{{1}}{{c|}}{{f16}} &
   &
   \\\\ \\cline{{3-10}}
 &
  \\multicolumn{{1}}{{c|}}{{}} &
  \\multicolumn{{1}}{{c|}}{{f17}} &
  \\multicolumn{{1}}{{c|}}{{f18}} &
  \\multicolumn{{1}}{{c|}}{{f19}} &
  \\multicolumn{{1}}{{c|}}{{f20}} &
  \\multicolumn{{1}}{{c|}}{{f21}} &
  \\multicolumn{{1}}{{c|}}{{f22}} &
  \\multicolumn{{1}}{{c|}}{{f23}} &
  \\multicolumn{{1}}{{c|}}{{f24}} &
   &
   \\\\ \\cline{{3-10}}
 &
  \\multicolumn{{1}}{{c|}}{{}} &
  \\multicolumn{{1}}{{c|}}{{f25}} &
  \\multicolumn{{1}}{{c|}}{{f26}} &
  \\multicolumn{{1}}{{c|}}{{f27}} &
  \\multicolumn{{1}}{{c|}}{{f28}} &
  \\multicolumn{{1}}{{c|}}{{f29}} &
  \\multicolumn{{1}}{{c|}}{{f30}} &
  \\multicolumn{{1}}{{c|}}{{f31}} &
  \\multicolumn{{1}}{{c|}}{{f32}} &
   &
   \\\\ \\cline{{3-10}}
 &
  \\multicolumn{{1}}{{c|}}{{}} &
  \\multicolumn{{1}}{{c|}}{{f33}} &
  \\multicolumn{{1}}{{c|}}{{f34}} &
  \\multicolumn{{1}}{{c|}}{{f35}} &
  \\multicolumn{{1}}{{c|}}{{f36}} &
  \\multicolumn{{1}}{{c|}}{{f37}} &
  \\multicolumn{{1}}{{c|}}{{f38}} &
  \\multicolumn{{1}}{{c|}}{{f39}} &
  \\multicolumn{{1}}{{c|}}{{f40}} &
   &
   \\\\ \\cline{{3-10}}
 &
  \\multicolumn{{1}}{{c|}}{{}} &
  \\multicolumn{{1}}{{c|}}{{f41}} &
  \\multicolumn{{1}}{{c|}}{{f42}} &
  \\multicolumn{{1}}{{c|}}{{f43}} &
  \\multicolumn{{1}}{{c|}}{{f44}} &
  \\multicolumn{{1}}{{c|}}{{f45}} &
  \\multicolumn{{1}}{{c|}}{{f46}} &
  \\multicolumn{{1}}{{c|}}{{f47}} &
  \\multicolumn{{1}}{{c|}}{{f48}} &
   &
   \\\\ \\cline{{3-10}}
 &
  \\multicolumn{{1}}{{c|}}{{}} &
  \\multicolumn{{1}}{{c|}}{{f49}} &
  \\multicolumn{{1}}{{c|}}{{f50}} &
  \\multicolumn{{1}}{{c|}}{{f51}} &
  \\multicolumn{{1}}{{c|}}{{f52}} &
  \\multicolumn{{1}}{{c|}}{{f53}} &
  \\multicolumn{{1}}{{c|}}{{f54}} &
  \\multicolumn{{1}}{{c|}}{{f55}} &
  \\multicolumn{{1}}{{c|}}{{f56}} &
   &
   \\\\ \\cline{{3-10}}
 &
  \\multicolumn{{1}}{{c|}}{{}} &
  \\multicolumn{{1}}{{c|}}{{f57}} &
  \\multicolumn{{1}}{{c|}}{{f58}} &
  \\multicolumn{{1}}{{c|}}{{f59}} &
  \\multicolumn{{1}}{{c|}}{{f60}} &
  \\multicolumn{{1}}{{c|}}{{f61}} &
  \\multicolumn{{1}}{{c|}}{{f62}} &
  \\multicolumn{{1}}{{c|}}{{f63}} &
  \\multicolumn{{1}}{{c|}}{{f64}} &
   &
   \\\\ \\cline{{3-10}}
\\end{{tabular}}
\\end{{minipage}}
\\end{{table}}

\\textbf{{Защита работы:}} \\\\
\\begin{{flushleft}}
\\hspace*{{15pt}} Предоставить черновик рассуждений, из которого будет видно, как вы рассуждали при решениии задачи (этапы сокращения функций и тд). Привести таблицу истинности, которая получилась на основе карт Карно. Обратите внимание, что в них не указан порядок входных сигналов. Т.е. например для функции \\textit{{f(ABC)}} необъязательно, что \\textbf{{А}} всегда слева, а \\textbf{{BC}} сверху. Это вы должны указать самостоятельно, особенно для заданий повышенной сложности.
\\end{{flushleft}}

\\end{{document}}

"""
            )



generate_and_save_documents()

