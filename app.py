class Hora:
    def __init__(self):
        self.day = int(input('วันที่เกิด : '))
        while ((self.day > 31) or (self.day < 1)):
            print('คุณกรอกวันเกิดไม่ถูกต้อง กรุณากรอกใหม่โดยเลข 1-31')
            self.day = int(input('วันที่เกิด : '))

        self.month = int(input('เดือนเกิด(กรอกเป็นตัวเลข) : '))
        while ((self.month > 12) or (self.month < 1)):
            print('คุณกรอกเดือนเกิดไม่ถูกต้อง กรุณากรอกใหม่โดยเลข 1-12')
            self.month = int(input('เดือนเกิด(กรอกเป็นตัวเลข) : '))
 
        self.hour = int(input('ชั่วโมงที่เกิด : '))
        while ((self.hour > 24) or (self.hour < 0)):
            print('คุณกรอกชั่วโมงเกิดไม่ถูกต้อง กรุณากรอกใหม่โดยเลข 0-24')
            self.hour = int(input('ชั่วโมงที่เกิด : '))

        self.minute = int(input('นาทีที่เกิด : '))
        while ((self.minute > 60) or (self.minute < 0)):
            print('คุณกรอกนาทีเกิดไม่ถูกต้อง กรุณากรอกใหม่โดยเลข 0-60')
            self.minute = int(input('นาทีที่เกิด : '))

        print ('----------\nคุณเกิดวันที่ {}/{} เวลา {}:{}น.'.format(self.day,self.month,self.hour,self.minute))

    def rasee (self):

        print('----------\nราศีของคุณ(แบบสากล) คือ ')
        
        if((( (self.day >= 22) and (self.day <= 31))and(self.month==12)) or (( (self.day >= 1) and (self.day <= 20))and(self.month==1))):
            print ('มังกร')
        
        elif((( (self.day >= 22) and (self.day <= 31))and(self.month==1)) or (( (self.day >= 1) and (self.day <= 19))and(self.month==2))):
            print ('กุมภ์')

        elif((( (self.day >= 20) and (self.day <= 31))and(self.month==2)) or (( (self.day >= 1) and (self.day <= 20))and(self.month==3))):
            print ('มีน')

        elif((( (self.day >= 21) and (self.day <= 31))and(self.month==3)) or (( (self.day >= 1) and (self.day <= 20))and(self.month==4))):
            print ('เมษ')
        
        elif((( (self.day >= 21) and (self.day <= 31))and(self.month==4)) or (( (self.day >= 1) and (self.day <= 20))and(self.month==5))):
            print ('พฤษก')
        
        elif((( (self.day >= 21) and (self.day <= 31))and(self.month==5)) or (( (self.day >= 1) and (self.day <= 21))and(self.month==6))):
            print ('เมถุน')

        elif((( (self.day >= 22) and (self.day <= 31))and(self.month==6)) or (( (self.day >= 1) and (self.day <= 23))and(self.month==7))):
            print ('กรกฎ')

        elif((( (self.day >= 24) and (self.day <= 31))and(self.month==7)) or (( (self.day >= 1) and (self.day <= 23))and(self.month==8))):
            print ('สิงห์')

        elif((( (self.day >= 24) and (self.day <= 31))and(self.month==8)) or (( (self.day >= 1) and (self.day <= 23))and(self.month==9))):
            print ('กันย์')

        elif((( (self.day >= 24) and (self.day <= 31))and(self.month==9)) or (( (self.day >= 1) and (self.day <= 23))and(self.month==10))):
            print ('ตุลย์')

        elif((( (self.day >= 24) and (self.day <= 31))and(self.month==10)) or (( (self.day >= 1) and (self.day <= 22))and(self.month==11))):
            print ('พิจิก')

        elif((( (self.day >= 23) and (self.day <= 31))and(self.month==11)) or (( (self.day >= 1) and (self.day <= 21))and(self.month==12))):
            print ('ธนู')

        else:
            print ('ไม่พบข้อมูล')

    def lakkana (self):

        print('----------\nลัคนาของคุณคือ คือ ')

        if ((self.hour == 5)or(self.hour == 6)):
            if((( (self.day >= 15) and (self.day <= 31))and(self.month==1)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==2))):
                print ('มังกร')
            elif((( (self.day >= 13) and (self.day <= 31))and(self.month==2)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==3))):
                print ('กุมภ์')
            elif((( (self.day >= 14) and (self.day <= 31))and(self.month==3)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==4))):
                print ('มีน')
            elif((( (self.day >= 13) and (self.day <= 31))and(self.month==4)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==5))):
                print ('เมษ')
            elif((( (self.day >= 14) and (self.day <= 31))and(self.month==5)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==6))):
                print ('พฤษก')
            elif((( (self.day >= 14) and (self.day <= 31))and(self.month==6)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==7))):
                print ('เมถุน')
            elif((( (self.day >= 15) and (self.day <= 31))and(self.month==7)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==8))):
                print ('กรกฎ')
            elif((( (self.day >= 17) and (self.day <= 31))and(self.month==8)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==9))):
                print ('สิงห์')
            elif((( (self.day >= 17) and (self.day <= 31))and(self.month==9)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==10))):
                print ('กันย์')
            elif((( (self.day >= 17) and (self.day <= 31))and(self.month==10)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==11))):
                print ('ตุลย์')
            elif((( (self.day >= 16) and (self.day <= 31))and(self.month==11)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==12))):
                print ('พิจิก')
            elif((( (self.day >= 16) and (self.day <= 31))and(self.month==12)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==1))):
                print ('ธนู')
            else:
                print ('ไม่พบข้อมูล')

        elif ((self.hour == 7)or(self.hour == 8)):
            if((( (self.day >= 15) and (self.day <= 31))and(self.month==1)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==2))):
                print ('กุมภ์')
            elif((( (self.day >= 13) and (self.day <= 31))and(self.month==2)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==3))):
                print ('มีน')
            elif((( (self.day >= 14) and (self.day <= 31))and(self.month==3)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==4))):
                print ('เมษ')
            elif((( (self.day >= 13) and (self.day <= 31))and(self.month==4)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==5))):
                print ('พฤษก')
            elif((( (self.day >= 14) and (self.day <= 31))and(self.month==5)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==6))):
                print ('เมถุน')
            elif((( (self.day >= 14) and (self.day <= 31))and(self.month==6)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==7))):
                print ('กรกฎ')
            elif((( (self.day >= 15) and (self.day <= 31))and(self.month==7)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==8))):
                print ('สิงห์')
            elif((( (self.day >= 17) and (self.day <= 31))and(self.month==8)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==9))):
                print ('กันย์')
            elif((( (self.day >= 17) and (self.day <= 31))and(self.month==9)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==10))):
                print ('ตุลย์')
            elif((( (self.day >= 17) and (self.day <= 31))and(self.month==10)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==11))):
                print ('พิจิก')
            elif((( (self.day >= 16) and (self.day <= 31))and(self.month==11)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==12))):
                print ('ธนู')
            elif((( (self.day >= 16) and (self.day <= 31))and(self.month==12)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==1))):
                print ('มังกร')
            else:
                print ('ไม่พบข้อมูล')

        elif ((self.hour == 9)or(self.hour == 10)):
            if((( (self.day >= 15) and (self.day <= 31))and(self.month==1)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==2))):
                print ('มีน')
            elif((( (self.day >= 13) and (self.day <= 31))and(self.month==2)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==3))):
                print ('เมษ')
            elif((( (self.day >= 14) and (self.day <= 31))and(self.month==3)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==4))):
                print ('พฤษก')
            elif((( (self.day >= 13) and (self.day <= 31))and(self.month==4)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==5))):
                print ('เมถุน')
            elif((( (self.day >= 14) and (self.day <= 31))and(self.month==5)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==6))):
                print ('กรกฎ')
            elif((( (self.day >= 14) and (self.day <= 31))and(self.month==6)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==7))):
                print ('สิงห์')
            elif((( (self.day >= 15) and (self.day <= 31))and(self.month==7)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==8))):
                print ('กันย์')
            elif((( (self.day >= 17) and (self.day <= 31))and(self.month==8)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==9))):
                print ('ตุลย์')
            elif((( (self.day >= 17) and (self.day <= 31))and(self.month==9)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==10))):
                print ('พิจิก')
            elif((( (self.day >= 17) and (self.day <= 31))and(self.month==10)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==11))):
                print ('ธนู')
            elif((( (self.day >= 16) and (self.day <= 31))and(self.month==11)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==12))):
                print ('มังกร')
            elif((( (self.day >= 16) and (self.day <= 31))and(self.month==12)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==1))):
                print ('กุมภ์')
            else:
                print ('ไม่พบข้อมูล')
        
        elif ((self.hour == 11)or(self.hour == 12)):
            if((( (self.day >= 15) and (self.day <= 31))and(self.month==1)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==2))):
                print ('เมษ')
            elif((( (self.day >= 13) and (self.day <= 31))and(self.month==2)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==3))):
                print ('พฤษก')
            elif((( (self.day >= 14) and (self.day <= 31))and(self.month==3)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==4))):
                print ('เมถุน')
            elif((( (self.day >= 13) and (self.day <= 31))and(self.month==4)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==5))):
                print ('กรกฎ')
            elif((( (self.day >= 14) and (self.day <= 31))and(self.month==5)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==6))):
                print ('สิงห์')
            elif((( (self.day >= 14) and (self.day <= 31))and(self.month==6)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==7))):
                print ('กันย์')
            elif((( (self.day >= 15) and (self.day <= 31))and(self.month==7)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==8))):
                print ('ตุลย์')
            elif((( (self.day >= 17) and (self.day <= 31))and(self.month==8)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==9))):
                print ('พิจิก')
            elif((( (self.day >= 17) and (self.day <= 31))and(self.month==9)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==10))):
                print ('ธนู')
            elif((( (self.day >= 17) and (self.day <= 31))and(self.month==10)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==11))):
                print ('มังกร')
            elif((( (self.day >= 16) and (self.day <= 31))and(self.month==11)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==12))):
                print ('กุมภ์')
            elif((( (self.day >= 16) and (self.day <= 31))and(self.month==12)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==1))):
                print ('มีน')
            else:
                print ('ไม่พบข้อมูล')

        elif ((self.hour == 13)or(self.hour == 14)):
            if((( (self.day >= 15) and (self.day <= 31))and(self.month==1)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==2))):
                print ('พฤษก')
            elif((( (self.day >= 13) and (self.day <= 31))and(self.month==2)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==3))):
                print ('เมถุน')
            elif((( (self.day >= 14) and (self.day <= 31))and(self.month==3)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==4))):
                print ('กรกฎ')
            elif((( (self.day >= 13) and (self.day <= 31))and(self.month==4)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==5))):
                print ('สิงห์')
            elif((( (self.day >= 14) and (self.day <= 31))and(self.month==5)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==6))):
                print ('กันย์')
            elif((( (self.day >= 14) and (self.day <= 31))and(self.month==6)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==7))):
                print ('ตุลย์')
            elif((( (self.day >= 15) and (self.day <= 31))and(self.month==7)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==8))):
                print ('พิจิก')
            elif((( (self.day >= 17) and (self.day <= 31))and(self.month==8)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==9))):
                print ('ธนู')
            elif((( (self.day >= 17) and (self.day <= 31))and(self.month==9)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==10))):
                print ('มังกร')
            elif((( (self.day >= 17) and (self.day <= 31))and(self.month==10)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==11))):
                print ('กุมภ์')
            elif((( (self.day >= 16) and (self.day <= 31))and(self.month==11)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==12))):
                print ('มีน')
            elif((( (self.day >= 16) and (self.day <= 31))and(self.month==12)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==1))):
                print ('เมษ')
            else:
                print ('ไม่พบข้อมูล')

        elif ((self.hour == 15)or(self.hour == 16)):
            if((( (self.day >= 15) and (self.day <= 31))and(self.month==1)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==2))):
                print ('เมถุน')
            elif((( (self.day >= 13) and (self.day <= 31))and(self.month==2)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==3))):
                print ('กรกฎ')
            elif((( (self.day >= 14) and (self.day <= 31))and(self.month==3)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==4))):
                print ('สิงห์')
            elif((( (self.day >= 13) and (self.day <= 31))and(self.month==4)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==5))):
                print ('กันย์')
            elif((( (self.day >= 14) and (self.day <= 31))and(self.month==5)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==6))):
                print ('ตุลย์')
            elif((( (self.day >= 14) and (self.day <= 31))and(self.month==6)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==7))):
                print ('พิจิก')
            elif((( (self.day >= 15) and (self.day <= 31))and(self.month==7)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==8))):
                print ('ธนู')
            elif((( (self.day >= 17) and (self.day <= 31))and(self.month==8)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==9))):
                print ('มังกร')
            elif((( (self.day >= 17) and (self.day <= 31))and(self.month==9)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==10))):
                print ('กุมภ์')
            elif((( (self.day >= 17) and (self.day <= 31))and(self.month==10)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==11))):
                print ('มีน')
            elif((( (self.day >= 16) and (self.day <= 31))and(self.month==11)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==12))):
                print ('เมษ')
            elif((( (self.day >= 16) and (self.day <= 31))and(self.month==12)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==1))):
                print ('พฤษก')
            else:
                print ('ไม่พบข้อมูล')

        elif ((self.hour == 17)or(self.hour == 18)):
            if((( (self.day >= 15) and (self.day <= 31))and(self.month==1)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==2))):
                print ('กรกฎ')
            elif((( (self.day >= 13) and (self.day <= 31))and(self.month==2)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==3))):
                print ('สิงห์')
            elif((( (self.day >= 14) and (self.day <= 31))and(self.month==3)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==4))):
                print ('กันย์')
            elif((( (self.day >= 13) and (self.day <= 31))and(self.month==4)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==5))):
                print ('ตุลย์')
            elif((( (self.day >= 14) and (self.day <= 31))and(self.month==5)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==6))):
                print ('พิจิก')
            elif((( (self.day >= 14) and (self.day <= 31))and(self.month==6)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==7))):
                print ('ธนู')
            elif((( (self.day >= 15) and (self.day <= 31))and(self.month==7)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==8))):
                print ('มังกร')
            elif((( (self.day >= 17) and (self.day <= 31))and(self.month==8)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==9))):
                print ('กุมภ์')
            elif((( (self.day >= 17) and (self.day <= 31))and(self.month==9)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==10))):
                print ('มีน')
            elif((( (self.day >= 17) and (self.day <= 31))and(self.month==10)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==11))):
                print ('เมษ')
            elif((( (self.day >= 16) and (self.day <= 31))and(self.month==11)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==12))):
                print ('พฤษก')
            elif((( (self.day >= 16) and (self.day <= 31))and(self.month==12)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==1))):
                print ('เมถุน')
            else:
                print ('ไม่พบข้อมูล')

        elif ((self.hour == 19)or(self.hour == 20)):
            if((( (self.day >= 15) and (self.day <= 31))and(self.month==1)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==2))):
                print ('สิงห์')
            elif((( (self.day >= 13) and (self.day <= 31))and(self.month==2)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==3))):
                print ('กันย์')
            elif((( (self.day >= 14) and (self.day <= 31))and(self.month==3)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==4))):
                print ('ตุลย์')
            elif((( (self.day >= 13) and (self.day <= 31))and(self.month==4)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==5))):
                print ('พิจิก')
            elif((( (self.day >= 14) and (self.day <= 31))and(self.month==5)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==6))):
                print ('ธนู')
            elif((( (self.day >= 14) and (self.day <= 31))and(self.month==6)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==7))):
                print ('มังกร')
            elif((( (self.day >= 15) and (self.day <= 31))and(self.month==7)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==8))):
                print ('กุมภ์')
            elif((( (self.day >= 17) and (self.day <= 31))and(self.month==8)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==9))):
                print ('มีน')
            elif((( (self.day >= 17) and (self.day <= 31))and(self.month==9)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==10))):
                print ('เมษ')
            elif((( (self.day >= 17) and (self.day <= 31))and(self.month==10)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==11))):
                print ('พฤษก')
            elif((( (self.day >= 16) and (self.day <= 31))and(self.month==11)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==12))):
                print ('เมถุน')
            elif((( (self.day >= 16) and (self.day <= 31))and(self.month==12)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==1))):
                print ('กรกฏ')
            else:
                print ('ไม่พบข้อมูล')

        elif ((self.hour == 21)or(self.hour == 22)):
            if((( (self.day >= 15) and (self.day <= 31))and(self.month==1)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==2))):
                print ('กันย์')
            elif((( (self.day >= 13) and (self.day <= 31))and(self.month==2)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==3))):
                print ('ตุลย์')
            elif((( (self.day >= 14) and (self.day <= 31))and(self.month==3)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==4))):
                print ('พิจิก')
            elif((( (self.day >= 13) and (self.day <= 31))and(self.month==4)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==5))):
                print ('ธนู')
            elif((( (self.day >= 14) and (self.day <= 31))and(self.month==5)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==6))):
                print ('มังกร')
            elif((( (self.day >= 14) and (self.day <= 31))and(self.month==6)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==7))):
                print ('กุมภ์')
            elif((( (self.day >= 15) and (self.day <= 31))and(self.month==7)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==8))):
                print ('มีน')
            elif((( (self.day >= 17) and (self.day <= 31))and(self.month==8)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==9))):
                print ('เมษ')
            elif((( (self.day >= 17) and (self.day <= 31))and(self.month==9)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==10))):
                print ('พฤษก')
            elif((( (self.day >= 17) and (self.day <= 31))and(self.month==10)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==11))):
                print ('เมถุน')
            elif((( (self.day >= 16) and (self.day <= 31))and(self.month==11)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==12))):
                print ('กรกฏ')
            elif((( (self.day >= 16) and (self.day <= 31))and(self.month==12)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==1))):
                print ('สิงห์')
            else:
                print ('ไม่พบข้อมูล')
            

        elif ((self.hour == 23)or(self.hour == 0)or(self.hour == 24)):
            if((( (self.day >= 15) and (self.day <= 31))and(self.month==1)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==2))):
                print ('ตุลย์')
            elif((( (self.day >= 13) and (self.day <= 31))and(self.month==2)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==3))):
                print ('พิจิก')
            elif((( (self.day >= 14) and (self.day <= 31))and(self.month==3)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==4))):
                print ('ธนู')
            elif((( (self.day >= 13) and (self.day <= 31))and(self.month==4)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==5))):
                print ('มังกร')
            elif((( (self.day >= 14) and (self.day <= 31))and(self.month==5)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==6))):
                print ('กุมภ์')
            elif((( (self.day >= 14) and (self.day <= 31))and(self.month==6)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==7))):
                print ('มีน')
            elif((( (self.day >= 15) and (self.day <= 31))and(self.month==7)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==8))):
                print ('เมษ')
            elif((( (self.day >= 17) and (self.day <= 31))and(self.month==8)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==9))):
                print ('พฤษก')
            elif((( (self.day >= 17) and (self.day <= 31))and(self.month==9)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==10))):
                print ('เมถุน')
            elif((( (self.day >= 17) and (self.day <= 31))and(self.month==10)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==11))):
                print ('กรกฏ')
            elif((( (self.day >= 16) and (self.day <= 31))and(self.month==11)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==12))):
                print ('สิงห์')
            elif((( (self.day >= 16) and (self.day <= 31))and(self.month==12)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==1))):
                print ('กันย์')
            else:
                print ('ไม่พบข้อมูล')

        elif ((self.hour == 1)or(self.hour == 2)):
            if((( (self.day >= 15) and (self.day <= 31))and(self.month==1)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==2))):
                print ('พิจิก')
            elif((( (self.day >= 13) and (self.day <= 31))and(self.month==2)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==3))):
                print ('ธนู')
            elif((( (self.day >= 14) and (self.day <= 31))and(self.month==3)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==4))):
                print ('มังกร')
            elif((( (self.day >= 13) and (self.day <= 31))and(self.month==4)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==5))):
                print ('กุมภ์')
            elif((( (self.day >= 14) and (self.day <= 31))and(self.month==5)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==6))):
                print ('มีน')
            elif((( (self.day >= 14) and (self.day <= 31))and(self.month==6)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==7))):
                print ('เมษ')
            elif((( (self.day >= 15) and (self.day <= 31))and(self.month==7)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==8))):
                print ('พฤษก')
            elif((( (self.day >= 17) and (self.day <= 31))and(self.month==8)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==9))):
                print ('เมถุน')
            elif((( (self.day >= 17) and (self.day <= 31))and(self.month==9)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==10))):
                print ('กรกฏ')
            elif((( (self.day >= 17) and (self.day <= 31))and(self.month==10)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==11))):
                print ('สิงห์')
            elif((( (self.day >= 16) and (self.day <= 31))and(self.month==11)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==12))):
                print ('กันย์')
            elif((( (self.day >= 16) and (self.day <= 31))and(self.month==12)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==1))):
                print ('ตุลย์')
            else:
                print ('ไม่พบข้อมูล')

        elif ((self.hour == 3)or(self.hour == 4)):
            if((( (self.day >= 15) and (self.day <= 31))and(self.month==1)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==2))):
                print ('ธนู')
            elif((( (self.day >= 13) and (self.day <= 31))and(self.month==2)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==3))):
                print ('มังกร')
            elif((( (self.day >= 14) and (self.day <= 31))and(self.month==3)) or (( (self.day >= 1) and (self.day <= 12))and(self.month==4))):
                print ('กุมภ์')
            elif((( (self.day >= 13) and (self.day <= 31))and(self.month==4)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==5))):
                print ('มีน')
            elif((( (self.day >= 14) and (self.day <= 31))and(self.month==5)) or (( (self.day >= 1) and (self.day <= 13))and(self.month==6))):
                print ('เมษ')
            elif((( (self.day >= 14) and (self.day <= 31))and(self.month==6)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==7))):
                print ('พฤษก')
            elif((( (self.day >= 15) and (self.day <= 31))and(self.month==7)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==8))):
                print ('เมถุน')
            elif((( (self.day >= 17) and (self.day <= 31))and(self.month==8)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==9))):
                print ('กรกฏ')
            elif((( (self.day >= 17) and (self.day <= 31))and(self.month==9)) or (( (self.day >= 1) and (self.day <= 16))and(self.month==10))):
                print ('สิงห์')
            elif((( (self.day >= 17) and (self.day <= 31))and(self.month==10)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==11))):
                print ('กันย์')
            elif((( (self.day >= 16) and (self.day <= 31))and(self.month==11)) or (( (self.day >= 1) and (self.day <= 15))and(self.month==12))):
                print ('ตุลย์')
            elif((( (self.day >= 16) and (self.day <= 31))and(self.month==12)) or (( (self.day >= 1) and (self.day <= 14))and(self.month==1))):
                print ('พิจิก')
            else:
                print ('ไม่พบข้อมูล')

        else:
            print ('ไม่พบข้อมูล')

duHora = Hora()
duHora.rasee()
duHora.lakkana()