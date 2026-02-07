# owasp-top-10-attack-and-defense
Learn OWASP Top 10 Web Application Security vulnerabilities with hands-on labs. This repository demonstrates how common web vulnerabilities work, how attackers exploit them in controlled lab environments, and how to mitigate them using secure coding and best practices.
📁 Recommended Folder Structure
owasp-top-10-attack-and-defense/
│
├── README.md
├── LICENSE
├── .gitignore
│
├── 01-Injection/
│   ├── README.md
│   ├── vulnerable_app/
│   ├── attack_scenario.md
│   └── mitigation.md
│
├── 02-Broken-Authentication/
│   ├── README.md
│   ├── vulnerable_app/
│   ├── attack_scenario.mds
│
├── 03-Sensitive-Data-Exposure/
├── 04-XML-External-Entities-XXE/
├── 05-Broken-Access-Control/
├── 06-Security-Misconfiguration/
├── 07-Cross-Site-Scripting-XSS/
├── 08-Insecure-Deserialization/
├── 09-Using-Vulnerable-Components/
├── 10-Insufficient-Logging-Monitoring/
│
├── labs-setup/
│   ├── docker-compose.yml
│   └── setup.md
│
└── resources/
    ├── owasp-cheatsheets.md
    └── learning-links.md
    📄 Files You MUST Add (Explaination)
1️⃣ README.md (Main File – VERY IMPORTANT)
This is what recruiters & interviewers read first.
2️⃣ attack_scenario.md
Vulnerability concept
How attackers abuse logic
No illegal real-world hacking
3️⃣ mitigation.md
Secure coding
OWASP best practices
Headers, validation, auth fixes
4️⃣ vulnerable_app/
Intentionally insecure demo code
Local lab only (Flask / Node / PHP)
# OWASP Top 10 – Attack & Defense Labs 🔐

## 📌 About the Project
This project is designed to help developers and DevOps engineers understand
the OWASP Top 10 web application vulnerabilities through practical examples.

Each module includes:
- Vulnerability explanation
- How attackers exploit it (educational labs)
- Secure coding and mitigation techniques

⚠️ All demonstrations are for **educational purposes only**.

---

## 🧩 OWASP Top 10 Covered

1. Injection
2. Broken Authentication
3. Sensitive Data Exposure
4. XML External Entities (XXE)
5. Broken Access Control
6. Security Misconfiguration
7. Cross-Site Scripting (XSS)
8. Insecure Deserialization
9. Using Vulnerable Components
10. Insufficient Logging & Monitoring

---

## 🛠️ Tech Stack
- Python (Flask)
- Node.js (Express)
- Docker
- OWASP Juice Shop (optional)
- Burp Suite (Community)

---

## 🚀 How to Run Labs

```bash
git clone https://github.com/yourusername/owasp-top-10-attack-and-defense.git
cd owasp-top-10-attack-and-defense
docker-compose up
🧠 Learning Outcome
Understand real-world web attacks
Learn secure coding practices
Improve DevSecOps & AppSec skills
📚 References
https://owasp.org/www-project-top-ten/
OWASP Cheat Sheets
---

## 🧪 Example: Module 01 – Injection (SQLi)

### `01-Injection/README.md`
```md
## Injection Vulnerability

Injection flaws occur when untrusted input is sent to an interpreter
without proper validation.

### Common Types
- SQL Injection
- Command Injection
- LDAP Injection
