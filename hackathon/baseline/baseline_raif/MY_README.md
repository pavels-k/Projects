# Описание
Это бенчмарк скрипт для хакатона от Раййфайзенбанка по оценке коммерческой недвижимости
Бенчмарк состоит из:
* requirements.txt - стандартный requirements для pip
* train.py - скрипт, который обучает модель и сохраняет ее
* predict.py - скрипт, который делает предсказание на отложенной тестовой выборке

# Запуск

Для train:
python train.py --train_data ../data/train.csv --model_path my.sav

Для predict:
python predict.py --model_path my.sav --test_data ../data/test.csv --output test_submission.csv