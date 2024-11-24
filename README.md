Client
  |
  |-- [POST /api/models/upload/] --------------------------> UploadModelView
  |                                                          |
  |                                                          |-- Валидация данных:
  |                                                          |     - Проверка названия модели
  |                                                          |     - Проверка файла
  |                                                          |
  |                                                          |-- Сохранение модели:
  |                                                          |     - Файл модели -> MEDIA_ROOT
  |                                                          |     - Данные о модели -> БД
  |                                                          |
  |                                                          --> Ответ:
  |                                                                {"id": <model_id>, "status": "uploaded"}
  |
  |-- [GET /api/models/] ----------------------------------> Список всех моделей
  |                                                          |
  |                                                          |-- Запрос к БД:
  |                                                          |     - ID модели
  |                                                          |     - Название
  |                                                          |     - Framework (TensorFlow/PyTorch)
  |                                                          |
  |                                                          --> Ответ:
  |                                                                [{"id": 1, "name": "model1", "framework": "tensorflow"}, ...]
  |
  |-- [GET /api/models/<model_id>/] -----------------------> Детали модели
  |                                                          |
  |                                                          |-- Запрос к БД:
  |                                                          |     - Подробная информация по ID модели
  |                                                          |
  |                                                          --> Ответ:
  |                                                                {"id": <model_id>, "name": "model1", "framework": "tensorflow", ...}
  |
  |-- [POST /api/models/<model_id>/predict/] -------------> PredictView
                                                             |
                                                             |-- Проверка наличия модели в БД
                                                             |-- Загрузка файла модели из MEDIA_ROOT
                                                             |-- Обработка входных данных:
                                                             |     - JSON: {"input_data": [...]}
                                                             |
                                                             |-- Предсказание:
                                                             |     - Если TensorFlow:
                                                             |         - model = tf.keras.models.load_model(...)
                                                             |         - prediction = model.predict(input_data)
                                                             |
                                                             |     - Если PyTorch:
                                                             |         - model = torch.load(...)
                                                             |         - model.eval()
                                                             |         - prediction = model(input_tensor).tolist()
                                                             |
                                                             --> Ответ:
                                                                   {"prediction": [...]}



**Объяснение карты:**
[POST /api/models/upload/]

API для загрузки моделей.
Выполняется проверка файла и данных, сохранение модели и возврат ID.
[GET /api/models/]

Список всех доступных моделей, хранящихся в базе данных.
[GET /api/models/<model_id>/]

Детальная информация о конкретной модели (название, framework, путь к файлу).
[POST /api/models/<model_id>/predict/]

API для выполнения предсказаний.
Загрузка модели по указанному ID.
Обработка данных, предсказание через TensorFlow или PyTorch, возврат результата.