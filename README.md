# Road Surface Defect Analysis (Анализ Дорог)

![Patent Pending](https://img.shields.io/badge/Status-Patent_Pending-red.svg)
![Grant Application](https://img.shields.io/badge/Grant-National_Youth_Projects_RF-blue.svg)
![YOLO11](https://img.shields.io/badge/Model-YOLO11s-00FFFF.svg)
![React](https://img.shields.io/badge/Frontend-React_TypeScript-blue.svg)

 **IMPORTANT NOTICE:**
> The source code, dataset, and trained model weights for this repository are currently **closed-source and hidden**. This restriction is strictly enforced because a **software patent for the algorithms is currently being prepared**, and the project is actively in the submission phase for a grant under the **National Youth Projects of the Russian Federation**. 

## Project Overview
This repository showcases the culmination of an undergraduate thesis (ВКР) aimed at automating the detection and mapping of road surface defects using Deep Convolutional Neural Networks. The system transitions road maintenance from a reactive approach to a **predictive maintenance** strategy, potentially reducing budget expenditures by 15-21%.

The software suite, **"Анализ Дорог"**, processes video streams from car dashcams, detects defects using a highly optimized **YOLO11s** model, and maps them onto an interactive GIS system with a gradient-based road condition score.

<img width="1441" height="773" alt="image" src="https://github.com/user-attachments/assets/3def179c-baa8-411e-8d21-deee4358bf4b" />

## Key Features
*  **High-Precision CV Pipeline:** Real-time defect detection based on the international RDD standard (D00: Longitudinal, D10: Transverse, D20: Alligator, D40: Pothole) [cite: 1, 2].
*  **GIS Integration & Gradient Mapping:** Defects are automatically tied to GPS coordinates. The system calculates a rolling "condition score" within a 25-meter radius and paints the road segments on a map from Green (Good) to Black (Critical) [cite: 1, 2].
*  **Automated PDF Reporting:** Generates comprehensive analytical reports for municipal authorities, highlighting critical zones and defect density [cite: 1, 2].
*  **Human-in-the-loop Annotation:** The custom dataset was meticulously refined using a dual-operator review system and CIoU penalty validation [cite: 1, 2].

##  Machine Learning Architecture
* **Model:** YOLO11s (selected over YOLOv8 and EfficientDet due to superior latency-accuracy balance) [cite: 1, 2].
* **Dataset:** 20,199 globally sourced images (India, Czech, USA, Japan, Samara) with a carefully balanced 9.1% background image ratio to minimize false positives [cite: 1, 2].
* **Performance:** 
  * `mAP@0.5`: **0.677** [cite: 1, 2]
  * `Inference Time`: **2.5 ms** (400 FPS on NVIDIA T4 via TensorRT) [cite: 1, 2]
* **Loss Functions:** CIoU (Complete Intersection over Union) for bounding box regression and Focal Loss for handling class imbalance (especially for D40 Potholes) [cite: 1, 2].

*(Note: Insert a screenshot of the YOLO bounding boxes / detection examples here. Example from thesis: Рисунок 2)*
`<!-- ![Detections](path/to/your/image.png) -->`

## Technology Stack
* **Computer Vision:** PyTorch, Ultralytics (YOLO11), OpenCV, TensorRT [cite: 1, 2]
* **Frontend:** React 18, TypeScript, Vite, Tailwind CSS [cite: 1, 2]
* **Mapping Engine:** Leaflet, OpenStreetMap, Overpass API [cite: 1, 2]
* **Data Processing:** Python, Pandas, NumPy [cite: 1, 2]

## Practical Impact & Future Plans
The project has been successfully presented to the **Youth Minister of Transport of the Samara Region** and received positive evaluations from major logistics operators like "Samara Avtogaz" [cite: 1, 2]. It is designed to be fully integrated into the "Smart City" concept to support the national "Safe Quality Roads" initiative [cite: 1, 2].

---
*Designed and developed by Nikita Kutsyba.*
