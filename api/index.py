from flask import Flask, render_template, request, redirect, session, url_for
import os
import sqlite3

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "your-secret-key")

# -------------------- ROUTES --------------------

@app.route('/')
def home():
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        session['user'] = 'guest'  # fallback for demo
    message = request.args.get('message')
    return render_template('dashboard.html', message=message)

@app.route('/toggle-theme')
def toggle_theme():
    current = session.get('theme', 'light')
    session['theme'] = 'dark' if current == 'light' else 'light'
    return redirect(request.referrer or url_for('dashboard'))

@app.route('/assistant', methods=['GET', 'POST'])
def branding_assistant():
    if 'user' not in session:
        session['user'] = 'guest'
    suggestions = None
    if request.method == 'POST':
        brand = request.form['brand']
        domain = request.form['domain']
        # Dummy response
        suggestions = {
            "font": "Sans-serif, 16px",
            "colors": "Blue, White",
            "logo_prompt": "Minimalist logo with bold initials",
            "domain_name": "mercatica.io",
            "languages": "Python, HTML, CSS"
        }
    return render_template('assistant.html', suggestions=suggestions)

@app.route('/roadmap', methods=['GET', 'POST'])
def roadmap():
    if 'user' not in session:
        session['user'] = 'guest'
    roadmap = None
    if request.method == 'POST':
        brand = request.form['brand']
        domain = request.form['domain']
        roadmap = f"""Week 1: Brand Discovery\nGoal: Define brand values\nTasks: Research, Interviews\nTools: Notion, Google Docs\n\nWeek 2: Visual Identity\nGoal: Create logo and palette\nTasks: Design drafts\nTools: Figma\n\nWeek 3: Web Presence\nGoal: Build landing page\nTasks: Code, Test\nTools: Vercel, Flask\n\nWeek 4: Launch Prep\nGoal: Finalize assets\nTasks: Social media, Email\nTools: Canva, Mailchimp"""
    return render_template('roadmap.html', roadmap=roadmap)

@app.route('/analyzer', methods=['GET', 'POST'])
def analyzer():
    if 'user' not in session:
        session['user'] = 'guest'
    sentiment = {}
    persona = {}
    swot = {}
    if request.method == 'POST':
        brand = request.form['brand']
        domain = request.form['domain']
        sentiment = {
            "Trust": 85,
            "Excitement": 70,
            "Elegance": 90,
            "Boldness": 75,
            "Friendliness": 80
        }
        persona = {
            "Demographics": "18–35, urban, tech-savvy",
            "Psychographics": "Creative, ambitious",
            "Motivations": "Growth, recognition",
            "Pain Points": "Lack of clarity, poor UX"
        }
        swot = {
            "Strengths": "Strong branding, clear vision",
            "Weaknesses": "Limited reach",
            "Opportunities": "Emerging markets",
            "Threats": "Competition"
        }
    return render_template('analyzer.html', sentiment=sentiment, persona=persona, swot=swot)

@app.route('/personality', methods=['GET', 'POST'])
def personality():
    if 'user' not in session:
        session['user'] = 'guest'
    profile = None
    if request.method == 'POST':
        brand = request.form['brand']
        domain = request.form['domain']
        profile = """Emotional Tone: Empowering\nBrand Archetype: Creator\nTone of Voice: Confident, clear\nAudience Traits: Curious, driven, design-conscious"""
    return render_template('personality.html', profile=profile)

@app.route('/history')
def history():
    if 'user' not in session:
        session['user'] = 'guest'
    # Dummy history
    rows = [
        ("Mercatica", "tech", "Sans-serif", "Blue, White", "Bold logo", "mercatica.io", "Python, HTML", "2025-11-08 20:00")
    ]
    return render_template('history.html', history=rows)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if 'user' not in session:
        session['user'] = 'guest'
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        return render_template('contact.html', success=True)
    return render_template('contact.html')

@app.route('/about')
def about():
    if 'user' not in session:
        session['user'] = 'guest'
    return render_template('about.html')

@app.route('/help')
def help():
    if 'user' not in session:
        session['user'] = 'guest'
    return render_template('help.html')

@app.route('/settings')
def settings():
    if 'user' not in session:
        session['user'] = 'guest'
    return render_template('settings.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/dashboard')

# -------------------- VERCEL ENTRY --------------------

def handler(environ, start_response):
    return app(environ, start_response)