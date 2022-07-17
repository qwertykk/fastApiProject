# fastapi imports
from fastapi import APIRouter, UploadFile

# OpenCV tools
import cv2
import cvzone

# typings
from typing import Union

from sklearn.model_selection import train_test_split
from urllib3.util import Url
from pydantic.typing import PathLike

# code imports
from data.enums.schema_examples import OPENCV_OBJECT_TRACKERS
from utils.clean_data import clean_data
from utils.draw import draw
from utils.run_model import run_model, transfer_learn_custom_model, score_on_a_model

router = APIRouter()


@router.post("/upload-file")
async def say_hello(
    files: list[UploadFile] = None
) -> dict:
    """
    Just a simple method that accepts a bunch of files from Front End.
    :param files: files from FE
    :return: random json for now
    """
    for file in files:
        print(file)
    print("I can print")
    return {"head": "worker"}


@router.get("/tracker")
async def track_horses(
    video: Union[PathLike, Url, UploadFile] = None,
    tracker: OPENCV_OBJECT_TRACKERS = 'kcf',
):
    """
    NOTE: This method doesn't work yet since the data loader doesn't do much.
    Simple endpoint to track objects in a video based on a certain numer of options.
    :param video: the video file or path to video file
    :param tracker: specify a tracker from accepted list
    :return: None
    """


    tracker = OPENCV_OBJECT_TRACKERS[tracker]()

    if video is None:
        video = "../static/videos/horse_race.mp4"

    cap = cv2.VideoCapture(video)

    f = []
    fpsr = cvzone.FPS()
    success, img = cap.read()

    bbox = cv2.selectROI("output", img, False)

    while True:
        success, img = cap.read()
        cv2.imshow("output", img)
        k = cv2.waitKey(1)
        if k == 27:  # press "ESC" key to exit
            break

        bbox = cv2.selectROI("output", img, False)
        tracker.init(img, bbox)
        success, bbox = tracker.update(img)
        if success:
            draw(img, bbox)  # we will write this UDF later
        else:
            cv2.putText(img, "lost", (75, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

    # TODO return some thing back
    return None

@router.post("/run_custom_model")
async def data_cleaning(
    csv_file: Union[PathLike, Url, UploadFile] = None,
    model_file: Union[PathLike, Url] = None,
    retrain: bool = False
):
    """
    A simple example of running a csv file on a custom model.
    :param csv_file: csv file (path/url/file)
    :param model_file: (path/url)
    :param retrain: boolean to check if the model should be retrained,

    :return: the predicted score for the file
    """
    # clean the data
    df = await clean_data(csv_file)

    # split to test and train
    x, y = df[:, 0:2]

    # retrain only if user says so.
    if retrain:
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

        # retrain the model
        await transfer_learn_custom_model(model_file, x_train, y_train)
    else:
        x_test, y_test = x, y

    # score on the new model
    predictions = await run_model(model_file, x_test)

    return await score_on_a_model(model_file, y_test, predictions)





