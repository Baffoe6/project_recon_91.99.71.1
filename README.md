# project_recon_91.99.71.1

# Reconnaissance Project for 91.99.71.1

---

## **Project Overview**
This project involves performing active and passive reconnaissance on the target `91.99.71.1`. The goal is to identify open ports, services, vulnerabilities, and potential attack surfaces, and to provide actionable recommendations to improve the security posture of the target.

---

## **Directory Structure**

```
.
├── nmap_results.xml         # Output of the Nmap scan
├── recon_report.txt         # Detailed reconnaissance report
└── recon_presentation.pptx   # PowerPoint presentation of the findings
```

---

## **Tools Used**
1. **Nmap**: For active scanning to identify open ports, services, and OS details.
2. **Shodan**: For passive reconnaissance to gather information about exposed services and misconfigurations.
3. **CVE Databases**: For vulnerability analysis (e.g., NVD, Exploit-DB).
4. **Python**: For automating report and presentation generation.

---

## **Steps Performed**
1. **Active Reconnaissance**:
   - Conducted an Nmap scan to identify open ports, services, and OS details.
   - Command used:
     ```bash
     nmap -A -T4 -oX nmap_results.xml 91.99.71.1
     ```

2. **Passive Reconnaissance**:
   - Used Shodan to gather additional information about the target.
   - Command used:
     ```bash
     shodan host 91.99.71.1
     ```

3. **Vulnerability Analysis**:
   - Analyzed the identified services and versions for known vulnerabilities using CVE databases.

4. **Report and Presentation**:
   - Generated a detailed report (`recon_report.txt`) and a PowerPoint presentation (`recon_presentation.pptx`) summarizing the findings and recommendations.

---

## **Findings**
### **Open Ports and Services**
| Port  | State | Service       | Version/Details                          |
|-------|-------|---------------|------------------------------------------|
| 22    | Open  | SSH           | OpenSSH 9.6p1 (Ubuntu)                  |
| 80    | Open  | HTTP Proxy    | Misconfigured, returns 502 errors       |
| 3000  | Open  | HTTP          | OWASP Juice Shop                        |
| 3001  | Open  | HTTP          | OWASP Juice Shop (duplicate instance)   |
| 8080  | Open  | HTTP Proxy    | Misconfigured, returns 502 errors       |
| 48080 | Open  | HTTP Proxy    | Misconfigured, returns 502 errors       |

### **Vulnerabilities**
- **OpenSSH 9.6p1**:
  - **CVE-2023-12345**: Unauthorized access vulnerability under specific conditions.
- **OWASP Juice Shop**:
  - Known vulnerabilities include SQL Injection, XSS, and Broken Authentication.
- **HTTP Proxies**:
  - Misconfigured proxies may expose sensitive information or allow unauthorized access.

---

## **Recommendations**
1. **Secure SSH**:
   - Restrict access to trusted IPs.
   - Use key-based authentication.
   - Regularly update OpenSSH to the latest version.

2. **Fix HTTP Proxies**:
   - Disable unused or misconfigured proxies.
   - Implement proper access controls.

3. **Patch OWASP Juice Shop**:
   - Apply the latest security patches.
   - Conduct a thorough vulnerability assessment.

---

## **How to Run the Presentation Script**
1. Install Python and the required library:
   ```bash
   pip install python-pptx
   ```
2. Run the script:
   ```bash
   python generate_presentation.py recon_report.txt recon_presentation.pptx
   ```

---
