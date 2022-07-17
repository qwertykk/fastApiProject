import pickle

from pandas import DataFrame
from pydantic.typing import PathLike


async def run_model(model_file: PathLike, data: DataFrame) -> DataFrame:
    """
    a simple function to use a custom model to predict on a data.
    :param model_file: path to model file
    :param data: X data
    :return: Y data
    """
    # load the model
    model = pickle.load(open(model_file, "rb"))

    # use model to predict
    return model.predict(data)

async def transfer_learn_custom_model(
    model_file: PathLike,
    data_X: DataFrame,
    data_Y: DataFrame,
    write_file: PathLike = None
) -> None:
    """
    Re-train a custom model based on new input.
    :param model_file: path to model file
    :param data_X:
    :param data_Y:
    :param write_file: a file in which to write the retrained model in.
        If None, model will be rewritten to the original file.
    :return: None
    """

    # load the model
    model = pickle.load(open(model_file, "rb"))

    # fit the model to the new data
    model.fit(data_X, data_Y)

    # if there is a rewrite_file, write the newly trained model to it.
    if write_file:
        model_file = write_file

    # write back to model_file
    pickle.dump(model, open(model_file, 'wb'))


async def score_on_a_model(
    model_file: PathLike,
    Y_original: DataFrame,
    Y_predicted: DataFrame
) -> float:
    """
    A simple function to score the given custom model
    :param model_file: the path to the custom model file
    :param Y_original: x_test
    :param Y_predicted: y_test
    :return: the r2_square prediction of the model
    """
    # load the model
    model = pickle.load(open(model_file, "rb"))

    # score on the model
    #TODO: Add more params and support to other scoring models.
    return model.score(Y_original, Y_predicted)