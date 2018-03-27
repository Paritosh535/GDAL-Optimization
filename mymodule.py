# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 16:34:00 2018

@author: paritosh.yadav
"""

import json
import _pickle as pickle # cPickle packge for serializer/Desecrializer

#def WeatherHistory(longitude,latitude):
    
    
""" Weather history analysis Precip,Min Temp,Max Temp,Cloud info, Avg Temp """
#x = float(x)
#y = float(y)

x = float(-122.431297)
y = float(37.773972)
months=['Jan','Feb','Mar','Apr',
        'May','Jun','Jul','Aug',
        'Sep','Oct','Nov','Dec'] # months for load file and json data display month wise
#### Precip logic #####
precip=[]
for month in range(len(months)): # loop for load pickle file data month wise
    """loding pickle file """
    with open('pickle/precip/Precip_norm_'+months[month]+'_transform.pickle', 'rb') as handle:
        transform = pickle.load(handle)
    with open('pickle/precip/Precip_norm_'+months[month]+'_data.pickle', 'rb') as handle:
        data = pickle.load(handle)

    xOrigin = transform[0]
    yOrigin = transform[3]
    pixelWidth = transform[1]
    pixelHeight = -transform[5]
    col = int((x - xOrigin) / pixelWidth)
    row = int((yOrigin - y) / pixelHeight)
    precip.append(json.dumps(float("{0:.2f}".format(data[row][col])))) #append data into precep array
    
#### End Precip logic #####

#### Temp Max logic #####
tmax=[]
for month in range(len(months)): # loop for load pickle file data month wise
    """loding pickle file """
    with open('pickle/max/Norm_'+months[month]+'_Max_transform.pickle', 'rb') as handle:
        transform = pickle.load(handle)
    with open('pickle/max/Norm_'+months[month]+'_Max_data.pickle', 'rb') as handle:
        data = pickle.load(handle)

    
    xOrigin = transform[0]
    yOrigin = transform[3]
    pixelWidth = transform[1]
    pixelHeight = -transform[5]
    col = int((x - xOrigin) / pixelWidth)
    row = int((yOrigin - y) / pixelHeight)
    tmax.append(json.dumps(float("{0:.2f}".format(data[row][col]))))
#### End Temp Max logic #####

#### Temp Min logic #####
tmin=[]
for month in range(len(months)):# loop for load pickle file data month wise
    """loding pickle file """
    with open('pickle/min/Norm_'+months[month]+'_Min_transform.pickle', 'rb') as handle:
        transform = pickle.load(handle)
    with open('pickle/min/Norm_'+months[month]+'_Min_data.pickle', 'rb') as handle:
        data = pickle.load(handle)
    
    xOrigin = transform[0]
    yOrigin = transform[3]
    pixelWidth = transform[1]
    pixelHeight = -transform[5]
    col = int((x - xOrigin) / pixelWidth)
    row = int((yOrigin - y) / pixelHeight)
    tmin.append(json.dumps(float("{0:.2f}".format(data[row][col]))))
    
#### End Temp Min logic #####    

#### Cloud info logic #####
clouds=[]
for month in range(len(months)):# loop for load pickle file data month wise
    """loding pickle file """
    with open('pickle/cloud/'+months[month]+'CloudCover_transform.pickle', 'rb') as handle:
        transform = pickle.load(handle)
    with open('pickle/cloud/'+months[month]+'CloudCover_data.pickle', 'rb') as handle:
        data = pickle.load(handle)

    xOrigin = transform[0]
    yOrigin = transform[3]
    pixelWidth = transform[1]
    pixelHeight = -transform[5]
    col = int((x - xOrigin) / pixelWidth)
    row = int((yOrigin - y) / pixelHeight)
    clouds.append(json.dumps(float("{0:.2f}".format(data[row][col]))))
#### End Cloud info logic #####
 
#### Temp Avg logic #####
    
tave1=[]
for month in range(len(months)):# loop for load pickle file data month wise
    """loding pickle file """
    with open('pickle/avg/'+months[month]+'_Ave_Temp_transform.pickle', 'rb') as handle:
        transform = pickle.load(handle)
    with open('pickle/avg/'+months[month]+'_Ave_Temp_data.pickle', 'rb') as handle:
        data = pickle.load(handle)

    
    xOrigin = transform[0]
    yOrigin = transform[3]
    pixelWidth = transform[1]
    pixelHeight = -transform[5]
    col = int((x - xOrigin) / pixelWidth)
    row = int((yOrigin - y) / pixelHeight)
    tave1.append(json.dumps(float("{0:.2f}".format(data[row][col]))))
#### End Temp Avg info logic #####

#combine all Data here
    
#array = [{'month': months,
#          'average_mly_precip': precip,
#          'average_mly_max_temp': tmax,
#          'average_mly_min_temp': tmin,
#          'average_mly_cloud_cover': clouds,
#          'average-mly-temp': tave} 
#    for month, precip, tmax, tmin, clouds,tave in zip(months, precip, tmax, tmin, clouds,tave)]

months = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
	
array = [{'month': month, 'average-mly-precip': precip, 'average-mly-max-temp': tmax, 'average-mly-temp': tave, 'average-mly-min-temp': tmin, 'average-mly-cloud-cover': clouds} for month, precip, tmax, tave, tmin, clouds in zip(months, precip, tmax, tave, tmin, clouds)]
	
table = json.dumps(array)
#json convertion 
#    return(json.dumps(array))
