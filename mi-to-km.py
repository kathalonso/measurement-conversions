#define class, instantiate, use to convert miles to km
class MilesToKMConverter:
  kms_per_mile = 1.609
  def how_many_kms(self, miles):
    return miles * self.kms_per_mile
 
converter = MilesToKMConverter()
kms_in_5_miles = converter.how_many_kms(5)
print(kms_in_5_miles)
# prints "8.045"
