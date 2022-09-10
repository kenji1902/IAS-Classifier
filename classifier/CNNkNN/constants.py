fileName = "IASleavesv3"
Path = "static/classifier/classification_models"

class_names = [
  'Basella Alba (Basale)',
  'Bpapyrifera',
  'Hagonoy',
  'Ipil_ipil',
  'Mahogany',
  'Muntingia Calabura (Jamaica Cherry-Gasagase)',
  'Plectranthus Amboinicus (Mexican Mint)',
  'Pongamia Pinnata (Indian Beech)',
  'Psidium Guajava (Guava)',
  # 'Syzygium Jambos (Rose Apple)',
]

CNNModel = f'{fileName}.h5'
CNNModelPath = f'{Path}/CNN/{CNNModel}'

kNNModel = f'{fileName}.pkl'
kNNModelPath = f'{Path}/kNN/{kNNModel}'
