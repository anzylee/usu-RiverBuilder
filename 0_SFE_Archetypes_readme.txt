# HOW to create an archetype using River Builder

## 0. Preparation ###

(0) Create a folder, "sfeXX_gcs_analysis" in usu-RiverBuilder folder
(1) Create a folder, "Tuflow_output_rasters" in sfeXX_gcs_analysis folder
(2) Put clipeed WSE files (e.g. F:\tuflow_runs\sfe_XX_tuflow\results\XXX\grids\clipped) dlineating baseflow/bf flow 
    in Tuflow_output_rasters folder.
(3) Create a folder, "gis". Put the terrain file (sfe_XX) in sfeXX_gcs_analysis and clip polygon (2d_trim_sfe_XX) in gis folder
(4) Open ArcGIS Pro and load (2) and (3)
(5) Convert WSE rasters to polygon
    1) https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-analyst/raster-calculator.htm
    -> e.g. Con( "T1_h_013_clip.tif">0, 1,0)
    : save as h_13_polygon
    2) raster to polygon
(6) Clip the terrain file with clip polygon if needed
(7) save the loaded files as a project, sfe_XX, in sfeXX_gcs_analysis folder


### 1. How to generate W_bf series ###

(0) Create a thalweg (manually) and centerline of bankfull polygon (Using ET or manually)
   https://pro.arcgis.com/en/pro-app/latest/help/editing/create-polyline-features.htm
    -> Or just copy and paste Thalweg.shp, StraightLine.shp and Outer_Cl.shp from other folder
(1) Create Station Lines for thalweg and centerline (Using ET: Miscellaneous > Create Station Lines)
	- Distance = X m (depending on the area), station line length = 30 m, both
(2) Clip polylines generated in (1) with base or bankfull polygon (Using ArcGIS)
(3) Buffer the clipped polylines (Using ET: Polyine > Buffer Polylines)
	- Distance = 1 m
	- Flat end, Both side

### 2. Making RB Input txt file ###

(1) Obtain elevation (Z) and width (W_base, W_bf) series. 
	- For Zs, Generate points along lines -> Distance = X meters, don't include end points
	  : Save as gis/Thalweg_nodes
          Then, Extract values to points -> Feature: Thalweg_nodes, raster: topo, check interpolate)
	  : Save as gis/Thalweg_elev
	- For WESs, follow the procedure for Zs, but with raster: WSE
	  : Save as gis/Thalweg_baseWSE.dbf and gis/Thalweg_bfWSE.dbf
	- For Ws, Attribute table -> Calculate Geometry, Coordinate system = Current map)
	  : Save as gis/Inner_CL_Xm_Clip.dbf and gis/Outer_CL_Xm_Clip.dbf

(2) Copy and paste (1) to RiverBuilder metrics excel file along with the distance. 
	- Specify whether the series is from down station or from up station.
(3) For Z, do a linear regression and obtain detrended elevation, Zd.
(4) For W, divided the values by 2.
(5) Copy and paste the distance, Zd, Wb/2, and Wbf/2 to a site-specific .xlsx file, 
	- Default: 0_SFE-322_RiverBuilder_metrics.
	- Use "spatial_series" tab
(6) Follow the steps in "cheatsheet" in the main RB folder.

(+) Open field survey excel sheet for each site and calculate the total number of particles exceeding 1m.
The total number of elements is L/W*n^2 where L is the length of reach, W is the average bankfull width
and n is the average number of boulders exceeding 1m. Bedrock is not inlcuded.

(+) From Xavier's analysis of baseflow Zd, it looks like the "power method" performed best at matching the overall pool-riffle morphology in terms of total amplitude. This is the one with 8 harmonics.
Similarly, the power method worked best for baseflow W series. Has 38 harmonics

(+) For the bankfull flow W series, because it has a trend, it isn't as good, but the power method is still quite good.
