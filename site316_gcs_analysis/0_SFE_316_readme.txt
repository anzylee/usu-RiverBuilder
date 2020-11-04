# Site 316 notes

1. How to generate W_bf series
(0) Create a centerline of bankfull polygon (Using ET or manually)
(1) Create Station Lines (Using ET: Miscellaneous > Create Station Lines)
	- Distance = 2 m
(2) Clip polylines generated in (1)with bankfull polygon (Using ArcGIS)
(3) Buffer the clipped polylines (Using ET: Polyine > Buffer Polylines)
	- Distance = 1 m
	- Flat end, Both side

2. Making RB Input txt file
(1) Obtain elevation (Z) and width (W_base, W_bf) series.
(2) Copy and paste (1) to RiverBuilder metrics excel file along with the distance. 
	- Specify whether the series is from down station or from up station.
(3) For Z, do a linear regression and obtain detrended elevation, Zd.
(4) For W, divided the values by 2.
(5) Copy and paste the distance, Zd, Wb/2, and Wbf/2 to a site-specific .csv file, e.g. SFE_316_series.csv.
(6) Put (5) into a site-specific folder.
(7) Run "signal_to_riverbuilder.py" from usu-RiverBuilder folder.
	- It will generate Wbase, Wbf, Zd series.
	(+) From Xavier's analysis of baseflow Zd, it looks like the "power method" performed best at matching the overall pool-riffle morphology in terms of total amplitude.
(8) Copy and paste these files to RB folder. e.g. samples/site316

(+) From Xavier's analysis of baseflow Zd, it looks like the "power method" performed best at matching the overall pool-riffle morphology in terms of total amplitude. This is the one with 8 harmonics.
Similarly, the power method worked best for baseflow W series. Has 38 harmonics

(+) For the bankfull flow W series, because it has a trend, it isn't as good, but the power method is still quite good.

3. Run RB and generate ASCII DEM
(1) Run "RB_run.py" to run riverbuilder
	- Specify the folder name and input txt file name
(2) Run "RB_to_terrain.py" to create points, DEM, ASCII DEM
