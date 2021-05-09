#   dlens_cockatrice_converter ver. 2
#
#   converts delver lens card lists exported via .csv into 
#   cockatrice-importable .cod files
#
#   Copyright (C) 2021 Michael Warz
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#   contact me via email: warzmic(at)outlook.com
#
#   (please do not contact me unless there is a serious issue.)
#
#
#   how to: export delver lens cardlist to a .csv file with standard
#   configuration (tabulator seperated, first row number of cards, second
#   row card name), then put it in the same folder as the converter, run 
#   converter with python 3.x, then import the created .cod into cockatrice.
#


import os, csv, msvcrt

print('searching for .csv files ...')

filenames = os.listdir('.')

csvnames = list(())
codnames = list(())

counter = 0
while counter < len(filenames) :
    if filenames[counter].endswith('.csv') == True :
        csvnames.append(filenames[counter])
    counter = counter + 1

counter = 0
while counter < len(csvnames) :
    csvnames[counter] = csvnames[counter][:-4]
    counter = counter + 1

filecounter = 0

while filecounter < len(csvnames) :
    print(f'{csvnames[filecounter]}.csv detected ...')

    if f'{csvnames[filecounter]}.cod' not in filenames :     
        print('and no matching .cod file ...')

        csvlist = list(csv.reader(open(f'{csvnames[filecounter]}.csv', 'r', encoding = 'utf-8'), delimiter='\t'))
        codfile = open(f'{csvnames[filecounter]}.cod', 'w', encoding = 'utf-8')     

        codfile.write(f'<?xml version=\"1.0\" encoding=\"UTF-8\"?>')
        codfile.write(f'\n<cockatrice_deck version=\"1\">')
        codfile.write(f'\n\t<deckname>{csvnames[filecounter]}</deckname>')
        codfile.write(f'\n\t<comments></comments>')
        codfile.write(f'\n\t<zone name=\"main\">')

        try :
            counter = 1
            while counter < len(csvlist) :
                codfile.write(f'\n\t\t<card number=\"{csvlist[counter][0][:-1]}\" name=\"')
                codfile.write(fr'{csvlist[counter][1]}')
                codfile.write(f'\"/>')
                counter = counter + 1

            codfile.write(f'\n\t</zone>')
            codfile.write(f'\n</cockatrice_deck>')

            print(f'{csvnames[filecounter]}.cod created successfully! now you can import it to cockatrice!')
            filecounter = filecounter + 1

        except :
            print(f'something went wrong with {csvnames[filecounter]}.csv! use delver lens .csv export files with tab seperator!')
            filecounter = filecounter + 1

    else :
        print(f'matching .cod file detected! converter does not overwrite files! rename or delete {csvnames[filecounter]}.cod manually and try again!')
        filecounter = filecounter + 1
    
keyboardinput = msvcrt.getwch()
