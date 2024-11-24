```bash
[CLIENT]
   |
   | 1. Upload Model (POST /api/models/upload/)
   v
[Upload Model]
   |
   |-- Check data (model name, file)
   |-- Save model (file + info)
   |
   --> Response: {"id": <model_id>, "status": "uploaded"}

   |
   | 2. List Models (GET /api/models/)
   v
[List Models]
   |
   |-- Get all models from database
   |
   --> Response: [{"id": 1, "name": "model1", "framework": "tensorflow"}, ...]

   |
   | 3. Get Model Details (GET /api/models/<model_id>/)
   v
[Model Details]
   |
   |-- Get model info by ID from database
   |
   --> Response: {"id": <model_id>, "name": "model1", "framework": "tensorflow", ...}

   |
   | 4. Predict (POST /api/models/<model_id>/predict/)
   v
[Make Prediction]
   |
   |-- Check if model exists
   |-- Load model file
   |-- Process input data
   |-- Run prediction (TensorFlow/PyTorch)
   |
   --> Response: {"prediction": [...]}

```
