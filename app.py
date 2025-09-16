# ---------------------------
# Import Libraries & Packages
# ---------------------------
import streamlit as st

# ---------------------------
# Team Data Info
# ---------------------------
teammates = [
    {"name": "Ezz Al-Din Emad Ali Aref",
     "role": "ML Engineer",
     "bio": "Experienced in machine learning, deep learning, and MLOps.",
     "github": 'https://github.com/EzzAl-Din',
     "linkedin": 'https://www.linkedin.com/in/ezzal-din',
     "portfolio": ""
     },
    {"name": "Adel Maher Hakim Pekhet",
     "role": "Data Analyst ",
     "bio": "Experienced in data analysis and data science .",
     "github": 'https://github.com/Adel-Maher',
     "linkedin": 'https://www.linkedin.com/in/adel-maher-52b908315 ',
     "portfolio": ""
     },
    {"name": "Abdallah Mohamed Mohamed Rashad",
     "role": "Data scientist",
     "bio": "Passionate about AI and deep learning.",
     "github": 'https://github.com/',
     "linkedin": 'https://www.linkedin.com/',
     "portfolio": ""
     },
    {"name": "Ali Ahmed Youssef",
     "role": "Data scientist",
     "bio": "Expert in market research and business strategy.",
     "github": 'https://github.com/ZeeeCS',
     "linkedin": 'www.linkedin.com/in/aliahmed-11m04',
     "portfolio": "https://zeeeecs.github.io/"
     }
]


# ---------------------------
# Streamlit App
# ---------------------------
def main():
    # ---------------------------
    # Page Content
    # ---------------------------
    st.set_page_config(page_title="Meet the DataMentes Team")
    st.title("Meet the DataMentes Team")
    for member in teammates:
        st.subheader(member["name"])
        st.markdown(f"**Role:** {member['role']}")
        st.markdown(f"**Summary:** {member['bio']}")
        st.markdown(f"**View GitHub:** [{member['github']}]({member['github']})")
        st.markdown(f"**View LinkedIn:** [{member['linkedin']}]({member['linkedin']})")
        st.markdown(f"**View Portfolio:** [{member['portfolio']}]({member['portfolio']})")
        st.markdown("---")

    # ---------------------------
    # Footer or Credits
    # ---------------------------
    st.markdown("Created by DataMentes Team")


if __name__ == "__main__":
    main()
