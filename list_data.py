names = ['Mohamed', 'Sara', 'Xia', 'Paul', 'Valentina', 'Jide', 'Aaron', 'Emily', 'Nikita', 'Paul']
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# add Priscilla's data
names.append('Priscilla')
insurance_costs.append(8320.0)

# combine two lists into a single 2D list
medical_records = list(zip(names, insurance_costs))
print(medical_records)

# print number of medical records
num_medical_records = len(medical_records)
print('There are', num_medical_records, 'medical records.')

# print first record
first_medical_record = medical_records[0]
print('Here is the first medical record:', first_medical_record)

# sort records from lowest to highest cost
medical_records.sort(key=lambda item: item[1])
print('Here are the medical records sorted by insurance cost: ' + str(medical_records))

# store and print the three least expensive insurance costs
cheapest_three = medical_records[0:3]
print('Here are the three cheapest insurance costs in our medical records: ' + str(cheapest_three))

# store and print the three most expensive insurance costs
priciest_three = medical_records[-3:]
print('Here are the three most expensive insurance costs in our medical records: ' + str(priciest_three))

# count and print the number of records containing the name 'Paul'
occurrences_paul = names.count('Paul')
print('There are', occurrences_paul, 'individuals with the name Paul in our medical records.')