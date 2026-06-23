# Signup_automation
User registration flow including form filling, dropdown selection, file upload, and OTP handling using mailosau

## Prerequisites
- Python installed
- Google Chrome browser installed
- Mailosaur account (for otp)  

## Setup
### 1.Clone this repository:
### 2.Install required dependency
- pip install selenium
- pip install mailosaur
### 3.Set up Mailosaur account
- Create account
- Get API key + server ID
- Add them in your script
### 3.Run the project

## Environment Details

| Tool         | Version          |
|--------------|---------------------------|
| Python       | 3.14.5                    |
| Selenium     | 4.44.0                    |                
| Mailosaur    | API-based tool            |

## How this works
- The script opens Google Chrome using Selenium WebDriver.
- Navigates to the signup page of the application.
- Fills out the form with random data ( email and phone).
- Uses Mailosaur to handle email testing / OTP verification.
- After successful OTP verification, the flow continues to agency details,professional experience and verification & preferance.
- The script uses explicit waits to handle dynamic page loading between steps.
- After successful submission, the script performs an assertion to verify successful form submission.
