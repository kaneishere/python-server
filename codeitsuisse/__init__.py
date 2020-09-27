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
# import codeitsuisse.routes.olympiad_of_babylon
import codeitsuisse.routes.contact_trace
import codeitsuisse.routes.cluster
import codeitsuisse.routes.social_distancing
import codeitsuisse.routes.optimizedportfolio
#import codeitsuisse.routes.slsm
#import codeitsuisse.routes.bored_scribe
# import codeitsuisse.routes.bored_scribe_copy
import codeitsuisse.routes.snakeladder
import codeitsuisse.routes.tem
import codeitsuisse.routes.bucket_fill