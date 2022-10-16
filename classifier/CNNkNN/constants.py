fileName = "IASleavesv8"
Path = "static/classifier/classification_models"

class_names = [
  'Basella alba',
  'Broussonetia papyrifera',
  'Chromolaena odorata',
  'Leucaena leucocephala',
  'Swietenia macrophylla',
  'Gmelina arborea',
  'Muntingia calabura',
  'Plectranthus amboinicus',
  'Pongamia pinnata',
  'Psidium guajava',
  'Syzygium jambos',
]

CNNModel = f'{fileName}.h5'
CNNModelPath = f'{Path}/CNN/{CNNModel}'

kNNModel = f'{fileName}.pkl'
kNNModelPath = f'{Path}/kNN/{kNNModel}'
