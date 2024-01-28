# Drowsiness and Awareness Monitoring Python Application

## Overview

This Python application is designed to monitor user awareness and detect drowsiness in real-time. It utilizes computer vision techniques and machine learning models and techniques to analyze facial features and provide alerts when potential mishaps are detected.

## Features

- *Facial Landmark Detection:* The application uses facial landmark detection to identify key points on the face, such as eyes, nose, and mouth.

- *Drowsiness Detection:* A machine learning model using Opencv is employed to analyze facial features and determine if the user is showing signs of drowsiness.

- *Alert System:* When drowsiness is detected, the application triggers an alert to notify the user, prompting them to stay alert or take a break.

- *User Awareness Monitoring:* The application also tracks overall user awareness by analyzing factors such as head position and eye movement.

- *Prevention of Under Influence Mishaps:* Using microcontrollers such as Arduino Uno R3 and micro devices we detect and prevent drunk driving. 

## Pre-requisites

Before running the application, ensure you have the following installed:

- Python 3.8+
- OpenCV
- Face Recognition
- Other dependencies (installable via requirements.txt)

## Installation

1. *Clone the repository:*

   bash
   git clone https://github.com/AyushKatochh/HackJNU-Drive-Guard.git
   

2. *Create new environment*

conda create -n drive-guard

3. *Activate the environment*

conda activate drive-guard

3. *Install the dependencies*

pip install -r requirements.txt


## Usage

python gain/main.py

Arduino is used to detect the whether driver is under the influence of alcoholic substance and thus prevents the starting of vehicle if found so, and consistently monitors the behaviour using the live monitoring feed