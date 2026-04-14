'''travel_log ={
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"]
}
#print(travel_log["France"][1])'''

#nested_list = ["A", "B", ["C", "D"]]
#print(nested_list[2][1])

'''travel_log ={
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Stuttgart", "Berlin"],
        "total_visits": 5
    },
}

print(travel_log["Germany"]["cities_visited"][0])'''

dict = {
    "a":1,
    "b":2,
    "c":3,
}
dict["c"] = [1,2,3]

for key in dict:
    dict[key] += 1

dict[1] = 4
print(dict[1])
print(dict["a"])
print(dict["c"])
