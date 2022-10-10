fileName = "IASleavesv8"
Path = "static/classifier/classification_models"

class_names = [
  'Basella Alba',
  'Broussonetia papyrifera',
  'Chromolaena odorata',
  'Leucaena leucocephala',
  'Swietenia Macrophylla',
  'Gmelina arborea',
  'Muntingia Calabura',
  'Plectranthus Amboinicus',
  'Pongamia Pinnata',
  'Psidium Guajava',
  'Syzygium Jambos',
]

CNNModel = f'{fileName}.h5'
CNNModelPath = f'{Path}/CNN/{CNNModel}'

kNNModel = f'{fileName}.pkl'
kNNModelPath = f'{Path}/kNN/{kNNModel}'
