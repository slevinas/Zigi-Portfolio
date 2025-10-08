
### Spec‑Driven CI Orchestration Template (GitHub Actions + Ansible)

A minimal, reusable pattern for running end‑to‑end tests on a remote VM using GitHub Actions + Ansible. The pipeline loads config files (YAML → JSON), conditionally ensures infra (Python, Docker, directories, files), runs tests via pytest, and publishes results to Allure. Artifacts (`raw-results-*.tgz`) are retained for traceability.

#### Features

* Config‑first: YAML specs drive the pipeline; no hard‑coding of hosts or paths.
* Conditional ensure steps (install Python/Docker, create directories, upload files, bring up Compose stacks).
* Secure secret handling (ephemeral SSH agent; `.env` contents passed via GitHub Secrets, never as plaintext files).
* Inventory‑scoped Ansible runs using `--limit <inventory_host>`.
* Artifact contracts: `raw-results-*.tgz` enforced and uploaded.

#### High‑level architecture

* **Orchestrator:** GitHub Actions (self‑hosted or hosted) running Ansible playbooks.
* **Tester VM:** Target host for services/tests (addressed via inventory/limit).
* **Reporting:** Allure server (self‑hosted or cloud) receives results.

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
    branches: [ ci/spec-driven-template ]
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
inventory_host: "<INVENTORY_HOST>"  # e.g. tester-01
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

* Store **all secrets** (SSH key, `.env` contents, tokens) only in **GitHub Secrets**.
* Do not commit inventories with real hostnames or IPs; use placeholders in public repos.
* Ensure playbooks are **idempotent**; cleanup SSH agents at job end.

#### Getting started

1. Add a tester host to your private inventory and configure SSH.
2. Create GitHub Secrets: `TESTER_SSH_KEY`, `TESTER_ENV_FILE_CONTENTS`, `ALLURE_TOKEN` (if needed).
3. Adjust the three configs: infra spec, pytest spec, Allure inputs.
4. Push a branch (e.g., `ci/spec-driven-template`) and check the Actions tab.

#### Redaction checklist (public repos)

* [ ] Replace real org/app names with neutral terms ("Service A").
* [ ] Remove internal paths/IPs; keep relative, template paths.
* [ ] Strip test data; keep small, synthetic samples only.
* [ ] Confirm no logs or artifacts contain PHI/PII.

#### License

MIT (or your preferred permissive license).
