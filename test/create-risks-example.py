import eav
from risks.models import Risk
from eav.models import Value, Attribute, EnumValue, EnumGroup
from django.utils import timezone


eav.register(Risk)

# create attributes
# text, number, date, or enum
weight_att = Attribute.objects.create(name='Weight', datatype=Attribute.TYPE_FLOAT)
height_att = Attribute.objects.create(name='Height', datatype=Attribute.TYPE_INT)
birth_att = Attribute.objects.create(name='Birthdate', datatype=Attribute.TYPE_DATE)
breed_att = Attribute.objects.create(name='Breed', datatype=Attribute.TYPE_TEXT)

yes = EnumValue.objects.create(value='Yes') # doctest: SKIP
no = EnumValue.objects.create(value='No')
unkown = EnumValue.objects.create(value='Unkown')
ynu = EnumGroup.objects.create(name='Yes / No / Unkown')
ynu.enums.add(yes, no, unkown)

castrated_att = Attribute.objects.create(
    name='Is castrated?', datatype=Attribute.TYPE_ENUM, enum_group=ynu)

risk = Risk()
risk.name = 'Cat'
risk.eav.weight = 5.25
risk.eav.height = 12
risk.eav.birthdate = timezone.now()
risk.eav.breed = 'Persian Cat'
risk.eav.is_castrated = yes
risk.save()
risk.eav.get_values()

risk = Risk()
risk.name = 'Dog'
risk.eav.weight = 4.19
risk.eav.height = 11
risk.eav.birthdate = timezone.now()
risk.eav.breed = 'Bulldog'
risk.eav.is_castrated = no
risk.save()

Attribute.objects.create(name='Marketprice', datatype=Attribute.TYPE_FLOAT)
Attribute.objects.create(name='Year', datatype=Attribute.TYPE_INT)
Attribute.objects.create(name='Purchase', datatype=Attribute.TYPE_DATE)

risk = Risk()
risk.name = 'Motorcycle'
risk.eav.marketprice = 5678.99
risk.eav.year = 1998
risk.eav.purchase = timezone.now()
risk.save()
