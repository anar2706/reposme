counties = ["Naxçıvan Muxtar Respublikası","Bakı şəhəri","Abşeron rayonu","Xızı rayon","Sumqayıt şəhəri", "Ağstafa rayonu","Daşkəsən rayonu","Gədəbəy rayonu","Goranboy rayonu","Göygöl rayonu","Qazax rayonu","Samux  rayonu","Şəmkir  rayonu","Tovuz rayonu","Gəncə  şəhəri","Naftalan şəhəri","Balakən rayonu","Qax rayonu","Qəbələ rayonu","Oğuz rayonu","Şəki şəhəri","Zaqatala rayonu","Astara rayonu","Cəlilabad rayonu","Lerik rayonu","Lənkəran şəhəri","Masallı rayon","Yardımlı rayonu","Şabran rayonu","Xaçmaz rayonu","Quba rayonu","Qusar rayonu","Siyəzən rayonu","Ağcabədi rayonu","Ağdaş rayonu","Bərdə rayonu","Beyləqan rayonu","Biləsuvar rayonu","Göyçay rayonu","Hacıqabul rayonu","İmişli rayonu","Kürdəmir rayonu","Neftçala rayonu","Saatlı rayonu","Sabirabad rayonu","Salyan rayonu","Ucar rayonu","Yevlax şəhəri","Zərdab rayonu","Şirvan şəhəri","Mingəçevir şəhəri","Ağdam rayonu","Tərtər rayonu","Xocavənd rayonu","Xocalı rayonu","Şuşa rayonu","Cəbrayıl rayonu","Füzuli rayonu","Xankəndi şəhəri","Kəlbəcər rayonu","Laçın rayonu","Qubadlı rayonu","Zəngilan  rayonu","Ağsu rayonu","İsmayıllı rayonu","Qobustan  rayonu","Şamaxı rayonu"]


import os
import sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blood_bank_project.settings')


import django
django.setup()


from region_app.models import County

for county in counties:
    County.objects.create(county=county)