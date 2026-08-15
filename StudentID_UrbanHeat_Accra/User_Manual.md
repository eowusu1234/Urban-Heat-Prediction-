# User Manual

## UrbanHeat Accra Dashboard

---

**Date:** 15 August 2026

---

## 1. Introduction
Welcome to the **UrbanHeat Accra** dashboard. This application is an AI-assisted planning support tool designed to help urban planners and environmental officers identify, understand, and mitigate urban heat vulnerability across the Greater Accra Metropolitan Area.

## 2. System Requirements
- **Device:** Desktop computer or laptop (recommended), tablet, or modern smartphone.
- **Browser:** Recent versions of Google Chrome, Mozilla Firefox, Apple Safari, or Microsoft Edge.
- **Internet:** A stable internet connection is required to load map tiles and communicate with the prediction API.

## 3. Accessing the Application
Navigate to the live URL: https://urban-heat-prediction-frontend.vercel.app/
The application requires no login or installation.

## 4. Map Dashboard
Upon opening the application, you will be presented with the Map Dashboard.
- **Location Pins:** The map displays monitored locations.
  - **Green:** Low Risk
  - **Amber:** Moderate Risk
  - **Red:** High Risk
  - **Dark Red:** Severe Risk
- **KPI Summary:** The top of the screen displays Key Performance Indicators (Total Locations, High Risk Count, Average Risk).
- **Filtering:** Use the buttons at the top ("Low", "Moderate", "High", "Severe") to filter the visible map pins.
- **Search:** Use the search bar in the top right to find a specific location or neighbourhood.

*[INSERT SCREENSHOT — Map Dashboard]*

## 5. Location Details & Explainability
1. **Select a Location:** Click any pin on the map.
2. **Detail Drawer:** A panel will slide in from the right.
3. **Overview Tab:** This tab shows:
   - The Heat Risk Score (0-100) and category.
   - The Environmental Baseline (NDVI, Built-up Density, Green Space Distance, Elevation).
   - **Top Contributing Factors:** A bar chart explaining *why* the location has its score. Red bars indicate factors increasing heat risk; green bars indicate cooling factors.

*[INSERT SCREENSHOT — Location Detail Drawer]*

## 6. Mitigation Simulator
To see how planting trees or increasing green cover might lower temperatures:
1. Open a Location Detail drawer.
2. Click the **Mitigation Simulator** tab.
3. Click a preset button (e.g., "+10% Vegetation") or adjust the custom slider.
4. The system uses Machine Learning to recalculate the risk.
5. Review the **Before vs After** comparison to see the projected drop in the heat risk score.
6. Click **Reset to Baseline** to revert the simulation.

*[INSERT SCREENSHOT — Mitigation Simulator]*

## 7. Data Explorer
To view the raw dataset:
1. Click the **Data Explorer** icon in the left sidebar.
2. You will see a tabular view of all locations.
3. **Sorting:** Click any column header to sort the data.
4. **Export:** Click the **Export CSV** button in the top right to download the data for use in Excel or GIS software.

*[INSERT SCREENSHOT — Data Explorer]*

## 8. Custom Risk Predictor Tool
If you want to test hypothetical environmental conditions for an unmapped area:
1. Click the **Risk Predictor Tool** in the sidebar.
2. Adjust the sliders for NDVI, Built-up Density, Distance to Green Space, and Elevation.
3. Click **Calculate Heat Risk Score**.
4. The system will provide an instant prediction based on the trained model.

*[INSERT SCREENSHOT — Predictor Tool]*

## 9. Troubleshooting
- **Map Not Loading:** Ensure you have an active internet connection.
- **"Connecting..." or "API Offline" in sidebar:** The frontend cannot reach the backend server. If you are running locally, ensure the FastAPI server is running. If online, the server may be waking up from sleep (Render free tier); please wait 30-60 seconds and refresh.
- **Simulation Error:** If the simulation fails, refresh the page and try again.

---
*End of User Manual*
