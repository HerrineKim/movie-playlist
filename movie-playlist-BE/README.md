# π API Docs

### I. [User API](https://github.com/HerrineKim/movie-playlist/blob/master/movie-playlist-BE/docs/User%20API.md)

### II. [Article API](https://github.com/HerrineKim/movie-playlist/blob/master/movie-playlist-BE/docs/Article%20API.md)

### III. [Movie API](https://github.com/HerrineKim/movie-playlist/blob/master/movie-playlist-BE/docs/Movie%20API.md)

<br>

# π API μλ² κ΅¬μΆ

### 1. κ°μνκ²½ μμ±

```bash
python -m venv venv
```

<br>

### 2. κ°μνκ²½ μ€ν

```python
source venv/Scripts/activate
```

<br>

### 3. ν¨ν€μ§ μ€μΉ

```bash
pip install -r requirements.txt
```

<br>

### 4. migration

```bash
python manage.py makemigrations
python manage.py migrate
```

<br>

### 5. fixture λ°μ΄ν° λ‘λ

```bash
python manage.py loaddata moodtag.json casetag.json genre.json actor.json movie.json
```

<br>

### 6. μλ² μ€ν

```bash
python manage.py runserver
```

