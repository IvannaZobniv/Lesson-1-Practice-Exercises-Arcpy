
import arcpy
arcpy.env.overwriteOutput = True
try:
    foxlake = arcpy.GetParameterAsText(0)
    FoxLake_contours2_shp = "D:\\MY\\KNU\\3_COURSE\\2_Semertr\\Programing_GIS\\My_work\\Arcpy\\Programming_in_GIS_2021_L5_materials\\Lesson1\\FoxLake_contours2.shp"
    
    arcpy.AddMessage("All done!")
except:
    arcpy.AddError("Could not complete the vector model")
    arcpy.AddMessage(arcpy.GetMessages())
arcpy.gp.Contour_sa(foxlake, FoxLake_contours2_shp, "25", "0", "1")



