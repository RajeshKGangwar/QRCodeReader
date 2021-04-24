# QR Code Reader, Using OpenCv:
![Python 3.6](https://img.shields.io/badge/Python-v3.6-green) ![Opencv-Python](https://img.shields.io/badge/OpenCv--Python-v4.5-red) ![pyzbar](https://img.shields.io/badge/pyzbar-0.1.8-orange)

## Table of Content
  * [Application Demo](#Application-demo)
  * [Overview](#overview)
  * [Technical Aspect](#technical-aspect)
  * [Installation](#installation)
  * [Bug / Feature Request](#bug---feature-request)
  * [Technologies Used](#technologies-used)
  * [Credits](#credits)


## Demo


## Overview
This is an Elementry App for Detecting QRCode. The App has been Designed using Python. The model is created by Using OpenCv and Pyzbar Library for Qr Code Detection.
The App Captures live frame from webcam/device camera and returns the value of QR Code.


## Technical Aspect
This App is divided into two part:
1. __QRCodeReader.py__ : This file is responsible for getting live video frames from WebCam/Device camera and returing value of QR code After Detection, Whether the QR Code is Authororized/Un-Authorized.


2. __AuthorizedStuff.txt__: All the Data which is Authorized is stored over here. As QR code is detected, it will search the value of detected output in this file. If both the result matches then it Results as Authorized, Un-Authorized Otherwise.

    

## Installation
The QRCodeDetection is coded in python version 3.6, with other libraries as keras, tensorflow, numpy etc. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). Upgrade using pip package if you are using any lower version. The dependencies are mentioned in the requirements.txt file. Go with the below mentioned command for installing them in one go.
```bash
pip install -r requirements.txt
```

## Bug / Feature Request

If you find some bug/defect or if you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/RajeshKGangwar/QRCodeReader/issues).

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

<p align="left"> <a href="https://www.w3schools.com/css/" target="_blank"></a> <img src="https://www.vectorlogo.zone/logos/opencv/opencv-ar21.svg" alt="open-cv" width="150" height="150"/> <img src="https://www.vectorlogo.zone/logos/numpy/numpy-ar21.svg" alt="numpy" width="150" height="150"/>
</a> 


## Credits

- [Pyzbar](https://github.com/NaturalHistoryMuseum/pyzbar) 
