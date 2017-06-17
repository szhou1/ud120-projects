#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


print 'people count:', len(enron_data)
print 'features count: ', len(enron_data[enron_data.keys()[0]])
# print ' - ', len(enron_data[0])

print 'poi count:', sum(1 for x in enron_data.keys() if enron_data[x]['poi']==1)

print enron_data.keys()
print enron_data['PRENTICE JAMES']['total_stock_value']
print enron_data['COLWELL WESLEY']['from_this_person_to_poi']
print enron_data['SKILLING JEFFREY K']['exercised_stock_options']
print 'lay', enron_data['LAY KENNETH L']
print 'lay', enron_data['LAY KENNETH L']['exercised_stock_options']
print enron_data['FASTOW ANDREW S']['exercised_stock_options']

# quantified salary
print 'have salary info:', sum(1 for x in enron_data.keys() if enron_data[x]['salary']!='NaN')

# known email address
print 'have email addr:', sum(1 for x in enron_data.keys() if enron_data[x]['email_address']<>'NaN')

# no total payments
print 'no total payments:', sum(1 for x in enron_data.keys() if enron_data[x]['total_payments']=='NaN')

# no total payments and POI
print 'no total payments and poi:', sum(1 for x in enron_data.keys() if enron_data[x]['total_payments']=='NaN' and enron_data[x]['poi']==True)
