# ------------------------------------------------------------------------------------
# The following 2D lists mimic a restaurant seating layout, similar to a grid.
# 
# - Row 0 is a "header row":
#     - The first cell (index 0) is just a row label (0).
#     - The remaining cells are table labels with capacities in parentheses,
#       e.g., 'T1(2)' means "Table 1" has capacity 2.
#
# - Rows 1 through 6 each represent a distinct "timeslot" or "seating period":
#     - The first cell in each row (e.g., [1], [2], etc.) is that row's label (the timeslot number).
#     - Each subsequent cell shows whether the table (from the header row) is
#       free ('o') or occupied ('x') during that timeslot.
#
# In other words, restaurant_tables[row][column] tells you the status of a
# particular table (column) at a particular timeslot (row).
# ------------------------------------------------------------------------------------

# Shows the structure of the restaurant layout with all tables free ("o" = open).
restaurant_tables = [
    [0,        'T1(2)',  'T2(4)',  'T3(2)',  'T4(6)',  'T5(4)',  'T6(2)'],
    [1,        'o',      'o',      'o',      'o',      'o',      'o'],
    [2,        'o',      'o',      'o',      'o',      'o',      'o'],
    [3,        'o',      'o',      'o',      'o',      'o',      'o'],
    [4,        'o',      'o',      'o',      'o',      'o',      'o'],
    [5,        'o',      'o',      'o',      'o',      'o',      'o'],
    [6,        'o',      'o',      'o',      'o',      'o',      'o']
]

# ------------------------------------------------------------------------------------
# This second layout serves as a test case where some tables ('x') are already occupied.
# Use this for testing your logic to:
#   - Find free tables (marked 'o')
#   - Check if those tables meet a certain capacity (from the header row, e.g. 'T1(2)')
#   - Potentially combine adjacent tables if one alone isn't enough for a larger party.
# ------------------------------------------------------------------------------------

restaurant_tables2 = [
    [0,        'T1(2)',  'T2(4)',  'T3(2)',  'T4(6)',  'T5(4)',  'T6(2)'],
    [1,        'x',      'o',      'o',      'o',      'o',      'x'],
    [2,        'o',      'x',      'o',      'o',      'x',      'o'],
    [3,        'x',      'x',      'o',      'x',      'o',      'o'],
    [4,        'o',      'o',      'o',      'x',      'o',      'x'],
    [5,        'o',      'x',      'o',      'x',      'o',      'o'],
    [6,        'o',      'o',      'o',      'o',      'x',      'o']
]
#LV1 
print (restaurant_tables2[1][2]) #should print the respectve index at 1,2
print (restaurant_tables2[2][1]) # returns return corrdinate 2,1
print (restaurant_tables2[4][1]) # prints out fourth index first column

open_tables =[] # empty list to get everything 
for table_data in (restaurant_tables2): #for loop that contains from the varaible [considers everything]
    if len(table_data)>0:  #Reurns a letter  within the sta structure above index zero
        table_index=table_data[1] #assigned varaible that skips straight to index one for open tables
        status= table_data[1]
        if status=='o': # if statement that checks for tables marked o
            open_tables.append(table_index) # function built to add / include more tables marked o in process
    print(f"open tables: {open_tables}")  # desired output 

    # LV 2 
def one_table_for_more(free_tables, party_size): # two parameters dealing with tables and size
    if table_capacity >=party_size: # condition checking for capacity over num of people
        print("None, fully occupied ")
    elif party size <= table capacity:
        print("Ay, it's open over here")
        
    return free_tables

# LV 3
def available_seats():
 empty_seats= [0,        'T1(2)',  'T2(4)',  'T3(2)',  'T4(6)',  'T5(4)',  'T6(2)'],
    [1,        'x',      'o',      'o',      'o',      'o',      'x'],
    [2,        'o',      'x',      'o',      'o',      'x',      'o'],
    [3,        'x',      'x',      'o',      'x',      'o',      'o']

    #message([start: stop: step])

#    o      x  o  x   o   x  o   x  o  x  o  x  o  x   o   x 
#   T1(2)   T2(3)          T2(4)

print (message[T1(2):T2(4)])