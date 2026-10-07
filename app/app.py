from flask import Flask, render_template_string
import mysql.connector

app = Flask(__name__)

# Portfolio HTML template
portfolio_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Vivek Kumar Jha - Portfolio</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; background: #f4f4f4; }
        header { background: linear-gradient(135deg, #333, #555); color: #fff; padding: 30px; text-align: center; }
        header h1 { margin: 0; font-size: 2.5em; }
        header h2 { margin: 5px 0; font-weight: normal; font-size: 1.5em; color: #ddd; }
        header p { font-size: 1.1em; color: #ccc; }
        nav { background: #222; padding: 10px; text-align: center; }
        nav a { color: #fff; margin: 0 15px; text-decoration: none; font-weight: bold; }
        nav a:hover { color: #00ccff; }
        section { padding: 20px; max-width: 900px; margin: auto; }
        h2 { color: #333; border-bottom: 2px solid #ddd; padding-bottom: 5px; }
        .skills ul { list-style: none; padding: 0; }
        .skills li { background: #fff; margin: 5px 0; padding: 10px; border-radius: 5px; }
        .project { background: #fff; margin: 15px 0; padding: 15px; border-radius: 5px; }
        .project h3 { margin-top: 0; }
        .project a { color: #0066cc; text-decoration: none; }
        footer { background: #333; color: #fff; text-align: center; padding: 15px; margin-top: 20px; }
        footer a { color: #00ccff; text-decoration: none; margin: 0 10px; }
        footer a:hover { text-decoration: underline; }
        @media (max-width: 600px) {
            header h1 { font-size: 2em; }
            header h2 { font-size: 1.2em; }
            nav a { display: block; margin: 10px 0; }
        }
    </style>
</head>
<body>
    <header>
        <h1>Vivek Kumar Jha</h1>
        <h2>Aspiring DevOps Engineer</h2>
        <p>Final-Year Computer Science Graduate | Skilled in Linux, Git, Docker, Jenkins, AWS</p>
    </header>

    <nav>
        <a href="#about">About</a>
        <a href="#skills">Skills</a>
        <a href="#projects">Projects</a>
        <a href="#contact">Contact</a>
    </nav>

    <section id="about">
        <h2>About Me</h2>
        <p>I am a Computer Science student passionate about DevOps, automation, and cloud technologies.
        Skilled in Linux, Shell scripting, Git/GitHub, Docker, Jenkins, and AWS. I enjoy building CI/CD pipelines,
        containerized applications, and automating infrastructure deployments.</p>
    </section>

    <section id="skills" class="skills">
        <h2>Skills</h2>
        <ul>
            <li>Linux & Shell Scripting</li>
            <li>Networking Fundamentals</li>
            <li>Git & GitHub</li>
            <li>Docker & Docker Compose</li>
            <li>Jenkins (CI/CD)</li>
            <li>AWS (EC2, Security Groups)</li>
        </ul>
    </section>

    <section id="projects">
        <h2>Projects</h2>
        <div class="project">
            <h3>Amazon Clone CI/CD</h3>
            <p>Built a Jenkins pipeline to deploy a Dockerized static web app on AWS EC2.</p>
            <p><a href="https://github.com/VivekJha2k05/Amazon-Clone-Devops" target="_blank">View on GitHub</a></p>
        </div>
        <div class="project">
            <h3>Multi-Container Web App</h3>
            <p>Flask + MySQL application orchestrated with Docker Compose and deployed on AWS.</p>
            <p><a href="https://github.com/VivekJha2k05/Portfolio-Docker-Compose" target="_blank">View on GitHub</a></p>
        </div>
    </section>

    <section id="contact">
        <h2>Contact</h2>
        <p>Email: vjha00900@gmail.com</p>
        <p>GitHub: <a href="https://github.com/VivekJha2k05" target="_blank">github.com/VivekJha2k05</a></p>
        <p>LinkedIn: <a href="https://linkedin.com/in/vivek" target="_blank">linkedin.com/in/vivek</a></p>
    </section>

    <footer>
        <p>© 2026 Vivek Kumar Jha</p>
        <p>
            <a href="https://github.com/VivekJha2k05" target="_blank">GitHub</a> |
            <a href="https://linkedin.com/in/vivek" target="_blank">LinkedIn</a>
        </p>
    </footer>
</body>
</html>
"""

@app.route('/')
def home():
    try:
        conn = mysql.connector.connect(
            host="db",
            user="root",
            password="root",
            database="devopsdb"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 'Hello from MySQL!'")
        result = cursor.fetchone()
        message = result[0]
    except Exception as e:
        message = f"Error: {e}"

    return render_template_string(portfolio_html + f"<p>Message from MySQL: {message}</p>")

@app.route('/check')
def check():
    try:
        conn = mysql.connector.connect(
            host="db",
            user="root",
            password="root",
            database="devopsdb"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 'Database connection successful'")
        result = cursor.fetchone()
        message = result[0]
    except Exception as e:
        message = f"Error: {e}"

    return f"<h2>{message}</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
