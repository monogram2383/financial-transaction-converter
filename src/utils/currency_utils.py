import numpy as np

from config import logger


def convert_fiat(amounts: list[float], dates: list[str], from_="UAH", to_="USD") -> list[float]:
    logger.info(
        f"[CURRENCY CONVERSION] Beginning convertion of {len(amounts)} fiat transactions from {from_} to {to_}:")

    # converted_amounts = []
    # for amount, date in tqdm(zip(amounts, dates), desc="Converting...", leave=True):
    #     try:
    #         converted_amounts.append(
    #             fiat_converter.convert(from_, to_, amount, date)
    #         )
    #     except Exception as e:
    #         logger.error(f"[CURRENCY CONVERSION] Failed to convert currency: {e}")
    #         return [np.nan] * len(amounts)

    # TODO: fix with a new API
    converted_amounts = [np.nan] * len(amounts)
    logger.info(f"[CURRENCY CONVERSION] Conversion finished")
    return converted_amounts
