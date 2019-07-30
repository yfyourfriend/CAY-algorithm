# CAY-algorithm

## Overview
- The CAY-algorithm is the code-base for the CelloBot project by C.A.Y, a Making and Tinkering team at NTU.
- The CelloBot is an autonomous, battery-operated hand-held device designed to read sheet music (plays audio at designated point of musical score through web server).  The sheet music to be read must first be prepared by overlaying small 2mm by 2mm 2-dimensional code. It was our team's design objective to shrink such codes to be invisble to the naked eye while providing enough information for music retrieval. 
- The CAY-algorithm consists of 3 distinct parts:
	1. Image processing on [OpenMV H7 Cam](https://openmv.io/products/openmv-cam-h7)
	2. Web server on [ESPRESSIF ESP32-WROOM-32](https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32_datasheet_en.pdf)
	3. Utilities on Linux / arbitrary computer
		- pdf_overlay using reportlab, pypdf2 and their pre-requisites
		- score_partitioning; image processing for sheet music to automatically generate parameters (length of each musical bar etc) for reportlab

## Software pre-requisites
	- python 3.6
	- micropython 1.11
	- reportlab 3.5.23
	- pypdf2 1.26.0
	- matplotlib 3.1.1
	- skimage 0.16


