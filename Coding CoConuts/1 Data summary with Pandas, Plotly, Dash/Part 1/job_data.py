import pandas as pd
import numpy as np

def ship_type(ship_str):
    """
    if it less than 50, 
    then it means it is ARG type,
    but if it is greater or equal than 50
    then it means it is CRO type.
    """
    if not ship_str.lower().startswith("ship"):
        return "-"
    
    ship_type = int(ship_str.split()[1])
    
    if ship_type < 50:
        return "ARG"
    
    return "CRO"

def get_worker_names(dataframe):
    # Get unique worker names
    worker_collabs = dataframe["Workers"].unique()
    workers = []
    for collab in worker_collabs:
        for worker in collab.split("|"):
            worker = worker.strip()
            workers.append(worker)
    workers = list(set(workers))
    return workers

def create_df():
    source_df = pd.read_csv(r"rlzd.csv").set_index("S.NO")
    new_df = pd.DataFrame()
    new_df["Equipment"] = source_df["2. Equipo"]
    new_df.insert(1, "Ship Type", new_df["Equipment"].map(ship_type))
    new_df["Job type"] = source_df["4. Tipo de tarea"]
    new_df["Category"] = source_df["5. Categoría técnica"]
    new_df["Workers"] = source_df["7. Participante adicional"]
    
    # Add worker names columns
    worker_names = get_worker_names(new_df)
    for worker in worker_names:
        new_df[worker] = np.where(\
            new_df["Workers"].astype(str).\
            str.contains(worker, regex=False), 1, 0)
        
    return new_df
        

def create_summary_df(source_df):
    worker_names = get_worker_names(source_df)
    return pd.DataFrame(source_df.groupby("Equipment", as_index=False)[worker_names].sum())

def create_datatable_df(source_df, worker_names):
    return pd.DataFrame(source_df.groupby(["Equipment", "Ship Type"], as_index=False)[worker_names].sum())

def save_to_csv(df, name, encoding="utf-8"):
    df.to_csv(name, encoding=encoding)

if __name__ == "__main__":
    source_df = create_df()
    worker_names = get_worker_names(source_df)
    summary_df = pd.DataFrame(source_df.groupby(["Equipment"], as_index = False)[worker_names].sum())
    datatable_df = create_datatable_df(source_df, worker_names)
    
    save_to_csv(summary_df, r"Summary.csv")
    save_to_csv(datatable_df, r"Datatable.csv")
    
    
    
    
    
    
    
    
    
    

