# Notes

- `venv` creates an isolated Python environment for this project.
- `pip` installs packages *into the active environment*.
- If activation scripts are blocked by PowerShell policy, you can try:
  ```powershell
  Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
  ```
  (Reverting later is recommended.)
- Prefer `python -m <module>` (e.g. `python -m pip`) to avoid accidentally using the wrong Python.

