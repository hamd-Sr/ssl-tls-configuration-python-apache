# 🔐 SSL/TLS Configuration and HTTPS Communication using Python & Apache

This repository demonstrates a complete implementation of **secure HTTPS communication** using **Python’s built-in HTTPServer** and **Apache HTTP Server** with **SSL/TLS encryption**.  

It guides you through the process of generating SSL/TLS certificates using **OpenSSL**, configuring both Python and Apache servers for encrypted connections, and verifying the secure data transmission through **Wireshark packet analysis**.  

This project was developed as part of a cybersecurity lab exercise at **King Fahd University of Petroleum and Minerals (KFUPM)** under the **SEC 521 – Network Security** course.

---

## 📘 Project Overview

In this project, you’ll learn how HTTPS ensures **data confidentiality, integrity, and authentication** through the **SSL/TLS handshake** process.  

You will:
- Generate and verify self-signed certificates.
- Configure a **Python HTTPS server** that uses SSL/TLS for encryption.
- Configure **Apache HTTP Server** to serve HTTPS using `mod_ssl` and `proxy_http`.
- Capture and analyze the TLS handshake and encrypted traffic using **Wireshark**.
- Understand how browsers validate certificates and establish trust.

By the end of this lab, you’ll have a complete end-to-end understanding of how HTTPS secures web communication — from cryptographic key generation to packet-level analysis.

---

## ⚙️ Technologies & Tools Used

| Category | Tools / Technologies |
|-----------|----------------------|
| Programming | Python 3.x |
| Server | Apache HTTP Server |
| Encryption | OpenSSL |
| Traffic Analysis | Wireshark |
| OS Environment | Linux / Ubuntu |
| Proxy Module | `mod_ssl`, `proxy_http` |
| Browser Validation | Chrome / Firefox |

---

## 🧩 Repository Structure
ssl-tls-configuration-python-apache/
│
├── 521.html # Simple HTML page served via HTTPS
├── HTTP_server.py # Basic HTTP server implementation (non-encrypted)
├── HTTPS_server.py # Python HTTPS server using SSL/TLS certificates
│
├── openssl/ # Certificate generation scripts & logs
│ ├── generate_certs.sh
│ ├── server.crt
│ ├── server.key
│ └── command_log.txt
│
├── apache_config/ # Apache SSL and proxy configurations
│ ├── task2-ssl.conf
│ └── proxy_notes.txt
│
├── wireshark/ # TLS packet traces and analysis notes
│ ├── packets_summary.txt
│ └── tls_trace.png
│
├── screenshots/ # Screenshots of browser & terminal verification
│ ├── ssl_creation.png
│ ├── apache_status.png
│ ├── browser_https.png
│ └── https_traffic.png
│
├── instructor_photo.jpg # Project-related image
├── kfupm.png # Placeholder / branding image
├── favicon.ico
│
├── .gitignore # Excludes private keys and system files
├── LICENSE # Apache 2.0 License
└── README.md # Project documentation


 
# 🧭 Step-by-Step Guide: SSL/TLS Configuration and HTTPS Communication using Python & Apache

This guide provides **detailed, executable steps** for replicating the HTTPS configuration project that integrates **Python’s HTTPServer**, **Apache HTTP Server**, and **OpenSSL** for SSL/TLS encryption.  

Follow these steps in sequence to build, run, and verify a secure HTTPS environment.

---

## ⚙️ Prerequisites

Before starting, ensure you have the following installed:

| Tool | Version | Purpose |
|------|----------|----------|
| Python | ≥ 3.8 | Run HTTPS server |
| Apache2 | Latest | Web server with SSL/TLS support |
| OpenSSL | Latest | Certificate generation |
| Wireshark | Latest | Packet capture & TLS analysis |
| OS | Linux / Ubuntu recommended | Development environment |

---

## 🪜 Step 1 — Setup the Working Directory

Create a folder and clone or download this repository:

```bash
mkdir ssl-tls-configuration-python-apache
cd ssl-tls-configuration-python-apache
````

This folder contains all required files:

* `HTTP_server.py`, `HTTPS_server.py`
* `openssl/` → certificate scripts
* `apache_config/` → configuration files
* `wireshark/` and `screenshots/` → analysis and evidence

---

## 🔐 Step 2 — Generate SSL/TLS Certificates using OpenSSL

### 📄 Command:

```bash
cd openssl
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout server.key -out server.crt \
  -subj "/C=SA/ST=Eastern/L=Dhahran/O=KFUPM/OU=SEC521/CN=localhost"

openssl verify server.crt
```

### ✅ Output:

```
server.crt: OK
```

You now have:

* `server.crt` → Public certificate
* `server.key` → Private key

Both are required for HTTPS encryption.

> 🧠 Tip: These are **self-signed** certificates for testing.
> For production, use a certificate issued by a **trusted Certificate Authority (CA)**.

---

## 🐍 Step 3 — Run the Python HTTPS Server

Navigate to the project root and start your server:

```bash
python3 HTTPS_server.py
```

Expected output:

```
Starting HTTPS server on https://127.0.0.1:9090
```

### 🖥️ Verification:

Open a browser and visit:

```
https://127.0.0.1:9090
```

You should see your `521.html` page.
If the browser shows a certificate warning — that’s expected for self-signed certs.

---

## 🌐 Step 4 — Configure Apache for HTTPS & Proxy Setup

### 4.1 Install Apache (if not already installed)

```bash
sudo apt update
sudo apt install apache2
```

### 4.2 Enable SSL and Proxy Modules

```bash
sudo a2enmod ssl
sudo a2enmod proxy_http
sudo systemctl restart apache2
```

### 4.3 Copy Configuration File

```bash
sudo cp apache_config/task2-ssl.conf /etc/apache2/sites-available/task2-ssl.conf
sudo a2ensite task2-ssl.conf
sudo systemctl restart apache2
```

The `task2-ssl.conf` file enables HTTPS on port **443** and proxies requests to your **Python server** running on **port 9595**.

---

## 🌍 Step 5 — Verify HTTPS Functionality via Browser

1. Open your browser and go to:

   ```
   https://127.0.0.1/
   ```
2. Look for:

   * ✅ **Lock icon (🔒)** – confirms an HTTPS connection.
   * ✅ **Valid certificate details** – verify it matches your generated cert.
   * ✅ **Content served** – your 521.html page or test webpage should load.

---

## 🧪 Step 6 — Capture and Analyze TLS Packets using Wireshark

### 6.1 Start Capture:

* Open Wireshark
* Select the **loopback interface (lo)** on Linux or **Localhost** on Windows
* Start recording traffic

### 6.2 Apply Filter:

```
tls
```

### 6.3 Visit:

```
https://127.0.0.1:9090
```

### 6.4 Stop Capture:

Now analyze:

* **ClientHello** → Client initiates the handshake.
* **ServerHello** → Server responds with chosen cipher suite.
* **Certificate** → Server sends certificate.
* **Key Exchange** → Shared secret established.
* **Application Data** → Encrypted communication starts.

### 6.5 Verify Encryption:

Check the TLS record layer packets — the payload should appear as unreadable encrypted data.

---

## 🔍 Step 7 — Common Troubleshooting

| Issue                         | Cause                   | Solution                           |
| ----------------------------- | ----------------------- | ---------------------------------- |
| `SSL_ERROR_SYSCALL`           | Key or cert not found   | Check paths in `HTTPS_server.py`   |
| Browser “Not Secure”          | Self-signed certificate | Accept manually for testing        |
| Apache not starting           | Port conflict           | Stop other services using port 443 |
| Wireshark not showing packets | Wrong interface         | Select `lo` or localhost capture   |

---

## 🔬 Understanding the SSL/TLS Handshake

| Stage                       | Description                                 |
| --------------------------- | ------------------------------------------- |
| **1. ClientHello**          | Client proposes cipher suites & TLS version |
| **2. ServerHello**          | Server selects cipher & sends certificate   |
| **3. Certificate Exchange** | Authentication of server                    |
| **4. Key Exchange**         | Secure symmetric session key established    |
| **5. Data Transfer**        | Encrypted data exchange begins              |

This process ensures:

* **Authentication** (who you’re talking to)
* **Confidentiality** (data encryption)
* **Integrity** (no tampering in transit)

---

## 📸 Step 8 — Document the Results

Take screenshots of the following and place them in the `/screenshots` folder:

* ✅ OpenSSL certificate generation terminal output
* ✅ Python server terminal showing HTTPS startup
* ✅ Browser showing padlock and HTTPS page
* ✅ Wireshark packet capture showing TLS handshake

These serve as your **proof of completion and evidence of encryption**.

---

## 🧠 Step 9 — Summary of Key Learnings

* You configured both **application-level** and **server-level** encryption.
* You understood the **certificate generation, trust, and verification process**.
* You captured and decoded the **TLS handshake**.
* You confirmed **end-to-end encryption** from browser to Python server via Apache.

---

## 📄 Step 10 — Clean Up Environment

When done:

```bash
sudo a2dissite task2-ssl.conf
sudo systemctl reload apache2
```

Optional cleanup:

```bash
rm -rf openssl/server.*
```

---

## ✅ Final Outcome

You now have:

* A **working HTTPS setup** using Python & Apache.
* Verified encrypted communication in Wireshark.
* A documented workflow demonstrating applied **network security and cryptography** concepts.

---

## 🧾 License

This step-by-step guide and project are covered under the **Apache License 2.0**.
You’re free to reuse and modify this workflow with proper attribution.

---

## 🧑‍💻 Author

**Hamdan Ahmed**
Master’s in Information Assurance and Security — *KFUPM*
📍 Dhahran, Eastern Province, Saudi Arabia
🔗 [LinkedIn](https://linkedin.com/in/HamdanAhmed)

