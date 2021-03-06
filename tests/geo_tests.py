import util.geo as geo
import util.testingProfile
import math

def test_deltaTime_dateAware():
    '''
    make sure deltaTime is coping with real dates correctly
    '''

    # 2 days on a leap year:
    early = (2004, 2, 28, 0)
    late  = (2004, 3, 1, 0)

    diff = geo.deltaTime(early, late)
    assert diff == 172800., 'incorrect date difference on leap year'

    # 1 day on not a leap year:
    early = (2005, 2, 28, 0)
    late  = (2005, 3, 1, 0)

    diff = geo.deltaTime(early, late)
    assert diff == 86400., 'incorrect date difference on non-leap year'

    # 30 days in June:
    early = (2004, 6, 30, 0)
    late  = (2004, 7, 1, 0)

    diff = geo.deltaTime(early, late)
    assert diff == 86400., 'should only be 1 day between June 30 and July 1'

    # 31 days in July:
    early = (2004, 7, 30, 0)
    late  = (2004, 8, 1, 0)

    diff = geo.deltaTime(early, late)
    assert diff == 172800., 'should be 2 days between July 30 and August 1'

def test_deltaTime_times():
    '''
    make sure deltaTime is dealing with times correctly
    '''  

    # same day, same time:
    early = (2004, 2, 28, 0)
    late  = (2004, 2, 28, 0)

    diff = geo.deltaTime(early, late)
    assert diff == 0., 'incorrect time difference for identical dates and times'

    # same day, different time:
    early = (2004, 2, 28, 0)
    late  = (2004, 2, 28, 1.5)

    diff = geo.deltaTime(early, late)
    assert diff == 5400., 'incorrect time difference for identical dates and different times'


    # earlier time on later day
    early = (2005, 2, 27, 2)
    late  = (2005, 2, 28, 1)

    diff = geo.deltaTime(early, late)
    assert diff == 82800., 'incorrect time difference for earlier times but later days'

def test_haversineAngle():
    '''
    check some nominal behavior of great circle intersections.
    '''
    
    lat1 = 0
    lon1 = 10
    lat2 = 0
    lon2 = 20
    lat3 = 0
    lon3 = 30

    angle = geo.haversineAngle(lat1, lon1, lat2, lon2, lat3, lon3) 
    assert angle - math.pi < 0.000001, 'point on a circle had a non-zero angle between them: {}'.format(angle)

    lat3 = 90
    lon3 = 20
    angle = geo.haversineAngle(lat1, lon1, lat2, lon2, lat3, lon3)
    assert angle - math.pi/2 < 0.000001, 'orthogonal great circles had an angle of {} between them.'.format(angle)

def test_archaversine_domain():
    '''
    make sure archaversine does something sensible if it ends up with an argument of 1+epislon or -1-epsilon
    '''

    assert geo.arcHaversine(1.00000000000000004) == geo.arcHaversine(1.0), 'archaversine fooled by floating point problems'
