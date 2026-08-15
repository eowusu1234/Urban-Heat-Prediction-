# Technical Debt Plan

## UrbanHeat Accra — Machine-Learning-Based Urban Heat Risk Prediction & Mitigation-Simulation Dashboard

---

**Document Version:** 1.0

**Date:** 15 August 2026

**Student Name:** Emmanuel Owusu

**Student ID:** 22425075

---

## 1. Introduction
This document outlines the technical debt accumulated during the development of the UrbanHeat Accra MVP, driven largely by the 48-hour development constraint. It classifies the debt and provides a roadmap for repayment in future iterations of the software.

## 2. Technical Debt Register

| Debt ID | Technical Debt | Cause | Impact | Priority | Classification | Proposed Resolution | Target Version |
|---------|---------------|-------|--------|----------|----------------|---------------------|----------------|
| **TD-01** | Synthetic training data instead of real satellite-derived data | 48-hour constraint; no access to curated dataset | Model predictions are illustrative, not calibrated to real-world conditions | High | Scheduled for Future Resolution | Integrate real Landsat/Sentinel satellite-derived features and ground-truth temperature measurements | v2.0 |
| **TD-02** | Global feature importance instead of per-instance SHAP values | Development time constraint; SHAP library adds complexity | Explanation is the same for all locations rather than location-specific | Medium | Acceptable Temporarily | Integrate SHAP library for local interpretable explanations | v1.1 |
| **TD-03** | No authentication or authorisation | FR9 descoped; MVP is read-only public tool | No access control; all endpoints publicly accessible | Medium | Scheduled for Future Resolution | Implement JWT authentication with role-based access control | v2.0 |
| **TD-04** | Simplified linear NDVI simulation model | Physical simulation requires domain expertise beyond scope | Simulation results are indicative, not physically accurate | Medium | Acceptable Temporarily | Partner with environmental scientists for physics-based vegetation-temperature models | v2.0 |
| **TD-05** | No rate limiting on API endpoints | Development time constraint | Potential for API abuse or denial of service | Low | Scheduled for Future Resolution | Add FastAPI rate limiting middleware (e.g., slowapi) | v1.1 |
| **TD-06** | SQLite in production (Render) | Zero-config database for rapid deployment | Not suitable for concurrent writes; file-based, no connection pooling | Medium | Scheduled for Future Resolution | Migrate to PostgreSQL on Render | v1.1 |
| **TD-07** | No automated CI/CD pipeline | 48-hour constraint; manual deployment | Risk of deployment inconsistencies; no automated test enforcement | Low | Scheduled for Future Resolution | Set up GitHub Actions for automated testing and deployment | v1.1 |
| **TD-08** | Limited automated test coverage | Time constraint; focused on critical API paths | 8 test cases cover core paths but not edge cases or frontend | Medium | Scheduled for Future Resolution | Expand test suite; add frontend component tests with Vitest | v1.1 |
| **TD-09** | No real-time data ingestion | Live satellite data integration is complex and out of scope | Data is static; no automatic updates when conditions change | High | Scheduled for Future Resolution | Build a data pipeline for periodic satellite data refresh | v2.0 |
| **TD-10** | Single-city deployment | MVP scope limited to Accra | System cannot be used for other cities without manual data preparation | Low | Scheduled for Future Resolution | Generalise data model and UI for multi-city support | Long-term |
| **TD-11** | No content security policy (CSP) headers | Not configured | Minor XSS vulnerability surface | Low | Scheduled for Future Resolution | Add security headers middleware | v1.1 |
| **TD-12** | Frontend mobile responsiveness incomplete | Time constraint; optimised for desktop first | Some components may not display optimally on very small screens | Low | Acceptable Temporarily | Complete responsive implementation with mobile-specific patterns | v1.1 |

---

## 3. Technical Debt Repayment Roadmap

### Immediate Action Items
- Run the API test suite and document baseline functional status.
- Verify environment variables and CORS configuration in Render/Vercel.

### Version 1.1 (Short-Term Focus: Stability and Security)
- **TD-02:** Switch from global `feature_importances_` to SHAP for accurate local explanations.
- **TD-05, TD-11:** Implement API rate limiting and security headers to harden the public endpoints.
- **TD-06:** Provision a managed PostgreSQL instance and update `DATABASE_URL`.
- **TD-07, TD-08:** Establish GitHub Actions CI/CD and expand test coverage.
- **TD-12:** Refine mobile CSS (bottom sheets, card lists instead of tables).

### Version 2.0 (Medium-Term Focus: Data Fidelity and Features)
- **TD-01, TD-09:** Build a data pipeline to ingest real Landsat-8/Sentinel-2 imagery, replacing the synthetic dataset.
- **TD-03:** Introduce an Admin role with JWT authentication to manage location data.
- **TD-04:** Replace linear simulation with a robust physics-based thermal model.

### Long-Term Vision
- **TD-10:** Abstract the data schema to support multiple cities and regions dynamically.

---
*End of Technical Debt Plan*
