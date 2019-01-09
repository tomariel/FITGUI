def Make_Data_Readable(filename):
    #THIS PART OPENS THE FILE AND ASSIGNS IT TO A GROUP
    File_Data = open(filename,'r')
    Measurement_Data = File_Data.readlines()
    Measurement_Data_Lines = []
    for i in Measurement_Data:
        line = i
        line.split(' ')
        Measurement_Data_Lines.append(line)
        #print(line)
        #print(Measurement_Data_Lines)
        #THIS PART ASSIGNS EACH LINE IN THE DATA TO A GROUP
    for i in Measurement_Data_Lines:
        Measurement_Data_Lines[Measurement_Data_Lines.index(i)] = i.strip('\n')
        #print(Measurement_Data_Lines)
        #THIS PART REMOVES THE \n FROM THE LAST LINE
    Splitted_Measurement_Data_Lines=[]
    for i in Measurement_Data_Lines:
        Splitted_Measurement_Data_Lines.append(i.split(' '))
    #THIS PART SPLITS THE DATA INTO ROWS AND COLLUMNS SO WE CAN MANIPULATE IT EASILY
    #'splitted measruemtn....' is the data in rows and collumns
    X_Values_List = []
    Y_Values_List = []
    DX_Values_List =[]
    DY_Values_List = []
    for i in Splitted_Measurement_Data_Lines:
        while i.count('') > 0:
            for j in i:
                if j == '':
                    i.remove(j)
        if i == [] or i == ['']:
            Splitted_Measurement_Data_Lines.remove(i)
    #This part removes any empty objects in the data
    for i in Splitted_Measurement_Data_Lines[0]:
        if i.lower() == 'x':
            x_column_value = Splitted_Measurement_Data_Lines[0].index(i)
            for i in range(1,len(Splitted_Measurement_Data_Lines)-2):
                 X_Values_List.append(float(Splitted_Measurement_Data_Lines[i][x_column_value]))
        elif i.lower() == 'y':
            y_column_value = Splitted_Measurement_Data_Lines[0].index(i)
            for i in range(1,len(Splitted_Measurement_Data_Lines)-2):
                 Y_Values_List.append(float(Splitted_Measurement_Data_Lines[i][y_column_value]))
        elif i.lower() == 'dx':
            dx_column_value = Splitted_Measurement_Data_Lines[0].index(i)
            for i in range(1,len(Splitted_Measurement_Data_Lines)-2):
                 DX_Values_List.append(float(Splitted_Measurement_Data_Lines[i][dx_column_value]))
        elif i.lower() == 'dy':
            dy_column_value = Splitted_Measurement_Data_Lines[0].index(i)
            for i in range(1,len(Splitted_Measurement_Data_Lines)-2):
                 DY_Values_List.append(float(Splitted_Measurement_Data_Lines[i][dy_column_value]))
    #This part assigns x,y,dx and dy values to seperate groups
    data_length_indicator = 1
    for i in Splitted_Measurement_Data_Lines:
        if len(i) != 4:
            data_length_indicator = 0
    data_dictionary = {}
    data_dictionary.update({'x values': X_Values_List})
    data_dictionary.update({'y values': Y_Values_List})
    data_dictionary.update({'dx values': DX_Values_List})
    data_dictionary.update({'dy values': DY_Values_List})
    if data_length_indicator == 0:
        return('FileLengthError')
    else:
        m=0
        for i in DY_Values_List:
            if i == 0:
                m=1
                break
        for i in DX_Values_List:
            if i== 0:
                m = 1
                break
        if m == 1:
            return('UncertaintyError')
        else:
            return(data_dictionary)
print(Make_Data_Readable('input.txt'))