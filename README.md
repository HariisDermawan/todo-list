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
* Edit tugas
* Tandai tugas selesai
* Hapus tugas

## Halaman Utama

Halaman utama digunakan untuk menampilkan daftar tugas yang telah dibuat. User dapat menambahkan tugas baru, menandai tugas sebagai selesai, mengedit, atau menghapus tugas.

## Cara Menjalankan

### 1. Clone Repository

```bash
git clone https://github.com/HariisDermawan/todo-list.git
cd todo-list
```

### 2. Cek Virtual Environment

Pastikan folder `venv` tersedia:

```powershell
dir .\venv\Scripts
```

Pastikan terdapat file `Activate.ps1`.

### 3. Aktifkan Virtual Environment

```powershell
.\venv\Scripts\Activate.ps1
```

Jika berhasil, terminal akan berubah menjadi:

```text
(venv) PS C:\Users\darma\todo_list>
```

### 4. Install Dependency

```bash
pip install -r requirements.txt
```

### 5. Buat Database MySQL

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

### 6. Konfigurasi Database

Sesuaikan `config.py`:

```python
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = ""
MYSQL_DATABASE = "daily_task_db"
```

### 7. Jalankan Aplikasi

```bash
python app.py
```

Kemudian buka:

```text
http://127.0.0.1:5000
```

```bash
deactivate
```
