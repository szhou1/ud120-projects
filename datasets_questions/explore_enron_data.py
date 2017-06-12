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

poi_count = 0;
for person in enron_data:
    # print person
    if enron_data[person]["poi"] == 1:
        poi_count += 1

print 'poi count:', poi_count
# print enron_data.keys()
print enron_data['PRENTICE JAMES']['total_stock_value']

