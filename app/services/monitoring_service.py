import os

import pandas as pd

from pandas.errors import EmptyDataError

from app.core.config import LOG_PATH


def log_interaction(data):

    os.makedirs("app/logs", exist_ok=True)

    df_new = pd.DataFrame([data])

    try:

        if os.path.exists(LOG_PATH):

            df_existing = pd.read_csv(LOG_PATH)

            df = pd.concat(
                [df_existing, df_new],
                ignore_index=True
            )

        else:

            df = df_new

    except EmptyDataError:

        df = df_new

    df.to_csv(LOG_PATH, index=False)