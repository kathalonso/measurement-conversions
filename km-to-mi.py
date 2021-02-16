#define class, instantiate, use to convert km to miles
class KMToMilesConverter:
  miles_per_km = 0.6213
  def how_many_mi(self, kms):
    return kms * self.miles_per_km
 
converter = KMToMilesConverter()
mi_in_10_km = converter.how_many_mi(10)
print(mi_in_10_km)
# prints "6.21371192"
