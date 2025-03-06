import streamlit as st
import os

# Setring page
st.set_page_config(page_title="My Digital Footprint - Blessing Allison", page_icon="🎓", layout="wide")

#CSS for animations
st.markdown("""
    <style>
    .fade-in {
        animation: fadeIn 1s ease-in;
    }
    @keyframes fadeIn {
        0% { opacity: 0; }
        100% { opacity: 1; }
    }
    .hover-effect:hover {
        transform: scale(1.05);
        transition: transform 0.3s;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("📍 Navigation")
page = st.sidebar.radio("Go To:", ["Home", "Projects", "Skills", "Customize Profile", "Contacts"])

# Initialize session state for profile customization
if "profile" not in st.session_state:
    st.session_state.profile = {
        "name": "Blessing Allison",
        "location": "Musanze",
        "field_of_study": "BSc Computer Science",
        "university": "INES",
        "skills": "graphic Design, Video Editing and UX/UI Design",
        "about_me": "I’m Blessing Allison, a passionate software engineer, graphic designer, customer engagement analyst, and social media marketer. With a strong background in technology-driven solutions, I thrive on creating innovative applications that enhance user experience, streamline operations, and solve real-world problems. My expertise spans web and mobile development, AI-based systems, fintech solutions, and digital engagement strategies.Technology excites me because of its endless potential to transform lives. I love how it enables automation, smarter decision-making, and seamless connectivity across different industries. Whether it's developing AI-driven attendance systems, fintech solutions, or interactive web applications, I’m always eager to push the boundaries of innovation and create solutions that make a lasting impact. 🚀",
        "testimonials": []
    }

# Home Section
if page == "Home":
    st.title("🎓 My Digital Footprint")
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)

    # Profile Image
    uploaded_image = st.file_uploader("Upload Profile Picture", type=["jpg", "png"])
    if uploaded_image is not None:
        st.image(uploaded_image, width=150, caption="My Profile")
    else:
        st.image("WhatsApp Image 2025-03-05 at 04.39.14.jpeg", width=150, caption="Default Profile")

    # Personal Information
    st.subheader("About Me")
    st.write(f"**Name**: {st.session_state.profile['name']}")
    st.write(f"📍 **Location**: {st.session_state.profile['location']}")
    st.write(f"📚 **Field of Study**: {st.session_state.profile['field_of_study']}, Year 3")
    st.write(f"🎓 **University**: {st.session_state.profile['university']}")
    st.write(f"📄 **Skills**: {st.session_state.profile['skills']}")
    st.write(st.session_state.profile['about_me'])

    # Testimonials
    st.subheader("Testimonials")
    if st.session_state.profile["testimonials"]:
        for testimony in st.session_state.profile["testimonials"]:
            st.write(f"\"{testimony}\"")
    else:
        st.write("No testimonials yet. Be the first to leave one!")

    # Submit a Testimony
    st.subheader("Leave a Testimony")
    with st.form("testimony_form"):
        testimony = st.text_area("Your Testimony", max_chars=300)
        submit_testimony = st.form_submit_button("Submit Testimony")

        if submit_testimony:
            if testimony:
                st.session_state.profile["testimonials"].append(testimony)
                st.success("Testimony submitted successfully!")
            else:
                st.warning("Please write a testimony before submitting.")

    # Resume Download
    try:
        with open("resume.pdf", "rb") as file:
            st.download_button(
                label="Download Resume",
                data=file.read(),
                file_name="",
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.warning("Resume file 'resume.pdf' not found. Please upload it.")

    st.markdown('</div>', unsafe_allow_html=True)

# Projects Section
elif page == "Projects":
    st.title("💻 My Projects")
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)

    # Project Filtering System
    project_categories = ["All", "Year 1", "Year 2", "Year 3", "Group", "Dissertation"]
    filter_category = st.selectbox("Filter Projects By:", project_categories)

    projects = [
        {
            "title": "Student Attendance System",
            "type": "Year 2",
            "problem": "Traditional attendance systems are inefficient and prone to proxy attendance.",
            "solution": "Developed an AI-powered facial recognition system to automate attendance tracking.",
            "technologies": "Python, OpenCV, TensorFlow, Streamlit",
            "link": "https://github.com/blessingallison/attendance-system"
        },
        {
            "title": "AI Chatbot",
            "type": "Group",
            "problem": "Customer support teams struggle with handling repetitive queries efficiently.",
            "solution": "Created an AI-powered chatbot that provides instant responses and learns over time.",
            "technologies": "Python, NLP, TensorFlow, Flask",
            "link": "https://github.com/blessingallison/ai-chatbot"
        },
        {
            "title": "Dissertation: AI-Driven Smart House Search System (IoT)",
            "type": "Dissertation",
            "problem": "Finding rental properties is often time-consuming and lacks real-time insights.",
            "solution": "Built a web-based IoT-enabled platform that integrates smart search filters and AI recommendations.",
            "technologies": "React.js, Node.js, MongoDB, Google Maps API, IoT Sensors",
            "link": ""
        }
    ]

    for project in projects:
        if filter_category == "All" or filter_category in project["type"]:
            with st.expander(f"{project['title']} ({project['type']})", expanded=False):
                st.markdown(f'<div class="hover-effect">', unsafe_allow_html=True)
                st.write(f"**Problem:** {project['problem']}")
                st.write(f"**Solution:** {project['solution']}")
                st.write(f"**Technologies Used:** {project['technologies']}")
                if project["link"]:
                    st.write(f"[View Code]({project['link']})")
                st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# Skills Section
elif page == "Skills":
    st.title("🛠️ My Skills & Achievements")
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)

    # Skills with Progress Bars
    st.subheader("Technical Skills")
    skill_python = st.slider("Python", 0, 100, 90)
    st.progress(skill_python)
    skill_js = st.slider("JavaScript", 0, 100, 75)
    st.progress(skill_js)
    skill_html = st.slider("HTML/CSS", 0, 100, 80)
    st.progress(skill_html)
    skill_ml = st.slider("Machine Learning", 0, 100, 60)
    st.progress(skill_ml)

    # Certifications & Achievements
    st.subheader("Certifications & Achievements")
    st.write("✔️ Google Data Analytics Certification")
    st.write("✔️ Certified Web Developer (W3Schools)")
    st.write("✔️ Hackathon Finalist - INES Tech Challenge 2024")
    st.write("✔️ Completed 6-month Python Internship")

    st.markdown('</div>', unsafe_allow_html=True)

# Customize Profile Section
elif page == "Customize Profile":
    st.title("✏️ Customize Your Profile")
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)

    # Editable Profile Details
    new_name = st.text_input("Full Name", st.session_state.profile["name"])
    new_location = st.text_input("Location", st.session_state.profile["location"])
    new_field = st.text_input("Field of Study", st.session_state.profile["field_of_study"])
    new_university = st.text_input("University", st.session_state.profile["university"])
    new_skills = st.text_input("Skills", st.session_state.profile["skills"])
    new_about = st.text_area("About Me", st.session_state.profile["about_me"])

    if st.button("Save Changes"):
        st.session_state.profile.update({
            "name": new_name,
            "location": new_location,
            "field_of_study": new_field,
            "university": new_university,
            "skills": new_skills,
            "about_me": new_about
        })
        st.success("Profile updated successfully!")

    st.markdown('</div>', unsafe_allow_html=True)

# Contacts Section
elif page == "Contacts":
    st.title("📞 Contact Me")
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)

    # Contact Form
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit = st.form_submit_button("Send Message")

        if submit:
            st.success("Message sent successfully!")
            st.write(f"**Name**: {name}")
            st.write(f"**Email**: {email}")
            st.write(f"**Message**: {message}")

    # Professional Links
    st.subheader("Connect With Me")
    st.write("[LinkedIn](https://linkedin.com/in/blessing-allison)")
    st.write("[GitHub](https://github.com/blessingallison)")
    st.write("Email: blessing.allison@gamil.com")

    st.markdown('</div>', unsafe_allow_html=True)
