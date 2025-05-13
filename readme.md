# 🧠 MindCanvas – A Dynamic Blog Website Built with Django

**MindCanvas** is a powerful, full-stack blog platform that enables users to explore, create, and engage with content across diverse topics. Built using **Django (Python)**, it integrates modern web features like user authentication, categories, search, likes, comments, and a featured post system — all wrapped in a clean, responsive UI.

---

## 🚀 Features

### 👤 User Management
- Sign up, log in, and log out securely using Django’s built-in authentication system.
- Only logged-in users can like, comment, or create posts.

### 📝 Blog Management
- Create, edit, and delete your own blog posts.
- Upload and display images with posts.
- View full blog content with author details and timestamps.

### 💬 Commenting System
- Comment on blog posts.
- Only comment authors can delete their comments.

### ❤️ Like System
- Like or unlike blog posts.
- Posts can only be liked by logged-in users.
- Total like count displayed per post.

### 🌟 Featured Post
- Automatically displays the post with the highest number of likes at the top of the homepage.

### 🆕 Latest Posts Section
- Lists all recent posts in reverse chronological order.

### 📂 Category Filtering
- Assign posts to categories.
- Sidebar allows users to filter posts by category.

### 🔍 Blog Search
- Search blog posts by title or content.

### 🔥 Trending Authors
- Display top authors based on blog popularity and engagement.

### 📱 Responsive Design
- Uses Bootstrap for a mobile-friendly and modern UI.

---

## 🛠️ Tech Stack

| Layer        | Technology         |
|--------------|--------------------|
| Backend      | Django (Python)     |
| Frontend     | HTML5, CSS3, Bootstrap 5 |
| Database     | SQLite (Django ORM) |
| Templates    | Django Template Language |
| Auth & Admin | Django Auth System |
| Image Upload | Django ImageField   |

---

## 📁 Project Structure

- `MindCanvas/`
  - `blog/`
    - `migrations/` – Database migration files
    - `templates/blog/` – HTML templates
      - `base.html` – Main layout
      - `home.html` – Homepage with featured and latest posts
      - `post_detail.html` – Blog detail view
    - `static/blog/` – Static files like CSS
      - `style.css`
    - `admin.py` – Register models in Django admin
    - `models.py` – Database models (Post, Comment, Category)
    - `views.py` – Core views (home, post detail, like, comment, category)
    - `forms.py` – Django ModelForms for posts
    - `urls.py` – URL routing
  - `manage.py` – Django management script
  - `db.sqlite3` – SQLite database

---

## 🔍 SEO Highlights

- Dynamic blog titles and meta descriptions
- User-generated content boosts relevance
- Internal linking through categories and related posts
- Clean and semantic HTML using Django templating

---

## 🧑‍💻 Contributing

Contributions are welcome! If you have suggestions or find bugs, feel free to open an issue or submit a pull request.

## 📄 License

This project is licensed under the MIT License.
