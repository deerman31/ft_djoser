#!/bin/bash

# 環境変数を設定
export DATABASE_URL=postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}

echo "Waiting for postgres..."
while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  sleep 1
done
echo "PostgreSQL started"

python3 ft_djoser/manage.py makemigrations accounts

# データベースマイグレーションを実行
python3 ft_djoser/manage.py migrate

# ディレクトリを /app/mysite に変更
cd /app/ft_djoser

python3 manage.py runserver 0.0.0.0:${BACKEND_PORT}
