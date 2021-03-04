#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
import inspect
import json 

import ejerico_sdk.rdf.entity as my_module

#from ejerico_sdk.rdf.entity import Catalog,Concept,ConceptSchema
#from ejerico_sdk.rdf.entity import Dataset,Distribution,Document
#from ejerico_sdk.rdf.entity import Equipment,Entity
#from ejerico_sdk.rdf.entity import Frequency
#from ejerico_sdk.rdf.entity import Organization
#from ejerico_sdk.rdf.entity import Person,Project,PropertyValue
#from ejerico_sdk.rdf.entity import Relation
#from ejerico_sdk.rdf.entity import Spatial,Service
#from ejerico_sdk.rdf.entity import Temporal
#from ejerico_sdk.rdf.entity import Vcard

clazzes = [m[1] for m in inspect.getmembers(my_module, inspect.isclass) if issubclass(m[1], my_module.Entity) and m[1] != my_module.Entity]
for clazz in clazzes:
    #attributes = inspect.getmembers(entity, lambda a:not(inspect.isroutine(a)))
    template = {"_class": clazz.__name__}
    for attribute in sorted([d for d in clazz().__dict__ if not d.startswith('_')]):
        if "mapper" == attribute: continue
        template[attribute] = ""
    with open("template_{}.json".format(clazz.__name__.lower()), 'w') as template_file: json.dump(template, template_file, indent=4)



