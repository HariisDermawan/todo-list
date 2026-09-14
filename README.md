# Todo List

Aplikasi web sederhana untuk mencatat dan mengelola tugas harian.

## Teknologi

* Python
* Flask
* MySQL
* HTML
* Bootstrap

## Fitur

* Tambah tugas
* Lihat tugas
* Edit tugas
* Tandai tugas selesai
* Hapus tugas

## Cara Menjalankan

1. Clone repository.
2. Install dependency:

```bash
pip install -r requirements.txt
```

3. Buat database MySQL:

```sql
CREATE DATABASE daily_task_db;

USE daily_task_db;

CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    status ENUM('pending', 'completed') DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

4. Sesuaikan konfigurasi database di `config.py`.
5. Jalankan aplikasi:

```bash
python app.py
```

6. Buka:

```text
http://127.0.0.1:5000
```
