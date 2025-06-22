from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'

achievements = [
    {"title": "Best Ayurveda Student Award", "year": "2024", "desc": "Received for outstanding academic and extracurricular performance."},
    {"title": "Research Paper Published", "year": "2023", "desc": "Published a paper on 'Herbs and Healing' in Ayurveda Journal."},
    {"title": "Ayurveda Awareness Camp", "year": "2022", "desc": "Organized a community health camp for Ayurveda awareness."},
]

education = [
    {"degree": "BAMS (Bachelor of Ayurvedic Medicine & Surgery)", "school": "Govt. Ayurveda College, Kerala", "year": "2021 - Present"},
    {"degree": "High School", "school": "Sacred Heart School", "year": "2019 - 2021"},
]

FACE_IMAGE_FILENAME = 'image.png'
CAROUSEL_IMAGES = [
    '1.jpg',
    '2.jpg',
    '3.jpg',
    '4.jpg',
    '5.jpg'
]
ICONS = [
    {"src": 'lotus.svg', "class": "lotus", "alt": "Lotus"},
    {"src": 'leaf.svg', "class": "leaf", "alt": "Leaf"},
    {"src": 'herb.svg', "class": "herb", "alt": "Herb"},
    {"src": 'mandala.svg', "class": "mandala", "alt": "Mandala"},
]
SHAPES = [
    {"class": "circle-green", "style": "top:8%;left:68%;width:120px;height:120px;"},
    {"class": "circle-white", "style": "bottom:14%;left:12%;width:90px;height:90px;"},
    {"class": "circle-outline", "style": "top:73%;right:10%;width:170px;height:170px;"},
]

TRAITS = [
    "Hardworking & Determined",
    "Enthusiastic Learner",
    "Compassionate & Empathetic",
    "Organized & Proactive",
    "Loves Ayurveda & Nature"
]

def get_common_context():
    return {
        "name": "SHIVANI SHREE G",
        "face_image": url_for('static', filename=FACE_IMAGE_FILENAME),
        "ayurveda_icons": [
            {
                "src": url_for('static', filename=icon["src"]),
                "class": icon["class"],
                "alt": icon["alt"]
            }
            for icon in ICONS
        ],
        "shapes": SHAPES
    }

@app.route("/")
def home():
    # Ensure face_image is included in context for index.html
    context = get_common_context()
    return render_template("index.html", **context)

@app.route("/about")
def about():
    context = get_common_context()
    # Pass all images except 'image.png' (in case it ever appears in CAROUSEL_IMAGES)
    context["carousel_images"] = [
        url_for('static', filename=img)
        for img in CAROUSEL_IMAGES
        if img != FACE_IMAGE_FILENAME
    ]
    context["traits"] = TRAITS
    return render_template("about.html", **context)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thank you for your message! I will get back to you soon.", "success")
        return redirect(url_for('contact'))
    return render_template("contact.html", **get_common_context())

@app.route("/achievements")
def achievements_page():
    ctx = get_common_context()
    ctx["achievements"] = achievements
    return render_template("achievements.html", **ctx)

@app.route("/education")
def education_page():
    ctx = get_common_context()
    ctx["education"] = education
    return render_template("education.html", **ctx)

@app.route("/services")
def services():
    return render_template("services.html", **get_common_context())

if __name__ == "__main__":
    app.run(debug=True)