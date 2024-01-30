# ANSI color codes for formatting
COLOR_RESET = '\033[0m'
COLOR_BOLD = '\033[1m'
COLOR_RED = '\033[91m'
COLOR_GREEN = '\033[92m'
COLOR_YELLOW = '\033[93m'

# Import System Python
import calendar
import time
from datetime import datetime
from tabulate import tabulate
from plyer import notification
from tqdm import tqdm

def kalender(highlighted_tenggat):
    current_year = datetime.now().year
    print(COLOR_BOLD + COLOR_GREEN + f"\nYear {current_year}\n" + COLOR_RESET)

    # Loop untuk setiap bulan
    for month in range(1, 13):
        cal = calendar.monthcalendar(current_year, month)

        # Print colored month header
        month_name = calendar.month_name[month]
        print(COLOR_BOLD + COLOR_GREEN + f"\n{month_name}\n" + COLOR_RESET)

        # Print colored calendar for the month
        print(COLOR_BOLD + COLOR_YELLOW + " Mo Tu We Th Fr Sa Su" + COLOR_RESET)

        # Loop untuk setiap minggu dalam bulan
        for week in cal:
            for day in week:
                formatted_day = f"{day:2}" if day != 0 else "  "
                
                # Logic untuk menentukan warna
                if formatted_day != "  ":
                    now = datetime.strptime(f"{current_year}-{month}-{formatted_day}", "%Y-%m-%d").date() 
                    if isinstance(highlighted_tenggat, (list, tuple, set)) and any(sublist for sublist in highlighted_tenggat if now in sublist):
                        colored_day = COLOR_BOLD + COLOR_RED + formatted_day + COLOR_RESET
                    else:
                        colored_day = formatted_day
                else:
                    colored_day = formatted_day
                print(colored_day, end=" ")
            print()
        print()

def bubble_sort(arr):
    n = len(arr)

    # Traverse through all elements in the array
    for i in range(n):
        # Last i elements are already sorted, so we don't need to check them
        for j in range(0, n-i-1):
            date_j = datetime.strptime(arr[j][1], '%d-%m-%Y') if isinstance(arr[j][1], str) else arr[j][1]
            date_j_plus_1 = datetime.strptime(arr[j+1][1], '%d-%m-%Y') if isinstance(arr[j+1][1], str) else arr[j+1][1]
            # Swap if the element found is greater than the next element
            if date_j > date_j_plus_1 or (date_j == date_j_plus_1 and arr[j][2] > arr[j+1][2]):
                arr[j], arr[j+1] = arr[j+1],arr[j]

highlighted_tenggat = []
while True :

    tugasArray = []
    moneyArray = []
    examArray = []
    goalsArray = []
    done = []
    
    print ("===============")
    print ("    CALENDS    ")
    print ("===============")
    print ("Choose :")
    print ("1. Assignment")
    print ("2. Exam")
    print ("3. Money Report")
    print ("4. Goals")
    print ("5. Exit")
    
    pilih0 = input("Number : ")

    if pilih0 == "1" :
        while (True) :
            print ("===========================")
            print ("         ASSIGNMENT        ")
            print ("===========================")

            tugasHeaders = ["Activiy Name","Deadline Date", "Deadline Hour","Late", "Status"]
            print ("Choose : ")
            print ("1. Add tasks")
            print ("2. Show tasks")
            print ("3. Update Checklist")
            print ("4. Back")
            pilih = input("Number : ")
            
            if pilih == "1" :
                print ("==========================")
                print ("         ADD TASKS        ")
                print ("==========================")
                
                currentDateAndTime = datetime.now()  
                current_date = currentDateAndTime.strftime('%d-%m-%Y')
                current_time = currentDateAndTime.strftime("%H:%M")

                current_date_obj = currentDateAndTime.strptime(current_date, "%d-%m-%Y")
                current_time_obj = currentDateAndTime.strptime(current_time, "%H:%M")

                print(current_date, current_time)
                work = input(f"Work : ")
                deadline = input(f"Deadline Date (DD-MM-YYYY): ").strip()
                deadline_hour = input(f"Deadline Hour (HH:MM): ")
                deadlineDate = datetime.strptime(deadline, '%d-%m-%Y')
                deadlineHourReal = currentDateAndTime.strptime(deadline_hour, "%H:%M")
                done.append("Not Done")
                tugasArray.append((work,deadline,deadline_hour, "Not Late", "Not Done"))

                date_format = "%d-%m-%Y"
                deadline = datetime.strptime(deadline,date_format)
                highlighted_tenggat.append([deadline.date()])

                kalender(highlighted_tenggat)
                
                bubble_sort(tugasArray)
                print('=============')
                print(current_date, current_time)
                print("Assignment Information : ")

                for j in range(0, len(tugasArray)):
                    baba = currentDateAndTime.strptime(tugasArray[j][1],'%d-%m-%Y')
                    caca = currentDateAndTime.strptime(tugasArray[j][2], "%H:%M")
                    lateBy = (baba-current_date_obj)*-1
                    if baba < current_date_obj and caca < current_time_obj :
                        tugasArray[j] = (tugasArray[j][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), f"Late by {lateBy}", tugasArray[j][4])
                    elif baba < current_date_obj and caca > current_time_obj:
                        tugasArray[j] = (tugasArray[j][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), f"Late by {lateBy}", tugasArray[j][4])
                    elif baba == current_date_obj and caca < current_time_obj :
                        tugasArray[j] = (tugasArray[j][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), f"Late by {lateBy}", tugasArray[j][4])
                    elif baba == current_date_obj and caca > current_time_obj :
                        tugasArray[j] = (tugasArray[j][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late", tugasArray[j][4])
                    elif baba == current_date_obj and caca == current_time_obj :
                        tugasArray[j] = (tugasArray[j][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late", tugasArray[j][4])
                    elif baba > current_date_obj and caca > current_time_obj :
                        tugasArray[j] = (tugasArray[j][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late", tugasArray[j][4])
                    elif baba > current_date_obj and caca < current_time_obj :
                        tugasArray[j] = (tugasArray[j][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late", tugasArray[j][4])
                    elif baba > current_date_obj and caca == current_time_obj :
                        tugasArray[j] = (tugasArray[j][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late",tugasArray[j][4])

                print(tabulate(tugasArray , headers=tugasHeaders, tablefmt="grid"))
                print()

                current_datetime = datetime.now()
                days_until_due = (deadline - datetime.strptime(current_datetime.strftime('%d-%m-%Y'), date_format)).days

                if days_until_due > 0:
                    hours_until_due = (datetime.strptime(deadline.strftime('%d-%m-%Y')+deadlineHourReal.strftime('%H:%M'), '%d-%m-%Y%H:%M') - datetime.strptime(current_datetime.strftime('%d-%m-%Y%H:%M'), '%d-%m-%Y%H:%M')).seconds // 3600
                else:
                    jam_atur = int(deadlineHourReal.strftime('%H:%M')[0:2])
                    menit_atur = int(deadlineHourReal.strftime('%H:%M')[-2:])
                    jam_atur_now = int(current_datetime.strftime('%d-%m-%Y%H:%M')[-5:][0:2])
                    menit_atur_now = int(current_datetime.strftime('%d-%m-%Y%H:%M')[-2:])
                    jam_deadline = jam_atur - jam_atur_now
                    if jam_deadline <= 0:
                        menit_deadline = menit_atur - menit_atur_now
                        if menit_deadline < 0:
                            hours_until_due = -1
                        elif menit_deadline == 0:
                            hours_until_due = 0
                        else:
                            hours_until_due = 1
                    else:
                        hours_until_due = jam_deadline

                if days_until_due >= 0 and hours_until_due > 0:
                    notification.notify(
                    title="New Assignment",
                    message=f"There is a new task {work}",
                    timeout=10
                )
                    notification.notify(
                    title=f"Assignment Deadlines {work}!!!",
                    message=f"{work} task will end in {days_until_due} days, {hours_until_due} hours.",
                    timeout=10
                )
                elif days_until_due == 0 and hours_until_due > 0:
                    notification.notify(
                    title="New Assignment",
                    message=f"There is a new task {work}",
                    timeout=10
                )
                    notification.notify(
                    title=f"Assignment Deadlines {work}!!!",
                    message=f"{work} task will end in {days_until_due} days, {hours_until_due} hours.",
                    timeout=10
                ) 
                elif days_until_due == 0 and hours_until_due == 0 :
                    notification.notify(
                    title=f"{work} Assignment Ends!!!",
                    message=f"{work}'s assignment has ended",
                    timeout=10
                )
                elif days_until_due < 0 and hours_until_due <= 0:
                    notification.notify(
                    title=f"{work}'s assignment deadline has passed!!!",
                    message=f"{work}'s task has ended in the past {days_until_due*-1} days",
                    timeout=10
                )
                elif days_until_due < 0 and hours_until_due >= 0:
                    notification.notify(
                    title=f"{work}'s assignment deadline has passed!!!",
                    message=f"{work}'s task has ended in the past {days_until_due*-1} days",
                    timeout=10
                )
                elif days_until_due > 0 and hours_until_due <= 0:
                    notification.notify(
                    title=f"{work}'s assignment deadline has passed!!!",
                    message=f"{work}'s task has ended in the past {days_until_due*-1} days",
                    timeout=10
                )

            elif pilih == "2":
                    print("Assignment Information :")
                    print(tabulate(tugasArray, headers=tugasHeaders, tablefmt="grid"))
         
            elif pilih == "3" :
                print("====================")
                print("  UPDATE CHECKLIST  ")
                print("====================")

                print(tabulate(tugasArray , headers=tugasHeaders, tablefmt="grid"))
                print()

                kerja = int(input("Num : "))

                if 1 <= kerja <= len(tugasArray):
                    nomor = kerja-1
                    if done[nomor] == "Not Done":
                        done[nomor] = "Done"
                        baba = currentDateAndTime.strptime(tugasArray[nomor][1], '%d-%m-%Y')
                        caca = currentDateAndTime.strptime(tugasArray[nomor][2], "%H:%M")
                        lateBy = (baba-current_date_obj)*-1
                    
                        if baba < current_date_obj and caca < current_time_obj:
                            tugasArray[nomor] = (tugasArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), f"Late by {lateBy}", "Done")
                        elif baba < current_date_obj and caca > current_time_obj:
                            tugasArray[nomor] = (tugasArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), f"Late by {lateBy}", "Done")
                        elif baba == current_date_obj and caca < current_time_obj :
                            tugasArray[nomor] = (tugasArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), f"Late by {lateBy}", "Done")
                        elif baba == current_date_obj and caca > current_time_obj :
                            tugasArray[nomor] = (tugasArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late", "Done")
                        elif baba == current_date_obj and caca == current_time_obj :
                            tugasArray[nomor] = (tugasArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late", "Done")
                        elif baba> current_date_obj and caca> current_time_obj :
                            tugasArray[nomor] = (tugasArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late", "Done")
                        elif baba > current_date_obj and caca < current_time_obj :
                            tugasArray[nomor] = (tugasArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late", "Done")
                        elif baba> current_date_obj and caca == current_time_obj :
                            tugasArray[nomor] = (tugasArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late","Done")
                    
                    elif done[nomor] == "Not Done":
                            done[nomor] = "Not Done"
                            lateBy = (baba-current_date_obj)*-1
                            if baba < current_date_obj and caca < current_time_obj:
                                tugasArray[nomor] = (tugasArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), f"Late by {lateBy}", "Not Done")
                            elif baba < current_date_obj and caca > current_time_obj:
                                tugasArray[nomor] = (tugasArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), f"Late by {lateBy}", "Not Done")
                            elif baba == current_date_obj and caca < current_time_obj :
                                tugasArray[nomor] = (tugasArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), f"Late by {lateBy}", "Not Done")
                            elif baba == current_date_obj and caca > current_time_obj :
                                tugasArray[nomor] = (tugasArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late", "Not Done")
                            elif baba == current_date_obj and caca == current_time_obj :
                                tugasArray[nomor] = (tugasArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late", "Not Done")
                            elif baba> current_date_obj and caca> current_time_obj :
                                tugasArray[nomor] = (tugasArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late", "Not Done")
                            elif baba > current_date_obj and caca < current_time_obj :
                                tugasArray[nomor] = (tugasArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late", "Not Done")
                            elif baba> current_date_obj and caca == current_time_obj :
                                tugasArray[nomor] = (tugasArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late","Not Done")
                    
                    elif done[nomor] == "Done":
                            done[nomor] = "Not Done"
                            lateBy = (baba-current_date_obj)*-1
                            if baba < current_date_obj and caca < current_time_obj:
                                tugasArray[nomor] = (tugasArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), f"Late by {lateBy}", "Not Done")
                            elif baba < current_date_obj and caca > current_time_obj:
                                tugasArray[nomor] = (tugasArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), f"Late by {lateBy}", "Not Done")
                            elif baba == current_date_obj and caca < current_time_obj :
                                tugasArray[nomor] = (tugasArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), f"Late by {lateBy}", "Not Done")
                            elif baba == current_date_obj and caca > current_time_obj :
                                tugasArray[nomor] = (tugasArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late", "Not Done")
                            elif baba == current_date_obj and caca == current_time_obj :
                                tugasArray[nomor] = (tugasArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late", "Not Done")
                            elif baba> current_date_obj and caca> current_time_obj :
                                tugasArray[nomor] = (tugasArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late", "Not Done")
                            elif baba > current_date_obj and caca < current_time_obj :
                                tugasArray[nomor] = (tugasArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late", "Not Done")
                            elif baba> current_date_obj and caca == current_time_obj :
                                tugasArray[nomor] = (tugasArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late","Not Done")

                print("!! Checklist Updated !! ")
                print("====================")
                print("     Checklist")
                print("--------------------")
                print(tabulate(tugasArray , headers=tugasHeaders, tablefmt="grid"))
                print()

            elif pilih == "4" :
                break
            else :
                print ("Your Choice Is Invalid. Please Try Again.")

    elif pilih0 == "2" :
        while (True) :
            print ("======================")
            print ("         EXAM         ")
            print ("======================")

            examHeaders = ["Activiy Name","Deadline Date", "Deadline Hour", "Late", "Status"]
            print ("Choose : ")
            print ("1. Add exam")
            print ("2. Show exam")
            print ("3. Update Checklist")
            print ("4. Back")
            pilih = input("Number : ")
            
            if pilih == "1" :
                print ("===========================")
                print ("          ADD EXAM         ")
                print ("===========================")
                
                currentDateAndTime = datetime.now()  
                current_date = currentDateAndTime.strftime('%d-%m-%Y')
                current_time = currentDateAndTime.strftime("%H:%M")

                current_date_obj = currentDateAndTime.strptime(current_date, "%d-%m-%Y")
                current_time_obj = currentDateAndTime.strptime(current_time, "%H:%M")

                print(current_date, current_time)
                
                exam = input(f"Exam : ")
                deadline = input(f"Deadline Date (DD-MM-YYYY): ").strip()
                deadline_hour = input(f"Deadline Hour (HH:MM): ")
                deadlineDate = datetime.strptime(deadline,'%d-%m-%Y')
                deadlineHourReal = currentDateAndTime.strptime(deadline_hour, "%H:%M")
                
                done.append("Not Done")
                examArray.append((exam,deadline,deadline_hour, "Not Late", "Not Done"))

                date_format = "%d-%m-%Y"
                deadline = datetime.strptime(deadline,date_format)
                highlighted_tenggat.append([deadline.date()])

                kalender(highlighted_tenggat)
                
                bubble_sort(examArray)
                print('=============')
                print(current_date, current_time)
                print("Exam Information : ")

                for j in range(0, len(examArray)):
                    baba = currentDateAndTime.strptime(examArray[j][1],'%d-%m-%Y')
                    caca = currentDateAndTime.strptime(examArray[j][2], "%H:%M")
                    lateBy = (baba-current_date_obj)*-1
                    if baba < current_date_obj and caca < current_time_obj:
                        examArray[j] = (examArray[j][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), f"Late by {lateBy}", examArray[j][4])
                    elif baba < current_date_obj and caca > current_time_obj:
                        examArray[j] = (examArray[j][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), f"Late by {lateBy}", examArray[j][4])
                    elif baba == current_date_obj and caca < current_time_obj :
                        examArray[j] = (examArray[j][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), f"Late by {lateBy}", examArray[j][4])
                    elif baba == current_date_obj and caca > current_time_obj :
                        examArray[j] = (examArray[j][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late", examArray[j][4])
                    elif baba == current_date_obj and caca == current_time_obj :
                        examArray[j] = (examArray[j][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late", examArray[j][4])
                    elif baba> current_date_obj and caca> current_time_obj :
                        examArray[j] = (examArray[j][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late", examArray[j][4])
                    elif baba > current_date_obj and caca < current_time_obj :
                        examArray[j] = (examArray[j][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late", examArray[j][4])
                    elif baba> current_date_obj and caca == current_time_obj :
                        examArray[j] = (examArray[j][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late",examArray[j][4])

                print(tabulate(examArray , headers=examHeaders, tablefmt="grid"))
                print()

                current_datetime = datetime.now()
                days_until_due = (deadline - datetime.strptime(current_datetime.strftime('%d-%m-%Y'), date_format)).days

                if days_until_due > 0:
                    hours_until_due = (datetime.strptime(deadline.strftime('%d-%m-%Y')+deadlineHourReal.strftime('%H:%M'), '%d-%m-%Y%H:%M') - datetime.strptime(current_datetime.strftime('%d-%m-%Y%H:%M'), '%d-%m-%Y%H:%M')).seconds // 3600
                else:
                    jam_atur = int(deadlineHourReal.strftime('%H:%M')[0:2])
                    menit_atur = int(deadlineHourReal.strftime('%H:%M')[-2:])
                    jam_atur_now = int(current_datetime.strftime('%d-%m-%Y%H:%M')[-5:][0:2])
                    menit_atur_now = int(current_datetime.strftime('%d-%m-%Y%H:%M')[-2:])
                    jam_deadline = jam_atur - jam_atur_now
                    if jam_deadline <= 0:
                        menit_deadline = menit_atur - menit_atur_now
                        if menit_deadline < 0:
                            hours_until_due = -1
                        elif menit_deadline == 0:
                            hours_until_due = 0
                        else:
                            hours_until_due = 1
                    else:
                        hours_until_due = jam_deadline

                if days_until_due >= 0 and hours_until_due > 0:
                    notification.notify(
                    title="New Exam",
                    message=f"There is a new exam {exam}",
                    timeout=10
                )
                    notification.notify(
                    title=f"Exam Deadlines {exam}!!!",
                    message=f"{exam} exam will end in {days_until_due} days, {hours_until_due} hours.",
                    timeout=10
                )
                elif days_until_due == 0 and hours_until_due > 0:
                    notification.notify(
                    title="New Exam",
                    message=f"There is a new exam {exam}",
                    timeout=10
                )
                    notification.notify(
                    title=f"Exam Deadlines {exam}!!!",
                    message=f"{exam} exam will end in {days_until_due} days, {hours_until_due} hours.",
                    timeout=10
                )
                elif days_until_due == 0 and hours_until_due == 0 :
                    notification.notify(
                    title=f"{exam} Exam Ends!!!",
                    message=f"{exam}'s exam has ended",
                    timeout=10
                )
                elif days_until_due < 0 and hours_until_due <= 0:
                    notification.notify(
                    title=f"{exam}'s exam deadline has passed!!!",
                    message=f"{exam}'s exam has ended in the past {days_until_due*-1} days",
                    timeout=10
                )
                elif days_until_due > 0 and hours_until_due <= 0:
                    notification.notify(
                    title=f"{exam}'s exam deadline has passed!!!",
                    message=f"{exam}'s exam has ended in the past {days_until_due*-1} days",
                    timeout=10
                )
                elif days_until_due < 0 and hours_until_due >= 0:
                    notification.notify(
                    title=f"{exam}'s exam deadline has passed!!!",
                    message=f"{exam}'s exam has ended in the past {days_until_due*-1} days",
                    timeout=10
                )

            elif pilih == "2":
                kalender(highlighted_tenggat)
                print("Exam Information : ")
                print(tabulate(examArray, headers=examHeaders, tablefmt="grid"))

            elif pilih == "3" :
                print("====================")
                print("  Update Checklist  ")
                print("====================")

                print(tabulate(examArray , headers=examHeaders, tablefmt="grid"))
                print()

                kerja = int(input("Number : "))

                if 1 <= kerja <= len(examArray):
                    nomor = kerja-1
                    if done[nomor] == "Not Done":
                        done[nomor] = "Done"
                        baba = currentDateAndTime.strptime(examArray[nomor][1], '%d-%m-%Y')
                        caca = currentDateAndTime.strptime(examArray[nomor][2], "%H:%M")
                        lateBy = (baba-current_date_obj)*-1
                    
                        if baba < current_date_obj and caca < current_time_obj:
                            examArray[nomor] = (examArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), f"Late by {lateBy}", "Done")
                        elif baba < current_date_obj and caca > current_time_obj:
                            examArray[nomor] = (examArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), f"Late by {lateBy}", "Done")
                        elif baba == current_date_obj and caca < current_time_obj :
                            examArray[nomor] = (examArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), f"Late by {lateBy}", "Done")
                        elif baba == current_date_obj and caca > current_time_obj :
                            examArray[nomor] = (examArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late", "Done")
                        elif baba == current_date_obj and caca == current_time_obj :
                            examArray[nomor] = (examArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late", "Done")
                        elif baba> current_date_obj and caca> current_time_obj :
                            examArray[nomor] = (examArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late", "Done")
                        elif baba > current_date_obj and caca < current_time_obj :
                            examArray[nomor] = (examArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late", "Done")
                        elif baba> current_date_obj and caca == current_time_obj :
                            examArray[nomor] = (examArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late","Done")
                    elif done[nomor] == "Not Done":
                            done[nomor] = "Not Done"
                            lateBy = (baba-current_date_obj)*-1
                            if baba < current_date_obj and caca < current_time_obj:
                                examArray[nomor] = (examArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), f"Late by {lateBy}", "Not Done")
                            elif baba < current_date_obj and caca > current_time_obj:
                                examArray[nomor] = (examArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), f"Late by {lateBy}", "Not Done")
                            elif baba == current_date_obj and caca < current_time_obj :
                                examArray[nomor] = (examArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), f"Late by {lateBy}", "Not Done")
                            elif baba == current_date_obj and caca > current_time_obj :
                                examArray[nomor] = (examArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late", "Not Done")
                            elif baba == current_date_obj and caca == current_time_obj :
                                examArray[nomor] = (examArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late", "Not Done")
                            elif baba> current_date_obj and caca> current_time_obj :
                                examArray[nomor] = (examArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late", "Not Done")
                            elif baba > current_date_obj and caca < current_time_obj :
                                examArray[nomor] = (examArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late", "Not Done")
                            elif baba> current_date_obj and caca == current_time_obj :
                                examArray[nomor] = (examArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late","Not Done")
                    elif done[nomor] == "Done":
                            done[nomor] = "Not Done"
                            lateBy = (baba-current_date_obj)*-1
                            if baba < current_date_obj and caca < current_time_obj:
                                examArray[nomor] = (examArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), f"Late by {lateBy}", "Not Done")
                            elif baba < current_date_obj and caca > current_time_obj:
                                examArray[nomor] = (examArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), f"Late by {lateBy}", "Not Done")
                            elif baba == current_date_obj and caca < current_time_obj :
                                examArray[nomor] = (examArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), f"Late by {lateBy}", "Not Done")
                            elif baba == current_date_obj and caca > current_time_obj :
                                examArray[nomor] = (examArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late", "Not Done")
                            elif baba == current_date_obj and caca == current_time_obj :
                                examArray[nomor] = (examArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late", "Not Done")
                            elif baba> current_date_obj and caca> current_time_obj :
                                examArray[nomor] = (examArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late", "Not Done")
                            elif baba > current_date_obj and caca < current_time_obj :
                                examArray[nomor] = (examArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late", "Not Done")
                            elif baba> current_date_obj and caca == current_time_obj :
                                examArray[nomor] = (examArray[nomor][0], baba.strftime('%d-%m-%Y'), caca.strftime('%H:%M'), "Not Late","Not Done")

                print("!! Checklist Updated !! ")
                print("====================")
                print("     Checklist")
                print("--------------------")
                print(tabulate(examArray , headers=examHeaders, tablefmt="grid"))
                print()
         
            elif pilih == "4" :
                break
            else :
                print ("Your Choice Is Invalid. Please Try Again.")

    elif pilih0 == "3" :
        while True :
            current_date = datetime.today().strftime('%d %b %Y')
            tugasHeaders = ["Item Name","Price","Quantity","Total Price Per Item"]

            print("==================================")
            print("           MONEY REPORT           ")
            print("==================================")
            print("1. Add List Item")
            print("2. Show Money Report")
            print("3. Back")

            pilih = input("Number : ")

            current_date = datetime.today().strftime('%d %b %Y')
            moneyHeaders = ["Item Name","Price","Quantity","Total Price Per Item"]


            if pilih == "1" :
                print(current_date)
                print('----------------------------------')
                print('              BUDGET              ')
                print('----------------------------------')
                bulan_awal = input("Early Month : ")
                bulan_akhir = input("End of Month: ")
                date = input(f"Date (DD-MM-YYYY): ").strip()
                budget = int(input("A Month's Budget : "))

                banyakItem = int(input("How Many Items? "))
                print('==================================')
                # moneyArray = []
                moneyArray_sum = 0
                for i in range(0,banyakItem):
                    name = (input(f"Input item {i + 1} name : "))
                    harga = int(input(f"Input item {i + 1} price : Rp."))
                    quantity = int(input(f"Input item {i+1}'s quantity : "))
                    print('==================================')
                    total_price = harga * quantity
                    moneyArray_sum += total_price
                    moneyArray.append((name, harga, quantity, total_price))

                sisaUang = budget-moneyArray_sum
                #Kondisi Untuk Menentutkan jumlah uang dengan pengeluaran (Untuk mengantisipasi pengeluaran > pemasukan)
                if budget >= moneyArray_sum:
                    sisa_pengeluaran = (budget - moneyArray_sum)
                    #Perulangan Untuk Progress bar
                    for j in tqdm(range (0, budget)):
                        time.sleep(0)
                        if j == moneyArray_sum:
                            break

                print(f"Money Report as of {current_date}")

                print(tabulate(moneyArray , headers=moneyHeaders, tablefmt="grid"))
                print()

                print('==============================================================')
                print(f"The expenditure target during {bulan_awal}-{bulan_akhir} : {budget}")
                print(f"Sum of Expenses as of {current_date} : Rp.", moneyArray_sum)
                print(f"The remainder of your budget on the date {current_date} : Rp.", sisaUang)

            elif pilih == "2" :
                sisaUang = budget-moneyArray_sum
                if budget >= moneyArray_sum:
                    sisa_pengeluaran = (budget - moneyArray_sum)
                    #Perulangan Untuk Progress bar
                    for j in tqdm(range (0, budget)):
                        time.sleep(0)
                        if j == moneyArray_sum:
                            break

                print(f"Money Report as of {current_date}")

                print(tabulate(moneyArray , headers=moneyHeaders, tablefmt="grid"))
                print()

                print('==============================================================')
                print(f"The expenditure target during {bulan_awal}-{bulan_akhir} : {budget}")
                print(f"Sum of Expenses as of {current_date} : Rp.", moneyArray_sum)
                print(f"The remainder of your budget on the date {current_date} : Rp.", sisaUang)

            elif pilih == "3" :
                break

    elif pilih0 == "4" :
         while (True) :
            print ("======================")
            print ("         GOALS        ")
            print ("======================")

            goalsHeaders = ["Activiy Name", "Status"]
            print ("Choose : ")
            print ("1. Add Goals")
            print ("2. Show Goals")
            print ("3. Update Checklist")
            print ("4. Back")
            pilih = input("Number : ")
            
            if pilih == "1" :
                print ("==========================")
                print ("         ADD GOALS        ")
                print ("==========================")
                
                currentDateAndTime = datetime.now()  
                current_date = currentDateAndTime.strftime('%d-%m-%Y')
                current_time = currentDateAndTime.strftime("%H:%M")

                current_date_obj = currentDateAndTime.strptime(current_date, "%d-%m-%Y")
                current_time_obj = currentDateAndTime.strptime(current_time, "%H:%M")

                print(current_date, current_time)
                goals = input(f"Goals : ")
                
                done.append("Not Done")
                goalsArray.append((goals, "Not Done"))

                current_year = datetime.now().year

                print('=============')
                print(current_date, current_time)
                print("Goals : ")
                
                for j in range(0, len(goalsArray)):
                    goalsArray[j] = (goalsArray[j][0], goalsArray[j][1])

                print(tabulate(goalsArray , headers=goalsHeaders, tablefmt="grid"))
                print()

                notification.notify(
                    title="There is a new goal",
                    message=f"{goals}",
                    timeout=10
                )

            elif pilih == "2":
                print ("==========================")
                print ("        SHOW GOALS        ")
                print ("==========================")
                print("Goals Information :")
                print(tabulate(goalsArray, headers=goalsHeaders, tablefmt="grid"))
         
            elif pilih == "3" :
                print("====================")
                print("  UPDATE CHECKLIST  ")
                print("====================")

                print(tabulate(goalsArray , headers=goalsHeaders, tablefmt="grid"))
                print()

                kerja = int(input("Number: "))

                if 1 <= kerja <= len(goalsArray):
                    nomor = kerja-1
                    if done[nomor] == "Not Done":
                        done[nomor] = "Done"
                        goalsArray[nomor] = (goalsArray[nomor][0], "Done")
                        notification.notify(
                            title=f"Goals {goals}",
                            message=f"Done",
                            timeout=10
                        )
                    elif done[nomor] == "Done":
                            done[nomor] = "Not Done"
                            goalsArray[nomor] = (goalsArray[nomor][0], "Not Done")
                            notification.notify(
                            title=f"Goals {goals}",
                            message=f"Not Done",
                            timeout=10
                        )

                print("!! Checklist Updated !! ")
                print("====================")
                print("     Checklist")
                print("--------------------")
                print(tabulate(goalsArray , headers=goalsHeaders, tablefmt="grid"))
                print()
            elif pilih == "4" :
                break
            else :
                print ("Your Choice Is Invalid. Please Try Again.")

    elif pilih0 == "5" :
        break

    else :
        print("ERROR!!!")
        print("The number you entered is invalid.")
