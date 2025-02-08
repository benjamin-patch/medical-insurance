# Insurance Estimation Using Lists

# estimate insurance cost
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  return estimated_cost
 
# estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name = 'Maria', age = 31, sex = 0, bmi = 23.1, num_of_children = 1, smoker = 0)

# estimate Rohan's insurance cost
rohan_insurance_cost = estimate_insurance_cost(name = 'Rohan', age = 25, sex = 1, bmi = 28.5, num_of_children = 3, smoker = 0)

# estimate Valentina's insurance cost
valentina_insurance_cost = estimate_insurance_cost(name = 'Valentina', age = 53, sex = 0, bmi = 31.4, num_of_children = 0, smoker = 1)

# list actual insurance costs
names = ['Maria', 'Rohan', 'Valentina']
insurance_costs = [4150.0, 5320.0, 35210.0]

insurance_data = list(zip(names, insurance_costs))
print('Actual insurance cost data:', insurance_data)

# consolidate estimated insurance data
estimated_insurance_data = []

estimated_insurance_data.append(('Maria', maria_insurance_cost))
estimated_insurance_data.append(('Rohan', rohan_insurance_cost))
estimated_insurance_data.append(('Valentina', valentina_insurance_cost))

print('Estimated insurance cost data:', estimated_insurance_data)

# calculate difference between actual cost and estimated cost
maria_cost_difference = maria_insurance_cost - insurance_costs[0]
rohan_cost_difference = rohan_insurance_cost - insurance_costs[1]
valentina_cost_difference = valentina_insurance_cost - insurance_costs[2]

# list difference between actual cost and estimated cost
insurance_cost_difference = []

insurance_cost_difference.append(('Maria', maria_cost_difference))
insurance_cost_difference.append(('Rohan', rohan_cost_difference))
insurance_cost_difference.append(('Valentina', valentina_cost_difference))

print('Difference between actual and estimated costs:', insurance_cost_difference)