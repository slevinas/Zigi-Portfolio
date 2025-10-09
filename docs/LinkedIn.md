## LinkedIn “Experience” entry (copy‑paste ready)

**Title:** Senior DevOps / CI & Test Automation Engineer (Contract)

**Company:** XPLG
**Dates:** May 2025 – Dec 2025 (7 months)
**Location:** Remote

**Summary:** Led a five‑month transition to a modern, AI‑assisted CI/testing service using GitHub Actions + Ansible. Replaced a monolithic `flux-test` job with a DAG of reusable workflows; standardized remote VM setup; implemented artifact fetch/upload; and integrated Allure reporting for end‑to‑end visibility.

**Key contributions**

- Designed a modular CI DAG with `needs:` to express dependencies across `setup`, `start-service`, `run-tests`, and `upload-results` phases.
- Introduced Ansible‑based provisioning for a dedicated Tester VM (deterministic environment, fewer flaky runs, easier recovery).
- Standardized Python/pytest environment setup via a reusable workflow that runs `setup_python_env.sh` remotely.
- Automated data/service bootstrapping and remote filesystem prep (directory creation and file upload as parameterized inputs).
- Implemented a clean separation of concerns: provisioning, test execution, artifact collection, and results publishing.
- **Provisioned and operated a self‑hosted Allure service on a separate VM**; wired CI to publish results and generate reports with history.

**Reusable workflows delivered**

- Create directories on remote (Ansible)
- Upload files to remote (Ansible)
- Setup testing env & dependencies on remote (runs `setup_python_env.sh`)
- Data‑service bootstrap step (copy/synthetic data for test seed)
- Start service via Compose (prepared to consume a retrieved “composer”/compose file)
- Get deployment configuration → Upload “composer” to remote (two‑step chain)
- Run pytest on remote (Ansible)
- Fetch Allure raw results (+ optional `history`) back to orchestrator
- Upload test results to Allure server

**Stack & tooling**
GitHub Actions (reusable workflows, DAG with `needs:`), Ansible, Python, Pytest, Docker/Compose, Bash, Linux, Git, Allure (results & history), JSON‑based inputs, artifact management.

**Outcomes** _(customize with your numbers)_

- ↓ Pipeline brittleness / flaky runs by **[X]%**
- ↓ Mean time to configure a fresh Tester VM by **[Y] min**
- ↑ Time‑to‑signal from test execution to Allure report by **[Z]%**
- Enabled parallel reuse of steps across suites (no duplicated YAML/scripts)

---
