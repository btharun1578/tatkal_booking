class Tatkal_Ticket_booking:
    def __init__(self,coaches="unknown"):
        self.coaches={"coach1":self.coach1,
        "coach2":self.coach2
        }
        self.tatkal_price=450
        self.general_price=375
        self.premium_price=450
        self.current_price=0
        self.lines_available={"GEN":{1:0,2:0,3:0,4:0,5:0},
                              "PRE":{1:0,2:0,3:0,4:0,5:0},
                              "TAT":{1:0,2:0,3:0,4:0,5:0}}
        self.recent_bookings={}
        


    coach1=[[{'name': 'Amelia', 'seat': 1, 'berth': 'LB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Ethan', 'seat': 2, 'berth': 'MB', 'category': 'GEN', 'status': 'Filled'}, {'name': '', 'seat': 3, 'berth': 'UB', 'category': 'PRE', 'status': 'empty'}, {'name': '', 'seat': 4, 'berth': 'LB', 'category': 'PRE', 'status': 'empty'}, {'name': 'Olivia', 'seat': 5, 'berth': 'MB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Liam', 'seat': 6, 'berth': 'UB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Ava', 'seat': 7, 'berth': 'SL', 'category': 'GEN', 'status': 'Filled'}, {'name': '', 'seat': 8, 'berth': 'SU', 'category': 'PRE', 'status': 'empty'}], [{'name': '', 'seat': 9, 'berth': 'LB', 'category': 'TAT', 'status': 'empty'}, {'name': 'panchami', 'seat': 10, 'berth': 'MB', 'category': 'GEN', 'status': 'Filled'}, {'name': '', 'seat': 11, 'berth': 'UB', 'category': 'TAT', 'status': 'empty'}, {'name': '', 'seat': 12, 'berth': 'LB', 'category': 'TAT', 'status': 'empty'}, {'name': '', 'seat': 13, 'berth': 'MB', 'category': 'TAT', 'status': 'empty'}, {'name': 'pashupati', 'seat': 14, 'berth': 'UB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Arun', 'seat': 15, 'berth': 'SL', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Rani', 'seat': 16, 'berth': 'SU', 'category': 'GEN', 'status': 'Filled'}], [{'name': 'Sriram', 'seat': 17, 'berth': 'LB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Rajesh', 'seat': 18, 'berth': 'MB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Rohit', 'seat': 19, 'berth': 'UB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Sharath', 'seat': 20, 'berth': 'LB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Raju', 'seat': 21, 'berth': 'MB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Sreenu', 'seat': 22, 'berth': 'UB', 'category': 'GEN', 'status': 'Filled'}, {'name': '', 'seat': 23, 'berth': 'SL', 'category': 'TAT', 'status': 'empty'}, {'name': 'surya', 'seat': 24, 'berth': 'SU', 'category': 'GEN', 'status': 'Filled'}], [{'name': 'Roja', 'seat': 25, 'berth': 'LB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Netro', 'seat': 26, 'berth': 'MB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Simbhu', 'seat': 27, 'berth': 'UB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'sreeja', 'seat': 28, 'berth': 'LB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Rahim', 'seat': 29, 'berth': 'MB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'babu', 'seat': 30, 'berth': 'UB', 'category': 'GEN', 'status': 'Filled'}, {'name': '', 'seat': 31, 'berth': 'SL', 'category': 'TAT', 'status': 'empty'}, {'name': '', 'seat': 32, 'berth': 'SU', 'category': 'TAT', 'status': 'empty'}], [{'name': '', 'seat': 33, 'berth': 'LB', 'category': 'TAT', 'status': 'empty'}, {'name': 'Kokila', 'seat': 34, 'berth': 'MB', 'category': 'GEN', 'status': 'Filled'}, {'name': '', 'seat': 35, 'berth': 'UB', 'category': 'TAT', 'status': 'empty'}, {'name': 'kaveri', 'seat': 36, 'berth': 'LB', 'category': 'GEN', 'status': 'Filled'}, {'name': '', 'seat': 37, 'berth': 'MB', 'category': 'TAT', 'status': 'empty'}, {'name': 'Kumar', 'seat': 38, 'berth': 'UB', 'category': 'GEN', 'status': 'Filled'}, {'name': '', 'seat': 39, 'berth': 'SL', 'category': 'TAT', 'status': 'empty'}, {'name': 'Karna', 'seat': 40, 'berth': 'SU', 'category': 'GEN', 'status': 'Filled'}], [{'name': 'Santhosh', 'seat': 41, 'berth': 'LB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Bhavi', 'seat': 42, 'berth': 'MB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Chandramuki', 'seat': 43, 'berth': 'UB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Kanchana', 'seat': 44, 'berth': 'LB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Alex', 'seat': 45, 'berth': 'MB', 'category': 'GEN', 'status': 'Filled'}, {'name': '', 'seat': 46, 'berth': 'UB', 'category': 'GEN', 'status': 'empty'}, {'name': '', 'seat': 47, 'berth': 'SL', 'category': 'GEN', 'status': 'empty'}, {'name': 'Ganga', 'seat': 48, 'berth': 'SU', 'category': 'GEN', 'status': 'Filled'}], [{'name': 'Roopesh', 'seat': 49, 'berth': 'LB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Mitra', 'seat': 50, 'berth': 'MB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Raja', 'seat': 51, 'berth': 'UB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Chandra', 'seat': 52, 'berth': 'LB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Ramu', 'seat': 53, 'berth': 'MB', 'category': 'GEN', 'status': 'Filled'}, {'name': '', 'seat': 54, 'berth': 'UB', 'category': 'GEN', 'status': 'empty'}, {'name': '', 'seat': 55, 'berth': 'SL', 'category': 'GEN', 'status': 'empty'}, {'name': '', 'seat': 56, 'berth': 'SU', 'category': 'GEN', 'status': 'empty'}], [{'name': 'Ramesh', 'seat': 57, 'berth': 'LB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Villu', 'seat': 58, 'berth': 'MB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Raju', 'seat': 59, 'berth': 'UB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Koti', 'seat': 60, 'berth': 'LB', 'category': 'GEN', 'status': 'Filled'}, {'name': '', 'seat': 61, 'berth': 'MB', 'category': 'TAT', 'status': 'empty'}, {'name': 'Srikanth', 'seat': 62, 'berth': 'UB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Kranti', 'seat': 63, 'berth': 'SL', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Bhai', 'seat': 64, 'berth': 'SU', 'category': 'GEN', 'status': 'Filled'}], [{'name': 'Tharun', 'seat': 65, 'berth': 'LB', 'category': 'GEN', 'status': 'Filled'}, {'name': '', 'seat': 66, 'berth': 'MB', 'category': 'PRE', 'status': 'empty'}, {'name': '', 'seat': 67, 'berth': 'UB', 'category': 'PRE', 'status': 'empty'}, {'name': 'Kamesh', 'seat': 68, 'berth': 'LB', 'category': 'GEN', 'status': 'Filled'}, {'name': '', 'seat': 69, 'berth': 'MB', 'category': 'PRE', 'status': 'empty'}, {'name': '', 'seat': 70, 'berth': 'UB', 'category': 'PRE', 'status': 'empty'}, {'name': 'Priya', 'seat': 71, 'berth': 'SL', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Naresh', 'seat': 72, 'berth': 'SU', 'category': 'GEN', 'status': 'Filled'}], [{'name': 'Sridhar', 'seat': 73, 'berth': 'LB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Chandhu', 'seat': 74, 'berth': 'MB', 'category': 'GEN', 'status': 'Filled'}, {'name': '', 'seat': 75, 'berth': 'UB', 'category': 'PRE', 'status': 'empty'}, {'name': '', 'seat': 76, 'berth': 'LB', 'category': 'PRE', 'status': 'empty'}, {'name': '', 'seat': 77, 'berth': 'MB', 'category': 'PRE', 'status': 'empty'}, {'name': 'Siri', 'seat': 78, 'berth': 'UB', 'category': 'GEN', 'status': 'Filled'}, {'name': '', 'seat': 79, 'berth': 'SL', 'category': 'PRE', 'status': 'empty'}, {'name': '', 'seat': 80, 'berth': 'SU', 'category': 'PRE', 'status': 'empty'}]]
    coach2=[[{'name': 'Amelia', 'seat': 1, 'berth': 'LB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Ethan', 'seat': 2, 'berth': 'MB', 'category': 'GEN', 'status': 'Filled'}, {'name': '', 'seat': 3, 'berth': 'UB', 'category': 'PRE', 'status': 'empty'}, {'name': '', 'seat': 4, 'berth': 'LB', 'category': 'PRE', 'status': 'empty'}, {'name': 'Olivia', 'seat': 5, 'berth': 'MB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Liam', 'seat': 6, 'berth': 'UB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Ava', 'seat': 7, 'berth': 'SL', 'category': 'GEN', 'status': 'Filled'}, {'name': '', 'seat': 8, 'berth': 'SU', 'category': 'PRE', 'status': 'empty'}], [{'name': '', 'seat': 9, 'berth': 'LB', 'category': 'TAT', 'status': 'empty'}, {'name': 'panchami', 'seat': 10, 'berth': 'MB', 'category': 'GEN', 'status': 'Filled'}, {'name': '', 'seat': 11, 'berth': 'UB', 'category': 'TAT', 'status': 'empty'}, {'name': '', 'seat': 12, 'berth': 'LB', 'category': 'TAT', 'status': 'empty'}, {'name': '', 'seat': 13, 'berth': 'MB', 'category': 'TAT', 'status': 'empty'}, {'name': 'pashupati', 'seat': 14, 'berth': 'UB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Arun', 'seat': 15, 'berth': 'SL', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Rani', 'seat': 16, 'berth': 'SU', 'category': 'GEN', 'status': 'Filled'}], [{'name': 'Sriram', 'seat': 17, 'berth': 'LB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Rajesh', 'seat': 18, 'berth': 'MB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Rohit', 'seat': 19, 'berth': 'UB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Sharath', 'seat': 20, 'berth': 'LB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Raju', 'seat': 21, 'berth': 'MB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Sreenu', 'seat': 22, 'berth': 'UB', 'category': 'GEN', 'status': 'Filled'}, {'name': '', 'seat': 23, 'berth': 'SL', 'category': 'TAT', 'status': 'empty'}, {'name': 'surya', 'seat': 24, 'berth': 'SU', 'category': 'GEN', 'status': 'Filled'}], [{'name': 'Roja', 'seat': 25, 'berth': 'LB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Netro', 'seat': 26, 'berth': 'MB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Simbhu', 'seat': 27, 'berth': 'UB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'sreeja', 'seat': 28, 'berth': 'LB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Rahim', 'seat': 29, 'berth': 'MB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'babu', 'seat': 30, 'berth': 'UB', 'category': 'GEN', 'status': 'Filled'}, {'name': '', 'seat': 31, 'berth': 'SL', 'category': 'TAT', 'status': 'empty'}, {'name': '', 'seat': 32, 'berth': 'SU', 'category': 'TAT', 'status': 'empty'}], [{'name': '', 'seat': 33, 'berth': 'LB', 'category': 'TAT', 'status': 'empty'}, {'name': 'Kokila', 'seat': 34, 'berth': 'MB', 'category': 'GEN', 'status': 'Filled'}, {'name': '', 'seat': 35, 'berth': 'UB', 'category': 'TAT', 'status': 'empty'}, {'name': 'kaveri', 'seat': 36, 'berth': 'LB', 'category': 'GEN', 'status': 'Filled'}, {'name': '', 'seat': 37, 'berth': 'MB', 'category': 'TAT', 'status': 'empty'}, {'name': 'Kumar', 'seat': 38, 'berth': 'UB', 'category': 'GEN', 'status': 'Filled'}, {'name': '', 'seat': 39, 'berth': 'SL', 'category': 'TAT', 'status': 'empty'}, {'name': 'Karna', 'seat': 40, 'berth': 'SU', 'category': 'GEN', 'status': 'Filled'}], [{'name': 'Santhosh', 'seat': 41, 'berth': 'LB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Bhavi', 'seat': 42, 'berth': 'MB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Chandramuki', 'seat': 43, 'berth': 'UB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Kanchana', 'seat': 44, 'berth': 'LB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Alex', 'seat': 45, 'berth': 'MB', 'category': 'GEN', 'status': 'Filled'}, {'name': '', 'seat': 46, 'berth': 'UB', 'category': 'GEN', 'status': 'empty'}, {'name': '', 'seat': 47, 'berth': 'SL', 'category': 'GEN', 'status': 'empty'}, {'name': 'Ganga', 'seat': 48, 'berth': 'SU', 'category': 'GEN', 'status': 'Filled'}], [{'name': 'Roopesh', 'seat': 49, 'berth': 'LB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Mitra', 'seat': 50, 'berth': 'MB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Raja', 'seat': 51, 'berth': 'UB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Chandra', 'seat': 52, 'berth': 'LB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Ramu', 'seat': 53, 'berth': 'MB', 'category': 'GEN', 'status': 'Filled'}, {'name': '', 'seat': 54, 'berth': 'UB', 'category': 'GEN', 'status': 'empty'}, {'name': '', 'seat': 55, 'berth': 'SL', 'category': 'GEN', 'status': 'empty'}, {'name': '', 'seat': 56, 'berth': 'SU', 'category': 'GEN', 'status': 'empty'}], [{'name': 'Ramesh', 'seat': 57, 'berth': 'LB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Villu', 'seat': 58, 'berth': 'MB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Raju', 'seat': 59, 'berth': 'UB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Koti', 'seat': 60, 'berth': 'LB', 'category': 'GEN', 'status': 'Filled'}, {'name': '', 'seat': 61, 'berth': 'MB', 'category': 'TAT', 'status': 'empty'}, {'name': 'Srikanth', 'seat': 62, 'berth': 'UB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Kranti', 'seat': 63, 'berth': 'SL', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Bhai', 'seat': 64, 'berth': 'SU', 'category': 'GEN', 'status': 'Filled'}], [{'name': 'Tharun', 'seat': 65, 'berth': 'LB', 'category': 'GEN', 'status': 'Filled'}, {'name': '', 'seat': 66, 'berth': 'MB', 'category': 'PRE', 'status': 'empty'}, {'name': '', 'seat': 67, 'berth': 'UB', 'category': 'PRE', 'status': 'empty'}, {'name': 'Kamesh', 'seat': 68, 'berth': 'LB', 'category': 'GEN', 'status': 'Filled'}, {'name': '', 'seat': 69, 'berth': 'MB', 'category': 'PRE', 'status': 'empty'}, {'name': '', 'seat': 70, 'berth': 'UB', 'category': 'PRE', 'status': 'empty'}, {'name': 'Priya', 'seat': 71, 'berth': 'SL', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Naresh', 'seat': 72, 'berth': 'SU', 'category': 'GEN', 'status': 'Filled'}], [{'name': 'Sridhar', 'seat': 73, 'berth': 'LB', 'category': 'GEN', 'status': 'Filled'}, {'name': 'Chandhu', 'seat': 74, 'berth': 'MB', 'category': 'GEN', 'status': 'Filled'}, {'name': '', 'seat': 75, 'berth': 'UB', 'category': 'PRE', 'status': 'empty'}, {'name': '', 'seat': 76, 'berth': 'LB', 'category': 'PRE', 'status': 'empty'}, {'name': '', 'seat': 77, 'berth': 'MB', 'category': 'PRE', 'status': 'empty'}, {'name': 'Siri', 'seat': 78, 'berth': 'UB', 'category': 'GEN', 'status': 'Filled'}, {'name': '', 'seat': 79, 'berth': 'SL', 'category': 'PRE', 'status': 'empty'}, {'name': '', 'seat': 80, 'berth': 'SU', 'category': 'PRE', 'status': 'empty'}]]
    def create_coach(self):
        seat=1
        x=[]
        for i in range(10):
            y=[]
            for j in range(8):
                dicta={}
                if(j==0 or j==3):
                    dicta["name"]=""
                    dicta["seat"]=seat
                    dicta["berth"]="LB"
                    dicta["category"]="GEN"
                    dicta["status"]="empty"
                    seat=seat+1
                elif(j==1 or j==4):
                    dicta["name"]=""
                    dicta["seat"]=seat
                    dicta["berth"]="MB"
                    dicta["category"]="GEN"
                    dicta["status"]="empty"
                    seat=seat+1
                elif(j==2 or j==5):
                    dicta["name"]=""
                    dicta["seat"]=seat
                    dicta["berth"]="UB"
                    dicta["category"]="GEN"
                    dicta["status"]="empty"
                    seat=seat+1
                elif(j==6):
                    dicta["name"]=""
                    dicta["seat"]=seat
                    dicta["berth"]="SL"
                    dicta["category"]="GEN"
                    dicta["status"]="empty"
                    seat=seat+1
                else:
                    dicta["name"]=""
                    dicta["seat"]=seat
                    dicta["berth"]="SU"
                    dicta["category"]="GEN"
                    dicta["status"]="empty"
                    seat=seat+1
                y.append(dicta)
            x.append(y)
        #print(x)
    
    def check_availability(self,seat_type):
        self.available=0
        self.seat_type=seat_type
        self.lines_available={"GEN":{1:0,2:0,3:0,4:0,5:0},
                              "PRE":{1:0,2:0,3:0,4:0,5:0},
                              "TAT":{1:0,2:0,3:0,4:0,5:0}}
        #print(self.coaches["coach1"])
        for i in self.coaches:
            coach=self.coaches[i]
            for line in coach:
                count=0
                for seat in line:
                    if(seat["status"]=="empty" and seat["category"]==self.seat_type):
                        self.available+=1
                        count+=1
                if count in self.lines_available[self.seat_type]:
                    self.lines_available[self.seat_type][count] += 1

        print(self.lines_available)
        self.prices={
            "PRE":self.premium_price,
            "TAT":self.tatkal_price,
            "GEN":self.general_price
        }
        self.current_price=self.prices[self.seat_type]
        return f"{self.available} seats Availabity with fare per seat is Rs:{self.current_price}"
            
class User(Tatkal_Ticket_booking):
    def __init__(self):
        super().__init__()

    def review_journey(self,user,names,category):
        passengers=len(names)
        if(user not in self.recent_bookings):
            self.recent_bookings[user]=[]
        print(self.recent_bookings)
        print(self.check_availability(category))
        print(f"{names} {category} Price:{self.prices[category]*len(names)}")
        self.confirmation=input("Are you OK with the details.To Proceed Enter 'Y' to Reject Enter 'N':")
        if(self.confirmation.lower()=="y"):
            print("Booking Started....")
            paid=input("Please pay the amount for the Journey 'P' for Paid and 'D' for decline:")
            if(paid.lower()=="p"):
                print("Transaction Successfull...Please wait for the Confirmation")
                if(passengers<self.available):
                    self.selecting_same_seat(user,names,category)

                else:
                    print("No sufficient Tickets...Sorry for inconvience")

            else:
                print("Transaction Dropped...Ticket Failed ")
        else:
            print("Booking Failed!!!...Sorry for the inconvience")
            return "Booking Failed!!!...Sorry for the inconvience"
        
    def selecting_same_seat(self,user,names,category):
        length=len(names)
        lines_available=self.lines_available[category]
        same_line=False
        for i in lines_available:
            if i>=length:
                if(lines_available[i]>0):
                    same_line=True
                    
                    print("U are getting same line")
                    break
        if(same_line==False):
            print("YOU ARE GETTING SEATS IN DIFFERENT POSITIONS")
            final_accept=input("Enter if 'Y' you are Ok and 'N' for No:")
            print(final_accept)
        
              
        


        

    


#Implementing the code 
#venkatadri=Tatkal_Ticket_booking()
#For Checking Availability you should compulsory have to mention the Type
# Premium Tickets="PRE"  or General Tickets="GEN" and Tatkal Tickets="TAT"
#General =10   Premium=24  Tatkal=24
#print(venkatadri.check_availability("GEN"))

user1=User()

print(user1.check_availability("GEN"))
print(user1.check_availability("PRE"))
print(user1.check_availability("TAT"))


user1.review_journey("user1",["Tharun","Suri","Tharun","Suri","Tharun","Suri"],"GEN")




