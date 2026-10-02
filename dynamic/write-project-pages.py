TAGS = [
("Predictive modelling", "used {lowername}", """Predictive modelling is the classic tool of artificial intelligence and machine learning.
Predictive modelling is most often classification (automatically putting data into known categories) or regression (automatically estimating some target quantity for each data point).
There are several challenges in predictive modelling relating to how to best exploit information to predict a target, how to measure how well a system predicts and whether it is successful, and how to measure the confidence of the system in its predictions."""),
("Description and basic visualization", "used {lowername}", """"""),
("Inferential modelling", "used {lowername}", """"""),
("Time series", "used {lowername} analysis and modelling", """"""),
("Creative visualization", "used {lowername}", """"""),
("Data-store development", "used {lowername}", """"""),
("Language as data", "worked with {lowername}", """"""),
("Data linkage", "used {lowername}", """"""),
("Data collection", "used {lowername} and curation", """"""),
("Software", "delivered {lowername}", """Our projects often involve developing and delivering software.

This may be a web app, such as a data mangement tool. It may be a data collection or analysis tool that runs repeatedly. Or it migth be a script that the client can run several times to perform modelling, prediction, simulation or visualisation.

We mostly develop software in Python or R, together with backend technologies such as SQL and frontend technologies like JavaScript/HTML and even Excel! We may employ one of several software frameworks such as R Shiny, Django, Scientific Python and AngularJS.
"""),
("Report", "delivered a {lowername}", """"""),
("Transformed data", "delivered {lowername}", """"""),
("Paper", "delivered a contribution to a {lowername}", """"""),
("Verbal advice", "delivered {lowername}", """"""),
("Web app", "delivered {lowername}", """"""),
]

TPL = '''+++
title = "Projects : %(name)s"
draft = false
type = "nosidebar"
+++

%(descr)s

Below we showcase several projects in which SIH has %(delivery)s.
<a href="/projects">See all projects.</a>

{{< project adminMode="0" tagFilter="%(name)s" >}}'''


for name, delivery, descr in TAGS:
    delivery = delivery.replace('{lowername}', name.lower())
    slug = name.lower().replace(' ', '_')
    with open('content/projects/{}.md'.format(slug), 'w') as f:
        print(TPL % dict(name=name, delivery=delivery, descr=descr),
              file=f)
