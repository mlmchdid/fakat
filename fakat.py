def fakat(TheNo, MyCur, MySubCur):

    Mybillion = ''

    MyMillion = ''

    MyThou = ''

    MyHun = ''

    MyFraction = ''

    if TheNo > 999999999999.99:
        return fn_return_value
    if TheNo < 0:
        TheNo = TheNo * (- 1)
        ReMark = 'يتبقى لكم '
    else:
        ReMark = 'فقط '
    if TheNo == 0:
        fn_return_value = 'صفر'
        return fn_return_value
    MyAnd = ' و'
    MyArry1 = ['', 'مائة', 'مائتان', 'ثلاثمائة', 'أربعمائة', 'خمسمائة', 'ستمائة', 'سبعمائة', 'ثمانمائة', 'تسعمائة']
    MyArry2 = ['', ' عشر', 'عشرون', 'ثلاثون', 'أربعون', 'خمسون', 'ستون', 'سبعون', 'ثمانون', 'تسعون']
    MyArry3 = ['', 'واحد', 'اثنان', 'ثلاثة', 'أربعة', 'خمسة', 'ستة', 'سبعة', 'ثمانية', 'تسعة']
    #======================
    GetNo = "%016.2f" %TheNo
    I = 0
    while I < 15:
        if I < 12:
            Myno = GetNo[I+1:I + 4]
        else:
            Myno = '0' + GetNo[I + 2:I + 4]
        if int(Myno[0:3]) > 0:
            RdNo = int(Myno[0])
            My100 = MyArry1[RdNo]
            RdNo = int(Myno[2])
            My1 = MyArry3[RdNo]
            RdNo = int(Myno[1])
            My10 = MyArry2[RdNo]
            if int(Myno[1:3]) == 11:
                My11 = 'إحدى عشر'
            if int(Myno[1:3]) == 12:
                My12 = 'إثنى عشر'
            if int(Myno[1:3]) == 10:
                My10 = 'عشرة'
            if ( ( int(Myno[0]) )  > 0 )  and  ( ( int(Myno[1:3]) )  > 0 ) :
                My100 = My100 + MyAnd
            if ( ( int(Myno[2]) )  > 0 )  and  ( ( int(Myno[1]) )  > 1 ) :
                My1 = My1 + MyAnd
            GetTxt = My100 + My1 + My10
            if ( ( int(Myno[2]) )  == 1 )  and  ( ( int(Myno[1]) )  == 1 ) :
                GetTxt = My100 + My11
                if ( ( int(Myno[0]) )  == 0 ) :
                    GetTxt = My11
            if ( ( int(Myno[2]) )  == 2 )  and  ( ( int(Myno[1]) )  == 1 ) :
                GetTxt = My100 + My12
                if ( ( int(Myno[0]) )  == 0 ) :
                    GetTxt = My12
            if ( I == 0 )  and  ( GetTxt != '' ) :
                if ( ( int(Myno[0:3] ))  > 10 ) :
                    Mybillion = GetTxt + ' مليار'
                else:
                    Mybillion = GetTxt + ' مليارات'
                    if ( ( int(Myno[0:3]) )  == 1 ) :
                        Mybillion = ' مليار'
                    if ( ( int(Myno[0:3]) )  == 2 ) :
                        Mybillion = ' ملياران'
            if ( I == 3 )  and  ( GetTxt != '' ) :
                if ( ( int(Myno[0:3]) )  > 10 ) :
                    MyMillion = GetTxt + ' مليون'
                else:
                    MyMillion = GetTxt + ' ملايين'
                    if ( ( int(Myno[0:3]) )  == 1 ) :
                        MyMillion = ' مليون'
                    if ( ( int(Myno[0:3]) )  == 2 ) :
                        MyMillion = ' مليونان'
            if ( I == 6 )  and  ( GetTxt != '' ) :
                if ( ( int(Myno[0:3]) )  > 10 ) :
                    MyThou = GetTxt + ' ألف'
                else:
                    MyThou = GetTxt + ' آلاف'
                    if ( ( int(Myno[2]) )  == 1 ) :
                        MyThou = ' ألف'
                    if ( ( int(Myno[2]) )  == 2 ) :
                        MyThou = ' ألفان'
            if ( I == 9 )  and  ( GetTxt != '' ) :
                MyHun = GetTxt
            if ( I == 12 )  and  ( GetTxt != '' ) :
                MyFraction = GetTxt
        I = I + 3
    if ( Mybillion != '' ) :
        if ( MyMillion != '' )  or  ( MyThou != '' )  or  ( MyHun != '' ) :
            Mybillion = Mybillion + MyAnd
    if ( MyMillion != '' ) :
        if ( MyThou != '' )  or  ( MyHun != '' ) :
            MyMillion = MyMillion + MyAnd
    if ( MyThou != '' ) :
        if ( MyHun != '' ) :
            MyThou = MyThou + MyAnd
    if MyFraction != '':
        if ( Mybillion != '' )  or  ( MyMillion != '' )  or  ( MyThou != '' )  or  ( MyHun != '' ) :
            fn_return_value = ReMark + Mybillion + MyMillion + MyThou + MyHun + ' ' + MyCur + MyAnd + MyFraction + ' ' + MySubCur
        else:
            fn_return_value = ReMark + MyFraction + ' ' + MySubCur
    else:
        fn_return_value = ReMark + Mybillion + MyMillion + MyThou + MyHun + ' ' + MyCur
    return fn_return_value
