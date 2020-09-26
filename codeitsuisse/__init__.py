from flask import Flask
app = Flask(__name__)
import codeitsuisse.routes.square
import codeitsuisse.routes.sort
import codeitsuisse.routes.salad
import codeitsuisse.routes.clean_floor
import codeitsuisse.routes.revisitgeometry
import codeitsuisse.routes.fruitbasket
import codeitsuisse.routes.inventory
import codeitsuisse.routes.GMO
import codeitsuisse.routes.olympiad_of_babylon
import codeitsuisse.routes.contact_trace
import codeitsuisse.routes.cluster
import codeitsuisse.routes.social_distancing