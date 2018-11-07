from math import sin, cos, atan2, sqrt, radians

EARTH_RADIUS_IN_METERS = 6371000


def distance(start, end):
    startLatitude = radians(start.latitude)
    startLongitude = radians(start.longitude)
    endLatitude = radians(end.latitude)
    endLongitude = radians(end.longitude)
    distanceLatitude = endLatitude - startLatitude
    distanceLongitude = endLongitude - startLongitude

    angle = sin(distanceLatitude / 2) * sin(distanceLatitude / 2) + \
            cos(startLatitude) * cos(endLatitude) * \
            sin(distanceLongitude / 2) * sin(distanceLongitude / 2)

    radDistance = 2 * atan2(sqrt(angle), sqrt(1 - angle))

    return EARTH_RADIUS_IN_METERS * radDistance


def bearing_rad(start, end):
    startLatitude = radians(start.latitude)
    startLongitude = radians(start.longitude)
    endLatitude = radians(end.latitude)
    endLongitude = radians(end.longitude)

    y = sin(endLongitude - startLongitude) * cos(endLatitude)
    x = cos(startLatitude) * sin(endLatitude) - \
        sin(startLatitude) * cos(endLatitude) * \
        cos(endLongitude - startLongitude)
    return atan2(y, x)

'''
    FAI FS TOOL
    Class: Fs/FsGeo/GeoUtil.cs:1204 (cc4bc86d027fed6084dda7f484d059c1866379c3)
    https://en.wikipedia.org/wiki/Haversine_formula

      double rLon1 = GeoConst.DEG2RAD * dLon1;
      double rLat1 = GeoConst.DEG2RAD * dLat1;
      double rLon2 = GeoConst.DEG2RAD * dLon2;
      double rLat2 = GeoConst.DEG2RAD * dLat2;
      double distLon = rLon2 - rLon1;
      double distLat = rLat2 - rLat1;
      double a
        = Math.Sin(distLat / 2)
        * Math.Sin(distLat / 2)
        + Math.Cos(rLat1)
        * Math.Cos(rLat2)
        * Math.Sin(distLon / 2)
        * Math.Sin(distLon / 2);
      // distance in radians
      double c = 2 * Math.Atan2(Math.Sqrt(a), Math.Sqrt(1 - a));
      // const int EARTHRADIUS = 6367000; // earth radius in meters taken from  http://www.census.gov/cgi-bin/geo/gisfaq?Q5.1
      const int EARTHRADIUS = 6371000; // FAI def. SC gen. section 7.3.1.1
      // const int EARTHRADIUS = 6378137; // WGS84 Semi major axis(a):
      // const int EARTHRADIUS = 6390000;    // Garmin seems to use this radius for the earth
      // distance in meters
      return EARTHRADIUS * c;
'''
