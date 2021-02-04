from django.db import models

class Examscore(models.Model):

	allsubject = (('คณิตศาสตร์','คณิตศาสตร์'),
				  ('เคมี','เคมี'),
				  ('ศิลป์','ศิลป์'),
				  ('อังกฤษ','อังกฤษ'),
				  ('ฟิสิกส์','ฟิสิกส์'),
				  ('ชีวะ','ชีวะ'))

	subject = models.CharField(max_length=50, choices=allsubject, default='math')
	student_name = models.CharField(max_length=30)
	score = models.IntegerField(default=0)

	def __str__(self):
		return self.student_name +'-'+ self.subject +'-'+ str(self.score)
class AllStudent(models.Model):
	levellist = (('ม.1','ม.1'),
				  ('ม.2','ม.2'),
				  ('ม.3','ม.3'),
				  ('ม.4','ม.4'),
				  ('ม.5','ม.5'),
				  ('ม.6','ม.6'))
	level = models.CharField(max_length=50, choices=levellist, default='ม.1')
	student_name = models.CharField(max_length=30)
	student_id = models.CharField(max_length=30)
	student_tel = models.CharField(max_length=30, blank=True, null=True)
	parent_name = models.CharField(max_length=30, blank=True, null=True)
	parent_tel = models.CharField(max_length=30, blank=True, null=True)
	other = models.TextField(blank=True, null=True)

	def __str__(self):
		return '[{}]{}'.format(self.student_id,self.student_name)
