from django.template import Template,Context

names = ["Jey","Sathish","Pradeep"]

t = Template("Name is {{name}}")
for name in names:
    t.render(Context({"name":name}))