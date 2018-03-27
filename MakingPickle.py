# Python Script to return a list of values from a list of rasters based on coordinates (Long/Lat).  
# Trevor Hobbs - Contour Geographic
# Requires GDAL (Geographic Data Abstraction Library).  

import json
from sys import argv
from osgeo import gdal

import _pickle as pickle

# Script arguments
#x = float(argv[1]) # longitude
#y = float(argv[2]) # latitude
x = float(-122.431297)
y = float(37.773972)
#list of filepaths to precipitation rasters.  Rasters must be in projection EPSG:4326 (WGS84).  Replace filepaths with final destination of raster files, wherever they are exposed online.
precip_filename = [ "D:/wether/5_march/Data/precip/Precip_norm_Jan.tif",
                   "D:/wether/5_march/Data/precip/Precip_norm_Feb.tif",
                   "D:/wether/5_march/Data/precip/Precip_norm_Mar.tif",
                   "D:/wether/5_march/Data/precip/Precip_norm_Apr.tif",
                   "D:/wether/5_march/Data/precip/Precip_norm_May.tif",
                   "D:/wether/5_march/Data/precip/Precip_norm_Jun.tif",
                   "D:/wether/5_march/Data/precip/Precip_norm_Jul.tif",
                   "D:/wether/5_march/Data/precip/Precip_norm_Aug.tif",
                   "D:/wether/5_march/Data/precip/Precip_norm_Sep.tif",
                   "D:/wether/5_march/Data/precip/Precip_norm_Oct.tif",
                   "D:/wether/5_march/Data/precip/Precip_norm_Nov.tif",
                   "D:/wether/5_march/Data/precip/Precip_norm_Dec.tif"]

# define a dictionary to hold results of for-loop, which queries the raster.tif files in precip_filename (above)

precip = []

#for rs in precip_filename:
#    print(rs.split('/')[-1].split('.')[0]) 
# for-loop to iterate through rasters and extract precip value according to long/lat arguments
for raster in precip_filename:
    driver = gdal.GetDriverByName('GTiff')
    dataset = gdal.Open(raster)
    band = dataset.GetRasterBand(1)
    
    cols = dataset.RasterXSize
    rows = dataset.RasterYSize
    data = band.ReadAsArray(0, 0, cols, rows)

    transform = dataset.GetGeoTransform()
    
    xOrigin = transform[0]
    yOrigin = transform[3]
    pixelWidth = transform[1]
    pixelHeight = -transform[5]
    
    
    with open('pickle/precip/'+raster.split('/')[-1].split('.')[0]+'_data.pickle', 'wb') as handle:
        pickle.dump(data, handle)
    
    with open('pickle/precip/'+raster.split('/')[-1].split('.')[0]+'_transform.pickle', 'wb') as handle:
        pickle.dump(transform, handle)
    
    col = int((x - xOrigin) / pixelWidth)
    row = int((yOrigin - y) / pixelHeight)
    print(data[row][col])
    # Append the results of the for-loop to the precip dictionary and re-format the results to JSON with two decimal places.
    precip.append(json.dumps(float("{0:.2f}".format(data[row][col]))))
    


#=================================================================================================
precip1=[]
months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
for month in range(0,12):
    with open('pickle/precip/Precip_norm_'+months[month]+'_transform.pickle', 'rb') as handle:
        transform = pickle.load(handle)
    with open('pickle/precip/Precip_norm_'+months[month]+'_data.pickle', 'rb') as handle:
        data = pickle.load(handle)

    
    xOrigin = transform1[0]
    yOrigin = transform1[3]
    pixelWidth = transform1[1]
    pixelHeight = -transform1[5]
    col = int((x - xOrigin) / pixelWidth)
    row = int((yOrigin - y) / pixelHeight)
    print(data1[row][col])
    precip1.append(json.dumps(float("{0:.2f}".format(data[row][col]))))
#=========================================================================================
    
    
 #list of filepaths to monthly MAX temperature rasters.  Rasters must be in projection EPSG:4326 (WGS84).  Replace filepaths with final destination of raster files, wherever they are exposed online.
    tmax_filename = ["D:/wether/5_march/Data/max/Norm_Jan_Max.tif",
                  "D:/wether/5_march/Data/max/Norm_Feb_Max.tif",
                  "D:/wether/5_march/Data/max/Norm_Mar_Max.tif",
                  "D:/wether/5_march/Data/max/Norm_Apr_Max.tif",
                  "D:/wether/5_march/Data/max/Norm_May_Max.tif",
                  "D:/wether/5_march/Data/max/Norm_Jun_Max.tif",
                  "D:/wether/5_march/Data/max/Norm_Jul_Max.tif",
                  "D:/wether/5_march/Data/max/Norm_Aug_Max.tif",
                  "D:/wether/5_march/Data/max/Norm_Sep_Max.tif",
                  "D:/wether/5_march/Data/max/Norm_Oct_Max.tif",
                  "D:/wether/5_march/Data/max/Norm_Nov_Max.tif",
                  "D:/wether/5_march/Data/max/Norm_Dec_Max.tif"]

 # define a dictionary to hold results of for-loop, which queries the raster.tif files in tmax_filename (above)
 tmax = []
	
 # for-loop to iterate through rasters and extract value according to long/lat arguments
 for raster in tmax_filename:
    driver = gdal.GetDriverByName('GTiff')
    dataset = gdal.Open(raster)
    band = dataset.GetRasterBand(1)
    cols = dataset.RasterXSize
    rows = dataset.RasterYSize
    
    transform = dataset.GetGeoTransform()
    
    xOrigin = transform[0]
    yOrigin = transform[3]
    pixelWidth = transform[1]
    pixelHeight = -transform[5]
    
    data = band.ReadAsArray(0, 0, cols, rows)
    
        
    with open('pickle/max/'+raster.split('/')[-1].split('.')[0]+'_data.pickle', 'wb') as handle:
        pickle.dump(data, handle)
    
    with open('pickle/max/'+raster.split('/')[-1].split('.')[0]+'_transform.pickle', 'wb') as handle:
        pickle.dump(transform, handle)
    
    col = int((x - xOrigin) / pixelWidth)
    row = int((yOrigin - y) / pixelHeight)
    print(data[row][col])
    # Append the results of the for-loop to the tmax dictionary and re-format the results to JSON with 1 decimal place.
    tmax.append(json.dumps(float("{0:.1f}".format(data[row][col]))))

#=======================================
tmax=[]
months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
for month in range(0,12):
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
    print(data[row][col])
    tmax.append(json.dumps(float("{0:.2f}".format(data[row][col]))))
    
#========================
	
# #list of filepaths to monthly MIN temperature rasters.  Rasters must be in projection EPSG:4326 (WGS84).  Replace filepaths with final destination of raster files, wherever they are exposed online.
 tmin_filename = [ "D:/wether/5_march/Data/min/Norm_Jan_Min.tif",
                  "D:/wether/5_march/Data/min/Norm_Feb_Min.tif",
                  "D:/wether/5_march/Data/min/Norm_Mar_Min.tif",
                  "D:/wether/5_march/Data/min/Norm_Apr_Min.tif",
                  "D:/wether/5_march/Data/min/Norm_May_Min.tif",
                  "D:/wether/5_march/Data/min/Norm_Jun_Min.tif",
                  "D:/wether/5_march/Data/min/Norm_Jul_Min.tif",
                  "D:/wether/5_march/Data/min/Norm_Aug_Min.tif",
                  "D:/wether/5_march/Data/min/Norm_Sep_Min.tif",
                  "D:/wether/5_march/Data/min/Norm_Oct_Min.tif",
                  "D:/wether/5_march/Data/min/Norm_Nov_Min.tif",
                  "D:/wether/5_march/Data/min/Norm_Dec_Min.tif"]

 # define a dictionary to hold results of for-loop, which queries the raster.tif files in tmin_filename (above)
 tmin = []
	
 # for-loop to iterate through rasters and extract value according to long/lat arguments
 for raster in tmin_filename:
    driver = gdal.GetDriverByName('GTiff')
    dataset = gdal.Open(raster)
    band = dataset.GetRasterBand(1)
    
    cols = dataset.RasterXSize
    rows = dataset.RasterYSize
    
    transform = dataset.GetGeoTransform()
    
    xOrigin = transform[0]
    yOrigin = transform[3]
    pixelWidth = transform[1]
    pixelHeight = -transform[5]
    
    data = band.ReadAsArray(0, 0, cols, rows)
    
    with open('pickle/min/'+raster.split('/')[-1].split('.')[0]+'_data.pickle', 'wb') as handle:
        pickle.dump(data, handle)
    
    with open('pickle/min/'+raster.split('/')[-1].split('.')[0]+'_transform.pickle', 'wb') as handle:
        pickle.dump(transform, handle)
        
    col = int((x - xOrigin) / pixelWidth)
    row = int((yOrigin - y) / pixelHeight)
    print(data[row][col])
# Append the results of the for-loop to the tmin dictionary and re-format the results to JSON with 1 decimal place.
    tmin.append(json.dumps(float("{0:.1f}".format(data[row][col]))))

#=======================================
tmin=[]
months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
for month in range(0,12):
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
    print(data[row][col])
    tmin.append(json.dumps(float("{0:.2f}".format(data[row][col]))))
    
#========================
    
# #list of filepaths to monthly average cloud cover rasters.  Rasters must be in projection EPSG:4326 (WGS84).  Replace filepaths with final destination of raster files, wherever they are exposed online.
 clouds_filename = [ "D:/wether/5_march/Data/cloudgrids/JanCloudCover.tif",
                    "D:/wether/5_march/Data/cloudgrids/FebCloudCover.tif",
                    "D:/wether/5_march/Data/cloudgrids/MarCloudCover.tif",
                    "D:/wether/5_march/Data/cloudgrids/AprCloudCover.tif",
                    "D:/wether/5_march/Data/cloudgrids/MayCloudCover.tif",
                    "D:/wether/5_march/Data/cloudgrids/JunCloudCover.tif",
                    "D:/wether/5_march/Data/cloudgrids/JulCloudCover.tif",
                    "D:/wether/5_march/Data/cloudgrids/AugCloudCover.tif",
                    "D:/wether/5_march/Data/cloudgrids/SepCloudCover.tif",
                    "D:/wether/5_march/Data/cloudgrids/OctCloudCover.tif",
                    "D:/wether/5_march/Data/cloudgrids/NovCloudCover.tif",
                    "D:/wether/5_march/Data/cloudgrids/DecCloudCover.tif"]

 # define a dictionary to hold results of for-loop, which queries the raster.tif files in clouds_filename (above)
 clouds = []
	
 # for-loop to iterate through rasters and extract value according to long/lat arguments
 for raster in clouds_filename:
    driver = gdal.GetDriverByName('GTiff')
    dataset = gdal.Open(raster)
    band = dataset.GetRasterBand(1)
    
    cols = dataset.RasterXSize
    rows = dataset.RasterYSize
    
    transform = dataset.GetGeoTransform()
    
    xOrigin = transform[0]
    yOrigin = transform[3]
    pixelWidth = transform[1]
    pixelHeight = -transform[5]
    
    data = band.ReadAsArray(0, 0, cols, rows)

    with open('pickle/cloud/'+raster.split('/')[-1].split('.')[0]+'_data.pickle', 'wb') as handle:
        pickle.dump(data, handle)
    
    with open('pickle/cloud/'+raster.split('/')[-1].split('.')[0]+'_transform.pickle', 'wb') as handle:
        pickle.dump(transform, handle)
        
    col = int((x - xOrigin) / pixelWidth)
    row = int((yOrigin - y) / pixelHeight)
    print(data[row][col])
    # Append the results of the for-loop to the clouds dictionary and re-format the results to JSON with 1 decimal place.
    clouds.append(json.dumps(float("{0:.1f}".format(data[row][col]))))


#=======================================
clouds=[]
months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
for month in range(0,12):
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
    print(data[row][col])
    clouds.append(json.dumps(float("{0:.2f}".format(data[row][col]))))
    
#========================
    

tave_filename = [ "D:/wether/5_march/Data/avg/Jan_Ave_Temp.tif",
                 "D:/wether/5_march/Data/avg/Feb_Ave_Temp.tif",
                 "D:/wether/5_march/Data/avg/Mar_Ave_Temp.tif",
                 "D:/wether/5_march/Data/avg/Apr_Ave_Temp.tif",
                 "D:/wether/5_march/Data/avg/May_Ave_Temp.tif",
                 "D:/wether/5_march/Data/avg/Jun_Ave_Temp.tif",
                 "D:/wether/5_march/Data/avg/Jul_Ave_Temp.tif",
                 "D:/wether/5_march/Data/avg/Aug_Ave_Temp.tif",
                 "D:/wether/5_march/Data/avg/Sep_Ave_Temp.tif",
                 "D:/wether/5_march/Data/avg/Oct_Ave_Temp.tif",
                 "D:/wether/5_march/Data/avg/Nov_Ave_Temp.tif",
                 "D:/wether/5_march/Data/avg/Dec_Ave_Temp.tif"]

# define a dictionary to hold results of for-loop, which queries the raster.tif files in tave_filename (above)
tave = []
	
# for-loop to iterate through rasters and extract value according to long/lat arguments
for raster in tave_filename:
    driver = gdal.GetDriverByName('GTiff')
    dataset = gdal.Open(raster)
    band = dataset.GetRasterBand(1)
    
    cols = dataset.RasterXSize
    rows = dataset.RasterYSize
    
    transform = dataset.GetGeoTransform()
    
    xOrigin = transform[0]
    yOrigin = transform[3]
    pixelWidth = transform[1]
    pixelHeight = -transform[5]
    
    data = band.ReadAsArray(0, 0, cols, rows)
    
    with open('pickle/avg/'+raster.split('/')[-1].split('.')[0]+'_data.pickle', 'wb') as handle:
        pickle.dump(data, handle)
    
    with open('pickle/avg/'+raster.split('/')[-1].split('.')[0]+'_transform.pickle', 'wb') as handle:
        pickle.dump(transform, handle)
        
    col = int((x - xOrigin) / pixelWidth)
    row = int((yOrigin - y) / pixelHeight)
    print(data[row][col])
    # Append the results of the for-loop to the tmin dictionary and re-format the results to JSON with 1 decimal place.
    tave.append(json.dumps(float("{0:.1f}".format(data[row][col]))))
    
#=====================
tave1=[]
months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
print(len(months))
for month in range(len(months)):
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
    print(data[row][col])
    tave1.append(json.dumps(float("{0:.2f}".format(data[row][col]))))
    
#========================
# # Create a list of months for the output data table.  The order of the months must correspond to the order of rasters in the three filename lists (precid, tmax, and tmin) above.
# months = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
	
# array = [{'month': month, 'average-mly-precip': precip, 'average-mly-max-temp': tmax, 'average-mly-min-temp': tmin, 'average-mly-cloud-cover': clouds} for month, precip, tmax, tmin, clouds in zip(months, precip, tmax, tmin, clouds)]
	
# table = json.dumps(array)
	
# print(table)
    
months = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
	
array = [{'month': month, 'average-mly-precip': precip, 'average-mly-max-temp': tmax, 'average-mly-temp': tave, 'average-mly-min-temp': tmin, 'average-mly-cloud-cover': clouds} for month, precip, tmax, tave, tmin, clouds in zip(months, precip, tmax, tave, tmin, clouds)]
	
table = json.dumps(array)