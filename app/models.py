from django.db import models
from django.contrib import admin
import yaml

data = yaml.load(open("foo.yaml"))


def create_model(name, fields=None, app_label='', module='', options=None,
                 admin_opts=None, verbose_name=None, verbose_name_plural=None):
    """
    Create specified model
    """
    class Meta:
        pass

    if app_label:
        # app_label must be set using the Meta inner class
        setattr(Meta, 'app_label', app_label)

    if verbose_name is not None:
        setattr(Meta, 'verbose_name', verbose_name)

    if verbose_name_plural is not None:
        setattr(Meta, 'verbose_name_plural', verbose_name_plural)

    # Update Meta with any options that were provided
    if options is not None:
        for key, value in options.iteritems():
            setattr(Meta, key, value)

    # Set up a dictionary to simulate declarations within a class
    attrs = {'__module__': module, 'Meta': Meta}

    # Add in any fields that were provided
    if fields:
        attrs.update(fields)

    # Create the class, which automatically triggers ModelBase processing
    model = type(name, (models.Model,), attrs)

    # Create an Admin class if admin options were provided
    if admin_opts is not None:
        class Admin(admin.ModelAdmin):
            pass
        for key, value in admin_opts:
            setattr(Admin, key, value)
        admin.site.register(model, Admin)

    return model


class DynamicModelCreator:
    def __init__(self):
        pass

    def prepare_models(self, yaml_data):

        for obj in yaml_data.keys():

            model_name = obj
            fields = {}

            for field in yaml_data[obj]['fields']:

                if field['type'] == 'int':
                    fields[field['title']] = models.IntegerField(verbose_name=field['title'])
                elif field['type'] == 'char':
                    fields[field['title']] = models.CharField(max_length=255,
                                                              verbose_name=field['title'])
                elif field['type'] == 'date':
                    fields[field['title']] = models.DateField(verbose_name=field['title'])

            admin_opts = {}
            module = 'smyt'
            model = create_model(model_name,
                                 fields,
                                 # options=options,
                                 admin_opts=admin_opts,
                                 verbose_name=yaml_data[obj]['title'],
                                 verbose_name_plural=yaml_data[obj]['title'],
                                 app_label='app',
                                 module=module,)

            from smyt.settings import INSTALLED_APPS
            INSTALLED_APPS += (module,)


# print('++++++++++++')
a = DynamicModelCreator
a.prepare_models(a, data)
# print('++++++++++++')
