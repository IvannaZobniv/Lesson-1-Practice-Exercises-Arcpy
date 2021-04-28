
# Import arcpy module
import arcpy


# Local variables:
Precip2008Readings = "D:\\MY\KNU\\3_COURSE\\2_Semertr\\Programing_GIS\\My_work\Arcpy\\Programming_in_GIS_2021_L5_materials\\Lesson1\\Nebraska.gdb\\Precip2008Readings"
IDW = "D:\\MY\KNU\\3_COURSE\\2_Semertr\\Programing_GIS\\My_work\Arcpy\\Programming_in_GIS_2021_L5_materials\\Lesson1\\Nebraska.gdb\\IDW"
Reclassify = "D:\\MY\KNU\\3_COURSE\\2_Semertr\\Programing_GIS\\My_work\Arcpy\\Programming_in_GIS_2021_L5_materials\\Lesson1\\Nebraska.gdb\\Reclassify"
Vector = "D:\\MY\KNU\\3_COURSE\\2_Semertr\\Programing_GIS\\My_work\Arcpy\\Programming_in_GIS_2021_L5_materials\\Lesson1\\Nebraska.gdb\\Vector"
Nebraska = "D:\\MY\KNU\\3_COURSE\\2_Semertr\\Programing_GIS\\My_work\Arcpy\\Programming_in_GIS_2021_L5_materials\\Lesson1\\Nebraska.gdb\\Nebraska"
Cordon = "D:\\MY\KNU\\3_COURSE\\2_Semertr\\Programing_GIS\\My_work\Arcpy\\Programming_in_GIS_2021_L5_materials\\Lesson1\\Nebraska.gdb\\Cordon"

# Process: IDW
arcpy.gp.Idw_sa(Precip2008Readings, "RASTERVALU", IDW, "1850,46467", "2", "VARIABLE 12", "")

# Process: Reclassify
arcpy.gp.Reclassify_sa(IDW, "VALUE", "27715,960938 57484,319210 1;57484,319210 80383,056342 2;80383,056342 111132,789063 3", Reclassify, "DATA")

# Process: Raster to Polygon
arcpy.RasterToPolygon_conversion(Reclassify, Vector, "SIMPLIFY", "VALUE")

# Process: Clip
arcpy.Clip_analysis(Vector, Nebraska, Cordon, "")
