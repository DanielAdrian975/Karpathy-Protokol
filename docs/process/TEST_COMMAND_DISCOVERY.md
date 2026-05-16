# Test Command Discovery

Date: 2026-05-16
Mode: Review/Audit + Wiki Maintenance
Scope: marker discovery only. No dependency installation, no test execution, no credential reads.

## Discovery Commands

```text
rg --files -g 'pyproject.toml' -g 'package.json' -g 'requirements.txt' -g 'setup.py' -g 'Makefile' -g 'docker-compose.yml' -g 'pytest.ini' -g 'tox.ini' -g 'noxfile.py' -g '!Bahan/.streamlit/**'
Get-ChildItem -Recurse -Force -File -Include pyproject.toml,package.json,requirements.txt,setup.py,Makefile,docker-compose.yml,pytest.ini,tox.ini,noxfile.py
git check-ignore -v _tmp_autoresearch_template/autoresearch_template_python_mas_c4et_boris/requirements.txt _tmp_skills_modular_build Bahan/.streamlit/secrets.toml
```

## Root Command Status

| Area | Status |
|---|---|
| Root `package.json` | Not found |
| Root `pyproject.toml` | Not found |
| Root `Makefile` | Not found |
| Root `docker-compose.yml` | Not found |
| Root pytest/tox/nox config | Not found |
| Canonical root test command | **Unresolved** |

## Subproject Command Matrix

| Path | Markers Found | Classification | Safe Candidate Commands | Staging Decision |
|---|---|---|---|---|
| `Bahan\Enhance Pengetahuan Ekstraktor\` | `README.md`, `requirements.txt` | Candidate Python source subproject | Create venv, install `requirements.txt`, then discover tests. No canonical test marker found. | NO-GO until source audit |
| `_tmp_autoresearch_template\autoresearch_template_python_mas_c4et_boris\` | `README.md`, `requirements.txt` | Ignored temporary/template Python workspace | Candidate commands likely Python-based, but path is ignored under `_tmp*/`; use only as reference unless promoted. | NO-GO as tracked source |
| `Bahan\Karpathy RAG system\llm-wiki\` | `AGENTS.md`, `README.md` | Nested Git/wiki subproject | Read-only review only until submodule/separate repo decision. | NO-GO until boundary decision |
| `Bahan\llm-wiki-ingest\` | `AGENTS.md`, `README.md` | Wiki tooling copy/subproject | Read-only review only until source audit. | NO-GO until source audit |

## Safe Verification Policy

- For root process/docs tasks, use structural checks: required files exist, `git diff --check`, `git diff --cached --check`, staged-file review, and process log consistency.
- For implementation tasks, stop until the authoritative subproject is selected and its test command is validated.
- Do not install dependencies or run executable scripts in source corpus without a separate implementation/test plan.

## Unresolved Blockers

- Authoritative implementation target is not selected.
- No root-level automated test command exists.
- Subproject requirements files have not been dependency-audited.
- `_tmp*/` is intentionally ignored and should not become the test authority without promotion.
