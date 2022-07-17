from os import PathLike
from typing import List, Union

import pandas as pd
from fastapi import File
from pandas import DataFrame
from pandas._typing import ReadCsvBuffer
from pydantic import Field


async def clean_data(
        data: Union[str, PathLike[str], ReadCsvBuffer[bytes], ReadCsvBuffer[str]] = File(...),
        to_drop: List[str] = [],
        remove_null_percent: Union[float, None] = Field(
            None, gt=0, le=100
        ),
) -> DataFrame:
    """
    Do some data cleaning and return a DF.
    This is just a generic example and data cleaning depends on the data itself
    and needs to be explored before cleaning
    :param data: a csv file with data
    :param to_drop: a list of columns to drop
    :param remove_null_percent: columns with this percentage of nulls will be removed

    :return: Dataframe with clean data
    """

    # Read the csv file into a pandas data frame
    df = pd.read_csv(data)

    if remove_null_percent:
        for col in df.columns:
            if df[col].is_null().sum()*100/len(df) > remove_null_percent:
                to_drop.append(col)

    # drop all user_defined and percentage checked columns
    if to_drop:
        df.drop(columns=to_drop, inplace=True)

    # for the other columns, fill data mean of the column
    df.fillna(df.mean(), inplace=True)

    # lets may be split birth_date(assuming it exists) into date, month and year
    df[['date', 'month', 'year']] = df['birth_date'].str.split('/', expand=True)

    # we can do a bunch of other things... like manipulate string columns, create hybrid columns, substitute missing data.


    return df
