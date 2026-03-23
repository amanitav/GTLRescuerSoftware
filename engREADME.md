# GTL - HÜMA TEKNOFEST LİSELEARARSI İHA 2026 
Hüma is an autonomous mission system aiming to provide reliable, useful geospatial data to first-aid teams and disaster management operations after an incident. The UAV records an overhead view of the area along the planned route using two high-resolution camera modules, efficiently capturing imagery together with geographic reference data.
Recorded data is transferred to the ground station after landing and, as a first step, is interpreted by the mission-specific image-processing model we trained. The project includes an original ground-station design; computers with the required hardware can be used as a ground station by installing the custom software and additional communication modules. The station ingests georeferenced image-processing outputs into a database and creates mapped layers. The map that visualizes these data is delivered to team members’ apps on devices connected to the local server and is updated with each refresh.

## HÜMA Software: Disaster Area Analysis and Mapping System
A software solution that processes raw images obtained by UAVs after earthquakes and converts them into meaningful, georeferenced map layers for disaster teams.
### Vision
To support fast and accurate decision-making after disasters:
- **Coordination:** Ensure teams proceed according to plan.
- **Speed:** Automate rubble detection and area analysis with artificial intelligence.
- **Transparency:** Present processed data to field teams via interactive maps.

### Computer Vision Model

- **Rubble Detection:** We trained a YOLOv8m model using our original dataset of 41,000 photos and used the resulting model for rubble detection.
- **Smart Mapping:** Mosaicked map layers composed by stitching photos taken with a Raspberry Pi based on their coordinate data.
- **Interface:** A Streamlit-based interactive control panel and a forthcoming offline-capable mobile app.
- **Data Analytics:** Real-time statistical reporting of detected rubble to disaster teams.

If you would like to review project details, you can follow the steps below.

How do I run the software?

    Contact us to request the model files for the demo and follow the subsequent steps.
    Find the Afet_Analiz_Sistemi.py file at this link and copy the code into your IDE: https://github.com/amanitav/GTLRescuerSoftware/blob/main/Afet\_Analiz\_Sistemi.py
    Install required libraries: pip install ultralytics streamlit folium streamlit-folium opencv-python
    Run in the terminal: streamlit run "your_filename".py Note (Important): If you run the code without contacting us, only the satellite-imagery portion will operate; external functions will produce errors. These errors are caused by missing photos and the YOLO model we trained. Currently, because we are participating in the TEKNOFEST INTERSCHOOL UAV Competition, we cannot share the model; as compensation, we uploaded screenshots of the other disaster map and processed map tabs.

Project Screenshots
Afet Haritası (Disaster Map):
https://github.com/amanitav/GTLRescuerSoftware/blob/main/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202026-03-16%20180119.png

İşlenmiş Harita (Processed Map — Rubble Detection):
https://github.com/amanitav/GTLRescuerSoftware/blob/main/Ekran%20g%C3%B6r%C3%BCnt%C3%BCs%C3%BC%202026-03-16%20180137.png

Development Status
Our project is in active development. The model currently shared on GitHub is an initial prototype trained for 20 epochs. Our team continues training and optimization to maximize rubble-detection accuracy.

HÜMA Design: Original VTOL UAV and Ground Station Design

Vision

    Efficiency: 4+1 twin-boom VTOL configuration provides efficiency and stability where takeoff/landing space is limited in disaster conditions.
    Modularity and Portability: A configuration in which wings and tail separate from the fuselage allows the UAV to be carried in a 118 × 100 × 50 cm case.
    Reliability: A redundant system architecture and the use of composite and high-quality materials ensure mission safety.

UAV Technical Drawing
[technical drawing image]
<img width="6250" height="4419" alt="Elektronik (6)" src="https://github.com/user-attachments/assets/61903862-fa3e-4901-9a52-292360dd6539" />

Anisopetra Biomimicry
[biomimicry image]
<img width="6250" height="4419" alt="Elektronik (7)" src="https://github.com/user-attachments/assets/c86d86d3-9b8b-4cd8-8daa-e1eef78ae972" />

Carrying Case and Modular Design of the UAV
[modular design image]
<img width="6250" height="4419" alt="Elektronik (8)" src="https://github.com/user-attachments/assets/9e2688a3-4a25-40d7-a7cc-f1e31d62fdcb" />

Ground Station Carrying Case
[carrying case image]
<img width="6250" height="4419" alt="Elektronik (9)" src="https://github.com/user-attachments/assets/c52ced26-569e-4696-83a9-62a767b6e43e" />


HÜMA Hardware: Our Hardware Schematic
[hardware schematic image]
<img width="4419" height="6250" alt="Elektronik (2)" src="https://github.com/user-attachments/assets/e075a6ac-3085-4c94-84d7-fb30c45c623c" />

R&D and CONTACT
Our project is in active development and we value your feedback. If you would like to provide financial or technical support, you can contact us.
CONTACT:
