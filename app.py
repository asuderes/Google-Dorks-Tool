import streamlit as st

st.set_page_config(page_title="Google Dork Generator", layout="wide")

st.title("🔍 Google Dork Generator")

domain = st.text_input(" Hedef Domain (örn: example.com)", "")
keywords = st.text_input(" Özel Anahtar Kelimeler (örn: admin, password)", "")

st.markdown("---")

st.subheader(" Dosya Tabanlı Dorklar")
file_dorks = st.multiselect(
    "Seçiniz:",
    ["PDF Dosyaları", "Office Dosyaları", "Arşiv Dosyaları", "Kod Dosyaları", "Veritabanı Dosyaları"]
)

st.subheader(" Zafiyet Tespiti")
vuln_dorks = st.multiselect(
    "Seçiniz:",
    ["Directory Listing", "Exposed Config", "Database Exposure", "Log Files", "Backup Files"]
)

st.subheader(" CMS ve Framework")
cms_dorks = st.multiselect(
    "Seçiniz:",
    ["WordPress Detection", "Joomla Detection", "Drupal Detection", "phpinfo() Pages"]
)

st.subheader(" Kimlik Doğrulama")
auth_dorks = st.multiselect(
    "Seçiniz:",
    ["Login Pages", "Admin Panels", "Password Files", "User Lists"]
)

st.subheader(" Hata ve Bilgi Sızıntıları")
error_dorks = st.multiselect(
    "Seçiniz:",
    ["SQL Errors", "Server Errors", "Stack Traces", "Debug Info"]
)

dork_map = {

    "PDF Dosyaları": "filetype:pdf",
    "Office Dosyaları": "(filetype:doc OR filetype:xls OR filetype:ppt OR filetype:docx OR filetype:xlsx)",
    "Arşiv Dosyaları": "(filetype:zip OR filetype:rar OR filetype:7z)",
    "Kod Dosyaları": "(filetype:php OR filetype:asp OR filetype:aspx OR filetype:jsp OR filetype:py)",
    "Veritabanı Dosyaları": "(filetype:sql OR filetype:db OR filetype:mdb)",

    # Zafiyet
    "Directory Listing": '"index of /"',
    "Exposed Config": 'ext:xml OR ext:conf OR ext:cnf OR ext:reg OR ext:inf',
    "Database Exposure": '"phpMyAdmin" OR "MySQL dump"',
    "Log Files": 'filetype:log',
    "Backup Files": 'filetype:bak OR filetype:old OR filetype:backup',

    "WordPress Detection": '"wp-content" OR "wp-includes"',
    "Joomla Detection": '"index.php?option=com_"',
    "Drupal Detection": 'inurl:"/sites/default/"',
    "phpinfo() Pages": '"ext:php intitle:phpinfo"',

    "Login Pages": 'inurl:login',
    "Admin Panels": 'inurl:admin OR intitle:"admin panel"',
    "Password Files": 'filetype:txt "password"',
    "User Lists": 'filetype:csv OR filetype:xls "username"',

    "SQL Errors": '"SQL syntax near" OR "syntax error has occurred"',
    "Server Errors": '"Internal Server Error" OR "Apache Server at"',
    "Stack Traces": '"at java." OR "at org." OR "NullPointerException"',
    "Debug Info": '"Warning: mysql_connect()" OR "Fatal error:"'
}

selected = file_dorks + vuln_dorks + cms_dorks + auth_dorks + error_dorks
dork_parts = [dork_map[s] for s in selected if s in dork_map]

query = ""
if domain:
    query += f"site:{domain} "
if keywords:
    query += f'"{keywords}" '
query += " ".join(dork_parts)

st.markdown("##  Oluşturulan Dork Sorgusu")
st.code(query.strip(), language="bash")

col1, col2 = st.columns(2)
with col1:
    st.button("Kopyala")
with col2:
    if query.strip():
        search_url = "https://www.google.com/search?q=" + query.strip().replace(" ", "+")
        st.markdown(f"[ Google'da Ara]({search_url})", unsafe_allow_html=True)
