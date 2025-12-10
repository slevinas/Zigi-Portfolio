import asyncio

def f():


    return [lambda x: i + x for i in range(3)]


async def fetch(n):
    await asyncio.sleep(1)
    return n

async def main():
    tasks = [fetch(i) for i in range(5)]
    return await asyncio.gather(*tasks)


from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter

styles = getSampleStyleSheet()
story = []

text = """
SAGI LEVINAS
DevOps & Python Automation Engineer
Email: slevinas@gmail.com | Brooksville, FL — Remote Only

SUMMARY
DevOps & Python Automation Engineer with 5+ years of experience building internal tooling, test infrastructures,
containerized services, CI/CD workflows, and backend automation. Strong at turning manual engineering processes
into reliable pipelines, designing clean observability, and building systems that help teams move faster.
Enjoys debugging, backend logic, designing test harnesses, and building developer tooling. Seeking a long-term
remote role where I can own internal tools, automation workflows, and reliability-focused engineering.

CORE SKILLS
• Python Automation (asyncio, httpx, CLI tools, pipelines)
• Backend (FastAPI, API tooling, microservice patterns)
• Testing (pytest, smoke tests, parametrized tests, synthetic load)
• CI/CD (GitHub Actions, Docker pipelines)
• Observability (OpenTelemetry traces/metrics, ClickHouse ingestion)
• Infrastructure Automation (Docker, Compose, Ansible)
• Debugging distributed systems

EXPERIENCE

Python Automation & Observability Engineer (Contract)
XPLG – Turn Data Into Action™ — Remote | 2024–2025
• Built full benchmarking system: FastAPI target → async client SDK → ClickHouse analytics.
• Instrumented FastAPI microservices with OpenTelemetry (metrics + traces).
• Designed GitHub Actions pipelines orchestrating containerized test networks.
• Migrated orchestration logic from bash/Python scripts to Ansible playbooks.
• Created concurrency test runners, synthetic load engines, and Arazzo-based API testing.
• Debugged distributed systems using telemetry, logs, and automation.

Advanced Software Engineer
VisionTree / Brainlab — Remote | 2021–2024
• Developed internal backend tools, schema validation layers, HL7/FHIR integrations.
• Built automation utilities improving reliability of cloud-based workflows.
• Enhanced multiple services in distributed environment (Node/Python toolchain).

SELECTED PROJECTS
Benchmaker-Lite — FastAPI Benchmarking & Observability System
• End-to-end pipeline: FastAPI target → OTel Collector → ClickHouse analytics.
• Async benchmarking engine (httpx + asyncio).
• Full documentation, diagrams, and GitHub Pages site.

Modular Test Orchestrator — CI/CD Smoke Test Harness
• Dockerized FastAPI test target + pytest smoke suite.
• GitHub Actions workflow builds container and runs tests on dedicated test network.
• Reusable pattern for CI/CD reliability.

TECHNOLOGIES
Python, FastAPI, httpx, asyncio, pytest, Docker, GitHub Actions, Ansible,
OpenTelemetry, ClickHouse, JSON, YAML, Linux, CI/CD automation.

EDUCATION
B.Sc Mechanical Engineering — Tel Aviv University
"""

for line in text.split("\n"):
    story.append(Paragraph(line, styles["Normal"]))
    story.append(Spacer(1, 6))

output_path = "/mnt/data/Sagi_Levinas_Resume.pdf"
doc = SimpleDocTemplate(output_path, pagesize=letter)
doc.build(story)

output_path



from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

styles = getSampleStyleSheet()
story = []

text = """
SAGI LEVINAS
DevOps & Python Automation Engineer
Email: slevinas@gmail.com | Brooksville, FL — Remote Only

SUMMARY
DevOps & Python Automation Engineer with 5+ years of experience building internal tooling, test infrastructures, 
containerized services, CI/CD workflows, and backend automation. Strong at turning manual engineering processes 
into reliable pipelines, designing clean observability, and building systems that help teams move faster.
Enjoys debugging, backend logic, designing test harnesses, and building developer tooling. Seeking a long-term 
remote role where I can own internal tools, automation workflows, and reliability-focused engineering.

CORE SKILLS
• Python Automation (asyncio, httpx, CLI tools, pipelines)
• Backend (FastAPI, API tooling, microservice patterns)
• Testing (pytest, smoke tests, parametrized tests, synthetic load)
• CI/CD (GitHub Actions, Docker pipelines)
• Observability (OpenTelemetry traces/metrics, ClickHouse ingestion)
• Infrastructure Automation (Docker, Compose, Ansible)
• Debugging distributed systems

EXPERIENCE

Python Automation & Observability Engineer (Contract)
XPLG – Turn Data Into Action™ — Remote | 2024–2025
• Built full benchmarking system: FastAPI target → async client SDK → ClickHouse analytics.
• Instrumented FastAPI microservices with OpenTelemetry (metrics + traces).
• Designed GitHub Actions pipelines orchestrating containerized test networks.
• Migrated orchestration logic from bash/Python scripts to Ansible playbooks.
• Created concurrency test runners, synthetic load engines, and Arazzo-based API testing.
• Debugged distributed systems using telemetry, logs, and automation.

Advanced Software Engineer
VisionTree / Brainlab — Remote | 2021–2024
• Developed internal backend tools, schema validation layers, HL7/FHIR integrations.
• Built automation utilities improving reliability of cloud-based workflows.
• Enhanced multiple services in distributed environment (Node/Python toolchain).

SELECTED PROJECTS
Benchmaker-Lite — FastAPI Benchmarking & Observability System
• End-to-end pipeline: FastAPI target → OTel Collector → ClickHouse analytics.
• Async benchmarking engine (httpx + asyncio).
• Full documentation, diagrams, and GitHub Pages site.

Modular Test Orchestrator — CI/CD Smoke Test Harness
• Dockerized FastAPI test target + pytest smoke suite.
• GitHub Actions workflow builds container and runs tests on dedicated test network.
• Reusable pattern for CI/CD reliability.

TECHNOLOGIES
Python, FastAPI, httpx, asyncio, pytest, Docker, GitHub Actions, Ansible,
OpenTelemetry, ClickHouse, JSON, YAML, Linux, CI/CD automation.

EDUCATION
B.Sc Mechanical Engineering — Tel Aviv University
"""

for line in text.split("\n"):
    story.append(Paragraph(line, styles["Normal"]))
    story.append(Spacer(1, 4))

output_path = "/mnt/data/Sagi_Levinas_Resume.pdf"
doc = SimpleDocTemplate(output_path, pagesize=letter)
doc.build(story)

output_path


if __name__ == "__main__":
    # funcs = f()
    # print([fn(10) for fn in funcs])
    # result = asyncio.run(main())
    # print(result)
    data = {}
    print(data["missing"])

    