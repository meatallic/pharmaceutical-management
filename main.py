import csv
import math
import random
from secrets import *
import datetime
import tabulate


class colors:
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'

    class fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'


mainloopvar = True

with open("MED_LIST.csv", 'r') as csv_file:
    reader = csv.reader(csv_file)
    rows = []

    for rec in reader:
        rows.append(rec)
csv_file.close()

with open("1000 Records (1).csv", 'r') as fi2:
    reader_emp = csv.reader(fi2)
    l_emp = []
    for i in reader_emp:
        l_emp.append(i)


def itemcode():
    digits = [i for i in range(0, 10)]
    random_str = ""
    for i in range(6):
        index = math.floor(random.random() * 10)
        random_str += str(digits[index])
    return random_str


def authentication(username1):
    """

    :return: this will return True if the user passes authentication
    """
    global Admin
    username = username1.upper()
    if username in userlist:
        print(colors.fg.orange, "Enter the password", end=' ')
        password1 = input()
        global Usrname
        Usrname = username

        if password1 == password:
            print("Access Granted!!")
            print(colors.fg.orange, " \n\t\t\t\t\t Welcome to Arsa Pharmacy Management System  \n\n")
            Admin = False
            return True

        elif password1 == stock_pass:
            print("Welcome Creator !!")
            print(colors.fg.orange, " \n\t\t\t\t\t Welcome to Arsa Pharmacy Management System  \n\n")
            Admin = True
            return True


        else:
            print(colors.fg.red, "Incorrect Password")
            Admin = False
            return False
    else:
        print(colors.fg.red, "sorry !!. Your not a verified user")
        return False


def serch_by_name(in_, data1):
    """

    :param in_: The input to be searched
    :param data1: The data where the input should be searched
    :return: A list of numbers which is the Si no of medicines that the input matches with
    :return: A dlist of numbers which is the Si no of medicines that the input matches with
    """
    main_l = []
    l2 = []
    for data in in_:
        l2.append(data.upper())

    for a in data1:
        l1 = []
        for b in a[1]:
            l1.append(b.upper())
        if l2 == l1[:len(l2)]:
            main_l.append(a[0])
    if len(main_l) == 0:
        return False
    else:
        return main_l


def search_by_num(list2):
    list1 = []
    for i in rows:
        if i[0] in list2:
            b1 = [i[0], i[1], i[3]]
            list1.append(b1)
    return list1


def Bill_Item_Search(keyword):
    Resultant_list = []
    keyword_list = []
    for i in keyword:
        keyword_list.append(i.upper())
    for medparticular in rows:
        med_search_list = []
        for medname in medparticular[1]:
            med_search_list.append(medname.upper())
        if keyword_list == med_search_list[:len(keyword_list)]:
            Med_details = medparticular[0], medparticular[1], medparticular[3], medparticular[5]
            Resultant_list.append(Med_details)
    if len(Resultant_list) >= 1:
        return Resultant_list
    else:
        return print(colors.fg.red, " ", " ", " ", " ")


def main():
    mainloopvar1 = True
    global Name_Or_Id
    print(colors.fg.orange, "Enter your registered name:", end=' ')
    username1 = input()
    Entry = authentication(username1)

    while mainloopvar1:
        if Entry:
            print(colors.fg.black,
                  '''\n\n1.\tSearch For Medicines\n2.\tCreate Bill\nsai3.\tAdd to stock\n4.\tEmployee Pharmasist Attendence\n5.\tView stocks\n6.\tSearch Employee in the Company\n7.\tAdd Employee\n8.\tExit\n''')
            print(colors.fg.blue, "Enter The Option:", end=" ")
            Option = int(input())
            if Option == 1:
                print(colors.fg.blue, "\nEnter the Keyword to search:", end=' ')
                a = input()
                op1_list = serch_by_name(a, rows)
                if op1_list is False:
                    print(colors.fg.red, "\nCurrently there is no Medicine that matches keyword {}".format(a))
                else:
                    else_out = search_by_num(op1_list)
                    print(colors.fg.black, "\nThe following Medicines meet the keyword")
                    out_list = [["Si No", "MED Name"]]
                    for i in else_out:
                        out_list.append([i[0], i[1]])
                    print(tabulate.tabulate(out_list))
            elif Option == 2:
                i = True
                Main_bill = []
                while i:
                    print(colors.fg.blue, "\nEnter The Keyword To Search", end=' ')
                    Keyword = input()
                    if Keyword.upper() != "EXIT":

                        keywordsearch = Bill_Item_Search(Keyword)
                        try:
                            format_string = "{:4} {:49} {:10}"
                            headers = ["Si No", "Med Name", "Mrp"]
                            header_row = format_string.format(*headers)
                            print(header_row)
                            print("-" * len(header_row))
                            for langauge in keywordsearch:
                                print(format_string.format(*langauge))
                            print("")
                            print(colors.fg.blue, "\nEnter The Medicine Code", end=' ')
                            Med_Number = int(input())
                            print(colors.fg.blue, "\nEnter The Quantity Required", end=' ')
                            Quantity = int(input())
                            values = [Med_Number, Quantity]
                            Main_bill.append(values)
                        except TypeError or IndexError:
                            print(colors.fg.red, "There are no medicines that meet the keyword")



                    else:
                        i = False
                if i == False:
                    print(colors.fg.orange, "\nDo you Want to Give any discount", end=' ')
                    Discount = input()
                    if Discount.upper() == "YES":
                        print(colors.fg.blue, "\nEnter the Discount Percentage", end=' ')
                        Discount_Percent = float(input())
                    else:
                        Discount_Percent = 0.0
                    print(colors.fg.blue, "\nDo You Want To Add 'Batch' No And 'Exp Date' To The Bill:", end=' ')
                    esp_tally = input()
                    if esp_tally.upper() == "YES":
                        Bill1list = [
                            ["SiNo", "Item Code", "particulars", "QTY", "MRP", "Discount%", "Batchno", "Exp date",
                             "Gst Amound", "Total"]]
                    else:
                        Bill1list = [["SiNo", "Item Code", "particulars", "QTY", "MRP", "Discount%",
                                      "Gst Amound", "Total"]]

                    for Variable in rows:
                        for Variable1 in Main_bill:
                            if int(Variable[0]) == Variable1[0]:
                                Itemcode = itemcode()
                                Si_no = int(Variable1[0])
                                Particulars = Variable[1]
                                Quty = int(Variable1[1])
                                Mrp = (float(Variable[3][1:]))
                                Batch = Variable[6]
                                Expdate = Variable[5]
                                Gstamd = float(Variable[7][:2]) * Quty
                                total = Mrp * Quty + (Mrp * Gstamd) / 100 - (Mrp * Discount_Percent) / 100
                                if esp_tally.upper() == 'YES':
                                    Input = [Si_no, Itemcode
                                        , Particulars, Quty, Mrp, Discount_Percent, Batch, Expdate,
                                             (Mrp * Gstamd) / 100,
                                             total]
                                    Bill1list.append(Input)


                                else:
                                    Input = [Si_no, Itemcode
                                        , Particulars, Quty, Mrp, Discount_Percent, (Mrp * Gstamd) / 100, total]
                                    Bill1list.append(Input)

                    print(colors.fg.black, tabulate.tabulate(Bill1list))



            elif Option == 3:
                if Admin:
                    print(colors.fg.black, "How Many New Medicines Do You Want To Add", end=' ')
                    medaddition_count = int(input())
                    for i in range(medaddition_count):
                        medname = input("medname")
                        lofmed = []
                        a = False
                        for i in medname:
                            lofmed.append(i.upper())
                        for i in rows:
                            l12 = []
                            for j in i[1]:
                                l12.append(j.upper())
                            if l12[:len(medname)] == lofmed:
                                a = True
                        if a:
                            print(colors.fg.red,
                                  "Sorry!!! You Cant Add This Medicine,This Medicine Is allready Present in the data")
                            b = False
                        else:
                            b = True
                        if b:
                            print(colors.fg.blue, "Enter The Form Of {}:".format(medname), end=' ')
                            med_form = input()
                            print(colors.fg.blue, "Enter The Price Of {} :".format(medname), end=' ')
                            med_price = input()
                            print(colors.fg.blue,
                                  "How Many Quantity Of {} Do Ypu Want To Add in Stock:".format(medname),
                                  end=' ')
                            med_stock = input()
                            print(colors.fg.blue, "Enter The Experiy Date Of {} Seprated By '\':".format(medname),
                                  end=' ')
                            med_exp = input()
                            print(colors.fg.blue, "Enter The Batch Id Of {} :".format(medname), end=' ')
                            med_batch = input()
                            print(colors.fg.blue, "Enter The GST % of {}:".format(medname), end=' ')
                            gst_ = input()
                            print(colors.fg.red, "Do You Want To Commit The Changes(YES,NO):", end=' ')
                            ask_user = input()
                            rowno = int(rows[-1][0]) + 1
                            in_1 = [rowno, medname, med_form, med_price, med_stock, med_exp, med_batch, gst_]
                            if ask_user.upper() == "YES":
                                with open('MED_LIST.csv', 'a') as file:
                                    writer = csv.writer(file, delimiter=',')
                                    writer.writerow(in_1)
                                print(colors.fg.green, "Process Sussecfull")
                            else:
                                print(colors.fg.red, "The User CAncel The Process")
                        else:
                            continue



                else:
                    print(colors.fg.red, "Sorry!! Permission Denied,You Need To Be Admin To Avail This Feature")





            elif Option == 4:
                usrpass = 0
                print(colors.fg.pink, "The current user is {}\n".format(Usrname))
                print(colors.fg.pink, "Do You Want To Use The Same Username:", end=' ')
                ask_user = input()
                A1 = False
                if ask_user.upper() == "NO":
                    print(colors.fg.pink, "Enter Your Name Or Id", end=' ')
                    Name_Or_Id = input()
                    try:
                        Name_Or_Id = int(Name_Or_Id)
                    except ValueError:
                        Name_Or_Id = str(Name_Or_Id)
                    if type(Name_Or_Id) == int:
                        for Namelist in Pharmasist_list:
                            if Namelist[1] == Name_Or_Id:
                                usr = Namelist[0]
                                usrid = Namelist[1]
                                usrpass = Namelist[2]
                                A1 = True
                            else:
                                print(colors.fg.red, "Attedence Denied!! \n Ivalid Userid")
                                A1 = False

                    elif type(Name_Or_Id) == str:
                        for Namelist in Pharmasist_list:
                            if Namelist[0].upper() == Name_Or_Id.upper():
                                usr = Namelist[0]
                                usrid = Namelist[1]
                                usrpass = Namelist[2]
                                A1 = True
                            else:
                                print(colors.fg.red, "Attedence Denied!! \n Ivalid Username")
                                A1 = False
                elif ask_user.upper() == 'YES':
                    usr = Usrname
                    for Namelist in name_pass:
                        if Namelist[0].upper() == usr.upper():
                            usrid = Namelist[0]
                            usrpass = Namelist[2]
                            print(usr, usrid, usrpass)
                            A1 = True
                if A1:
                    today = datetime.date.today()
                    month = today.month
                    month_name = months[month - 1]
                    year = today.year
                    day = today.day
                    print(colors.fg.orange, "Plaese Enter The User Password", end=' ')
                    pass1 = input()
                    if pass1 == usrpass:
                        with open("Attendence.txt", 'a') as file:
                            string = "\n{} was Present At {} {} {}".format(usrid, day, month_name, year)
                            file.write(string)
                            file.close()
                        print(colors.fg.green,
                              "You Attendence Have Been Marked for {} {} {}".format(day, month_name, year))
                    else:
                        print(colors.fg.red, " Attendence Denied\n The Password You have Entered is Incorrect")
            elif Option == 5:
                print('.')
                with open('MED_LIST.csv', 'r', encoding="utf-8") as fileeeee:
                    reader2 = csv.reader(fileeeee)
                    lt1 = []
                    for i in reader2:
                        lt1.append(i)

                    innerloopvar = True
                    while innerloopvar:
                        searchword = int(input("Enter the Sino of medicine"))
                        for variable3 in lt1:
                            if int(variable3[0]) == searchword:
                                print("currently we have ", variable3[4],
                                      " units of the medicine' {}'".format(variable3[1]))
                        ask_user2 = input("\nDo you want to check Stock of another medicine[Yes,No]:")
                        if ask_user2.upper() == 'YES':
                            innerloopvar = True
                        else:
                            innerloopvar = False
                input("Press Enter to continue")
            elif Option == 6:

                if Admin:
                    emp_id = input("enter the empoloye id")
                    for variable in l_emp:
                        if variable[0] == emp_id:
                            L12 = [
                                ["\nEmp ID :\t                 ", variable[0]],
                                ["\nName Prefix :\t            ", variable[1]],
                                ["\nFirst Name :\t            ", variable[2]],
                                ["\nLast Name :\t              ", variable[4]],
                                ["\nGender :\t                 ", variable[5]],
                                ["\nE Mail :\t                 ", variable[6]],
                                ["\nFather's Name :\t          ", variable[7]],
                                ["\nMother's Name :\t          ", variable[8]],
                                ["\nDate of Birth :\t          ", variable[10]],
                                ["\nAge in Yrs. :\t            ", variable[11]],
                                ["\nDate of Joining :\t        ", variable[12]],
                                ["\nYear of Joining :\t        ", variable[13]],
                                ["\nAge in Company (Years) :\t ", variable[14]],
                                ["\nSalary :\t                 ", variable[15]],
                                ["\nSalary% Hike :\t           ", variable[16]],
                                ["\nPhone No. :\t             ", variable[17]],
                                ["\nPlace Name :\t             ", variable[18]],
                                ["\nCounty :\t                 ", variable[19]],
                                ["\nCity :\t                   ", variable[20]],
                                ["\nState :\t                  ", variable[21]],
                                ["\nUser Name :\t              ", variable[22]],
                                ["\nPassword :\t               ", variable[23]]]
                            print(variable
                                  )
                        else:
                            L12 = ["There is No user with this id please refer to option 7 for adding emp"]
                    print(tabulate.tabulate(L12))


                else:
                    print(" please login as admin for this feature")


            elif Option == 7:
                if Admin:
                    EmpID = int(input("Enter the EmployeeID"))

                    Prefix = input("Enter The name prefix")
                    FirstName = input("Enter the First Name of Employee")
                    LastName = input("Enter the Last Name of Employee")
                    print("Enter The Gender of {}.{} ".format(Prefix,FirstName),end=' ')
                    Gender = input()
                    print("Enter The Email ID of {}.{} ".format(Prefix, FirstName), end=' ')
                    EMail = input()
                    print("Enter The Fathers Name of {}.{} ".format(Prefix, FirstName), end=' ')
                    FathersName = input()
                    print("Enter The Mothers's Name of {}.{} ".format(Prefix, FirstName), end=' ')
                    MothersName = input()
                    print("Enter The DOB of {}.{} ".format(Prefix, FirstName), end=' ')
                    DateofBirth = input()
                    print("Enter The Age in years of {}.{} ".format(Prefix, FirstName), end=' ')
                    AgeinYrs = input()
                    print("Enter The Date of joining(Seprated with  '-') of {}.{} ".format(Prefix, FirstName), end=' ')
                    DateoJoining = input()
                    print("Enter The Year of Joining of {}.{} ".format(Prefix, FirstName), end=' ')
                    YearofJoining = input()
                    print("Enter The Age in company(in years) of {}.{} ".format(Prefix, FirstName), end=' ')
                    AgeinCompany = input()
                    print("Enter The Salary of {}.{} ".format(Prefix, FirstName), end=' ')
                    Salary = float(input("Enter the salary"))
                    print("Enter The Salary hike Percent of {}.{} ".format(Prefix, FirstName), end=' ')
                    SalaryHike = input()
                    print("Enter ThePhone number of {}.{} ".format(Prefix, FirstName), end=' ')
                    Phone = input()
                    print("Enter The Place of {}.{} ".format(Prefix, FirstName), end=' ')
                    Place = input()
                    print("Enter The Country of {}.{} ".format(Prefix, FirstName), end=' ')
                    County = input()
                    print("Enter The city of {}.{} ".format(Prefix, FirstName), end=' ')
                    City = input()
                    print("Enter The State of {}.{} ".format(Prefix, FirstName), end=' ')
                    State = input()
                    print("Enter The UserName of {}.{} ".format(Prefix, FirstName), end=' ')
                    UserName = input()
                    print("Enter The Password of {}.{} ".format(Prefix, FirstName), end=' ')
                    Password = input()
                    blankvalue = ' '
                    in_2 = [EmpID, Prefix, FirstName, blankvalue, LastName, Gender, EMail, FathersName,
                            MothersName, blankvalue, DateofBirth, AgeinYrs, DateoJoining, YearofJoining,
                            AgeinCompany, Salary, SalaryHike, Phone, Place, County, City, State, UserName, Password]
                    print(colors.fg.red, "Do You Want To Commit The Changes(YES,NO):", end=' ')
                    ask_user1 = input()
                    if ask_user1.upper() == "YES":
                        with open('1000 Records (1).csv', 'a') as file:
                            writer = csv.writer(file, delimiter=',')
                            writer.writerow(in_2)
                        print(colors.fg.green, "Process Sussecfull")
                    else:
                        print(colors.fg.red, "The User CAnceled The Process")


                else:
                    print("You should have admin rights to avail this feature")

            elif Option == 8:

                mainloopvar1 = False

        else:
            mainloopvar1 = False


if __name__ == '__main__':
    main()
