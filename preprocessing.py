import pickle


def load_model(pth,vec):
    loaded_model = pickle.load(open(pth,'rb'))
    loaded_vec = pickle.load(open(vec,'rb'))
    return loaded_model,loaded_vec

