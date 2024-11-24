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


      
