
# 🚀 PostgreSQL Lab with Patroni, HAProxy & Barman

This project demonstrates a **complete High Availability (HA) and Disaster Recovery (DR) lab** for PostgreSQL, with open-source tools.  

It’s designed as a **hands-on demo environment** for learning, testing, and showcasing skills in PostgreSQL clustering, failover, backups, and PITR.

---

## ✨ Features

- **PostgreSQL 16**   
- **Patroni** – Automates leader election, failover, replication management  
- **Consul** – Distributed Configuration Store for Patroni  
- **HAProxy** – Routes traffic transparently to the current primary  
- **Barman** – Backup & Point-in-Time Recovery (PITR) solution  
- **Sample Flask App** – Demonstrates how client apps remain unaware of failover  
- **Helper Scripts** – Replication monitoring, manual backup trigger  

---

## 📂 Project Structure

```
postgres-patroni-lab/
├── app/                # Flask application (Dockerized)
├── barman/             # Local barman image + config
├── haproxy/            # HAProxy config
├── patroni/            # Patroni Dockerfile + node configs
├── primary/init/       # Init SQL for sample schema & data
├── scripts/            # Helper scripts (lag, backups)
├── docker-compose.yml  # Orchestration
├── .env                # Environment variables
└── README.md           # You are here!
```

---

## 🛠️ Quick Start

### 1. Clone & Build
```bash
git clone https://github.com/YOUR_USERNAME/postgres-patroni-lab.git
cd postgres-patroni-lab
docker compose build
```

### 2. Start the Lab
```bash
docker compose up -d
```

Wait 60–120 seconds for cluster formation. Patroni will elect a **leader** and register followers.

### 3. Verify Cluster
Check node roles via Patroni REST API:
```bash
curl http://localhost:80081/role
curl http://localhost:80082/role
curl http://localhost:80083/role
```

### 4. Test the App
```bash
curl http://localhost:8000/
```
👉 Returns the message count from the database.  
👉 Insert a message:
```bash
curl -X POST -H "Content-Type: application/json"      -d '{"text":"Hello HA!"}'      http://localhost:8000/messages
```

---

## 🔄 Simulating Failover

1. Stop the current primary:
   ```bash
   docker stop pg1
   ```
2. Patroni automatically promotes a standby.
3. HAProxy updates backend and routes to new primary.
4. The Flask app continues working with **no changes needed**.

Check roles again:
```bash
curl http://localhost:80082/role
```

---

## 💾 Backups & PITR with Barman

Run a backup:
```bash
./scripts/barman_backup.sh
```

List backups:
```bash
docker exec -it barman barman list-backup pg1
```

---

## 📊 Helper Scripts

- **Check replication lag**
  ```bash
  ./scripts/replication_lag.sh
  ```
- **Run Barman backup**
  ```bash
  ./scripts/barman_backup.sh
  ```

---

## 🎯 What You Learn

✅ How Patroni manages PostgreSQL HA  
✅ Automatic failover with transparent client redirection via HAProxy  
✅ Setting up backups with Barman  
✅ Building & deploying a simple app connected to a resilient Postgres cluster  
✅ Hands-on lab suitable for **interviews, demos, and learning**  

---

## 📸 Demo Architecture

```
        ┌─────────┐
        │  Consul │  (DCS)
        └────┬────┘
             │
 ┌───────────┴──────────────┐
 │        Patroni Cluster   │
 │   ┌──────┐  ┌──────┐     │
 │   │ pg1  │  │ pg2  │ ... │  (Postgres + Patroni)
 │   └──────┘  └──────┘     │
 └───────────┬──────────────┘
             │
         ┌───▼─────┐
         │ HAProxy │  (routes to leader)
         └───┬─────┘
             │
 ┌───────────▼────────────┐
 │   Flask Application    │
 └────────────────────────┘
```

---

## 📌 Notes

- All components are **open-source** and based on **official images** (no license issues).  
- Intended for **learning, POCs, and demos** – not for production.  

---

## 🙌 Credits

- [PostgreSQL](https://www.postgresql.org/)  
- [Patroni](https://patroni.readthedocs.io/)  
- [Consul](https://www.consul.io/)  
- [HAProxy](http://www.haproxy.org/)  
- [Barman](https://www.pgbarman.org/)  

---

💡 If you like this project, ⭐ star the repo and share it!
