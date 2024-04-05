import mysql.connector as msql
import datetime
import random
import pandas as pd
from colorama import Fore, Back, Style
import os

base = msql.connect(host='localhost', user='root', password='1012', database='covid_management')
curs = base.cursor()
if base.is_connected():
    print("")
    print(Fore.CYAN + "<", 65 * '-', " WELCOME ADMIN , PLEASE CONFIRM ITS YOU ", 65 * '-', ">")
u = input("USER  ID --> \t")
p = input("PASSWORD --> \t")
curs.execute("select * from admin")
a = curs.fetchall()
log = ''
for i in a:
    if i[0] == u and i[1] == p:
        k = i[0]
        log = True
    else:
        pass
if log == '':
    print(Fore.RED + ">>>Sorry your Password or User ID is incorrect" + Fore.BLUE)
while log == True:
    os.system('cls')
    print(Fore.GREEN + ">>>  Logged in as", k, "<<<<")
    text = r"""
 _______    _______              _________   ______           _______    _______    _          _______    _______    _______    _______    _______    _         _________
(  ____ \  (  ___  )  |\     /|  \__   __/  (  __  \         (       )  (  ___  )  ( (    /|  (  ___  )  (  ____ \  (  ____ \  (       )  (  ____ \  ( (    /|  \__   __/
| (    \/  | (   ) |  | )   ( |     ) (     | (  \  )        | () () |  | (   ) |  |  \  ( |  | (   ) |  | (    \/  | (    \/  | () () |  | (    \/  |  \  ( |     ) (   
| |        | |   | |  | |   | |     | |     | |   ) |        | || || |  | (___) |  |   \ | |  | (___) |  | |        | (__      | || || |  | (__      |   \ | |     | |   
| |        | |   | |  ( (   ) )     | |     | |   | |        | |(_)| |  |  ___  |  | (\ \) |  |  ___  |  | | ____   |  __)     | |(_)| |  |  __)     | (\ \) |     | |   
| |        | |   | |   \ \_/ /      | |     | |   ) |        | |   | |  | (   ) |  | | \   |  | (   ) |  | | \_  )  | (        | |   | |  | (        | | \   |     | |   
| (____/\  | (___) |    \   /    ___) (___  | (__/  )        | )   ( |  | )   ( |  | )  \  |  | )   ( |  | (___) |  | (____/\  | )   ( |  | (____/\  | )  \  |     | |   
(_______/  (_______)     \_/     \_______/  (______/         |/     \|  |/     \|  |/    )_)  |/     \|  (_______)  (_______/  |/     \|  (_______/  |/    )_)     )_(   

    """
    colors = [Fore.RED, Fore.CYAN, Fore.MAGENTA, Fore.GREEN, Fore.BLUE, Fore.BLACK, Fore.BLUE]
    colored_text = [random.choice(colors) + text]
    print(
        Back.BLACK + 176 * " " + Back.RESET)
    print(''.join(colored_text))
    print(
        Back.BLACK + 132 * " " + Back.RESET + Style.BRIGHT + Fore.GREEN + " Developed by - ANTHONIANS " + Back.BLACK + 16 * " " + Back.RESET)
    print("")
    print(random.choice(colors) + ">>>    CHOOSE NUMBER CORRESPONDING TO YOUR NEED TO PROCEED    <<<")
    print("")
    print(Fore.CYAN + "\t 1.  Register a new case .")
    print("\t 2.  Know details about a specific patient .")
    print("\t 3.  Know which bed is allocated to a specific patient .")
    print("\t 4.  Days left for quarantine period to finish.")
    print("\t 5.  Patients whose Quarantine period is over.")
    print("\t 6.  Patients tested today.")
    print(Fore.BLUE + "\t 7.  Precautions to follow to avoid being infected by COVID-19.")
    print("\t 8.  Postcautions to take once infected by this virus.")
    print("\t 9.  Signs and Symptoms of COVID-19.")
    print(Fore.GREEN + "\t 10. List top 10 countries with highest number of cases.")
    print("\t 11. List top 10 countries with highest number of patients recovered .")
    print("\t 12. List top 10 countries with highest number of deaths due to COVID-19.")
    print("\t 13. List top 10 countries with highest number of active cases at present. ")
    print(Fore.BLUE + "\t 14. List all the beds availabe\\occupied.")
    print("\t 15. Know about staff members .")
    print("\t 16. Know about Developers.")
    print("")
    print("")
    print(Fore.RED + "\t\t\t\t\t\t Press Q to exit application")
    print("")
    print("")
    task = input(Fore.MAGENTA + ">>>>  Please Give some Input to Proceed >> ")
    print("")


    def new_case():
        case_id = int(input(Fore.LIGHTBLUE_EX + ">>> Enter case id for the Patient --> "))
        name = input(">>> Enter name of the Patient --> ")
        doa = input(">>> Please specify Date of admitting the patient -->")
        dod = datetime.datetime.strptime(doa, "%Y-%m-%d") + datetime.timedelta(14)
        f_name = input(">>> Enter Father\'s name --> ")
        m_name = input(">>> Enter Mother\'s name --> ")
        city = input(">>> Enter city of the patient -->")
        bed = input(">>> Enter bed id of bed alloated -->")
        curs.execute(
            "insert into cases values ({},'{}','{}','{}','{}','{}','{}','{}')".format(case_id, name, doa, f_name,
                                                                                      m_name,
                                                                                      city, dod, bed))
        base.commit()


    def patient_details():
        print("")
        case_id = int(input(Fore.LIGHTBLUE_EX + ">>> Enter case id for the Patient --> "))
        curs.execute("select * from cases where case_number = {}".format(case_id))
        a = (curs.fetchall())
        name = a[0][1]
        date1 = a[0][2]
        father = a[0][3]
        mother = a[0][4]
        city = a[0][5]
        date2 = a[0][6]
        print(Fore.CYAN + "++ Name of patient with id", case_id, " --\t", name)
        print("++ Date of Admitting the patient --\t", date1)
        print("++ Father\'s name --\t\t\t", father)
        print("++ Mother\'s name --\t\t\t", mother)
        print("++ Current city --\t\t\t", city)
        print("++ Date of Discharging the patient--\t", date2)


    def quarantine_left():
        case_id = int(input(Fore.LIGHTBLUE_EX + ">>> Enter case id for the Patient --> "))
        curs.execute("select date_of_discharge, patient_name from cases where case_number = {}".format(case_id))
        a = curs.fetchall()
        day = a[0][0]
        name = a[0][1]
        print(Fore.CYAN + "++ There are", (day - datetime.date.today()).days, "days left to discharge", name)


    def precautions():
        print("")
        print(Fore.RED + "\"Protect yourself and others around you by taking appropriate precautions.\n"
                         "Follow these advices to prevent the spread of COVID-19:\"")
        print(Fore.MAGENTA + '''
    +++>  Clean your hands often. Use soap and water, or an alcohol-based hand rub.
    +++>  Maintain a safe distance from anyone who is coughing or sneezing.
    +++>  Wear a mask when physical distancing is not possible.
    +++>  Don’t touch your eyes, nose or mouth.
    +++>  Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.
    +++>  Stay home if you feel unwell.
    +++>  If you have a fever, cough and difficulty breathing, seek medical attention.''')


    def postcautions():
        print("")
        print(Fore.RED + "\" Now, once someone had recovered from Covid and got Discharged.\n"
                         "He/she must follow certain measures in order to enjoy a healthy life ahead.\"")
        print(Fore.MAGENTA + '''
    +++>  The first follow-up visit (physical/telephonic) should be within 7 days after discharge, preferably at the hospital where he/she underwent treatment.
    +++>  Subsequent treatment/follow up visits may be with the nearest qualified allopathic/AYUSH practitioner/medical facility of other systems of medicine.
    +++>  Poly-therapy is to be avoided due to potential for unknown drug-drug interaction, which may lead to Serious Adverse Events (SAE) or Adverse Effects (AE).
    +++>  The patients who had undergone home isolation, if they complain of persisting symptoms, will visit the nearest health facility.
    +++>  Severe cases requiring critical care support will require more stringent follow up.''')


    def signs_and_symptoms():
        print("")
        print(
            Fore.RED + "COVID-19 affects different people in different ways. Most infected people will develop mild to moderate illness and recover without hospitalization.")
        print(Fore.MAGENTA + ">>>  Most common symptoms:", Fore.BLUE + '''
              > fever
              > dry cough
              > tiredness''')
        print("")
        print(Fore.MAGENTA + ">>>  Less common symptoms:", Fore.BLUE + '''
              > aches and pains
              > sore throat
              > diarrhoea
              > conjunctivitis
              > headache
              > loss of taste or smell
              > a rash on skin, or discolouration of fingers or toes''')
        print("")
        print(Fore.MAGENTA + ">>>  Serious symptoms:", Fore.BLUE + '''
              > difficulty breathing or shortness of breath
              > chest pain or pressure
              > loss of speech or movement''' + Fore.RESET)


    def bed_count():
        log = input(Fore.LIGHTBLUE_EX + ">>> Enter 'O' to list down occupied beds and 'N' for not occupied --> ")
        print("")
        if log == 'N' or log == 'n':
            print(Fore.CYAN + "+++  List of occupied beds is as follows :-")
        elif log == 'O' or log == 'o':
            print(Fore.CYAN + "+++  List of empty beds is as follows :-")
        query = "select * from beds where Status = '{}';".format(log)
        curs.execute(query)
        a = curs.fetchall()
        for i in a:
            id = i[0]
            bt = i[1]
            room = i[2]
            print("")
            print(Fore.BLUE + "\t > bed id is \t\t : ", id)
            print("\t > bed type is \t\t : ", bt)
            print("\t > bed is in room\t : ", room + Fore.RESET)


    def active_cases_worldwide():
        for i in range(0, 30):
            today = datetime.date.today() - datetime.timedelta(i)
            b = (str(today.month) + '-' + str(today.day) + '-' + str(today.year))
            n = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/' + b + '.csv'
            try:
                covid_data = pd.read_csv(n, usecols=['Last_Update', 'Country_Region', 'Active'])
                result = covid_data.groupby('Country_Region').max().sort_values(by='Active', ascending=False)[:10]
                pd.set_option('display.max_column', None)
                print(Fore.LIGHTBLUE_EX + result)
            except Exception as e:
                print(e)
            else:
                break


    def total_worldwide():
        for i in range(0, 30):
            today = datetime.date.today() - datetime.timedelta(i)
            b = (str(today.month) + '-' + str(today.day) + '-' + str(today.year))
            n = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/' + b + '.csv'
            try:
                covid_data = pd.read_csv(n, usecols=['Last_Update', 'Country_Region', 'Confirmed'])
                result = covid_data.groupby('Country_Region').max().sort_values(by='Confirmed', ascending=False)[:10]
                pd.set_option('display.max_column', None)
                print(result)
            except:
                continue
            else:
                break


    def deaths_worldwide():
        for i in range(0, 30):
            today = datetime.date.today() - datetime.timedelta(i)
            b = (str(today.month) + '-' + str(today.day) + '-' + str(today.year))
            n = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/' + b + '.csv'
            try:
                covid_data = pd.read_csv(n, usecols=['Last_Update', 'Country_Region', 'Deaths'])
                result = covid_data.groupby('Country_Region').max().sort_values(by='Deaths', ascending=False)[:10]
                pd.set_option('display.max_column', None)
                print(result)
            except:
                continue
            else:
                break


    def recovered_worldwide():
        for i in range(0, 30):
            today = datetime.date.today() - datetime.timedelta(i)
            b = (str(today.month) + '-' + str(today.day) + '-' + str(today.year))
            n = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/' + b + '.csv'
            try:
                covid_data = pd.read_csv(n, usecols=['Last_Update', 'Country_Region', 'Recovered'])
                result = covid_data.groupby('Country_Region').max().sort_values(by='Recovered', ascending=False)[:10]
                pd.set_option('display.max_column', None)
                print(result)
            except:
                continue
            else:
                break


    def bed_alloated():
        case_id = int(input(Fore.LIGHTBLUE_EX + ">>> Enter case id for the Patient --> "))
        curs.execute(
            "select beds.bed_id , patient_name , room from cases , beds where case_number = {} and cases.bed_id = beds.bed_id".format(
                case_id))
        a = curs.fetchall()
        bed = a[0][0]
        name = a[0][1]
        room = a[0][2]
        print(Fore.CYAN + "++ Name of patient with id", case_id, " --\t", name)
        print("++ He/She is admitted in room ", room, "on bed number ", bed)


    def quarantine_completed():
        curs.execute(
            "select case_number , patient_name ,date_Of_discharge from cases where date_Of_discharge < '{}'".format(
                datetime.date.today()))
        a = curs.fetchall()
        print(Fore.GREEN + "++ Quarantine Period of following Patients is completed : ")
        for i in a:
            id = i[0]
            name = i[1]
            date2 = i[2]
            print("")
            print(Fore.CYAN + "++ Patient having id ", id, " and named --\t", name)
            print("++ Completed Quarantine period on --\t", date2)


    def tested():
        curs.execute("select * from tested")
        a = curs.fetchall()
        print("")
        print(Fore.CYAN + "LIST  OF  PEOPLE  TESTED  TODAY ---")
        print("")
        for i in a:
            t_no = i[0]
            name = i[1]
            gen = i[2]
            print(Fore.LIGHTGREEN_EX + ">", t_no, ">> Name = ", name, "and gender = ", gen)


    def staff_details():
        print('')
        print(Fore.MAGENTA + ">>>  Details of Staff Members")
        curs.execute("select * from staff_details")
        b = (curs.fetchall())
        for a in b:
            id = a[0]
            name = a[1]
            post = a[2]
            number = a[3]
            print('')
            print(Fore.CYAN + "++ Unique ID -- \t\t", id)
            print("++ Name of staff member --\t", name)
            print("++ His\\her post --\t\t", post)
            print("++ His\\her number --\t\t", number)


    def developers():
        print(Fore.CYAN + "This Application is developed by squad of four Friends :--")
        print(Fore.GREEN + "\t\t Harshit Singh")
        print(Fore.GREEN + "\t\t Shashwat Verma")
        print(Fore.GREEN + "\t\t Jatin Yadav")
        print(Fore.GREEN + "\t\t Faraz Khan")
        print("")


    if task == '1':
        new_case()

    if task == '2':
        patient_details()

    if task == '3':
        bed_alloated()

    if task == '4':
        quarantine_left()

    if task == '5':
        quarantine_completed()

    if task == '6':
        tested()

    if task == '7':
        precautions()

    if task == '8':
        postcautions()

    if task == '9':
        signs_and_symptoms()

    if task == '10':
        total_worldwide()

    if task == '11':
        recovered_worldwide()

    if task == '12':
        deaths_worldwide()

    if task == '13':
        active_cases_worldwide()

    if task == '14':
        bed_count()

    if task == '15':
        staff_details()

    if task == '16':
        developers()

    if task == 'Q':
        print(Fore.RESET + "")
        exit()

    print(Fore.GREEN + "")
    n = input("Press ENTER key to continue ")
