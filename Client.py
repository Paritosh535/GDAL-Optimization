# Python Script to return a list of values from a list of rasters based on coordinates (Long/Lat).  
# Trevor Hobbs - Contour Geographic
# Requires GDAL (Geographic Data Abstraction Library).  

import json
from sys import argv
from osgeo import gdal

# Script arguments
x = float(argv[1]) # longitude
y = float(argv[2]) # latitude

#list of filepaths to precipitation rasters.  Rasters must be in projection EPSG:4326 (WGS84).  Replace filepaths with final destination of raster files, wherever they are exposed online.
precip_filename = [ "D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/PrecipRasters_2ndAttempt/EPSG4326/Precip_norm_Jan.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/PrecipRasters_2ndAttempt/EPSG4326/Precip_norm_Feb.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/PrecipRasters_2ndAttempt/EPSG4326/Precip_norm_Mar.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/PrecipRasters_2ndAttempt/EPSG4326/Precip_norm_Apr.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/PrecipRasters_2ndAttempt/EPSG4326/Precip_norm_May.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/PrecipRasters_2ndAttempt/EPSG4326/Precip_norm_Jun.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/PrecipRasters_2ndAttempt/EPSG4326/Precip_norm_Jul.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/PrecipRasters_2ndAttempt/EPSG4326/Precip_norm_Aug.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/PrecipRasters_2ndAttempt/EPSG4326/Precip_norm_Sep.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/PrecipRasters_2ndAttempt/EPSG4326/Precip_norm_Oct.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/PrecipRasters_2ndAttempt/EPSG4326/Precip_norm_Nov.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/PrecipRasters_2ndAttempt/EPSG4326/Precip_norm_Dec.tif"]

# define a dictionary to hold results of for-loop, which queries the raster.tif files in precip_filename (above)
precip = []

# for-loop to iterate through rasters and extract precip value according to long/lat arguments
for raster in precip_filename:
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

	col = int((x - xOrigin) / pixelWidth)
	row = int((yOrigin - y) / pixelHeight)

# Append the results of the for-loop to the precip dictionary and re-format the results to JSON with two decimal places.
	precip.append(json.dumps(float("{0:.2f}".format(data[row][col]))))
	
#list of filepaths to monthly MAX temperature rasters.  Rasters must be in projection EPSG:4326 (WGS84).  Replace filepaths with final destination of raster files, wherever they are exposed online.
tmax_filename = [ "D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/MaxTempRasters/EPSG4326/Norm_Jan_Max.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/MaxTempRasters/EPSG4326/Norm_Feb_Max.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/MaxTempRasters/EPSG4326/Norm_Mar_Max.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/MaxTempRasters/EPSG4326/Norm_Apr_Max.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/MaxTempRasters/EPSG4326/Norm_May_Max.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/MaxTempRasters/EPSG4326/Norm_Jun_Max.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/MaxTempRasters/EPSG4326/Norm_Jul_Max.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/MaxTempRasters/EPSG4326/Norm_Aug_Max.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/MaxTempRasters/EPSG4326/Norm_Sep_Max.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/MaxTempRasters/EPSG4326/Norm_Oct_Max.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/MaxTempRasters/EPSG4326/Norm_Nov_Max.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/MaxTempRasters/EPSG4326/Norm_Dec_Max.tif"]

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

	col = int((x - xOrigin) / pixelWidth)
	row = int((yOrigin - y) / pixelHeight)

# Append the results of the for-loop to the tmax dictionary and re-format the results to JSON with 1 decimal place.
	tmax.append(json.dumps(float("{0:.1f}".format(data[row][col]))))
	
#list of filepaths to monthly MIN temperature rasters.  Rasters must be in projection EPSG:4326 (WGS84).  Replace filepaths with final destination of raster files, wherever they are exposed online.
tmin_filename = [ "D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/MinTempRasters/EPSG4326/Norm_Jan_Min.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/MinTempRasters/EPSG4326/Norm_Feb_Min.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/MinTempRasters/EPSG4326/Norm_Mar_Min.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/MinTempRasters/EPSG4326/Norm_Apr_Min.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/MinTempRasters/EPSG4326/Norm_May_Min.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/MinTempRasters/EPSG4326/Norm_Jun_Min.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/MinTempRasters/EPSG4326/Norm_Jul_Min.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/MinTempRasters/EPSG4326/Norm_Aug_Min.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/MinTempRasters/EPSG4326/Norm_Sep_Min.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/MinTempRasters/EPSG4326/Norm_Oct_Min.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/MinTempRasters/EPSG4326/Norm_Nov_Min.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/MinTempRasters/EPSG4326/Norm_Dec_Min.tif"]

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

	col = int((x - xOrigin) / pixelWidth)
	row = int((yOrigin - y) / pixelHeight)

# Append the results of the for-loop to the tmin dictionary and re-format the results to JSON with 1 decimal place.
	tmin.append(json.dumps(float("{0:.1f}".format(data[row][col]))))
	
#list of filepaths to monthly AVE temperature rasters.  Rasters must be in projection EPSG:4326 (WGS84).  Replace filepaths with final destination of raster files, wherever they are exposed online.
tave_filename = [ "D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/AveTempRasters/Converted_to_decimal/EPSG4326/Jan_Ave_Temp.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/AveTempRasters/Converted_to_decimal/EPSG4326/Feb_Ave_Temp.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/AveTempRasters/Converted_to_decimal/EPSG4326/Mar_Ave_Temp.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/AveTempRasters/Converted_to_decimal/EPSG4326/Apr_Ave_Temp.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/AveTempRasters/Converted_to_decimal/EPSG4326/May_Ave_Temp.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/AveTempRasters/Converted_to_decimal/EPSG4326/Jun_Ave_Temp.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/AveTempRasters/Converted_to_decimal/EPSG4326/Jul_Ave_Temp.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/AveTempRasters/Converted_to_decimal/EPSG4326/Aug_Ave_Temp.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/AveTempRasters/Converted_to_decimal/EPSG4326/Sep_Ave_Temp.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/AveTempRasters/Converted_to_decimal/EPSG4326/Oct_Ave_Temp.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/AveTempRasters/Converted_to_decimal/EPSG4326/Nov_Ave_Temp.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/AveTempRasters/Converted_to_decimal/EPSG4326/Dec_Ave_Temp.tif"]

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

	col = int((x - xOrigin) / pixelWidth)
	row = int((yOrigin - y) / pixelHeight)

# Append the results of the for-loop to the tmin dictionary and re-format the results to JSON with 1 decimal place.
	tave.append(json.dumps(float("{0:.1f}".format(data[row][col]))))
	
#list of filepaths to monthly average cloud cover rasters.  Rasters must be in projection EPSG:4326 (WGS84).  Replace filepaths with final destination of raster files, wherever they are exposed online.
clouds_filename = [ "D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/CloudCover/Grids/CloudGridsEPSG4326/JanCloudCover.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/CloudCover/Grids/CloudGridsEPSG4326/FebCloudCover.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/CloudCover/Grids/CloudGridsEPSG4326/MarCloudCover.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/CloudCover/Grids/CloudGridsEPSG4326/AprCloudCover.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/CloudCover/Grids/CloudGridsEPSG4326/MayCloudCover.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/CloudCover/Grids/CloudGridsEPSG4326/JunCloudCover.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/CloudCover/Grids/CloudGridsEPSG4326/JulCloudCover.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/CloudCover/Grids/CloudGridsEPSG4326/AugCloudCover.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/CloudCover/Grids/CloudGridsEPSG4326/SepCloudCover.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/CloudCover/Grids/CloudGridsEPSG4326/OctCloudCover.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/CloudCover/Grids/CloudGridsEPSG4326/NovCloudCover.tif","D:/ContourGeographic/Projects/Ongoing/Prairie/Map_Projects/Data/CloudCover/Grids/CloudGridsEPSG4326/DecCloudCover.tif"]

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

	col = int((x - xOrigin) / pixelWidth)
	row = int((yOrigin - y) / pixelHeight)

# Append the results of the for-loop to the clouds dictionary and re-format the results to JSON with 1 decimal place.
	clouds.append(json.dumps(float("{0:.1f}".format(data[row][col]))))

# Create a list of months for the output data table.  The order of the months must correspond to the order of rasters in the three filename lists (precid, tmax, and tmin) above.
months = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']
	
array = [{'month': month, 'average-mly-precip': precip, 'average-mly-max-temp': tmax, 'average-mly-temp': tave, 'average-mly-min-temp': tmin, 'average-mly-cloud-cover': clouds} for month, precip, tmax, tave, tmin, clouds in zip(months, precip, tmax, tave, tmin, clouds)]
	
table = json.dumps(array)
	
print(table)