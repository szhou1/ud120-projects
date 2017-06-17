#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here
    # print predictions[0]
    # print predictions[0][0]
    
    for index, pred in enumerate(predictions):
        cleaned_data.append((ages[index][0], net_worths[index][0], abs(pred[0] - net_worths[index][0])))

    
    cleaned_data.sort(key=lambda tup: tup[2])
    # print len(cleaned_data)
    cleaned_data = cleaned_data[:len(cleaned_data)-9]
    print len(cleaned_data)

    # print cleaned_data
    return cleaned_data

