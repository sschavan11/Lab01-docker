# 🐳 Lab 01 – Dockerizing a Machine Learning Training Pipeline

## 📌 Objective

The goal of this lab is to containerize a Machine Learning training script using Docker.  
This demonstrates how to create a reproducible ML environment using containerization.

The project trains a Logistic Regression model on the Wine dataset and saves the trained model inside the container.

---

## 📂 Project Structure

```
Lab01-docker/
│
├── Dockerfile
├── requirements.txt
└── src/
    └── main.py
```

---

## 🧠 Machine Learning Workflow

### Dataset
- Wine Dataset (from scikit-learn)

### Model
- Logistic Regression

### Pipeline
- StandardScaler (Feature Scaling)
- LogisticRegression (max_iter=5000, solver='lbfgs')

### Output

After successful training:

```
The model training was successful (Wine + Logistic Regression)
```

The trained model is saved as:

```
wine_model.pkl
```

---

## 🐳 Docker Configuration

### Base Image
```
python:3.10
```

### Recommended Dockerfile

```dockerfile
FROM python:3.10

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ .

CMD ["python", "main.py"]
```

### Dockerfile Explanation

- **FROM python:3.10** → Uses official Python runtime  
- **WORKDIR /app** → Sets working directory inside container  
- **COPY requirements.txt .** → Copies dependency file first (improves caching)  
- **RUN pip install -r requirements.txt** → Installs required dependencies  
- **COPY src/ .** → Copies ML script into container  
- **CMD ["python", "main.py"]** → Runs training script when container starts  

---

## 📦 Dependencies

Listed in `requirements.txt`:

```
scikit-learn
joblib
```

---

## 🚀 How to Run

### 1️⃣ Build Docker Image

```bash
docker build -t lab1:v1 .
```

---

### 2️⃣ Run Container

```bash
docker run --rm lab1:v1
```

### Expected Output

```
The model training was successful (Wine + Logistic Regression)
```

---

### 3️⃣ Save Model to Local Machine (Optional)

To save `wine_model.pkl` to your local folder:

**PowerShell (Windows):**

```powershell
docker run --rm -v ${PWD}:/app lab1:v1
```

After running this command, `wine_model.pkl` will appear in your local directory.

---

### 4️⃣ Save Docker Image as TAR

```bash
docker save lab1:v1 > my_image.tar
```

This exports the Docker image for portability and sharing.

---

## 🔍 Verify Docker Setup

List images:
```bash
docker images
```

List running containers:
```bash
docker ps
```

List all containers (including stopped):
```bash
docker ps -a
```

---

## 🎯 Key Concepts Demonstrated

- Dockerfile creation  
- Image building  
- Container execution  
- Reproducible ML environments  
- Dependency isolation  
- Volume mounting  
- Model serialization with joblib  

---

## 🔬 Reproducibility

This project demonstrates how Docker ensures:

- Environment consistency  
- Cross-machine portability  
- Dependency isolation  
- Reproducible ML pipelines  

The same image can be run on any system with Docker installed without additional configuration.

---

## 👤 Author

Saheel Chavan  
MLOps – Northeastern University  
Spring 2026

Ran the above command sucessfully
<img width="1200" height="225" alt="image" src="https://github.com/user-attachments/assets/e5bead6e-2ec9-4e7a-abbe-6dd93cd4ae1d" />

