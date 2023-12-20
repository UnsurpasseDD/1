from django import template

register = template.Library()
censorwords = ["США", "еда", "La Isla Bonita", "ненавидят", 'Frozen']

@register.filter(name='censor')
def censor(value):
    for a in censorwords:
        b = str(a + ",")
        с = str(b.title())
        value = value.replace(a, "*****")
        value = value.replace(b, "*****")
        value = value.replace(с, "*****")
    return value

@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()