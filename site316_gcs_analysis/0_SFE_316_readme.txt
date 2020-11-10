# Site 316 notes

### 1. How to generate W_bf series ###

(0) Create a centerline of bankfull polygon (Using ET or manually)
(1) Create Station Lines (Using ET: Miscellaneous > Create Station Lines)
	- Distance = 2 m
(2) Clip polylines generated in (1)with bankfull polygon (Using ArcGIS)
(3) Buffer the clipped polylines (Using ET: Polyine > Buffer Polylines)
	- Distance = 1 m
	- Flat end, Both side

### 2. Making RB Input txt file ###

(1) Obtain elevation (Z) and width (W_base, W_bf) series.
(2) Copy and paste (1) to RiverBuilder metrics excel file along with the distance. 
	- Specify whether the series is from down station or from up station.
(3) For Z, do a linear regression and obtain detrended elevation, Zd.
(4) For W, divided the values by 2.
(5) Copy and paste the distance, Zd, Wb/2, and Wbf/2 to a site-specific .csv file, e.g. SFE_316_series.csv.
(6) Follow the steps in "cheatsheet" in the main RB folder.

(+) From Xavier's analysis of baseflow Zd, it looks like the "power method" performed best at matching the overall pool-riffle morphology in terms of total amplitude. This is the one with 8 harmonics.
Similarly, the power method worked best for baseflow W series. Has 38 harmonics

(+) For the bankfull flow W series, because it has a trend, it isn't as good, but the power method is still quite good.
