from flask import Flask, render_template, request, send_file
import pdfkit
import os

app = Flask(__name__)
config = pdfkit.configuration(wkhtmltopdf=r'C:\resume_generator\wkhtmltopdf\bin\wkhtmltopdf.exe')

@app.route('/')
def home():
    return render_template('resume_form.html') 

@app.route('/generate_resume', methods=['POST'])
def generate_resume():
    data = {
        "name": request.form.get("name"),
        "email": request.form.get("email"),
        "phone": request.form.get("phone"),
        "address": request.form.get("address"),
        "linkedin": request.form.get("linkedin"),
        "github": request.form.get("github"),
        "portfolio": request.form.get("portfolio"),
        "image_url": request.form.get("image_url"),
        "background_color": request.form.get("background_color"),
        "professional_summary": request.form.get("professional_summary"),
        "education": request.form.get("education"),
        "experience": request.form.get("experience"),
        "skills": request.form.get("skills").split(", "),
        "languages": request.form.get("languages").split(", "),
        "certificates": request.form.get("certificates").split(", "),
        "projects": request.form.get("projects"),
        "awards": request.form.get("awards").split(", "),
        "interests": request.form.get("interests").split(", "),
        "affiliations": request.form.get("affiliations").split(", "),
        "references": request.form.get("references")
    }

    template_choice = request.form.get("template_choice")
    template_file = f'template{template_choice}.html'

    rendered = render_template(template_file, **data)

    pdf_path = os.path.join('static', 'output_resume.pdf')

    pdfkit.from_string(rendered, pdf_path, configuration=config)

    return send_file(pdf_path, as_attachment=True, download_name="resume.pdf")

if __name__ == '__main__':
    app.run(debug=True)
