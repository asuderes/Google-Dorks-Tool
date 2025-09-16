# Google Dork Generator Web Uygulaması

Bu çalışmada, güvenlik araştırmacılarının ve siber güvenlik meraklılarının Google arama motoru üzerinden hızlı ve özelleştirilmiş dork sorguları üretebilmeleri için bir **Google Dork Generator** web uygulaması geliştirilmiştir. Uygulama, kullanıcıların farklı parametreleri seçmesine olanak tanımakta ve bu parametrelerden otomatik olarak dork sorguları üretmektedir. Böylece manuel sorgu yazma süreci kısalmakta, hata riski azalmakta ve kullanıcıya daha pratik bir araştırma imkânı sunulmaktadır.

## 1. Giriş

Bu proje kapsamında, kullanıcıların çeşitli parametreler kullanarak özelleştirilmiş Google Dork sorguları oluşturabileceği bir web uygulaması geliştirdim. Uygulamanın temel amacı, bilgi güvenliği araştırmalarında veya hedef odaklı aramalarda kullanılan dork sorgularını kolay, hızlı ve kullanıcı dostu bir şekilde üretmektir.

Hazırladığım uygulamada, kullanıcıya interaktif bir arayüz sunulmaktadır. Bu arayüz üzerinden kullanıcı, hedef domain bilgisini, özel anahtar kelimeleri ve farklı dork parametrelerini (örneğin: site:, filetype:, inurl:, intitle: vb.) seçebilmektedir. Seçimlere göre dinamik olarak bir Google Dork sorgusu üretilmekte ve kullanıcı isterse bu sorguyu kopyalayabilmekte veya doğrudan Google üzerinde çalıştırabilmektedir.

Uygulamanın sunduğu özellikler arasında dosya tabanlı aramalar (PDF, Office, Arşiv, Kod ve Veritabanı dosyaları), zafiyet tespiti (Directory Listing, Config dosyaları, veritabanı sızıntıları vb.), CMS ve framework tespiti (WordPress, Joomla, Drupal) ve kimlik doğrulama açıklarının aranması (login sayfaları, admin panelleri, kullanıcı listeleri) bulunmaktadır. Ayrıca hata ve bilgi sızıntılarına yönelik dork parametreleri (SQL hataları, sunucu hataları, stack trace’ler) de desteklenmektedir.

Bu proje sayesinde, manuel olarak karmaşık dork sorguları yazmak yerine kullanıcı dostu bir arayüzle hızlı ve doğru sorgular oluşturmak mümkün hale gelmiştir. Geliştirme sürecinde Python programlama dili ve Streamlit kütüphanesini kullandım. Bu sayede proje hem kolayca çalıştırılabilir hem de görsel açıdan kullanıcıya pratik bir deneyim sunmaktadır.

Sonuç olarak, proje bilgi güvenliği çalışmalarında araştırmacılara ve siber güvenlik uzmanlarına zaman kazandıran, kullanışlı ve pratik bir araç ortaya çıkarmaktadır.

## 2. Amaç ve Hedefler

Bu çalışmanın temel amacı, Google Dork sorgularının daha hızlı ve kolay bir şekilde oluşturulmasını sağlayacak bir araç geliştirmektir.

**Projenin hedefleri şunlardır:**

- Kullanıcıların farklı kategorilerde dork sorguları oluşturabilmesi,
- Parametrelerin dinamik olarak birleştirilmesi,
- Hazırlanan sorguların tek tıkla kopyalanabilmesi veya Google üzerinde çalıştırılabilmesi,
- Güvenlik araştırmacılarına zaman kazandırılması.

## 3. Kullanılan Teknolojiler

Projenin geliştirilmesinde kullanılan araçlar ve teknolojiler:

- **Python:** Uygulamanın geliştirilmesinde kullanılan temel programlama dili.
- **Streamlit:** Python tabanlı, hızlı ve interaktif web uygulamaları geliştirmek için kullanılan kütüphane. Kullanıcı arayüzü bu teknoloji ile oluşturulmuştur.
- **Visual Studio Code (VSCode):** Geliştirme ortamı olarak kullanılmıştır.
- **Web Tarayıcı:** Kullanıcıların uygulamayı çalıştırması ve sorguları test etmesi için gerekli ortamdır.

## 4. Uygulamanın Özellikleri

Uygulama aşağıdaki temel özelliklere sahiptir:

- **Hedef Domain Araması:** Kullanıcı, belirli bir domain üzerinde arama yapabilir.
- **Anahtar Kelime Tabanlı Arama:** “admin”, “password”, “config” gibi özel kelimeler eklenebilir.
- **Dosya Tabanlı Dorklar:** PDF, Office, arşiv, kod ve veritabanı dosyalarına yönelik aramalar.
- **Zafiyet Tespiti:** Directory listing, exposed config, log files gibi açıklıkları bulmaya yönelik sorgular.
- **CMS ve Framework Tespiti:** WordPress, Joomla, Drupal ve phpinfo sayfaları için özel dorklar.
- **Kimlik Doğrulama ve Hata Sızıntıları:** Login sayfaları, admin panelleri, SQL hataları, server hataları gibi parametreler.

Her seçim, arka planda otomatik olarak uygun Google Dork sorgusuna dönüştürülmektedir.

## 5. Çalışma Mantığı

1. Kullanıcı, arayüz üzerinden parametreleri seçer (örn. site:example.com + filetype:pdf).
2. Sistem, bu parametreleri uygun formatta birleştirerek dork sorgusunu üretir.
3. Üretilen sorgu kullanıcıya gösterilir.
4. Kullanıcı isterse sorguyu kopyalar, isterse tek tıkla Google’da çalıştırır.

## 6. Sonuç ve Değerlendirme

Bu proje ile Google Dork sorgularının manuel yazılması yerine, interaktif bir web aracı geliştirilmiştir. Kullanıcıların güvenlik testlerinde zamandan tasarruf etmesini ve doğru formatta sorgular oluşturmasını sağlamaktadır.

**Gelecek çalışmalar için öneriler:**

- Daha fazla dork kategorisinin eklenmesi,
- Kullanıcıların kendi dork şablonlarını kaydedebilmesi,
- Mobil uyumlu bir arayüz geliştirilmesi,
- Dork sorgularının raporlanabilmesi.

## 7. Kaynakça

- Johnny Long, *Google Hacking for Penetration Testers*, 2005.
- Streamlit Resmi Dokümantasyonu: https://streamlit.io
- Google Dork Database (GHDB), Exploit-DB.

---

# Google Dork Generator Web Application

## Abstract

In this project, I developed a **Google Dork Generator** web application that allows security researchers and cybersecurity enthusiasts to quickly and easily generate customized Google Dork queries. The application enables users to select different parameters, which are then automatically combined into valid dork queries. This reduces the time and errors associated with manually writing dork queries and provides a practical tool for research purposes.

## 1. Introduction

Google Dorking is a technique used to discover sensitive information and potential security vulnerabilities by leveraging search engines. It is widely used by **pentesters, security analysts, and researchers**. However, creating accurate dork queries manually requires experience and can be time-consuming.

This project aims to simplify this process by providing a web application where users can select relevant parameters, and the system automatically generates properly formatted Google Dork queries. The interface is designed to be simple, intuitive, and user-friendly.

In this project, I developed a web application that allows users to create customized Google Dork queries using various parameters. The main goal of the application is to generate dork queries in a simple, fast, and user-friendly way, which can be useful in security research or targeted searches.

In the application I built, users are provided with an interactive interface. Through this interface, they can enter a target domain, define custom keywords, and select different dork parameters (such as site:, filetype:, inurl:, intitle: etc.). Based on these inputs, the application dynamically generates a Google Dork query. Users can either copy the query or directly run it on Google with a single click.

The features of the application include file-based searches (PDF, Office, Archive, Code, and Database files), vulnerability detection (Directory Listing, exposed configuration files, database leaks, etc.), CMS and framework detection (WordPress, Joomla, Drupal), and authentication-related searches (login pages, admin panels, user lists, and password files). In addition, it also supports dork parameters for detecting errors and information leaks (SQL errors, server errors, stack traces, debug info).

Instead of writing complex dork queries manually, this project enables users to generate them quickly and accurately through a user-friendly interface. I developed the project using Python and the Streamlit library, which makes it both easy to run and visually practical for the end user.

As a result, the project provides a useful and practical tool that helps researchers and cybersecurity professionals save time and work more efficiently during security investigations.

## 2. Objectives

The main objective of this project is to create a tool that generates **dynamic Google Dork queries** quickly and efficiently.

**Project goals include:**

- Allowing users to generate queries based on multiple categories,
- Automatically combining selected parameters into a valid dork query,
- Enabling users to copy the generated query or execute it directly on Google,
- Saving time for security researchers during investigations.

## 3. Technologies Used

The project was developed using the following technologies:

- **Python:** The primary programming language used to develop the application.
- **Streamlit:** A Python framework for building interactive web applications. The user interface was implemented using Streamlit.
- **Visual Studio Code (VSCode):** Used as the development environment for coding and debugging.
- **Web Browser:** Used for running the application and testing generated queries.

## 4. Application Features

The application provides the following key features:

- **Target Domain Search:** Users can specify a domain for the query.
- **Custom Keywords:** Users can input specific keywords such as “admin”, “password”, or “config”.
- **File-Based Dorks:** Support for PDF, Office, archive, code, and database file searches.
- **Vulnerability Detection:** Queries for directory listing, exposed config files, log files, database exposure, etc.
- **CMS and Framework Detection:** Special dorks for WordPress, Joomla, Drupal, and phpinfo pages.
- **Authentication and Error Detection:** Queries for login pages, admin panels, password files, SQL errors, server errors, and debug information.

Each selection is automatically converted into a properly formatted Google Dork query.

## 5. Working Logic

1. The user selects parameters through the interface (e.g., site:example.com + filetype:pdf).
2. The system automatically combines the parameters into a valid Google Dork query.
3. The generated query is displayed to the user.
4. The user can either copy the query or execute it on Google with a single click.

## 6. Results and Evaluation

The project provides an interactive web application that eliminates the need to manually write Google Dork queries. It saves time and ensures accuracy for users conducting security testing or research.

**Future work suggestions:**

- Adding more dork categories,
- Allowing users to save custom dork templates,
- Developing a mobile-friendly interface,
- Implementing query reporting and export functionality.

## 7. References

- Johnny Long, *Google Hacking for Penetration Testers*, 2005.
- Streamlit Official Documentation: https://streamlit.io
- Google Hacking Database (GHDB), Exploit-DB.
