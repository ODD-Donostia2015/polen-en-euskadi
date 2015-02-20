# -*- coding: utf-8 -*-

import csv
import sys
from dateutil import parser
from polen.models import *

def replaceMonth(date):
	months = {u'Ene': u'Jan', u'Abr': 'Apr', u'Ago': u'Aug', u'Dic': u'Dec'}

	for key, value in months.items():
		date = date.replace(key, value)

	return date

def load(file, sensor_name):
	with open(file, 'rb') as csvfile:
		reader = csv.reader(csvfile, delimiter=';')

		reader.next()
		header = reader.next()

		year = header[0].replace(',', '.')

		sensor = Sensor.objects.get(name=sensor_name)

		for row in reader:	
			month = replaceMonth(row[0])
			date = parser.parse(month + ' ' + year, fuzzy=False, default=None)

			for index, value in enumerate(row[2:]):
				print header[index + 2]
				allergen = Allergen.objects.get(pollen_type=header[index + 2])

				m = Measurement(date=date, allergen=allergen, sensor=sensor, value=value)
				m.save()
