# Zigi-2025-Work

---

# XPLG – AI-Driven Modular CI & Test Automation (May–Dec 2025)

> Five-month engagement modernizing CI/testing into a modular, reusable, and automation-first system. Delivered a GitHub Actions + Ansible framework that turns a formerly monolithic “flux-test” job into a DAG of reusable workflows, adds remote provisioning and artifact flows, and integrates reporting via Allure.

---

## LinkedIn headline ideas

- DevOps/CI Engineer • Modular GitHub Actions • Ansible • Pytest • Allure
- Senior CI/CD & Test Automation Engineer | GitHub Actions, Ansible, Python
- AI‑assisted CI Modernization | Reusable Workflows • Observability • Allure
- DevOps Consultant | Turning monolithic CI into modular DAGs
- Test Infra Engineer | Remote VM Orchestration • Artifacts • Reporting

---

## LinkedIn “About” (short)

I modernize CI/test infrastructure by turning brittle pipelines into modular, reusable systems. Recently helped XPLG transition to an AI‑assisted, Ansible‑driven GitHub Actions framework: DAG‑based workflows, remote VM execution, deterministic setup, and end‑to‑end reporting with Allure.

## LinkedIn “About” (long)

I design CI/test platforms that are modular, observable, and easy to evolve. Over the last five months I partnered with XPLG to refactor a monolithic GitHub Actions test job into a clean DAG of reusable workflows. I introduced Ansible‑based provisioning for a remote Tester VM, standardized setup for Python/pytest environments, and built artifact flows that move results bi‑directionally between the orchestrator and the remote host. The result is a robust, AI‑assisted CI framework where steps are composable, repeatable, and traceable—complete with Allure result publishing for fast feedback and historical trend analysis.

---

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

## Resume bullets (ATS‑friendly)

- Re‑architected a monolithic GitHub Actions test job into a modular DAG of reusable workflows with explicit `needs:` dependencies.
- Implemented Ansible‑based provisioning for a remote Tester VM, delivering deterministic Python/pytest setup via `setup_python_env.sh`.
- Built generic workflows to create directories and upload files to the remote host based on lists/JSON inputs.
- Added two‑step deployment config handling: retrieve a “composer” file and upload it to the Tester VM for service startup.
- Created a reusable step to run pytest remotely and collect artifacts (Allure raw results and optional history).
- Published results to a self‑hosted Allure service; standardized artifact retention for auditability.
- Introduced bi‑directional artifact movement between orchestrator and remote to improve debuggability and transparency.
- Established an AI‑assisted authoring pattern for reusable workflows to accelerate future CI extensions.

---

## Two STAR stories (interview‑ready)

**1) Modularizing a monolith**
**S**: A single GitHub Actions job ran setup, Docker startup, tests, and reporting; frequent flakes and hard‑to‑debug failures.
**T**: Make the pipeline composable and reliable without disrupting existing CI.
**A**: Split into a DAG of reusable workflows (`setup` → `start‑service` → `run‑tests` → `upload‑results`), introduced Ansible provisioning, and standardized pytest env setup.
**R**: Reduced brittle steps and shortened failure isolation; teams can now reuse steps across suites with minimal YAML.

**2) Closing the reporting loop**
**S**: Test results were difficult to compare across runs; limited visibility into history and trends.
**T**: Add consistent reporting and artifact retention.
**A**: Implemented a fetch‑and‑publish flow for Allure raw results/history; archived artifacts and published to a self‑hosted Allure server.
**R**: Faster time‑to‑signal and historical comparisons; improved triage and accountability.

---

## Short “project description” (for CV or portfolio)

Modernized XPLG’s CI/testing by replacing a monolithic GitHub Actions job with a reusable, DAG‑based system. Added Ansible‑driven remote provisioning, standardized Python/pytest setup, artifact flows, and Allure reporting, enabling composable steps, better observability, and faster feedback.

---

## Metrics you can add (how to get them)

- **Runtime deltas**: Compare median workflow runtime before/after modularization.
- **Flake rate**: % of reruns or failures attributed to environment/setup vs. test logic.
- **Time‑to‑signal**: Start of test run → Allure report available.
- **Reuse count**: Number of pipelines/jobs now calling the reusable workflows.

> Tip: Pull run durations from GitHub Actions run history; tag runs by commit or by workflow version to compare baselines.

---

## Confidentiality / NDA‑safe variant

If needed, replace “XPLG” with “Enterprise analytics vendor (NDA)” and remove internal filenames. Example:

_“Partnered with an enterprise analytics vendor (NDA) to modernize CI/test infrastructure. Delivered a modular, Ansible‑driven GitHub Actions framework with remote VM provisioning, reusable workflows, artifact flows, and Allure reporting.”_

---

## Skills & keywords

GitHub Actions • Reusable Workflows • DAG (`needs:`) • Ansible • Python • Pytest • Bash • Docker • Docker Compose • Linux • Artifact Management • Allure • Test Reporting • Observability • CI/CD • Remote VM Orchestration • DevOps • Automation • JSON‑driven inputs • Infrastructure as Code

---

## Quick checklist before publishing

- [ ] Replace placeholders **[X] [Y] [Z]** with real numbers
- [ ] Remove any internal filenames/paths/IPs
- [ ] Add links/screenshots of Allure dashboards or GH Actions runs
- [ ] Ensure job titles match your target roles (DevOps, SDET, Platform, etc.)

---

## Representative CI/Ansible Work (spec‑driven workflows)

These highlights reflect the concrete value in your YAML snippets and make your impact obvious to recruiters/hiring managers.

### Orchestrator (GitHub Actions)

- **CI orchestrator – Storm Setup → Run Tests → Upload to Allure** (branch: `ci/modular-testing-service`).

  - Chained reusable workflows: `ensure-infra-compose-orchestrator-ansi.yml` → `run-pytest-ansi.yml` → `push-results-to-allure-ansi.yml`.
  - Demonstrates clean **DAG composition** (via `needs:`) and environment‑safe **secret handling** (SSH agent + `secrets.TESTER_*`).

### Ensure Infra + Compose (unified)

- **Config‑first loading**: Normalize a v2 unified infra spec and emit `infra_config` JSON for downstream jobs.
- **Conditional execution** using `fromJSON(...)` gates:

  - Repo cloning (`any_clone`, `clone_specs`).
  - Optional ensure‑steps: **Python**, **Docker**, **directories**, **file uploads**, and **Compose stacks**.

- **JSON bridging**: `toJSON(...)` to pass lists into Ansible‑backed reusable workflows.
- **Inventory scoping**: Consistent `inventory_host` propagation so Ansible playbooks limit to the correct target.
- **Hygiene**: SSH agent cleanup, fail‑fast disabled for fan‑out clone matrix, and clear step naming for auditability.

### Run Pytest (spec‑driven)

- **Spec loader** turns a repo YAML into `pytest_config` JSON.
- **Secure env injection**: pass `.env` contents via secret `TESTER_ENV_FILE_CONTENTS`.
- **Bridge to Ansible**: materialize `pytest_vars.json` via `jq`, then execute `.ansible/playbooks/run_pytest.yml` with `--limit` set from the config.
- **Artifacts**: enforce presence of `raw-results-*.tgz` and upload via `actions/upload-artifact@v4`.

### Push Results to Allure

- **Inputs loader** → `push_inputs` JSON, then **preflight** inventory dump for diagnostics.
- **vars.json** builder enforces explicit values: `working_dir`, `results_dir`, `allure_url`, `project_id`, and feature toggles.
- **Idempotent publish**: `.ansible/playbooks/push_allure_results.yml` and post‑publish **tar** of remote `raw-results` for retention/traceability.

### Why this matters (talking points)

- **Spec‑driven orchestration**: Pipelines adapt to config, not hard‑coded YAML. Safer evolution, less duplication.
- **Separation of concerns**: Provision → Test → Collect → Publish, each with its own reusable workflow.
- **Observability**: Preflight checks, explicit JSON logs, and artifact retention simplify triage.
- **Security**: No plaintext env files; secrets flow through GitHub Actions secrets + ephemeral SSH agent.

### Plug‑and‑play resume bullets

- Built a **spec‑driven CI orchestrator** chaining infra setup, remote pytest execution, and Allure publishing via reusable GitHub Actions + Ansible, gated by JSON‑based inputs and `fromJSON(...)` conditions.
- Implemented **inventory‑scoped Ansible runs** with secure secret injection (SSH agent, encrypted `.env` contents), and enforced **artifact contracts** (`raw-results-*.tgz`) for reliable reporting.
- Created a **unified infra/compose ensure pipeline**: optional Python/Docker install, repo cloning, directory creation, file upload, and Compose stack bring‑up, all parameterized via a normalized spec.

> These have been folded into your LinkedIn/CV master copy above. Replace placeholders with your actual repo/branch names only if you’re comfortable disclosing them publicly.

---

## Architecture diagram (Mermaid)

> High-level view of the spec-driven CI orchestration and artifact/secret flows, redacted for public sharing.

```mermaid
flowchart LR
  subgraph Dev[Developer]
    Commit[Commit → Push]
  end

  subgraph GA[GitHub Actions Orchestrator]
    Loader[Load Infra/Compose Spec (Ansible, local)]
    Ensure[Ensure Infra (conditional):
Python · Docker · Directories · Files · Repo clones]
    Compose[Ensure Compose Stacks (optional)]
    PySpec[Load Pytest Spec (Ansible, local)]
    RunPy[Run Pytest on Tester VM (Ansible limit by inventory_host)]
    PushAllure[Push Results to Allure (Ansible)]
    Artifacts[[Upload raw-results-*.tgz to GHA Artifacts]]
    Observability[[Preflight dumps · JSON logs · tar retention]]
  end

  subgraph Tester[Tester VM]
    Service[Service(s) via Compose]
    Results[(raw-results/ + history/)]
  end

  subgraph Allure[Allure Server]
    Reports[(Project reports)]
  end

  Commit --> GA
  Loader --> Ensure --> Compose --> PySpec --> RunPy --> Artifacts
  RunPy -->|raw-results| Results
  Artifacts --> PushAllure --> Reports
  GA --> Observability

  %% Secrets flow (conceptual)
  subgraph Secrets[Secrets & Auth]
    GHSecrets[GitHub Secrets:
ssh-key, TESTER_ENV_FILE_CONTENTS]
    SSHAgent[Ephemeral SSH agent]
  end
  GHSecrets --> SSHAgent --> GA
  GHSecrets --> GA
```

---

## Public, redacted mini‑case — `README.md`

> Use this as a public template (no company names, no internal paths). Replace placeholders like `<INVENTORY_HOST>` and keep secrets in GitHub Secrets only.

### Spec‑Driven CI Orchestration Template (GitHub Actions + Ansible)

A minimal, reusable pattern for running end‑to‑end tests on a remote VM using GitHub Actions + Ansible. The pipeline loads config files (YAML → JSON), conditionally ensures infra (Python, Docker, directories, files), runs tests via pytest, and publishes results to Allure. Artifacts (`raw-results-*.tgz`) are retained for traceability.

#### Features

- Config‑first: YAML specs drive the pipeline; no hard‑coding of hosts or paths.
- Conditional ensure steps (install Python/Docker, create directories, upload files, bring up Compose stacks).
- Secure secret handling (ephemeral SSH agent; `.env` contents passed via GitHub Secrets, never as plaintext files).
- Inventory‑scoped Ansible runs using `--limit <inventory_host>`.
- Artifact contracts: `raw-results-*.tgz` enforced and uploaded.

#### High‑level architecture

- **Orchestrator:** GitHub Actions (self‑hosted or hosted) running Ansible playbooks.
- **Tester VM:** Target host for services/tests (addressed via inventory/limit).
- **Reporting:** Allure server (self‑hosted or cloud) receives results.

#### Repository sketch

```
.ansible/
  inventory/hosts.ini          # contains [tester] <INVENTORY_HOST>
  playbooks/
    load_infra_spec.yml        # reads config, emits JSON (infra_config)
    load_pytest_spec.yml       # reads spec, emits JSON (pytest_config)
    ensure_env.yml             # installs python/docker when requested
    create_directories.yml     # idempotent mkdir -p per JSON list
    upload_files.yml           # copies files described by JSON list
    ensure_compose.yml         # up/down services per setup path
    run_pytest.yml             # executes pytest, packs raw-results-*.tgz
    push_allure_results.yml    # posts to Allure REST API
.ci/
  infra/infra.compose.template.yml  # redacted infra spec (v2)
  pytest/pytest.template.yml        # redacted pytest spec
  allure/inputs-push-results.yml    # allure_url, project_id, flags
.github/workflows/
  ci-orchestrator.yml
  ensure-infra-compose.yml
  run-pytest.yml
  push-results-to-allure.yml
```

#### Example: `ci-orchestrator.yml` (redacted)

```yaml
name: CI Orchestrator — Ensure → Test → Publish
on:
  push:
    branches: [ci/spec-driven-template]
jobs:
  ensure-infra-compose:
    uses: ./.github/workflows/ensure-infra-compose.yml
    with:
      infra_path: .ci/infra/infra.compose.template.yml
    secrets:
      ssh-key: ${{ secrets.TESTER_SSH_KEY }}

  run-pytest:
    needs: ensure-infra-compose
    uses: ./.github/workflows/run-pytest.yml
    with:
      spec_path: .ci/pytest/pytest.template.yml
    secrets:
      ssh-key: ${{ secrets.TESTER_SSH_KEY }}
      TESTER_ENV_FILE_CONTENTS: ${{ secrets.TESTER_ENV_FILE_CONTENTS }}

  upload-results-to-allure:
    needs: run-pytest
    uses: ./.github/workflows/push-results-to-allure.yml
    with:
      inputs_path: .ci/allure/inputs-push-results.yml
    secrets:
      ssh-key: ${{ secrets.TESTER_SSH_KEY }}
```

#### Example: minimal infra spec (redacted)

```yaml
version: 2
inventory_host: "<INVENTORY_HOST>" # e.g. tester-01
ensure:
  python: true
  docker: true
  directories:
    - "/var/tmp/test-results"
  files:
    - src: ".ci/payloads/synthetic_flux_source.log"
      dest: "/var/tmp/synthetic_flux_source.log"
compose_setup_path: ".ci/compose/setup"
has_compose_setup: true
any_clone: false
clone_specs: []
```

#### Example: minimal pytest spec (redacted)

```yaml
inventory_host: "<INVENTORY_HOST>"
working_dir: "/opt/tests"
pytest:
  venv_path: "/opt/venv"
  test_command: "pytest -q tests/test_smoke.py"
artifacts:
  output_tgz: "raw-results-template.tgz"
```

#### Security notes

- Store **all secrets** (SSH key, `.env` contents, tokens) only in **GitHub Secrets**.
- Do not commit inventories with real hostnames or IPs; use placeholders in public repos.
- Ensure playbooks are **idempotent**; cleanup SSH agents at job end.

#### Getting started

1. Add a tester host to your private inventory and configure SSH.
2. Create GitHub Secrets: `TESTER_SSH_KEY`, `TESTER_ENV_FILE_CONTENTS`, `ALLURE_TOKEN` (if needed).
3. Adjust the three configs: infra spec, pytest spec, Allure inputs.
4. Push a branch (e.g., `ci/spec-driven-template`) and check the Actions tab.

#### Redaction checklist (public repos)

- [ ] Replace real org/app names with neutral terms ("Service A").
- [ ] Remove internal paths/IPs; keep relative, template paths.
- [ ] Strip test data; keep small, synthetic samples only.
- [ ] Confirm no logs or artifacts contain PHI/PII.

#### License

MIT (or your preferred permissive license).

```

> If you’d like, we can spin this out into its own GitHub repo and I’ll adapt filenames to a clean template naming scheme (`ensure-infra-compose.yml`, etc.).

```

Awesome—got it on both fronts.

### 1) Tiny public repo scaffold

I’ve spun up a complete, redacted repo skeleton you can copy-paste into GitHub. It includes:

- **.github/workflows**: `ci-orchestrator.yml`, `ensure-infra-compose.yml`, `run-pytest.yml`, `push-results-to-allure.yml`
- **.ansible/playbooks**: loaders, ensure env, create dirs, upload files, ensure compose, run pytest, push Allure results
- **.ci specs**: infra (v2), pytest, and Allure inputs
- **docs**: `allure-server-setup.md` (self-hosted Allure on a separate VM)
- `README.md`, `LICENSE`, `.gitignore`

Open the canvas titled **“Spec-Driven CI + Ansible – Public Repo Scaffold”** to grab the exact file contents and repo tree. If you want, I can add a tiny `tests/test_smoke.py`, a `compose` example, and a Makefile with helper targets—just say the word.

### 2) Your Allure server work + end date

I updated your main experience canvas to reflect:

- **You provisioned and operated a self-hosted Allure service on a separate VM** and wired CI to publish with history.
- **Dates updated:** May 2025 → **Dec 2025** (7 months). This matches your plan to wrap in December.

### Quick next steps

- Create a new GitHub repo (public or unlisted), paste the scaffold, and push a branch: `ci/spec-driven-template`.
- In the repo, set **GitHub Secrets**: `TESTER_SSH_KEY`, `TESTER_ENV_FILE_CONTENTS` (and Allure token if you add auth).
- Replace placeholders (`<INVENTORY_HOST>`, `<ALLURE_VM_HOST>`), keep inventories private.

Want me to:

- drop in the smoke test + Makefile,
- or tweak the workflows to include a simple Helm/K8s path as a commented section?

---

All set! I added the finalized CV (plus the K8s/Helm variant) to your canvas and generated downloadable files:

- [Download the CV – PDF](sandbox:/mnt/data/Sagi_Levinas_CV_Oct_2025.pdf)
- [Download the CV – Markdown](sandbox:/mnt/data/Sagi_Levinas_CV_Oct_2025.md)
- (Fallback) [Open the CV – HTML](sandbox:/mnt/data/Sagi_Levinas_CV_Oct_2025.html)
- Repo scaffold you can publish: [spec-driven-ci-ansible-template.zip](sandbox:/mnt/data/spec-driven-ci-ansible-template.zip)

Want me to also produce:

- a one-page version (tight for recruiters), or
- a Covera-specific cover letter using this CV wording?

# Sagi Levinas — CV (Oct 2025)

**Software Engineer — Python • CI/CD • Ansible • Healthcare**
Weeki Wachee, FL · Remote-friendly · [linkedin.com/in/sagilevinas](https://linkedin.com/in/sagilevinas)

## Summary

Software engineer specializing in **Python**, **CI/CD automation**, and **spec‑driven orchestration**. Built reusable **GitHub Actions + Ansible** pipelines, remote test execution, and **Allure** reporting. Health‑tech experience with **FHIR/HL7** and data pipelines (AWS RDS → Snowflake). Strong collaborator who ships secure, observable systems in regulated environments.

## Core Competencies

**Languages:** Python, TypeScript/JavaScript, SQL
**Infra/DevOps:** GitHub Actions, Ansible, Docker, Docker Compose, (basic) Kubernetes, CI/CD, IaC concepts
**Testing & Data:** Pytest, Allure, Playwright, ETL/ELT, Observability/Artifacts
**Web/App:** Node.js (NestJS), React/Vue/Nuxt, REST APIs (OpenAPI)

---

## Experience

**XPLG — Python/CI Consultant (Contract)** · Remote · **May 2025 – Dec 2025**

- Built a **spec‑driven CI orchestrator** chaining infra setup → remote **pytest** execution → **Allure** publishing via reusable **GitHub Actions + Ansible**; gated by JSON inputs and `fromJSON(...)` conditions.
- Implemented **inventory‑scoped** Ansible runs with secure secret injection (ephemeral SSH agent; `.env` via GitHub Secrets).
- Enforced **artifact contracts** (`raw-results-*.tgz`) and retained artifacts for auditability and faster triage.
- Created a unified **ensure‑infra/compose** pipeline: optional Python/Docker install, repo clones, directory creation, file upload, and compose bring‑up.
- Added a reusable step to run **pytest** on a remote tester VM and collect **Allure raw results** (+ optional `history`).
- **Provisioned and operated a self‑hosted Allure service on a separate VM**; wired CI to publish results and generate reports with history.
  **Impact (fill‑in):** ↓ flake/rerun rate **[X]%** · ↓ mean setup time **[Y] min** · ↓ time‑to‑signal (pytest→report) **[Z]%**

**VisionTree (Brainlab) — Advanced Software Engineer** · Weeki Wachee, FL · **Oct 2021 – Jul 2024**

- Delivered features aligned to **FHIR/HL7** for a patient‑reported outcomes platform used by major US hospitals.
- Built **ETL** from **AWS RDS (PostgreSQL)** to **Snowflake**; authored complex SQL views for patient compliance analytics.
- Migrated legacy **ColdFusion** endpoints to **NestJS (TypeScript)** APIs with modern patterns and tests.
- Implemented **automated testing** for a FHIR‑standard form builder to catch regressions pre‑release.
- Produced weekly query insights to identify heavy SQL paths and optimize performance.

**STRS Energy (fka Aniam Mechanical Engineering) — Engineering & Operations Manager** · Stuart, FL · **Feb 2018 – Oct 2021**

- Led development of an electro‑mechanical **battery‑brain** product; owned requirements → manufacturing → QA.
- Reduced manufacturing costs via process redesign across Israel, China, and Ireland suppliers.

**Additional Experience (Israel)**
**Project Manager, Combe Group** · **Jul 2015 – Jun 2016** — Managed ~$10M install/audits of fire/water/medical‑gas systems for a new hospital; led 3 subcontractors.
**Engineering Consultant, Aniam Mechanical Engineering** · **Jan 2012 – Jun 2016** — Product installs, QA, on‑site maintenance; iterative enhancements from customer feedback.
**Real Estate Broker/Apprentice Appraiser** · **Jul 2016 – Feb 2018** — Regulatory coordination, contract reviews, stakeholder management.

---

## Education

**Tel Aviv University** — B.S., Mechanical Engineering
**Ariel University** — Real Estate Appraisal (certificate)

## Professional Development

The Ultimate React Course (2024) · Full‑Stack Engineer Certificate (2023) · Playwright (2023) · Rice University: Python & Computing (2021) · U. Michigan: Python for Everybody (2020) · Analyzing Big Data with SQL (2021)

## Technical Snapshot

Python, TypeScript/JavaScript, NestJS, React/Vue/Nuxt, SQL/PostgreSQL, Git/GitHub, GitHub Actions, Ansible, Docker/Compose, basic Kubernetes, Playwright, Allure, AWS (RDS/S3 basics), Snowflake

---

# Variant: K8s/Helm + IaC Emphasis (use if accurate)

> Use this version only if you’ve touched Kubernetes/Helm in practice; add Terraform only if you have hands‑on exposure.

**Infra/DevOps (expanded):** Kubernetes (Helm/Kustomize basics), Terraform (modules/state/workspaces basics)
**Selected Additions (replace or append to XPLG bullets):**

- Containerized services via Docker/Compose with **migration patterns to Kubernetes** (Helm‑ready folder structure; values files per env).
- Authored starter **Terraform** module for CI prerequisites (e.g., artifact bucket, VM, security groups) and integrated plan/apply into CI with manual approvals.

**Tip:** If Terraform is not hands‑on, remove that bullet and keep only the Kubernetes line.

---

Perfect — I created both deliverables and laid out how to use them + a concrete job-hunt plan.

## Downloads

- One-pager CV: [PDF](sandbox:/mnt/data/Sagi_Levinas_OnePage_CV_Oct_2025.pdf) · [Markdown](sandbox:/mnt/data/Sagi_Levinas_OnePage_CV_Oct_2025.md)
- Covera-specific cover letter: [PDF](sandbox:/mnt/data/Sagi_Levinas_Cover_Letter_Covera_Oct_2025.pdf) · [Markdown](sandbox:/mnt/data/Sagi_Levinas_Cover_Letter_Covera_Oct_2025.md)
- (From earlier) Full CV: [PDF](sandbox:/mnt/data/Sagi_Levinas_CV_Oct_2025.pdf)
- Public repo scaffold to publish: [spec-driven-ci-ansible-template.zip](sandbox:/mnt/data/spec-driven-ci-ansible-template.zip)

## How to use them (quick playbook)

- **One-pager CV** → upload as your default resume. For each application, tweak 2–3 bullets to mirror the JD’s keywords (Python, CI/CD, Kubernetes, AWS/GCP, PostgreSQL, HL7/FHIR). Keep your X/Y/Z metrics updated.
- **Cover letter** → paste into the portal or email. Add one line pointing to your public “Spec-Driven CI + Ansible” repo once it’s on GitHub.
- **Full CV** → bring to recruiter calls or submit when they ask for a detailed version.
- **Repo** → publish publicly; add `tests/test_smoke.py`, a CI badge, and a redacted Allure screenshot (no PHI). Link it in your LinkedIn Featured section.

## 30-day “get hired” plan (concise)

**Week 1 (Materials):**

1. Publish the repo; add smoke test + badge.
2. Pull 3 metrics from recent runs (flake rate ↓, setup time ↓, time-to-signal ↓).
3. Update LinkedIn headline and About; add Featured: repo, Allure screenshot, CI diagram, full CV.

**Week 2 (Applications, 10–15 roles):** 4) Target health-tech + platform (Python/CI/CD/cloud). 5) For each role: tailor one-pager + cover letter; apply. 6) Track apps; follow up **7 days** later with a short note + repo link.

**Week 3 (Networking):** 7) Message 2–3 Covera engineers/PMs: 4-line note, repo link, 1 metric. 8) Ask 1–2 colleagues for a LinkedIn recommendation focused on outcomes. 9) Post a LinkedIn mini-thread: “Spec-driven CI for remote pytest + Allure in health-tech.”

**Week 4 (Interviews & momentum):** 10) Prep 3 STAR stories (modular CI, Allure reporting loop, FHIR/HL7 + ETL). 11) Rehearse a 12-minute whiteboard: “Compose → Helm on K8s in CI.” 12) Keep pipeline full (apply to 5 new roles); nudge pending apps with a fresh signal (e.g., repo improvement).

If you’d like, I can also:

- add a tiny `tests/test_smoke.py` + Makefile to the repo zip,
- generate a Covera recruiter outreach DM,
- or tailor the one-pager for 2–3 other target roles next.
