# Cortico-Test Project

## Overview
This repository contains two applications built from scratch:

1. **Textboard** – a minimal message board using Flask and SQLite.
2. **Monitoring App** – a simple Python-based monitoring service.

The applications are **dockerized** and can be run using `docker-compose up`.  

The focus of this project is **backend functionality, service communication, logging, error handling**, and **containerized deployment**, not the UI.  

---

## Live Websites

- **Textboard:** [https://cortico-test.arnoldgutib.com](https://cortico-test.arnoldgutib.com)  
- **Monitoring App:** [https://monitor.arnoldgutib.com](https://monitor.arnoldgutib.com) 

---

## Project Objectives

- Dockerize all applications for easy deployment.
- Implement simple automated testing (two test cases each).
- Use Python Flask backend.
- Keep UI simple and minimal.
- Include proper logging and error handling.
- Configure reverse proxy via Nginx with SSL.
- Ensure atomic commits for traceable development history.
- Provide clear setup instructions for cloning and running.

---

## Directory Structure

- **Textboard App:** contains Flask app, templates, Dockerfile, tests, and SQLite database.
- **Monitoring App:** simple Python app with Dockerfile and tests.
- **Nginx Configs:** separate configs for reverse proxy and subdomains.
- **Docker Compose:** orchestrates all services.

---

## Setup Instructions

1. Clone the repository.
2. Build and run all applications using Docker Compose.
3. Configure Nginx as a reverse proxy for the textboard subdomain.
4. Obtain SSL certificates with Certbot after creating the correct DNS CNAME record.
5. Verify the apps are running through the subdomain and internal Docker ports.

---

## Key Highlights

- **Flask Textboard App:** Stores messages with user names in SQLite. Errors are logged for Docker monitoring.
- **Monitoring App:** Simple Python service with health checks and Dockerized deployment.
- **Dockerization:** Each app runs in a container with proper port mappings.
- **Automated Tests:** Example test cases demonstrate core functionality of both apps.
- **Error Handling & Logging:** Database and Flask errors captured in logs. Nginx logs used for proxy issues.
- **Nginx & SSL:** Reverse proxy configured with SSL. DNS and certificate issues resolved during setup.

---

## Troubleshooting / Pain Points

1. **Port Conflicts:** Existing services used the same ports, resolved by stopping conflicting services or remapping Docker ports.
2. **Database Schema Issues:** Initial SQLite table lacked required columns; fixed by updating table schema.
3. **Docker File Permissions:** Ensured proper directories exist and permissions are correct for SQLite access.
4. **Nginx SSL Errors:** Certificates initially missing; resolved by adding proper DNS CNAME and using Certbot.
5. **DNS / NXDOMAIN:** Subdomain needed to be added to DNS for proper resolution.

---

## Conclusion

This project demonstrates:

- Building and dockerizing Python apps from scratch.
- Handling database schema and runtime errors.
- Configuring Nginx with SSL.
- Implementing automated tests and proper logging.
- Providing clear setup and troubleshooting documentation.

---

## Errors Encountered

1. **SQLite Database Missing / Schema Issues**
   - Initial SQLite database was missing (`data/messages.db`) in container.
   - SQLite table did not contain the `name` column, causing `sqlite3.OperationalError: no such column: name`.
   - Fixed by updating the `CREATE TABLE IF NOT EXISTS messages` schema to include `name` and `content`.

2. **Port Conflicts**
   - Flask default port 5000 was already in use on the host.
   - Resolved by mapping Docker container ports explicitly in `docker-compose.yml`.

3. **Missing SQLite3 in Container**
   - Attempting to access `sqlite3` inside container failed because the package wasn’t installed.
   - Resolved by handling DB schema creation through Python code at app startup instead.

4. **Nginx SSL Certificate Issues**
   - Nginx failed to start due to missing SSL certificates for `cortico-test.arnoldgutib.com`.
   - Error: `cannot load certificate ... No such file or directory`.
   - Resolved by creating proper DNS CNAME record and issuing certificate via Certbot.

5. **DNS Resolution**
   - Subdomain `cortico-test.arnoldgutib.com` could not be reached: `DNS_PROBE_FINISHED_NXDOMAIN`.
   - Fixed by adding a CNAME record pointing `cortico-test` to `arnoldgutib.com`.

6. **Incorrect Flask Logs / Internal Server Errors**
   - `Internal Server Error` due to database schema mismatch.
   - Resolved after schema update and ensuring the database file exists in the mounted volume.

---

## Atomic Commits (Supposedly)

- Database schema creation and fix.
- Dockerization of both apps.
- Nginx reverse proxy configuration for subdomain.
- SSL setup with Certbot.
- Documentation of setup, errors, and troubleshooting.

---


## Lessons Learned & Struggles

- Dockerizing multiple apps can quickly lead to port conflicts; planning ports ahead is crucial.
- SQLite schema updates in Docker volumes need careful handling to avoid runtime errors.
- Setting up Nginx with SSL requires valid DNS records; missing CNAMEs cause headaches.
- Keeping atomic commits helps trace back problems later.
- Even small apps can generate surprisingly tricky integration issues—but solving them is rewarding. 😅

---

## References

- Flask Documentation: [https://flask.palletsprojects.com](https://flask.palletsprojects.com)
- SQLite Documentation: [https://www.sqlite.org/docs.html](https://www.sqlite.org/docs.html)
- Docker Documentation: [https://docs.docker.com/](https://docs.docker.com/)
- Docker Compose: [https://docs.docker.com/compose/](https://docs.docker.com/compose/)
- Nginx Documentation: [https://nginx.org/en/docs/](https://nginx.org/en/docs/)
- Certbot / Let's Encrypt: [https://certbot.eff.org/](https://certbot.eff.org/)
- Stack Overflow Discussions:
  - SQLite column issues: [https://stackoverflow.com/questions/6244352/sqlite-adding-column-to-existing-table](https://stackoverflow.com/questions/6244352/sqlite-adding-column-to-existing-table)
  - Nginx SSL certificate permissions: [https://stackoverflow.com/questions/51164201/nginx-ssl-cert-permission-denied](https://stackoverflow.com/questions/51164201/nginx-ssl-cert-permission-denied)
  - Docker port conflicts: [https://stackoverflow.com/questions/30685716/docker-port-already-in-use](https://stackoverflow.com/questions/30685716/docker-port-already-in-use)
- Blog References:
  - Dockerizing Flask apps: [https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/](https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/)
  - Nginx reverse proxy for Docker: [https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-as-a-reverse-proxy-for-docker-containers-on-ubuntu-20-04](https://www.digitalocean.com/community/tutorials/how-to-set-up-nginx-as-a-reverse-proxy-for-docker-containers-on-ubuntu-20-04)
  - Certbot DNS and subdomain setup: [https://www.linode.com/docs/guides/how-to-secure-nginx-with-lets-encrypt-on-ubuntu-20-04/](https://www.linode.com/docs/guides/how-to-secure-nginx-with-lets-encrypt-on-ubuntu-20-04/)
