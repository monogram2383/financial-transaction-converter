import pandas as pd

from config import logger
from src.abstractions.pipelines.pipeline_abstract import PipelineAbstract
from src.utils.currency_utils import convert_fiat
from src.utils.translation_utils import translate_to_en


class PipelineProcessPrivat24Transactions(PipelineAbstract):
    @staticmethod
    def execute(file):
        logger.info(f"[PRIVAT24] Begin processing transactions.")

        # load csv data as a pandas DataFrame. Skip first empty row
        df: pd.DataFrame = pd.read_csv(file, skiprows=1)
        logger.info(f"[PRIVAT24] Number of rows: {len(df)}")

        # drop unneeded columns
        df = df.drop(columns=["Картка", "Сума в валюті транзакції", "Валюта транзакції", "Валюта залишку"])

        # set needed column names
        df.columns = ["date", "category", "description", "amount", "currency", "balance"]

        # delete time from the "date" column (leave only date itself)
        df["date"] = pd.to_datetime(df["date"]).dt.date

        # translate category and description
        df["category"] = translate_to_en(df["category"].values)
        df["description"] = translate_to_en(df["description"].values)

        # convert to USD
        df["amount_USD"] = convert_fiat(amounts=df["amount"].values, dates=df["date"].values, from_="UAH", to_="USD")

        # reorder
        df = df[["date", "category", "description", "amount", "amount_USD", "currency", "balance"]]

        logger.info(f"[PRIVAT24] Finished processing transactions.")

        return df
