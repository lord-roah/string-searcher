
def string_capture(point1,point2,searchstring):
    pos1=searchstring.find(point1)+ len(point1)
    pos2=searchstring.find(point2)
    captured=searchstring[pos1:pos2]
    return captured

