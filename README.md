# CSC-131-Website

# Ron Smithey Financial Services Website

This is a customizable and client-ready static website for Ron Smithey Financial Services. 

---

## 🚀 Features

- Easy-to-navigate financial service website
- Configurable via a JSON file (`Config.json`)
- Displays uploaded legal PDF documents dynamically as links
- Newsletter sign-up and inquiry form via `formsubmit.co`
- Responsive and mobile-friendly
- Sections include:
  - Home page
  - About us
  - Financial Planning
  - Corporate Solutions
  - Calculators
  - Newsletter
  - Client Success
  - Calendar
  - Contact Us

---

## 🛠 Setup Instructions

### 1. Clone or Download the Repository

```bash
git clone https://github.com/TheDude2701/CSC-131-Website.git
cd ./CSC-131-Website
```
### 2.Open the Config.json file and Enter in the required API keys and info
    
    For instance:
        "YOUR_EMAIL": "Ron@gmail.com"
    Place the required Info inside the " "

    Info On how to get the API keys are below

### 3.Run setup.py

```bash
python3 setup.py
```

### 3. intial setup
    1. Images used in the website can be found in the Images folder
        Once you have a photo of yourself you would like to use for the website, You can add the photo (preferably png format, if it's another format, you can convert it to png before adding it) to the Images folder and name it ron-smithey.png 
    2. For the customer photos on the front page, they work the same way and if you have photos for them, you can add them and name them    customer1.png, customer2.png, customer3.png and save them to the Images folder.
    3. For newsletter, You can upload the newsletter in txt format into the newsletter folder and  Make sure your .txt files are named in the format YYYY-MM-label.txt (e.g., 2025-01-january.txt, 2025-02-february.txt). This will automatically add the text in the txt file and add it to the site under the newsletter section. You can add as many as you would like and it will automatically append them to the site.
    4. For the legal documentation, You can upload the legal pdfs into the Legal_pdf folder. and they will be embeded under the legal documentation section that users can open and read.

    For the Legal_pdf and Newsletter folders, the contents in there currently are simply placeholders and can be deleted before you complete this step.
### 4.Run setup.py

```bash
python3 setup.py
```
### 5. Hosting the website

If you are web hosting with 3rd party services:
    1. Log in to your hosting control panel (e.g., cPanel)
    2. Go to File Manager or use FTP to upload your files into the public_html directory (or root directory).

If you want to host it locally on your machine to check it out first:
    run the following script:
 ```bash
    cd /path/to/your/website
    python3 -m http.server 8000
``` 
    Then navigate to http://localhost:8000 and you'll see the list of pages


### IMPORTANT!!!!
    For public HTML-based hosting, avoid uploading sensitive files like Config.json with private API keys
    The Config.json file is for first time setup and should not be uploaded with the rest of the sites. 



## Security Notes
    - No sensitive user data is stored or shared.
    - Email and API keys are injected locally during site generation and are not exposed beyond what you put into your HTML.


# Google API Setup Guide

This guide walks you through how to get your Google Calendar API Key, Calendar ID, and Google Sheets API Key for integrating with the Ron Smithey Financial Services website.

---

## 📅 Google Calendar API Setup

### 1. Create a Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/).
2. Click **Select a project** → **New Project**.
3. Name your project and click **Create**.

---

### 2. Enable Google Calendar API

1. Inside your project dashboard, go to the **API & Services > Library**.
2. Search for **Google Calendar API**.
3. Click it and press **Enable**.

---

### 3. Create API Credentials

1. Go to **API & Services > Credentials**.
2. Click **+ Create Credentials** → choose **API key**.
3. Copy the **API Key** — you’ll use this in your website.

---

### 4. Get Your Calendar ID

1. Go to [Google Calendar](https://calendar.google.com/).
2. On the left under **My calendars**, click the three dots next to the calendar you want to share.
3. Click **Settings and sharing**.
4. Scroll to **Integrate calendar** → copy the **Calendar ID** (e.g., `yourname@gmail.com` or `abc123@group.calendar.google.com`).

---

### 5. Make Calendar Public (Required for Public Sites)

1. Still in Calendar settings, under **Access permissions**, check **Make available to public**.
2. Confirm the prompt — this makes events visible.

---

## 📊 Google Sheets API Setup

### 1. Enable Google Sheets API

1. In your **Google Cloud Project**, go back to **API & Services > Library**.
2. Search for **Google Sheets API**.
3. Click and press **Enable**.

---

### 2. Create API Key (Reuse or Repeat)

If you already created an API key in the Calendar section, you can reuse it. If not:

1. Go to **API & Services > Credentials**.
2. Click **+ Create Credentials** → **API key**.
3. Copy and save the **API key**.

---

### 3. Share Your Sheet

1. Go to your [Google Sheet](https://sheets.google.com).
2. Click **Share** (top right).
3. Click **Anyone with the link → Viewer**.
4. Copy the Sheet **ID** from the URL: