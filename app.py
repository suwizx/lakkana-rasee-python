class Hora:
    def __init__(self):
        self.day = int(input('วันที่เกิด :'))
    

        self.month = int(input('เดือนเกิด(กรอกเป็นตัวเลข) :'))

 

        self.hour = int(input('ชั่วโมงที่เกิด :'))



        self.minute = int(input('นาทีที่เกิด :'))
        



        print ('----------\nคุณเกิดวันที่ {}/{} เวลา {}:{}น.'.format(self.day,self.month,self.hour,self.minute))

 

    def rasee (self):

        print('----------\nราศีของคุณ(แบบสากล) คือ ')
        
        if((( (self.day >= 22) and (self.day <= 31))and(self.month==12)) or (( (self.day >= 1) and (self.day <= 20))and(self.month==1))):
            print ('มังกร')
        
        if((( (self.day >= 22) and (self.day <= 31))and(self.month==1)) or (( (self.day >= 1) and (self.day <= 19))and(self.month==2))):
            print ('กุมภ์')

        if((( (self.day >= 20) and (self.day <= 31))and(self.month==2)) or (( (self.day >= 1) and (self.day <= 20))and(self.month==3))):
            print ('มีน')

        if((( (self.day >= 21) and (self.day <= 31))and(self.month==3)) or (( (self.day >= 1) and (self.day <= 20))and(self.month==4))):
            print ('เมษ')
        
        if((( (self.day >= 21) and (self.day <= 31))and(self.month==4)) or (( (self.day >= 1) and (self.day <= 20))and(self.month==5))):
            print ('พฤษก')
        
        if((( (self.day >= 21) and (self.day <= 31))and(self.month==5)) or (( (self.day >= 1) and (self.day <= 21))and(self.month==6))):
            print ('เมถุน')

        if((( (self.day >= 22) and (self.day <= 31))and(self.month==6)) or (( (self.day >= 1) and (self.day <= 23))and(self.month==7))):
            print ('กรกฎ')

        if((( (self.day >= 24) and (self.day <= 31))and(self.month==7)) or (( (self.day >= 1) and (self.day <= 23))and(self.month==8))):
            print ('สิงห์')

        if((( (self.day >= 24) and (self.day <= 31))and(self.month==8)) or (( (self.day >= 1) and (self.day <= 23))and(self.month==9))):
            print ('กันย์')

        if((( (self.day >= 24) and (self.day <= 31))and(self.month==9)) or (( (self.day >= 1) and (self.day <= 23))and(self.month==10))):
            print ('ตุลย์')

        if((( (self.day >= 24) and (self.day <= 31))and(self.month==10)) or (( (self.day >= 1) and (self.day <= 22))and(self.month==11))):
            print ('พิจิก')

        if((( (self.day >= 23) and (self.day <= 31))and(self.month==11)) or (( (self.day >= 1) and (self.day <= 21))and(self.month==12))):
            print ('ธนู')

    def lakkana (self):

        print('----------\nลัคนาของคุณคือ คือ ')

        if ((self.hour == 5)or(self.hour == 6)):
            if((( (self.day >= 15) and (self.day <= 31))and(self.month==1)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==2))):
                print ('มังกร')
            if((( (self.day >= 13) and (self.day <= 31))and(self.month==2)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==3))):
                print ('กุมภ์')
            if((( (self.day >= 14) and (self.day <= 31))and(self.month==3)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==4))):
                print ('มีน')
            if((( (self.day >= 13) and (self.day <= 31))and(self.month==4)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==5))):
                print ('เมษ')
            if((( (self.day >= 14) and (self.day <= 31))and(self.month==5)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==6))):
                print ('พฤษก')
            if((( (self.day >= 14) and (self.day <= 31))and(self.month==6)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==7))):
                print ('เมถุน')
            if((( (self.day >= 15) and (self.day <= 31))and(self.month==7)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==8))):
                print ('กรกฎ')
            if((( (self.day >= 17) and (self.day <= 31))and(self.month==8)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==9))):
                print ('สิงห์')
            if((( (self.day >= 17) and (self.day <= 31))and(self.month==9)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==10))):
                print ('กันย์')
            if((( (self.day >= 17) and (self.day <= 31))and(self.month==10)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==11))):
                print ('ตุลย์')
            if((( (self.day >= 16) and (self.day <= 31))and(self.month==11)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==12))):
                print ('พิจิก')
            if((( (self.day >= 16) and (self.day <= 31))and(self.month==12)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==1))):
                print ('ธนู')

        if ((self.hour == 7)or(self.hour == 8)):
            if((( (self.day >= 15) and (self.day <= 31))and(self.month==1)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==2))):
                print ('กุมภ์')
            if((( (self.day >= 13) and (self.day <= 31))and(self.month==2)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==3))):
                print ('มีน')
            if((( (self.day >= 14) and (self.day <= 31))and(self.month==3)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==4))):
                print ('เมษ')
            if((( (self.day >= 13) and (self.day <= 31))and(self.month==4)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==5))):
                print ('พฤษก')
            if((( (self.day >= 14) and (self.day <= 31))and(self.month==5)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==6))):
                print ('เมถุน')
            if((( (self.day >= 14) and (self.day <= 31))and(self.month==6)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==7))):
                print ('กรกฎ')
            if((( (self.day >= 15) and (self.day <= 31))and(self.month==7)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==8))):
                print ('สิงห์')
            if((( (self.day >= 17) and (self.day <= 31))and(self.month==8)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==9))):
                print ('กันย์')
            if((( (self.day >= 17) and (self.day <= 31))and(self.month==9)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==10))):
                print ('ตุลย์')
            if((( (self.day >= 17) and (self.day <= 31))and(self.month==10)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==11))):
                print ('พิจิก')
            if((( (self.day >= 16) and (self.day <= 31))and(self.month==11)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==12))):
                print ('ธนู')
            if((( (self.day >= 16) and (self.day <= 31))and(self.month==12)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==1))):
                print ('มังกร')
        
        if ((self.hour == 9)or(self.hour == 10)):
            if((( (self.day >= 15) and (self.day <= 31))and(self.month==1)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==2))):
                print ('มีน')
            if((( (self.day >= 13) and (self.day <= 31))and(self.month==2)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==3))):
                print ('เมษ')
            if((( (self.day >= 14) and (self.day <= 31))and(self.month==3)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==4))):
                print ('พฤษก')
            if((( (self.day >= 13) and (self.day <= 31))and(self.month==4)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==5))):
                print ('เมถุน')
            if((( (self.day >= 14) and (self.day <= 31))and(self.month==5)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==6))):
                print ('กรกฎ')
            if((( (self.day >= 14) and (self.day <= 31))and(self.month==6)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==7))):
                print ('สิงห์')
            if((( (self.day >= 15) and (self.day <= 31))and(self.month==7)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==8))):
                print ('กันย์')
            if((( (self.day >= 17) and (self.day <= 31))and(self.month==8)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==9))):
                print ('ตุลย์')
            if((( (self.day >= 17) and (self.day <= 31))and(self.month==9)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==10))):
                print ('พิจิก')
            if((( (self.day >= 17) and (self.day <= 31))and(self.month==10)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==11))):
                print ('ธนู')
            if((( (self.day >= 16) and (self.day <= 31))and(self.month==11)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==12))):
                print ('มังกร')
            if((( (self.day >= 16) and (self.day <= 31))and(self.month==12)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==1))):
                print ('กุมภ์')
        
        if ((self.hour == 11)or(self.hour == 12)):
            if((( (self.day >= 15) and (self.day <= 31))and(self.month==1)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==2))):
                print ('เมษ')
            if((( (self.day >= 13) and (self.day <= 31))and(self.month==2)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==3))):
                print ('พฤษก')
            if((( (self.day >= 14) and (self.day <= 31))and(self.month==3)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==4))):
                print ('เมถุน')
            if((( (self.day >= 13) and (self.day <= 31))and(self.month==4)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==5))):
                print ('กรกฎ')
            if((( (self.day >= 14) and (self.day <= 31))and(self.month==5)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==6))):
                print ('สิงห์')
            if((( (self.day >= 14) and (self.day <= 31))and(self.month==6)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==7))):
                print ('กันย์')
            if((( (self.day >= 15) and (self.day <= 31))and(self.month==7)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==8))):
                print ('ตุลย์')
            if((( (self.day >= 17) and (self.day <= 31))and(self.month==8)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==9))):
                print ('พิจิก')
            if((( (self.day >= 17) and (self.day <= 31))and(self.month==9)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==10))):
                print ('ธนู')
            if((( (self.day >= 17) and (self.day <= 31))and(self.month==10)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==11))):
                print ('มังกร')
            if((( (self.day >= 16) and (self.day <= 31))and(self.month==11)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==12))):
                print ('กุมภ์')
            if((( (self.day >= 16) and (self.day <= 31))and(self.month==12)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==1))):
                print ('มีน')

        if ((self.hour == 13)or(self.hour == 14)):
            if((( (self.day >= 15) and (self.day <= 31))and(self.month==1)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==2))):
                print ('พฤษก')
            if((( (self.day >= 13) and (self.day <= 31))and(self.month==2)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==3))):
                print ('เมถุน')
            if((( (self.day >= 14) and (self.day <= 31))and(self.month==3)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==4))):
                print ('กรกฎ')
            if((( (self.day >= 13) and (self.day <= 31))and(self.month==4)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==5))):
                print ('สิงห์')
            if((( (self.day >= 14) and (self.day <= 31))and(self.month==5)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==6))):
                print ('กันย์')
            if((( (self.day >= 14) and (self.day <= 31))and(self.month==6)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==7))):
                print ('ตุลย์')
            if((( (self.day >= 15) and (self.day <= 31))and(self.month==7)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==8))):
                print ('พิจิก')
            if((( (self.day >= 17) and (self.day <= 31))and(self.month==8)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==9))):
                print ('ธนู')
            if((( (self.day >= 17) and (self.day <= 31))and(self.month==9)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==10))):
                print ('มังกร')
            if((( (self.day >= 17) and (self.day <= 31))and(self.month==10)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==11))):
                print ('กุมภ์')
            if((( (self.day >= 16) and (self.day <= 31))and(self.month==11)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==12))):
                print ('มีน')
            if((( (self.day >= 16) and (self.day <= 31))and(self.month==12)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==1))):
                print ('เมษ')

        if ((self.hour == 15)or(self.hour == 16)):
            if((( (self.day >= 15) and (self.day <= 31))and(self.month==1)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==2))):
                print ('เมถุน')
            if((( (self.day >= 13) and (self.day <= 31))and(self.month==2)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==3))):
                print ('กรกฎ')
            if((( (self.day >= 14) and (self.day <= 31))and(self.month==3)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==4))):
                print ('สิงห์')
            if((( (self.day >= 13) and (self.day <= 31))and(self.month==4)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==5))):
                print ('กันย์')
            if((( (self.day >= 14) and (self.day <= 31))and(self.month==5)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==6))):
                print ('ตุลย์')
            if((( (self.day >= 14) and (self.day <= 31))and(self.month==6)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==7))):
                print ('พิจิก')
            if((( (self.day >= 15) and (self.day <= 31))and(self.month==7)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==8))):
                print ('ธนู')
            if((( (self.day >= 17) and (self.day <= 31))and(self.month==8)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==9))):
                print ('มังกร')
            if((( (self.day >= 17) and (self.day <= 31))and(self.month==9)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==10))):
                print ('กุมภ์')
            if((( (self.day >= 17) and (self.day <= 31))and(self.month==10)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==11))):
                print ('มีน')
            if((( (self.day >= 16) and (self.day <= 31))and(self.month==11)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==12))):
                print ('เมษ')
            if((( (self.day >= 16) and (self.day <= 31))and(self.month==12)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==1))):
                print ('พฤษก')

        if ((self.hour == 17)or(self.hour == 18)):
            if((( (self.day >= 15) and (self.day <= 31))and(self.month==1)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==2))):
                print ('กรกฎ')
            if((( (self.day >= 13) and (self.day <= 31))and(self.month==2)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==3))):
                print ('สิงห์')
            if((( (self.day >= 14) and (self.day <= 31))and(self.month==3)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==4))):
                print ('กันย์')
            if((( (self.day >= 13) and (self.day <= 31))and(self.month==4)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==5))):
                print ('ตุลย์')
            if((( (self.day >= 14) and (self.day <= 31))and(self.month==5)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==6))):
                print ('พิจิก')
            if((( (self.day >= 14) and (self.day <= 31))and(self.month==6)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==7))):
                print ('ธนู')
            if((( (self.day >= 15) and (self.day <= 31))and(self.month==7)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==8))):
                print ('มังกร')
            if((( (self.day >= 17) and (self.day <= 31))and(self.month==8)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==9))):
                print ('กุมภ์')
            if((( (self.day >= 17) and (self.day <= 31))and(self.month==9)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==10))):
                print ('มีน')
            if((( (self.day >= 17) and (self.day <= 31))and(self.month==10)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==11))):
                print ('เมษ')
            if((( (self.day >= 16) and (self.day <= 31))and(self.month==11)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==12))):
                print ('พฤษก')
            if((( (self.day >= 16) and (self.day <= 31))and(self.month==12)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==1))):
                print ('เมถุน')

        if ((self.hour == 19)or(self.hour == 20)):
            if((( (self.day >= 15) and (self.day <= 31))and(self.month==1)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==2))):
                print ('สิงห์')
            if((( (self.day >= 13) and (self.day <= 31))and(self.month==2)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==3))):
                print ('กันย์')
            if((( (self.day >= 14) and (self.day <= 31))and(self.month==3)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==4))):
                print ('ตุลย์')
            if((( (self.day >= 13) and (self.day <= 31))and(self.month==4)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==5))):
                print ('พิจิก')
            if((( (self.day >= 14) and (self.day <= 31))and(self.month==5)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==6))):
                print ('ธนู')
            if((( (self.day >= 14) and (self.day <= 31))and(self.month==6)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==7))):
                print ('มังกร')
            if((( (self.day >= 15) and (self.day <= 31))and(self.month==7)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==8))):
                print ('กุมภ์')
            if((( (self.day >= 17) and (self.day <= 31))and(self.month==8)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==9))):
                print ('มีน')
            if((( (self.day >= 17) and (self.day <= 31))and(self.month==9)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==10))):
                print ('เมษ')
            if((( (self.day >= 17) and (self.day <= 31))and(self.month==10)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==11))):
                print ('พฤษก')
            if((( (self.day >= 16) and (self.day <= 31))and(self.month==11)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==12))):
                print ('เมถุน')
            if((( (self.day >= 16) and (self.day <= 31))and(self.month==12)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==1))):
                print ('กรกฏ')

        if ((self.hour == 21)or(self.hour == 22)):
            if((( (self.day >= 15) and (self.day <= 31))and(self.month==1)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==2))):
                print ('กันย์')
            if((( (self.day >= 13) and (self.day <= 31))and(self.month==2)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==3))):
                print ('ตุลย์')
            if((( (self.day >= 14) and (self.day <= 31))and(self.month==3)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==4))):
                print ('พิจิก')
            if((( (self.day >= 13) and (self.day <= 31))and(self.month==4)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==5))):
                print ('ธนู')
            if((( (self.day >= 14) and (self.day <= 31))and(self.month==5)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==6))):
                print ('มังกร')
            if((( (self.day >= 14) and (self.day <= 31))and(self.month==6)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==7))):
                print ('กุมภ์')
            if((( (self.day >= 15) and (self.day <= 31))and(self.month==7)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==8))):
                print ('มีน')
            if((( (self.day >= 17) and (self.day <= 31))and(self.month==8)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==9))):
                print ('เมษ')
            if((( (self.day >= 17) and (self.day <= 31))and(self.month==9)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==10))):
                print ('พฤษก')
            if((( (self.day >= 17) and (self.day <= 31))and(self.month==10)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==11))):
                print ('เมถุน')
            if((( (self.day >= 16) and (self.day <= 31))and(self.month==11)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==12))):
                print ('กรกฏ')
            if((( (self.day >= 16) and (self.day <= 31))and(self.month==12)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==1))):
                print ('สิงห์')

        if ((self.hour == 23)or(self.hour == 0)or(self.hour == 24)):
            if((( (self.day >= 15) and (self.day <= 31))and(self.month==1)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==2))):
                print ('ตุลย์')
            if((( (self.day >= 13) and (self.day <= 31))and(self.month==2)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==3))):
                print ('พิจิก')
            if((( (self.day >= 14) and (self.day <= 31))and(self.month==3)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==4))):
                print ('ธนู')
            if((( (self.day >= 13) and (self.day <= 31))and(self.month==4)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==5))):
                print ('มังกร')
            if((( (self.day >= 14) and (self.day <= 31))and(self.month==5)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==6))):
                print ('กุมภ์')
            if((( (self.day >= 14) and (self.day <= 31))and(self.month==6)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==7))):
                print ('มีน')
            if((( (self.day >= 15) and (self.day <= 31))and(self.month==7)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==8))):
                print ('เมษ')
            if((( (self.day >= 17) and (self.day <= 31))and(self.month==8)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==9))):
                print ('พฤษก')
            if((( (self.day >= 17) and (self.day <= 31))and(self.month==9)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==10))):
                print ('เมถุน')
            if((( (self.day >= 17) and (self.day <= 31))and(self.month==10)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==11))):
                print ('กรกฏ')
            if((( (self.day >= 16) and (self.day <= 31))and(self.month==11)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==12))):
                print ('สิงห์')
            if((( (self.day >= 16) and (self.day <= 31))and(self.month==12)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==1))):
                print ('กันย์')

        if ((self.hour == 1)or(self.hour == 2)):
            if((( (self.day >= 15) and (self.day <= 31))and(self.month==1)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==2))):
                print ('พิจิก')
            if((( (self.day >= 13) and (self.day <= 31))and(self.month==2)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==3))):
                print ('ธนู')
            if((( (self.day >= 14) and (self.day <= 31))and(self.month==3)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==4))):
                print ('มังกร')
            if((( (self.day >= 13) and (self.day <= 31))and(self.month==4)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==5))):
                print ('กุมภ์')
            if((( (self.day >= 14) and (self.day <= 31))and(self.month==5)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==6))):
                print ('มีน')
            if((( (self.day >= 14) and (self.day <= 31))and(self.month==6)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==7))):
                print ('เมษ')
            if((( (self.day >= 15) and (self.day <= 31))and(self.month==7)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==8))):
                print ('พฤษก')
            if((( (self.day >= 17) and (self.day <= 31))and(self.month==8)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==9))):
                print ('เมถุน')
            if((( (self.day >= 17) and (self.day <= 31))and(self.month==9)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==10))):
                print ('กรกฏ')
            if((( (self.day >= 17) and (self.day <= 31))and(self.month==10)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==11))):
                print ('สิงห์')
            if((( (self.day >= 16) and (self.day <= 31))and(self.month==11)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==12))):
                print ('กันย์')
            if((( (self.day >= 16) and (self.day <= 31))and(self.month==12)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==1))):
                print ('ตุลย์')

        if ((self.hour == 3)or(self.hour == 4)):
            if((( (self.day >= 15) and (self.day <= 31))and(self.month==1)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==2))):
                print ('ธนู')
            if((( (self.day >= 13) and (self.day <= 31))and(self.month==2)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==3))):
                print ('มังกร')
            if((( (self.day >= 14) and (self.day <= 31))and(self.month==3)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==4))):
                print ('กุมภ์')
            if((( (self.day >= 13) and (self.day <= 31))and(self.month==4)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==5))):
                print ('มีน')
            if((( (self.day >= 14) and (self.day <= 31))and(self.month==5)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==6))):
                print ('เมษ')
            if((( (self.day >= 14) and (self.day <= 31))and(self.month==6)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==7))):
                print ('พฤษก')
            if((( (self.day >= 15) and (self.day <= 31))and(self.month==7)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==8))):
                print ('เมถุน')
            if((( (self.day >= 17) and (self.day <= 31))and(self.month==8)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==9))):
                print ('กรกฏ')
            if((( (self.day >= 17) and (self.day <= 31))and(self.month==9)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==10))):
                print ('สิงห์')
            if((( (self.day >= 17) and (self.day <= 31))and(self.month==10)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==11))):
                print ('กันย์')
            if((( (self.day >= 16) and (self.day <= 31))and(self.month==11)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==12))):
                print ('ตุลย์')
            if((( (self.day >= 16) and (self.day <= 31))and(self.month==12)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==1))):
                print ('พิจิก')


duHora = Hora()
duHora.rasee()
duHora.lakkana()