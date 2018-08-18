import pytest
import os
import cv2
from femida_detect.imgparse import (
    crop_image,
    validate_qr_code,
    CroppedAnswers
)


def test_crop_image(jpg):
    cropped = crop_image(cv2.imread(jpg))
    pytest.helpers.save_image(cropped, 'test_crop_image', os.path.basename(jpg) + '.cropped.jpg')


@pytest.fixture('module')
def cropped(jpg):
    return crop_image(cv2.imread(jpg))


def test_validate_qr(cropped):
    dic = validate_qr_code(cropped)
    return


def test_recognized_positions(cropped, jpg):
    answers = CroppedAnswers(cropped)
    recognized = answers.recognized_rectangles_image()
    pytest.helpers.save_image(recognized, 'test_recognized_positions', os.path.basename(jpg) + '.recognized.jpg')
