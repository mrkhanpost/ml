%config IPCompleter.greedy=True

def file_download(hurl=url , hpath=filepath):
    if not os.path.isdir(hpath):
        os.makedirs(hpath)

    tgzfile = os.path.join(filepath, "housing.tgz")
    urllib.request.urlretrieve(url, tgzfile)
    fl =  tarfile.open(tgzfile)
    fl.extractall (path=filepath)
    fl.close()
    

def load_housing_data(path=filepath, name="housing.csv"):
    file = os.path.join(path, name)
    return pd.read_csv(file)
    
