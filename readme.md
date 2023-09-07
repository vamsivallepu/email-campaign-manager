# Email Campaign Manager

Email Campaign Manager is a Django-based web application that allows you to manage and send email campaigns efficiently. This project includes features for adding subscribers, creating and scheduling campaigns, and optimizing email delivery using parallelization.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Sending Daily Campaigns](#sending-daily-campaigns)
- [Optimizing Email Delivery](#optimizing-email-delivery)
- [Unsubscribe Feature](#unsubscribe-feature)

## Introduction

Email Campaign Manager is a web-based platform designed to streamline email marketing campaigns. It provides a user-friendly interface for managing subscribers, creating and scheduling campaigns, and optimizing the delivery of emails.

## Features

- **Subscriber Management**: Easily add and manage subscribers with their email addresses and first names. Implement an unsubscribe feature to respect user preferences.

- **Campaign Creation**: Create email campaigns with various components, including subject, preview text, article URL, HTML content, plain text content, and published date.

- **Scheduling**: Schedule campaigns to be sent at specific dates, ensuring timely delivery to your subscribers.

- **Email Rendering**: Render campaign emails with dynamic content using a base template. Link article URLs, add plain text content to the email body, and include HTML content for rich email experiences.

- **Optimized Delivery**: Utilized parallelization to optimize email delivery time, ensuring efficient sending of campaigns.

## Getting Started

### Prerequisites

Before getting started, ensure that you have the following installed:
- Python >= 3.8
- Django >= 4.2
- Mailgun API credentials

### Installation

Follow these steps to set up the Email Campaign Manager:

1. Clone the repository:

   ```bash
   git clone https://github.com/vamsivallepu/email-campaign-manager.git
   cd email-campaign-manager
   ```
2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:

   ```bash
    source venv/bin/activate
   ```
4. Install the required packages:

   ```bash
    pip install -r requirements.txt
   ```
5. Configure AES_KEY, AES_IV, EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD and EMAIL_PORT in .env file.
6. Apply migrations and create the database tables:

   ```bash
    python manage.py makemigrations
    python manage.py migrate
   ```
7. Create a superuser:

   ```bash
    python manage.py createsuperuser
   ```
8. Run the server:

   ```bash
    python manage.py runserver
   ```

## Usage
1. Access the admin panel to manage subscribers and create campaigns:
    ```bash
     http://localhost:8000/admin/
    ```
2. Use the Django admin interface to add subscribers and create campaign records.

## Sending Daily Campaigns
1. Use the `/send-campaigns` endpoint to send campaigns scheduled for the current date:
    ```bash
     http://localhost:8000/send-campaigns/
    ```

## Optimizing Email Delivery
Email delivery is optimized using parallelization and a pub-sub mechanism :
1. Multiple threads are used to dispatch emails in parallel, reducing the time it takes to send campaigns to a large subscriber list.
2. Implemented a message queue (pub-sub) to ensure efficient handling and delivery of emails.

## Unsubscribe Feature
The application includes an unsubscribe feature accessible through the endpoint:
```bash
 http://localhost:8000/unsubscribe/<str:encrypted_email>
```
- Subscribers can use this endpoint to unsubscribe themselves from email campaigns.
- Encrypted email is passed as a parameter to the endpoint. 
- The email is decrypted and the corresponding subscriber is deleted from the database. 
- This feature is implemented securely to prevent unauthorized unsubscribes.

