from django.db import models
import pandas as pd

class Dataset(models.Model):
	name = models.CharField(max_length=256)
	created = models.DateTimeField(auto_now_add=True)
	content = models.TextField()
	
	def save(self, *args, **kwargs):
		df = pd.read_csv(self.content)
		self.content = df.to_json(orient='records')
		return super(Dataset, self).save(*args, **kwargs)
	
