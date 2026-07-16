# 01 - Environment Setup

Goal: get Python running locally and set up a clean virtual environment.

## 1) Install Python

- Install Python 3.10+ from the official installer: https://www.python.org/
- During install, enable: **“Add Python to PATH”**

## 2) Create a virtual environment

From this folder (or your project root), run:

```powershell
python -m venv .venv
```

## 3) Activate the virtual environment

```powershell
.venv\\Scripts\\Activate.ps1
```

## 4) Confirm Python works

```powershell
python --version
```

## 5) (Optional) Install requirements

If you later add a `requirements.txt`, install it with:

```powershell
pip install -r requirements.txt
```

