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
# check Marina's age
marina_age = names_to_ages.get('Marina', None)
# print("Marina's age is", marina_age)

# create new dictionary for medical records
medical_records = {}
# add to medical_records dictionary
medical_records["Marina"] = {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}
medical_records["Vinay"] = {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0}
medical_records["Connie"] = {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0}
medical_records["Isaac"] = {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0}
medical_records["Valentina"] = {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}

# lookup Connie's insurance cost
connies_cost = medical_records['Connie']['Insurance_cost']
# print("Connie's insurance cost is", connies_cost, "dollars.")

# remove Vinay's record
medical_records.pop("Vinay", "We're sorry, this record could not be found.")

# output
# print(medical_costs)
# print('Average Insurance Cost: $' + str(average_cost))