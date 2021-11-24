from DataGenerator import DataGenerator
import yaml

def load_definitions():
    # reading in feature/feature names 
    with open('references/definitions.yml') as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        definitions = yaml.load(file, Loader=yaml.FullLoader)

        features = definitions['features']
        spectators = definitions['spectators']
        labels = definitions['labels']

        nfeatures = definitions['nfeatures']
        nspectators = definitions['nspectators']
        nlabels = definitions['nlabels']
        ntracks = definitions['ntracks']
        return features,spectators,labels,nfeatures,nspectators,nlabels,ntracks

def process_data():
    # load in definitions 
    features, spectators, labels, nfeatures, nspectators, nlabels, ntracks = load_definitions()
    train_dir = ["data/raw/ntuple_merged_90.root"]

    train_generator = DataGenerator(train_dir, features, labels, spectators, batch_size=1024, n_dim=ntracks, 
                                remove_mass_pt_window=False, remove_unlabeled=True, max_entry=8000)

    # first index = train and labels; second index = jets (967 jets); third index = tracks (60); fourth index = features (48)
    # if each row represents a jet, would the pd.dataframe() have 967 rows with 60x48 columns? 
    train_1 = train_generator[0][0]
    labels_1 = train_generator[0][1]

    result_array = []
    for i in train_1:
        result_array.append(i.flatten())

    return result_array
