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

# output
print(medical_costs)