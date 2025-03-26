# initial records
medical_costs = {'Marina': 6607.0, 'Vinay': 3225.0}

# add records
medical_costs.update({
                      'Connie': 8886.0,
                      'Isaac': 16444.0,
                      'Valentina': 6420.0
                    })
# correct the value of Vinay's record
medical_costs['Vinay'] = 3325.0

# calculate average medical cost across patients
total_cost = 0
for cost in medical_costs.values():
  total_cost += cost
average_cost = total_cost / len(medical_costs)

# create a second dictionary from lists
names = ['Marina', 'Vinay', 'Connie', 'Isaac', 'Valentina']
ages = [27, 24, 43, 35, 52]
# zip names and ages together
zipped_ages = zip(names, ages)
# list comrehension to dictionary
names_to_ages = {key:value for key, value in zipped_ages}

# output
# print(medical_costs)
# print('Average Insurance Cost: $' + str(average_cost))
print(names_to_ages)