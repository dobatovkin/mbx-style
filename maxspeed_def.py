maxspeed_dict = dict(
    motorway=120,
    motorway_link=60,
    trunk=90,
    trunk_link=60,
    primary=80,
    primary_link=60,
    secondary=60,
    secondary_link=40,
    tertiary=40,
    tertiary_link=20,
    residential=40,
    living_street=20,
    service=20,
    unclassified=20,
    construction=15
)

def maxspeed_def(highway):
    result=maxspeed_dict.get(highway)
    if result == None:
        return 0
    else:
        return result
