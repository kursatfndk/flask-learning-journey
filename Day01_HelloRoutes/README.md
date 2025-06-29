# 📅 Gün 01 - Flask'ta Routing ve Template Kullanımı

Bu gün Flask framework'üne temel bir giriş yaptım.

## 📚 Öğrenilen Konular

- `@app.route()` ile sayfa yönlendirme
- `render_template()` ile HTML dosyası çağırma
- `redirect()` ve `url_for()` kullanımı
- URL parametreleri (`/hello-user/<name>`)
- HTML form üzerinden `POST` ile veri alma

## 📁 Dosya Yapısı

- `app.py` → Flask uygulaması
- `templates/` klasörü:
  - `hello.html`
  - `hello-admin.html`
  - `hello_user.html`
  - `login.html`

## ▶️ Uygulamayı Çalıştırmak

1. Terminalden klasöre gir:
   ```bash
   cd Day01_HelloRoutes
2. Flask sunucusunu başlat:
  flask run

📝Notlar
request.form ile form verisini alabilmek için formun POST metoduyla gönderilmesi gerekir.

url_for() fonksiyon isimleriyle yönlendirme yaparak daha esnek ve güvenli bir yapı sağlar.

🎯 Amaç
Bu örnek, Flask'ın temel yönlendirme ve şablon kullanımı özelliklerini öğrenmek amacıyla hazırlandı.

## 🇬🇧 **Day 1 - README.md (English)**

```markdown
# 📅 Day 01 - Routing and Template Rendering in Flask

Today I made my first steps into the Flask framework.

## 📚 Topics Covered

- Creating routes using `@app.route()`
- Rendering HTML templates with `render_template()`
- Redirecting with `redirect()` and `url_for()`
- Using URL parameters (`/hello-user/<name>`)
- Receiving form data via `POST` method

## 📁 File Structure

- `app.py` → Flask application
- `templates/` folder:
  - `hello.html`
  - `hello-admin.html`
  - `hello_user.html`
  - `login.html`

## ▶️ How to Run

1. Navigate to the folder:
   ```bash
   cd Day01_HelloRoutes
Start the Flask development server:

bash
Kopyala
Düzenle
flask run
📝 Notes
To get data from a form using request.form, the form must be submitted with the POST method.

url_for() allows for safer and more flexible routing by referencing function names.

🎯 Purpose
This example was created to practice the basic features of Flask such as routing and using templates.
