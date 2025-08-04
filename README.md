# Global Weather Model Viewer
This project is a backend service that fetches, processes, and visualizes current numerical weather prediction (NWP) model data — starting with the Global Forecast System (GFS).

The backend is built using FastAPI and will eventually support:
- Real-time model runs (e.g., GFS 00z, 06z, 12z, 18z)
- Forecast frame snapshot generation (e.g., 0–384 hours)
- Image hosting and metadata storage using PostgreSQL

Other global weather models and storm-specific models (HAFS) will be added in future versions.