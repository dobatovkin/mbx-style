x = "MyPoints"
f = "Value"
y = list()
with arcpy.da.SearchCursor(x,f) as cursor:
    for row in cursor:
        y.append(row[0])
z = sorted(y,reverse=True)[:10]

def top_ten_pc(fieldval):
    if fieldval in z:
        return True
    else:
        return False