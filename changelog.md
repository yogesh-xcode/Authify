# Changelog

All notable changes to this project will be documented here, in order.

This changelog follows the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format and uses [Semantic Versioning](https://semver.org/).

> ⚠️ This project is under active development. No official releases yet.
> All versions below are internal dev snapshots.

---

## [Unreleased]

### 🚧 In Progress
- Add upcoming changes here before they’re finalized

---

## [0.1.6-dev] - 2025-04-10

### ♻️ Lifespan Refactor
- 🧼 Extracted app startup/shutdown logic into `lifecycle.py`
- 🧠 Simplified lifespan flow for future scalability

---

## [0.1.5-dev] - 2025-04-09

### 🛠 Route Enhancements
- 🔄 Updated `auth_routes.py` to use unified success/error models
- 🧠 Improved endpoint logic for better error feedback and response

---

## [0.1.4-dev] - 2025-04-09

### 🧠 Service Integration & Logic Cleanup
- ⚙️ Integrated response model in `auth_service.py`
- 🚀 Optimized auth logic for validation and conflict handling
- 🔐 Updated `hashing.py` to align with new service requirements

---

## [0.1.3-dev] - 2025-04-09

### 🧩 API Response & Models
- ✨ Added `response_model.py` for consistent success/error returns
- 🧾 Created `type_model.py` for enums and structured response types

---

## [0.1.2-dev] - 2025-04-06

### 🔐 Core Authentication Logic
- 🔐 Added password hashing and verification in `core/crypto`
- 🛠 Created `auth_service.py` for user creation and validation
- 🧩 Connected routes with service and schemas

---

## [0.1.1-dev] - 2025-04-04

### 🗄 Database & Auth Schemas
- 🧩 Introduced SQLite for local development
- 🧠 Defined Pydantic schemas for user auth
- 🔐 Added auth routes for registration and login

---

## [0.1.0-dev] - 2025-04-04

### 🎉 Initial Setup
- 🧱 Set up base project structure
- 📦 Initialized `pyproject.toml` and `.gitignore` for Poetry
- 🗂 Created modular FastAPI layout
