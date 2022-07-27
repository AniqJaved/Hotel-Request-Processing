from collections import defaultdict

reservedRooms = defaultdict(int)

requestPro = []

for i in range(1,31):
    reservedRooms[i] = 15
    
requests = [
    [3, 5, 5],
    [15, 20, 6],
    [25, 28, 6]
]

reservations = [
    [4, 6, 6],
    [15, 20, 10]
]


def reservedRoomsCheck(start,end,rooms):
    for i in range(1,31):
        if i>= start and i<= end:
            if reservedRooms[i] - rooms >= 0:
                reservedRooms[i] = reservedRooms[i] - rooms

def checkRooms(start,end,rooms):
    for i in range(1,31):
        if i>= start and i<= end:
            if reservedRooms[i] - rooms >= 0:
                reservedRooms[i] = reservedRooms[i] - rooms
            else:
                return 0
    return 1

lenReservations = len(reservations)

for i in range(lenReservations):
    start = reservations[i][0]
    end = reservations[i][1]
    rooms = reservations[i][2]
    reservedRoomsCheck(start,end,rooms)
    

lenRequests = len(requests)

for i in range(lenRequests):
    start = requests[i][0]
    end = requests[i][1]
    rooms = requests[i][2]
    a = checkRooms(start,end,rooms)
    requestPro.append(a)
print(requestPro)
    
