import os
import numpy as np
import arcpy

# 0. Environment setting
#############################################################################################
# 1 Input variables
# 1.1 Specify the case name
case_name = 'site316_cleanbed'
site_name = 'sfe316_cleanbed'
NAME = 'sfe_316'
cell_size = '1'
execute = np.array([0, # 1 Table to point
                    1, # 2 Create TIN
                    1, # 3 TIN to Raster
                    1]) # 4 Raster to asc

#############################################################################################
arcpy.env.workspace = "./site316_cleanbed/site316_cleanbed"
sr = arcpy.SpatialReference(3857, 115700) #  WGS_1984_web_mercator, WGS 1984
#sr = arcpy.SpatialReference(4759, 115700) # WGS 1984, WGS 1984
arcpy.CheckOutExtension("3D")

if execute[0] == 1:
    # 1 Table to point
    in_Table = arcpy.env.workspace+"/SRVtopo.csv"
    output_point = case_name+'_xyz.shp'
    x_coords = "X"
    y_coords = "Y"
    z_coords = "Z"

    # Make the XY event layer...
    arcpy.management.XYTableToPoint(in_Table, output_point,
                                    x_coords, y_coords, z_coords,#arcpy.SpatialReference(4759, 115700))
                                    sr)
    print(arcpy.GetCount_management(output_point))

    # Points should be adjusted to create a "RUNWAY'
    print('Points should be adjusted to create a RUNWAY')
    os.system("pause")

if execute[1] == 1:
    # 2 Create TIN
    in_point = case_name+'_xyz.shp'
    output_TIN = case_name+'_TIN'

    arcpy.ddd.CreateTin(output_TIN, sr, in_point+" Z masspoints")

if execute[2] == 1:
    # 3 TIN to Raster
    in_TIN = case_name+'_TIN'
    out_tif = case_name+'.tif'
    # Set variables for TIN to Raster
    dataType = "FLOAT"  # Default
    method = "LINEAR"  # Default
    sampling = "CELLSIZE " + cell_size
    zfactor = "1"

    arcpy.ddd.TinRaster(in_TIN, out_tif, dataType,
                    method, sampling, zfactor)

if execute[3] == 1:
    # 4 Raster to ascii
    in_tif = case_name+'.tif'
    out_ascii = site_name + '.asc'

    arcpy.RasterToASCII_conversion(in_tif, out_ascii)
