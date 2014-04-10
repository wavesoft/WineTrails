from django.db import models
from django.contrib.auth.models import User

#:
#: Indexing information for Country 
#:
class Country(models.Model):

	name = models.CharField(max_length=128)

	complete = models.BooleanField(default=False)
	borders = models.TextField(blank=True)

	def __unicode__(self):
		return self.name

#:
#: Indexing information for Region 
#:
class Region(models.Model):

	name = models.CharField(max_length=128)

	complete = models.BooleanField(default=False)
	zipCode = models.IntegerField()
	country = models.ForeignKey(Country, blank=True, default=None)

	def __unicode__(self):
		return self.name + " (" + str(self.country) + ")"

#:
#: User profile
#: 
class Profile(models.Model):
	user = models.ForeignKey(User, unique=True)

	name = models.CharField(max_length=128)
	surname = models.CharField(max_length=128)

	address = models.CharField(max_length=128)
	country = models.ForeignKey(Country)
	region = models.ForeignKey(Region)

	phoneFixed = models.CharField(max_length=128, blank=True)
	phoneMobile = models.CharField(max_length=128, blank=True)
	email = models.EmailField()

	def __unicode__(self):
		return str(self.user)

#:
#: The wine type
#: (Ex. Rose, Sparkly, etc.)
#:
class WineType(models.Model):

	name = models.CharField(max_length=128)
	description = models.TextField()

	def __unicode__(self):
		return self.name

#:
#: The wine variety
#: (Ex. grapes)
#:
class WineVariety(models.Model):

	name = models.CharField(max_length=128)
	description = models.TextField()

	def __unicode__(self):
		return self.name
	
#:
#: The aging technique used by this model
#: (Ex. wooden barrels)
#:
class WineAgingType(models.Model):

	name = models.CharField(max_length=128)
	description = models.TextField()

	def __unicode__(self):
		return self.name

#:
#: The wine color
#: (Ex. rose, red)
#:
class WineColor(models.Model):

	name = models.CharField(max_length=128)
	description = models.TextField()

	def __unicode__(self):
		return self.name

#:
#: The wine character
#:
class WineCharacter(models.Model):

	name = models.CharField(max_length=128)
	description = models.TextField()

	def __unicode__(self):
		return self.name

#:
#: The wine aroma
#:
class WineAroma(models.Model):

	name = models.CharField(max_length=128)
	description = models.TextField()

	def __unicode__(self):
		return self.name

#:
#: The wine test (to the untrained mouth)
#:
class WineTaste(models.Model):

	name = models.CharField(max_length=128)
	description = models.TextField()

	def __unicode__(self):
		return self.name

#:
#: The wine instance
#:
class Wine(models.Model):

	# Short representations
	name = models.CharField(max_length=128)

	# Details for the wine itself
	wineType = models.ForeignKey(WineType)
	wineVariety = models.ForeignKey(WineVariety)
	wineAging = models.ForeignKey(WineAgingType)
	wineColor = models.ForeignKey(WineColor)
	wineCharacter = models.ForeignKey(WineCharacter)
	wineAroma = models.ForeignKey(WineAroma)
	wineTaste = models.ForeignKey(WineTaste)


	def __unicode__(self):
		return self.name

#:
#: The stockpile of the 
#:
class WineBottle(models.Model):

	wine = models.ForeignKey(Wine)
	year = models.IntegerField()

	def __unicode__(self):
		return unicode(self.wine) + u" of " + unicode(self.year)

#:
#: The Wine Maker
#:
class WineMaker(models.Model):
	
	name = models.CharField(max_length=128)
	address = models.TextField()

	country = models.ForeignKey(Country)
	region = models.ForeignKey(Region)

	lat = models.FloatField()
	lng = models.FloatField()

	wines = models.ManyToManyField(WineBottle, related_name="bottle")

	def __unicode__(self):
		return self.name

class ReservationSlotRequest(models.Model):

	REPEAT_MODEL = (
		(' ', 'None'),
		('D', 'Daily'),
	    ('W', 'Weekly'),
	    ('M', 'Monthly'),
	    ('Y', 'Yearly')
	)

	start = models.DateTimeField()
	end = models.DateTimeField()

	responsible = models.ForeignKey(Profile)
	winery = models.ForeignKey(WineMaker)

	repeatModel = models.CharField(choices=REPEAT_MODEL, max_length=1, default=" ")
	repeatInfo = models.TextField()

	def __unicode__(self):
		return str(self.winery)

class ReservationSlot(models.Model):

	request = models.ForeignKey(ReservationSlotRequest)
	start = models.DateTimeField()
	end = models.DateTimeField()

	people = models.IntegerField()

	def __unicode__(self):
		return "%s (%s - %s) [%i]" % (str(self.request), str(self.start), str(self.end), self.people)

class ReservationFill(models.Model):

	# Info for the reservation
	slot = models.ForeignKey(ReservationSlot)

	# Responsible person
	responsible = models.ForeignKey(Profile)
	people = models.IntegerField()
