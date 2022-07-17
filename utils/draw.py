import cv2


def draw(img, bbox: list[float, float, float, float]):
    """
    Method to draw bounding box on an image.
    :param img: image to draw the box on
    :param bbox: bounding box x, y, width, height coordinates
    :return:
    """
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x, y), ((x + w), (y + h)), (0, 255, 255), 3, 1)
