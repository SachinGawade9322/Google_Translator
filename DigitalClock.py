from tkinter import *
import datetime

def date_time():
    time = datetime.datetime.now() # it gives u current date and time
# here the all values of clock will be stored in the corresponding variables
    hr = time.strftime('%I') # it gives u hours I= hours
    mi = time.strftime('%M') # M = min
    sec = time.strftime('%S')# S = second
    am = time.strftime('%p') # (small) p = am/pm
    
# here the all values of date and day is stored in the variables    
    date = time.strftime('%d')# here strftime give the current value && d = day (it give the current day)
    month = time.strftime('%m')# (small) m = for the current value of month
    year = time.strftime('%y')#%  y used to give year
    day = time.strftime('%a')# % a give the value of day in only two/three initial letters
# here the actual chage of clock will take place with the help of "config" = it will give u actual value
    leb_hr.config(text=hr)# it change the value of "00" to the current hr value
    leb_min.config(text=mi) # change the min value 
    leb_sec.config(text=sec)# change the second value
    leb_am.config(text=am)# change the am/pm value
# here the change related to date and day take place because of "config"   
    leb_date.config(text=date)# change the value of "00" to the current value of date
    leb_mo.config(text=month)
    leb_yer.config(text=year)
    leb_day.config(text=day)
# here the change will take place in every 200 mili second (because of this the frequent change in clock take place)   
    leb_hr.after(200, date_time)# change the hour value in every 200 mili sec 
    
clock = Tk()# call the class
clock.geometry("1000x500") #here we set the geometry
clock.title("**Digital Clock**")# it will give the title to the main page
clock.config(bg="Yellow")

# padding of clock
leb_hr = Label(clock, text="00", font=("Time New Roman", 60, "bold"), bg="White", fg="Black")
leb_hr.place(x=120 , y=45 , width=100 , height=110 )

leb_hr_txt = Label(clock, text="Hour", font=("Time New Roman", 20, "bold"), bg="White", fg="Black")
leb_hr_txt.place(x=120 , y=190 , width=100 , height=40 )


leb_min = Label(clock, text="00", font=("Time New Roman", 60, "bold"), bg="White", fg="Black")
leb_min.place(x=340 , y=45 , width=100 , height=110 )

leb_min_txt = Label(clock, text="Minute", font=("Time New Roman", 20, "bold"), bg="White", fg="Black")
leb_min_txt.place(x=340 , y=190 , width=100 , height=40 )

leb_sec = Label(clock, text="00", font=("Time New Roman", 60, "bold"), bg="White", fg="Black")
leb_sec.place(x=560 , y=45 , width=100 , height=110 )

leb_sec_txt = Label(clock, text="Second", font=("Time New Roman", 20, "bold"), bg="White", fg="Black")
leb_sec_txt.place(x=560 , y=190 , width=100 , height=40 )

leb_am = Label(clock, text="00", font=("Time New Roman", 35, "bold"), bg="White", fg="Black")
leb_am.place(x=780 , y=45 , width=100 , height=110 )

leb_am_txt = Label(clock, text="am/pm", font=("Time New Roman", 20, "bold"), bg="White", fg="Black")
leb_am_txt.place(x=780 , y=190 , width=100 , height=40 )


# Padding of date and day

leb_date = Label(clock, text="00", font=("Time New Roman", 60, "bold"), bg="White", fg="Black")
leb_date.place(x=120 , y=270 , width=100 , height=110 )

leb_date_txt = Label(clock, text="Date", font=("Time New Roman", 20, "bold"), bg="White", fg="Black")
leb_date_txt.place(x=120 , y=410 , width=100 , height=40 )

leb_mo = Label(clock, text="00", font=("Time New Roman", 60, "bold"), bg="White", fg="Black")
leb_mo.place(x=340 , y=270 , width=100 , height=110 )

leb_mo_txt = Label(clock, text="Month", font=("Time New Roman", 20, "bold"), bg="White", fg="Black")
leb_mo_txt.place(x=340 , y=410 , width=100 , height=40 )

leb_yer = Label(clock, text="00", font=("Time New Roman", 60, "bold"), bg="White", fg="Black")
leb_yer.place(x=560 , y=270 , width=100 , height=110 )

leb_yer_txt = Label(clock, text="Year", font=("Time New Roman", 20, "bold"), bg="White", fg="Black")
leb_yer_txt.place(x=560 , y=410 , width=100 , height=40 )


leb_day = Label(clock, text="00", font=("Time New Roman", 35, "bold"), bg="White", fg="Black")
leb_day.place(x=780 , y=270 , width=100 , height=110 )

leb_day_txt = Label(clock, text="Day", font=("Time New Roman", 20, "bold"), bg="White", fg="Black")
leb_day_txt.place(x=780 , y=410 , width=100 , height=40 )

date_time() # the function call

clock.mainloop()# for continuous running the graphic