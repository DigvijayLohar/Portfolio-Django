# Portfolio-Django
### https://digvijaylohar.pythonanywhere.com (2 Dec 2024)

This is a personal portfolio website built using Django. The portfolio showcases my projects, skills, certificates, resume, and provides a contact form to reach out to me.

## Features

- **Home Page:** Overview of the portfolio.
- **About Section:** Information about me, my background, and my journey.
- **Resume Section:** Downloadable CV and detailed resume information.
- **Skills Section:** Display of my technical skills with progress bars and skill icons.
- **Projects Section:** Showcases the projects I've worked on, with descriptions and images.
- **Certificates Section:** List of my achievements and certificates.
- **Contact Form:** A form to send me a message directly via email.
- **Responsive Design:** The website is fully responsive and works well on all devices.

## Technologies Used

- **Django:** Backend framework to handle the server-side logic and templates.
- **Bootstrap:** CSS framework for responsive design and styling.
- **JavaScript:** To enhance interactivity on the frontend.
- **Google Forms & JavaScript:** Integrated to handle the contact form submissions.

## Setup and Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/DigvijayLohar/Portfolio-Django.git
# HomePage
![image](https://github.com/user-attachments/assets/77b15eca-0675-4916-9970-64d7c39a5776)
Add animated home page with profile image and buttons

- Implemented a full-height hero section for the home page.
- Added animated text introducing "Digvijay Lohar" as a developer.
- Included a centered profile image with responsive styling.
- Added "Hire Me" button linking to the resume and "Contact" button linking to the contact page.
- Enhanced accessibility and visual appeal with fade-in effects.

Updates the user experience on the home page to provide a more engaging introduction.
# About Page
![image](https://github.com/user-attachments/assets/75f0ab3c-ae89-4df0-b6be-3faf43fe21de)
Add About Me section with personal details and CV download

- Added an "About Me" section with a profile image and detailed personal information.
- Included a section highlighting educational background and key skills.
- Added a list of personal details such as date of birth, address, zip code, email, and phone number.
- Added a "DOWNLOAD CV" button linking to the CV file for download.
- Enhanced layout with Bootstrap classes and animations for a polished look.

Updates the about page to provide a comprehensive overview of the user, including contact information and a downloadable CV.
# Resume Page
![image](https://github.com/user-attachments/assets/2e52de86-ba9e-454e-a877-3587a5052a44)
## Resume Page

The **Resume** page provides a summary of educational qualifications and academic history. The page is organized as follows:

- **Bachelor of Technology** in Computer Science & Engineering (2020-2024)
- **Higher Secondary Education** from S.G.M College, Karad (2018-2020)
- **Secondary Education** from S.S.T.V.M (2017-2018)

Each educational milestone is displayed with relevant dates and institutions, offering a clear view of the user's academic background.

# Skill Page
![image](https://github.com/user-attachments/assets/60e3cdc2-68ce-4fee-8b78-f546f695810c)

The **Skills** page highlights the technical skills and expertise of the individual. 

# Project Page
![image](https://github.com/user-attachments/assets/899db497-e5f0-4d4b-997e-e3c260c54e11)
## Projects Page

The **Projects** page features a section showcasing various projects with images, titles, and descriptions.

### Projects Listed

1. **Cloud-based Skin Disease Detection using Machine Learning**
   - **Image**: `project-2.jpg`
   - **Description**: Developed a cloud-based application leveraging machine learning algorithms to detect and classify skin diseases from medical images.
   - **Link**: [GitHub Repository](https://github.com/DigvijayLohar/Cloud-based-skin-disease-detection-using-machine-learnig.git)

2. **Automating Bank Check Extraction from Scanned PDFs**
   - **Image**: `project-4.jpg`
   - **Description**: Created a system for automating the extraction of key information from bank checks in scanned PDFs.
   - **Link**: [GitHub Repository](https://github.com/Springboard-Internship-2024/Automating-Bank-Check-Extraction-from-Scanned-PDFs_May_2024.git)

3. **Feane Fast Food Web**
   - **Image**: `work-3.png`
   - **Description**: Designed and developed a responsive website for Feane, a fast-food restaurant, with a user-friendly interface for menu browsing.
   - **Link**: [GitHub Repository](https://github.com/DigvijayLohar/Restaurant-Web-Django.git)
# Certification Page
![image](https://github.com/user-attachments/assets/e1330a93-cb49-4f32-bd64-5cd925fc220b)

# Contact page
![image](https://github.com/user-attachments/assets/d8a8a4c9-ff18-44c7-8fe8-0b04a875b2f8)

## Contact Page

The **Contact** page allows users to get in touch by filling out a contact form and provides links to social media profiles.

### Features

- **Contact Form**: Users can submit their name, email, and message.
  - **Form Action URL**: Submits the form data to a Google Apps Script endpoint.
  - **Fields**:
    - Name
    - Email
    - Message
  - **Submit Button**: Sends the form data and displays an alert upon successful submission.

- **Social Media Links**: Includes icons linking to various social media profiles.
  - GitHub: [GitHub Profile](https://github.com/DigvijayLohar)
  - LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/digvijay-lohar-169230244/)
  - Email: [Email](mailto:digvijaylohat007@gmail.com)
  - WhatsApp: [WhatsApp Chat](https://wa.me/7277751007)
  - Instagram: [Instagram Profile](https://www.instagram.com/digya_lohar)

- **Download CV Button**: Allows users to download the CV.
  - **CV Link**: `{% static 'Resume/CV3.pdf' %}`

### JavaScript

Handles form submission by:
1. Preventing the default form submit action.
2. Sending the form data to the specified Google Apps Script URL using `fetch`.
3. Showing a success alert and reloading the page on successful submission.
4. Logging errors to the console if submission fails.

