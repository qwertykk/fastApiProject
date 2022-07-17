# System Imports
from enum import Enum

import cv2


class Schema1(str, Enum):
    example1 = "example1"
    example2  = "example2"

class OPENCV_OBJECT_TRACKERS():

    csrt = cv2.legacy.TrackerCSRT_create,
    kcf = cv2.legacy.TrackerKCF_create,
    boosting = cv2.legacy.TrackerBoosting_create,
    mil = cv2.legacy.TrackerMIL_create,
    tld = cv2.legacy.TrackerTLD_create,
    medianflow = cv2.legacy.TrackerMedianFlow_create,
    mosse = cv2.legacy.TrackerMOSSE_create

