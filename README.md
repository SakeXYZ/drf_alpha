---

# Model Deployment API (English)

This repository contains a simple Django REST Framework (DRF) application for managing and using machine learning models.

---

## Features

- Upload machine learning models (TensorFlow and PyTorch).
- List and retrieve details of uploaded models.
- Perform predictions using uploaded models.
- Flexible API design for easy integration.

---

## API Map

```
┌─────────────┐
│   CLIENT    │
└─────────────┘
      |
      | 1. Upload Model (POST /api/models/upload/)
      v
┌───────────────────┐
│ UploadModelView   │
└───────────────────┘
      |
      |-- Validate Data:
      |     - Check model name
      |     - Check uploaded file
      |
      |-- Save Model:
      |     - File -> MEDIA_ROOT
      |     - Metadata -> Database
      |
      └--> Response: {"id": <model_id>, "status": "uploaded"}

      |
      | 2. List Models (GET /api/models/)
      v
┌───────────────────┐
│   List Models     │
└───────────────────┘
      |
      |-- Query Database:
      |     - ID, Name, Framework
      |
      └--> Response: [{"id": 1, "name": "model1", "framework": "tensorflow"}, ...]

      |
      | 3. Get Model Details (GET /api/models/<model_id>/)
      v
┌───────────────────┐
│  Model Details    │
└───────────────────┘
      |
      |-- Query Database:
      |     - Fetch details by ID
      |
      └--> Response: {"id": <model_id>, "name": "model1", "framework": "tensorflow", ...}

      |
      | 4. Predict (POST /api/models/<model_id>/predict/)
      v
┌───────────────────┐
│    PredictView    │
└───────────────────┘
      |
      |-- Validate Model Exists
      |-- Load Model from MEDIA_ROOT
      |-- Process Input Data:
      |     - JSON: {"input_data": [...]}
      |
      |-- Perform Prediction:
      |     - TensorFlow or PyTorch
      |
      └--> Response: {"prediction": [...]}


```

---

## Explanation of Code

### UploadModelView
This view allows users to upload machine learning models. It validates the input data, saves the model file to the server, and stores metadata in the database.

Key methods:
- **POST**: Accepts a file and metadata, validates them, and saves the model.

---

### PredictView
This view performs predictions using uploaded models. It supports TensorFlow and PyTorch models.

Key methods:
- **POST**: Accepts input data, loads the selected model, and returns prediction results.

---

---

# API для развёртывания моделей (На русском)

Этот репозиторий содержит простое приложение Django REST Framework (DRF) для управления и использования моделей машинного обучения.

---

## Возможности

- Загрузка моделей машинного обучения (TensorFlow и PyTorch).
- Просмотр и получение деталей загруженных моделей.
- Выполнение предсказаний с использованием загруженных моделей.
- Гибкий API для лёгкой интеграции.

---

## Карта API


Вот переведённая карта API на русский язык:

```
┌─────────────┐
│   КЛИЕНТ    │
└─────────────┘
      |
      | 1. Загрузка модели (POST /api/models/upload/)
      v
┌───────────────────┐
│ Загрузка модели   │
└───────────────────┘
      |
      |-- Проверка данных:
      |     - Проверка имени модели
      |     - Проверка загруженного файла
      |
      |-- Сохранение модели:
      |     - Файл -> MEDIA_ROOT
      |     - Метаданные -> База данных
      |
      └--> Ответ: {"id": <model_id>, "status": "uploaded"}

      |
      | 2. Список моделей (GET /api/models/)
      v
┌───────────────────┐
│   Список моделей  │
└───────────────────┘
      |
      |-- Запрос к базе данных:
      |     - ID, Имя, Фреймворк
      |
      └--> Ответ: [{"id": 1, "name": "model1", "framework": "tensorflow"}, ...]

      |
      | 3. Детали модели (GET /api/models/<model_id>/)
      v
┌───────────────────┐
│   Детали модели   │
└───────────────────┘
      |
      |-- Запрос к базе данных:
      |     - Получение данных по ID
      |
      └--> Ответ: {"id": <model_id>, "name": "model1", "framework": "tensorflow", ...}

      |
      | 4. Предсказание (POST /api/models/<model_id>/predict/)
      v
┌───────────────────┐
│   Предсказание    │
└───────────────────┘
      |
      |-- Проверка существования модели
      |-- Загрузка модели из MEDIA_ROOT
      |-- Обработка входных данных:
      |     - JSON: {"input_data": [...]}
      |
      |-- Выполнение предсказания:
      |     - TensorFlow или PyTorch
      |
      └--> Ответ: {"prediction": [...]}
```

---

## Объяснение кода

### UploadModelView
Этот обработчик позволяет загружать модели машинного обучения. Он проверяет входные данные, сохраняет файл модели на сервере и добавляет метаданные в базу данных.

Основные методы:
- **POST**: Принимает файл и метаданные, проверяет их и сохраняет модель.

---

### PredictView
Этот обработчик выполняет предсказания с использованием загруженных моделей. Поддерживаются модели TensorFlow и PyTorch.

Основные методы:
- **POST**: Принимает входные данные, загружает выбранную модель и возвращает результаты предсказания.

---

Теперь README содержит разделение языков и полное описание.
