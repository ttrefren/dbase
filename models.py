from django.db import models
import datetime

def expand_choices_dict(choices):
    return tuple([(num, name) for num, name in choices.iteritems()])

def reverse_tuplize(choices):
    return tuple([(v, k) for k, v in choices.iteritems()])

class Model(models.Model):
    def save(self, *args, **kwargs):
        if not self.pk:
            if hasattr(self, 'created'):
                self.created = datetime.datetime.utcnow()
        if hasattr(self, 'last_modified'):
            self.last_modified = datetime.datetime.utcnow()
        return super(Model, self).save(*args, **kwargs)

    def refresh_from_db(self):
        """Refreshes this instance from db"""
        from_db = self.__class__.objects.get(pk=self.pk)
        fields = self.__class__._meta.get_all_field_names()

        #for each field in Model
        for field in fields:
            try:
                setattr(self, field, getattr(from_db, field)) #update this instances info from returned Model
            except AttributeError:
                pass

    class Meta:
        abstract = True

