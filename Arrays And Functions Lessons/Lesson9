import math
def Pow(a, b):
  return math.pow(a, b)

  
TdegC = -15 
windKPH = 30

def wc(TdegC, windKPH):
   """
    * Calculates the wind chill, given
    * TdegC: the temp in degrees C
    * windKPH: the wind speed in km/h
    *
    * Returns:
    * vTemp: Wind chill in degrees C
   """
   Tw = 0
   Tw = 13.2 + 0.6215 * TdegC
   Tw = Tw - 11.37 * Pow(windKPH, 0.16)
   Tw = Tw + 0.3965 * TdegC * Pow(windKPH, 0.16)

   return Tw

def WWarning(WindC):
  WindC = round(WindC)
  if WindC <= 0 and WindC >= -9:
    return("LowRisk")
  if WindC <= -10 and WindC >= -28:
    return("Moderate Risk Of Hypothermia")
  if WindC <= -29 and WindC >= -40:
    return("High Risk Of Frostbite")
  if WindC <= -41 and WindC >= -48:
    return("Severe Risk Of Frostbite: Exposed Skin Freezes In 5-10 Mins")
  if WindC <= -49 and WindC >= -55:
    return("Severe Risk Of Frostbite: Exposed Skin Freezes In 2-5 Mins")
  if WindC <= -55:
   return "Extreme risk: exposed skin freezes in under 2 minutes"


  
T = -5.0
W = 10.0
WC = (wc(T, W))
WCF = round(WC)
Warn = WWarning(WCF)

print("-------------------------------------")
print("WC=%6.3f T=%6.3f W=%6.3f km/h Waring: %s" % (WC, T, W, Warn))
print("-------------------------------------")
print("")

T = -20.0
W = 20.0
WC = (wc(T, W))
WCF = round(WC)
Warn = WWarning(WCF)

print("-------------------------------------")
print("WC=%6.3f T=%6.3f W=%6.3f km/h Waring: %s" % (WC, T, W, Warn))
print("-------------------------------------")
print("")

T = -45.0
W = 40.0
WC = (wc(T, W))
WCF = round(WC)
Warn = WWarning(WCF)

print("-------------------------------------")
print("WC=%6.3f T=%6.3f W=%6.3f km/h Waring: %s" % (WC, T, W, Warn))
print("-------------------------------------")
