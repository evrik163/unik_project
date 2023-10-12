import pandas as pd
import catboost as cb
from joblib import dump
from sqlalchemy import create_engine
from sklearn.model_selection import train_test_split


engine = create_engine('postgresql://postgres:123@localhost:5432/unik_db')


def start_train():
    df = pd.read_sql_query('select * from "final"', con=engine)
    df = df.drop(["index","blue", "clock_speed", "dual_sim", "fc", "four_g", "m_dep", "n_cores", "pc", "px_height", "px_width", "ram", "sc_h", "sc_w", "talk_time", "three_g", "touch_screen", "wifi"], axis=1)

    y = df["price_range"]
    X = df.drop("price_range", axis=1)

    x_train, x_val, y_train, y_val = train_test_split(X, y, test_size=0.20, random_state=42)
    pool_train = cb.Pool(x_train, y_train)
    model = cb.CatBoostRegressor(n_estimators=850, #число деревьев
                       loss_function='RMSE',
                       learning_rate=0.5,
                       depth=5, task_type='CPU', #глубина дерева
                       random_state=1,
                       verbose=False)

    model.fit(pool_train)
    dump(model, 'final.joblib')
