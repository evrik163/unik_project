import pandas as pd
from joblib import dump
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier




def start_train():
    engine = create_engine('postgresql://postgres:123@172.17.01:1234/unik_db')
    df = pd.read_sql_query('select * from "fin"', con=engine)
    df = df.drop(["index","blue", "clock_speed", "dual_sim", "fc", "four_g", "m_dep", "n_cores", "pc", "px_height", "px_width", "ram", "sc_h", "sc_w", "talk_time", "three_g", "touch_screen", "wifi"], axis=1)

    y = df["price_range"]
    X = df.drop("price_range", axis=1)

    x_train, x_val, y_train, y_val = train_test_split(X, y, test_size=0.20, random_state=42)
    gbc = GradientBoostingClassifier(n_estimators=300,
                                 learning_rate=0.05,
                                 random_state=100)
    model = gbc.fit(x_train, y_train)
    model.predict([[1,2,3]])
    dump(model, './machine_learning/final.joblib')

start_train()
