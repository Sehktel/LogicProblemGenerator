# Logic Problem Generator
Создает индивидуальные задания для минимизации логической функций от 3 до 6 переменных.
Данные задаются случайным образом. 
В задании создаются 3 таблицы Карно для базового уровня.
2 таблици от 3х переменных. 
1 таблица от 4х переменных.
Повышенный уровень сложности включает в себя одну функцию от 5 переменных и одну функцию от 6 переменных.


## Запуск
Для запуска запустите последовательно два файла:
generator.py -- он создаст папки с группами, указанными в файле grouplist.txt
В файлах с префиксом группы указаны Фамилии и Имена студентов. 
Например grp1_namelist.txt
В созданных папках будут созданы шаблоны документов в формате .tex
Затем запускается файл parser.py который производит замену переменных и индивидуализацию документов.
Далее pdfTeX или иной механизм компиляции tex файла в pdf.
Готово.


## Пример
Пример работы скриптов лежит в папке grp1.