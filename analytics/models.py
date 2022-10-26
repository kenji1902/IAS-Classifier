from email.policy import default
from pprint import pprint
from django.db import models
import json
# Create your models here.
class plantreports(models.Model):
    date = models.DateField(auto_now=True,primary_key=True)
    data_date_start = models.DateField()
    data_date_end = models.DateField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    chartdata = models.TextField(blank=True,null=True)
    active = models.BooleanField(default=True)

from django.db.models.signals import pre_save
from classifier.models import iasData, plantInformation
from django.dispatch import receiver
from classifier import constants as c
@receiver(pre_save, sender=plantreports)
def pre_save_votes(sender, instance,*args, **kwargs):
    print(instance.data_date_start)
    print(instance.data_date_end)
    iasdata = iasData.objects.filter(requestnum__date__gte=instance.data_date_start,
                                     requestnum__date__lte= instance.data_date_end)
    

    plants = {}
    ias = {}
    locationMapping = {}
    plant_List = plantInformation.objects.values_list('scientificName',flat=True)
    neighborMapping = {}
    result = None
    for element in iasdata:
        scientificName = element.scientificName.scientificName
        region = json.loads(element.reverseGeoLoc)['address']['region']
        neighbors = json.loads(element.seedlingDispersionAffectedAreas)

        # Plant Count
        if not plants.get(scientificName):
            plants[scientificName] = 1
        else:
            plants[scientificName] += 1
        
        # IAS Count
        if not ias.get(element.scientificName.invasiveType):
            ias[element.scientificName.invasiveType] = 1
        else:
            ias[element.scientificName.invasiveType] += 1

        # Plant per Region
        if not locationMapping.get(region):
            locationMapping[region] = {}
        if not locationMapping.get(region).get(scientificName):
            locationMapping[region][scientificName] = 1
        else:
            locationMapping[region][scientificName] += 1

        # if(neighborMapping)
        if neighbors:

            for value in neighbors:
                if value.get('tags').get('name'):
                    neighbor = value['tags']['name']
                    if not neighborMapping.get(region):
                        neighborMapping[region] = {}
                    if not neighborMapping.get(region).get(neighbor):
                        neighborMapping[region][neighbor] = 1
                    else:
                        neighborMapping[region][neighbor] += 1

        result = json.dumps({
            "plant_List": list(plant_List),
            "plants" : plants,
            "ias" : ias,
            "locationMapping" : locationMapping,
            "neighborMapping" : neighborMapping,
        }, indent=4)

    instance.chartdata = result


def json_load_byteified(file_handle):
    return _byteify(
        json.load(file_handle, object_hook=_byteify),
        ignore_dicts=True
    )

def json_loads_byteified(json_text):
    return _byteify(
        json.loads(json_text, object_hook=_byteify),
        ignore_dicts=True
    )

def _byteify(data, ignore_dicts = False):
    if isinstance(data, str):
        return data

    # If this is a list of values, return list of byteified values
    if isinstance(data, list):
        return [ _byteify(item, ignore_dicts=True) for item in data ]
    # If this is a dictionary, return dictionary of byteified keys and values
    # but only if we haven't already byteified it
    if isinstance(data, dict) and not ignore_dicts:
        return {
            _byteify(key, ignore_dicts=True): _byteify(value, ignore_dicts=True)
            for key, value in data.items() # changed to .items() for Python 2.7/3
        }

    # Python 3 compatible duck-typing
    # If this is a Unicode string, return its string representation
    if str(type(data)) == "<type 'unicode'>":
        return data.encode('utf-8')

    # If it's anything else, return it in its original form
    return data
