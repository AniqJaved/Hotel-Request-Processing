# Hotel-Request-Processing

A hotel management team decided to launch an online room booking system. Users can visit their website and book rooms in advance. When booking, the user must specify the start and end date, as well as the number of rooms to book. If the requested rooms are available for reservation for the period specified by the user, the system will accept the reservation request otherwise the request will be rejected. If the system receives more than one reservation request, the requests should be processed in order of arrival time, that is, the request that arrived first should be processed first.
Implement a function processRequests(reservations, requests, totalRooms) that, given the approved reservations, reservation requests and total rooms, returns an array of same length as requests. For each reservation request, populate the resultant array with 1 if the reservation is accepted else insert 0. The details of the input arguments is given below:

reservations:
2d array, containing all approved reservations. The structure of the array is as follows:

[
  [start, end, quantity],
  [start, end, quantity]
  ....
]

requests:
2d array, containing all reservation requests. The structure of the array is as follows:

[
  [start, end, quantity],
  [start, end, quantity]
  ....
]


totalRooms: Total rooms in the hotel (integer)

start: Day of month, 1 to 30 (integer)

end: Day of month, 1 to 30 (integer)

quantity: Number of rooms requested (integer)


Assume that all reservations have reached within one month, and all rooms have the same capacity. The order of the reservation requests is also kept relative to the arrival time, so the zero index request is the oldest request in requests array.
Note: While processing a request, you must consider previously approved requests, check example 2 for detail.

Example 1:

reservations:

{
  {04, 06, 02},
  {15, 20, 10}
}

requests:

{
  {03, 05, 05},
  {15, 20, 06},
  {25, 28, 06}
}


totalRooms: 15


Resultant Array -> {1, 0, 1}


Explanation:
In above example, total rooms available in the hotel are 15. Two reservations are already approved, i.e, initially two rooms are booked from 4 to 6 and 10 rooms are booked from 15 to 20.

request 1: {03, 05, 05}
A user requests 5 rooms from 3 to 5, based on approved bookings at current state, we have a maximum of 13 rooms available for the duration of 3 to 5, so the request will be approved.

request 2: {15, 20, 06}
Only 5 rooms are available for a period of 15 to 20, therefore the request will be rejected.

request 3: {25, 28, 06}
All 15 rooms are available for the duration of 25 to 28, so the request will be approved.


Example 2:


reservations:

{
  {04, 06, 10},
  {15, 20, 10}
}

requests:

{
  {05, 06, 05},
  {06, 09, 01}
}

totalRooms: 15

Resultant Array -> {1, 0}


Explanation:
Total rooms available in the hotel are 15. Two reservations are already approved, i.e, initially 10 rooms are booked from 4 to 6 and 10 rooms are booked from 15 to 20.

request 1: {05, 06, 05}
Based on approved bookings, we have a maximum of 5 rooms available for the duration of 5 to 6, so the request will be approved.

request 2: {06, 09, 01}
No rooms available on day 06, due to previously approved booking request, so the request will be rejected.
