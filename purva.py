import csv

def get_last_contacted(arr):
    index = 1
    result = -1
    count = 0

    for element in arr:
        # print(element)
        if(element[1] == '100.00%'):
            print(element)
            result = index + 1
            count = count + 1
        index = index + 1
    
    arr = [len(arr),count,result]
    return arr

 
def populate_final(dict,final):
    for key in dict:
        final[key] = get_last_contacted(dict[key])

def sort_my_dict(dict):
    for key in dict:
        dict[key].sort(key=lambda x:x[0])

def read_csv(filename,dict2):
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for line in csvreader:
            customer_id = line[1]
            date = line[0]
            flag = line[2]
            if customer_id in dict2 :
                dict2[customer_id].append([date,flag])
            else :
                dict2[customer_id] = []
                dict2[customer_id].append([date,flag])

# This will be the data that we will read from excel sheet. It is stored in the format shown below
# {
#   Customer_ID : [[Date1,100],[Date2,0],[Date3,100]]
# }
dict2 = {}

# dict2 = {
#     "1234" : [['1','100.00%'],['2','100.00%'],['3','100.00%']]
# }

# Final Output
# { Customer_Id1: [Total, Replied, Frequency], Customer_Id2 : [Total, Replied, Frequency]} 
final = {}

# Name of the CSV file
filename="testing.csv"

# Read the csv file into a dictionary
read_csv(filename,dict2)

# Sort the dictionary based on date
sort_my_dict(dict2)

# populate final dictionary
populate_final(dict2,final)

print(final)
