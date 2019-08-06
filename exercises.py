seats = [
  [None, "Pumpkin", None, None],
  ["Socks", None, "Mimi", None],
  ["Gismo", "Shadow", None, None],
  ["Smokey","Toast","Pacha","Mau"]
]

for index, row in enumerate(seats):
    for seat_number, seat in enumerate(row):
        if seat == None:
            print("Row " + str(index + 1) + " seat " + str(seat_number + 1) + " is free. Do you want to sit there? (y/n)")
            question = str(input())
            if question == "y":
                print("What is your name?")
                new_name = str(input())
                seats[index][seat_number] = new_name
print(seats)
