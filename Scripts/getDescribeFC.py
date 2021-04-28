# Opens a feature class from a geodatabase and prints the spatial reference
 
import arcpy
 
featureClass = r"D:\Seva2\2013-14\2015-2016\ProgramGIS\2018\5\PE\Lesson1\StateBoundaries.lyr"
 
# Describe the feature class and get its spatial reference   
desc = arcpy.Describe(featureClass)

print ("Describe object was created")

spatialRef = desc.spatialReference # Dataset

# Print the spatial reference name
print (spatialRef.Name) # spatialReference
print (desc.lengthFieldName) # GDBFeatureClass
print (desc.shapeType) # FeatureClass

