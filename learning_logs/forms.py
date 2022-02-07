from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
	"""A simple form for topics."""
	class Meta:
		model = Topic
		fields = ['text']
		labels = {'text': ''}

class EntryForm(forms.ModelForm):
	"""A simple form for entries."""
	class Meta:
		model = Entry
		fields = ['text']
		labels = {'text': 'Entry:'}
		widgets = {'text': forms.Textarea(attrs={'cols': 80})}