from django.forms import ModelForm
from resume_builder.models import personalInfo

class StudentForm(ModelForm):
	class Meta:
		model = personalInfo
		fields = '__all__'