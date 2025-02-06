# Chọn image Python làm nền tảng
FROM python:3.11.6

# Đặt thư mục làm việc trong container
WORKDIR /app

# Sao chép các file cần thiết vào container
COPY requirements.txt .

# Cài đặt thư viện cần thiết
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ mã nguồn vào container
COPY . .

# Mở port 8000 (Django mặc định chạy trên 8000)
EXPOSE 8000

# Lệnh chạy ứng dụng Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
