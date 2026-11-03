# Machine Vision

Lecture slides and assignments from a university machine vision course. You'll learn how cameras form images and how to process, segment, and detect objects in them using **Python and OpenCV**.

> **Prerequisite:** Finish at least Chapters 1–10 of [Python Crash Course](../Intro/) first.

## Folder layout

```
Machine-Vision/
├── Lectures/      Slide decks (PDF) for every lecture, numbered in order
└── Assignments/   Hands-on programming assignments
```

## Setup

You'll need:

- Python 3 (see [uv setup](../README.md#uv))
- A webcam (a laptop camera is fine)
- These packages:
  ```bash
  uv add opencv-python numpy matplotlib
  ```

Quick test that OpenCV can see your camera:

```python
import cv2 as cv

cam = cv.VideoCapture(0)
while True:
    ok, frame = cam.read()
    if not ok:
        break
    cv.imshow("webcam", frame)
    if cv.waitKey(1) & 0xFF == ord("q"):  # press q to quit
        break
cam.release()
cv.destroyAllWindows()
```

## Lectures

| # | Topic | Slides |
|:---:|---|---|
| 01 | Course Introduction | [PDF](Lectures/01_Course_Introduction.pdf) |
| 02 | Vision and Cameras | [PDF](Lectures/02_Vision-and-Cameras_Slides+Notes.pdf) |
| 03 | Camera Calibration I | [PDF](Lectures/03_Camera-Calibration-Slides+Notes.pdf) |
| 04 | Camera Calibration II | [PDF](Lectures/04_Camera-Calibration_Slides+Notes.pdf) |
| 05 | Affine Transformations | [PDF](Lectures/05_Affine-Transformations_Slides+Notes.pdf) |
| 06 | Convolution and Kernels | [PDF](Lectures/06_Convolution-And-Kernels_Slides+Notes.pdf) |
| 07 | Image Smoothing and Blurring | [PDF](Lectures/07_Image-Smoothing-and-Blurring_Slides+Notes.pdf) |
| 08 | Image Gradient and Topology | [PDF](Lectures/08_Image-Gradient-and-Topology_Slides+Notes.pdf) |
| 09 | Histograms | [PDF](Lectures/09_Histograms_Slides+Notes.pdf) |
| 10 | Thresholding | [PDF](Lectures/10_Thresholding_Slides+Notes.pdf) |
| 11 | Morphological Operations | [PDF](Lectures/11_Morphological-Operations_Slides+Notes.pdf) |
| 12 | Edge Detection | [PDF](Lectures/12_Edge-Detection_Slides+Notes.pdf) |
| 13 | Contours, Image Moments, and Hough Transforms | [PDF](Lectures/13_Contours-Image-Moments-and-Hough-Transforms_Slides+Notes.pdf) |
| 14 | Foreground Detection and Segmentation | [PDF](Lectures/14_Foreground-Detection-and-Segmentation_Slides.pdf) |
| 15 | Motion Detection | [PDF](Lectures/15_Motion-Detection_Slides.pdf) |
| 16 | Image Pyramids, Super Pixels, and Fourier Transforms | [PDF](Lectures/16_Image-Pyramids-Super-Pixels-and-FTs_Slides+Notes.pdf) |
| 17 | Object Detection I | [PDF](Lectures/17_Object-Detection-I_Slides.pdf) |
| 18 | Object Detection II | [PDF](Lectures/18_Object-Detection-II_Slides.pdf) |
| 19 | Object Detection III | [PDF](Lectures/19_Object-Detection-III_Slides.pdf) |

### Suggested grouping

| Block | Lectures | Focus |
|---|:---:|---|
| Cameras and geometry | 01–05 | How images are formed, calibration, transforms |
| Filtering | 06–09 | Kernels, blurring, gradients, histograms |
| Segmentation and shape | 10–14 | Thresholding, morphology, edges, contours |
| Motion and multi-scale | 15–16 | Motion detection, pyramids, frequency domain |
| Object detection | 17–19 | Classical detectors through learned models |

## Assignments

See [Assignments/](Assignments/). More details are coming as assignments are added.

## Resources

- [OpenCV-Python Tutorials](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html): the official tutorials, which follow the lecture topics closely
- [OpenCV Documentation](https://docs.opencv.org/4.x/): full API reference
- [NumPy: the absolute basics](https://numpy.org/doc/stable/user/absolute_beginners.html): images in OpenCV are NumPy arrays, so this is worth knowing
- [PyImageSearch](https://pyimagesearch.com/): practical tutorials on OpenCV and deep learning
- [Ultralytics YOLO Docs](https://docs.ultralytics.com/): a good starting point for modern detection and segmentation models
