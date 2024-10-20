def DateChecker():
    DateReal = False
    MonthList31 = [1, 3, 5, 6, 7, 8, 10, 12]
    MonthList30 = (4, 6, 9, 11)

    while DateReal == False:
        date = int(input('Please enter a day '))
        month = int(input('Please enter a month '))
        year = int(input('Please enter a year '))


        if month in MonthList31:
            if date <= 31:
                print('This day exists')
                DateReal == True
                break
            else:
                print('The date is invalid, please choose again ')

        elif month in MonthList30:
            if date <= 30:
                print('This day exists')
                DateReal == True
                break
            else:
                print('The date is invalid, please choose again ')

        elif month == 2:

            if year % 4 == 0:

                if year % 100 == 0:

                    if year % 400 == 0:
                        if date <= 29:
                            print('This day exists')
                            DateReal == True
                            break
                        else:
                            print('The date is invalid, please choose again ')

                    else:
                        if date <= 28:
                            print('This day exists')
                            DateReal == True
                            break
                        else:
                            print('The date is invalid, please choose again ')

                else:
                    if date <= 29:
                            print('This day exists')
                            DateReal == True
                            break
                    else:
                        print('The date is invalid, please choose again ')
                       
            else:
                if date <= 28:
                    print('This day exists')
                    DateReal == True
                    break
                else:
                    print('The date is invalid, please choose again ')

        else:
            print('The date is invalid, please choose again ')

DateChecker()