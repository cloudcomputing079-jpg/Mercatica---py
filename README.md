# Mercatica - AI-Powered Branding Assistant

Mercatica is a comprehensive web application designed to help entrepreneurs and businesses create powerful branding strategies using artificial intelligence. Built with Flask and powered by Google Gemini AI, it provides tools for brand generation, strategy roadmapping, personality profiling, and competitive analysis.

## 🚀 Features

### Core Functionality
- **AI Branding Assistant**: Generate font styles, color palettes, logo prompts, domain suggestions, and recommended technologies
- **Brand Strategy Roadmap**: Create 30-day launch roadmaps with weekly milestones and actionable tasks
- **Brand Personality Profiler**: Define emotional tone, brand archetypes, and audience traits
- **Brand Intelligence Analyzer**: Perform sentiment analysis, audience persona creation, and SWOT analysis
- **Branding History**: Track and review all your branding sessions with timestamps

### User Management
- Secure user authentication and registration
- Session-based login system
- User-specific branding history storage

### User Experience
- **Dark/Light Theme Toggle**: Seamless theme switching for user preference
- **Responsive Design**: Mobile-friendly interface that works on all devices
- **Internationalization**: Support for multiple languages (currently Tamil)
- **Modern UI**: Clean, professional design with intuitive navigation

## 🛠️ Technology Stack

### Backend
- **Flask**: Python web framework for robust API development
- **SQLite**: Lightweight database for user data and branding history
- **Google Gemini AI**: Advanced AI model for generating branding content
- **Python-Dotenv**: Environment variable management for API keys

### Frontend
- **Jinja2**: Template engine for dynamic HTML rendering
- **CSS3**: Custom styling with theme support
- **Chart.js**: Interactive charts for brand analysis visualization
- **Responsive Design**: Mobile-first approach with CSS media queries

### Deployment
- **Vercel**: Serverless deployment platform
- **Python Vercel Runtime**: Optimized for serverless functions

## 📁 Project Structure

```
Mercatica - py/
├── app.py                          # Main Flask application
├── api/
│   └── index.py                    # Vercel API endpoint
├── templates/                      # Jinja2 HTML templates
│   ├── base.html                   # Base template with navigation
│   ├── dashboard.html              # Main dashboard
│   ├── login.html                  # User login page
│   ├── signup.html                 # User registration
│   ├── assistant.html              # AI branding assistant
│   ├── history.html                # Branding history viewer
│   ├── roadmap.html                # Strategy roadmap generator
│   ├── personality.html            # Brand personality profiler
│   ├── analyzer.html               # Brand intelligence analyzer
│   ├── about.html                  # About page with team info
│   ├── help.html                   # Help and support
│   ├── contact.html                # Contact form
│   └── index.html                  # Legacy template
├── static/                         # Static assets
│   ├── style.css                   # Main stylesheet
│   ├── Mercatica.jpg               # Logo/favicon
│   └── images/                     # Team member photos
├── branding_utils.py               # AI integration utilities
├── setup_db.py                     # Database setup script
├── init_db.py                      # Initial database creation
├── branding.db                     # SQLite database file
├── requirements.txt                # Python dependencies
├── vercel.json                     # Vercel deployment config
├── babel.cfg                       # Internationalization config
├── translations/                   # Translation files
│   └── ta/                         # Tamil translations
└── messages.pot                    # Translation template
```

## 🔧 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key
- Virtual environment (recommended)

### Local Development

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd mercatica-py
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -f requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```
   GEMINI_API_KEY=your_google_gemini_api_key_here
   SECRET_KEY=your_flask_secret_key_here
   ```

5. **Initialize database**
   ```bash
   python init_db.py
   python setup_db.py
   ```

6. **Run the application**
   ```bash
   python app.py
   ```
   Access at `http://localhost:5000`

### Vercel Deployment

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Deploy**
   ```bash
   vercel
   ```

3. **Set environment variables in Vercel**
   ```bash
   vercel env add GEMINI_API_KEY
   vercel env add SECRET_KEY
   ```

## 🎯 Usage

### Getting Started
1. Visit the application and create an account
2. Log in to access the dashboard
3. Choose from available tools:
   - **AI Branding Assistant**: Input brand name and domain for AI suggestions
   - **Brand Strategy Roadmap**: Generate launch timelines
   - **Brand Personality Profiler**: Define brand characteristics
   - **Brand Intelligence Analyzer**: Analyze market positioning

### API Usage
The application provides RESTful endpoints for programmatic access:
- `GET /` - Dashboard
- `POST /assistant` - Generate branding suggestions
- `POST /roadmap` - Create strategy roadmap
- `POST /personality` - Generate personality profile
- `POST /analyzer` - Perform brand analysis

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Team

- **Jayden Felix** - Founder & Brand Strategist
- **Athithya P** - Co-Founder & Frontend Lead
- **Ibrahim M** - Backend Developer & Data Analyst
- **Girinath** - Product Manager & QA Specialist

## 🙏 Acknowledgments

- Google Gemini AI for powering the branding intelligence
- Flask community for the excellent web framework
- Vercel for seamless deployment platform
- Chart.js for beautiful data visualizations

## 📞 Support

For support, questions, or feedback:
- Create an issue on GitHub
- Use the in-app contact form
- Email: [cloudcomputing079@gmail.com]

---

**Conquer the market with Mercatica!** 🏆
