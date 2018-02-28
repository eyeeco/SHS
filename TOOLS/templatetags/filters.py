from django import template

register = template.Library()


@register.filter('addcls')
def addcls(field, cls):
    attr = cls.split(" ")
    return field.as_widget(attrs={"class": attr[0], "placeholder": attr[1]})
