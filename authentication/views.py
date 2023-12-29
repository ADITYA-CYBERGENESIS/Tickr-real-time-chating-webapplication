from django.shortcuts import render,redirect
import re
from customuserml.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
import time
from customuserml.manager import UserManager
# Create your views here.
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.core.mail import EmailMessage
from django.utils.html import strip_tags
from django.contrib.auth import get_user_model
import random
import string
def generate_unique_email_token(length):
    User = get_user_model()
    
    while True:
        # Generate a random string using URL-safe characters
        characters = string.ascii_letters + string.digits + '-_'
        random_string = ''.join(random.choice(characters) for _ in range(length))

        # Check if the random string is unique among existing users
        if not User.objects.filter(email_token=random_string).exists():
            return random_string
def generate_random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


def send_html_email(subject, to_email, html_content):
    # Create an EmailMultiAlternatives instance
    email = EmailMultiAlternatives(
        subject=subject,
        body=strip_tags(html_content),  # Use the stripped HTML content as the plain text content
        to=[to_email],
    )

    # Attach the HTML content as an alternative content type
    email.attach_alternative(html_content, 'text/html')

    # Send the email
    email.send()
def get_user_by_username(username):
    User = get_user_model()
    try:
        user = User.objects.get(username=username)
        return user
    except User.DoesNotExist:
        return None
def is_username_taken(username):
     return User.objects.filter(username=username).exists()
def is_email_taken(email):
    return User.objects.filter(email=email).exists() 
def is_email(s):
         email_pattern = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$")
         return bool(email_pattern.match(s))
def get_username_from_email(email):
          try:
           user = User.objects.get(email=email)
           return user.username
          except User.DoesNotExist:
           return None   
       
         
def register(request):
    context = 'success'
    reversed_numbers = reversed(range(1, 4))
    data = {'context': context, 'reversed_numbers': list(reversed_numbers)}
    if request.method == 'POST':
       
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', ';', ':', ',', '.', '<', '>', '?', '/', '|', '\\']
        username = request.POST.get('username').lower()
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email =request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')
        print(username,firstname,lastname,email,password,confirmpassword)
        if (not username or len(username) < 6 or any(char in special_characters for char in username) or len(username) > 20 or
    not firstname or any(char in numbers for char in firstname) or len(firstname) < 3 or len(firstname) > 20 or
    not lastname or any(char in numbers for char in lastname) or len(lastname) < 3 or len(lastname) > 20 or
    not is_email(email) or
    not password or not confirmpassword or
    not (any(c.islower() for c in password) or any(c.isupper() for c in password) or any(c in special_characters for c in password) or any(c.isdigit() for c in password) or not (6 <= len(password) <= 20)) or
    password != confirmpassword or is_username_taken(username) or is_email_taken(email)):
         print('error')
         return render(request, 'authentication/registrationform.html')
        else:
         model = User
         newuser = User.objects.create_user(username,email,password)
         newuser.first_name = firstname
         newuser.last_name = lastname
         newuser.email_token = generate_unique_email_token(100)
         print(newuser.email_token)
         subject = 'Tickr Account activation'
         to_email = f'{email}'
         activation_link = f'http://127.0.0.1:8000/activation/{username}/{newuser.email_token}'
         css = """<style>
    body {
      background: #FBFBFD;
      margin: 0;
      padding: 0;
      font-family: 'Arial', sans-serif;
    }

    .container {
      background: #d5d5f8;
      padding: 20px;
      border-radius: 10px;
      margin: 20px auto;
      max-width: 600px;
    }

    #logo {
      display: block;
      margin: 0 auto;
    }

    h2 {
      color: #7D4EF5;
      text-align: center;
    }

    p {
      color: #0B0910;
      text-align: center;
      line-height: 1.6;
    }

    .activate-btn {
      display: block;
      width: 100%;
      background: #461AB8;
      color: #EAE6F3;
      text-decoration: none;
      padding: 10px;
      border-radius: 5px;
      text-align: center;
      margin-top: 20px;
    }

    .footer {
      margin-top: 20px;
      text-align: center;
      color: #A489EA;
    }
  </style>"""
         html_content = f"""
                <!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tickr - Best Real-Time Chatting Website</title>
  
</head>
{css}

<body>
  <div class="container">
    <img style="width:100%" src="https://lh3.googleusercontent.com/u/1/drive-viewer/AEYmBYQSeV576e5RJr18ITMLv2AyqPxkyOVZvEsA4sPbUujT0jMMvhpy-Il5V-N6CQ77-ImEmsRwd9AzsT9PT1yFf3VuBv26EQ=w1868-h1072" alt="Tickr Logo" id="logo">
    <h2>Welcome to Tickr - The Best Real-Time Chatting Experience!</h2>
    <p>Tickr is your go-to platform for seamless and engaging real-time conversations. Connect with friends, family, and colleagues instantly and experience the joy of communication like never before.</p>
    <a href="{activation_link}" class="activate-btn">Activate Now</a>
    <p>Why Choose Tickr?</p>
    <ul>
      <li>Instant Messaging: Chat in real-time with anyone, anywhere.</li>
      <li>Intuitive Interface: Our user-friendly design makes chatting a breeze.</li>
      <li>End-to-End Encryption: Ensure your conversations are private and secure.</li>
      <li>Customizable Profiles: Personalize your Tickr experience.</li>
    </ul>
    <p>Click the button below to activate your Tickr account and start chatting!</p>
    
  </div>
  <div class="footer">
    <p>Thank you for choosing Tickr! For more information, visit <a href="https://www.tickr.com">www.tickr.com</a></p>
  </div>
</body>

</html>
                """
         send_html_email(subject, to_email, html_content)
         newuser.save()     
         return render(request,'authentication/registrationform.html',{'context':context})
         
         
         
            
    return render(request,'authentication/registrationform.html')


def user_login(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('usernameoremail')
        password = request.POST.get('password')

        if is_email(username_or_email):
            username_or_email = get_username_from_email(username_or_email)

        activation_check = get_user_by_username(username_or_email)

        if activation_check is not None:
            user = authenticate(username=username_or_email, password=password)

            if user is not None and activation_check.email_activated:
                login(request, user)
                return redirect('chathome')
            else:
                print('activate' if not activation_check.email_activated else 'bad')
                context = 'activate' if not activation_check.email_activated else 'bad'
                return render(request, 'authentication/login.html', {'context': context})
        else:
            print('bad')
            context = 'bad'
            return render(request, 'authentication/login.html', {'context': context})

    return render(request, 'authentication/login.html')

def forgotpassword(request):
     if request.method == 'POST':
      useroremail = request.POST['usernameoremail']
      if is_email(useroremail):
            username = get_username_from_email(useroremail)
            user = get_user_by_username(username)
            if user is not None:     
                subject = 'Tickr Account Password reset'
                to_email = f'{user.email}'
                
                reset_link = f'http://127.0.0.1:8000/reset/{user.username}/{user.email_token}'
                css = """<style>
    body {
      background: #FBFBFD;
      margin: 0;
      padding: 0;
      font-family: 'Arial', sans-serif;
    }

    .container {
      background: #d5d5f8;
      padding: 20px;
      border-radius: 10px;
      margin: 20px auto;
      max-width: 600px;
    }

    #logo {
      display: block;
      margin: 0 auto;
    }

    h2 {
      color: #7D4EF5;
      text-align: center;
    }

    p {
      color: #0B0910;
      text-align: center;
      line-height: 1.6;
    }

    .reset-btn {
      display: block;
      width: 100%;
      background: #461AB8;
      color: #EAE6F3;
      text-decoration: none;
      padding: 10px;
      border-radius: 5px;
      text-align: center;
      margin-top: 20px;
    }

    .footer {
      margin-top: 20px;
      text-align: center;
      color: #A489EA;
    }
  </style>"""
                html_content = f"""
                <!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tickr - Password Reset</title>
  {css}
</head>

<body>
  <div class="container">
    <img style="width:100%" src="https://lh3.googleusercontent.com/u/1/drive-viewer/AEYmBYQSeV576e5RJr18ITMLv2AyqPxkyOVZvEsA4sPbUujT0jMMvhpy-Il5V-N6CQ77-ImEmsRwd9AzsT9PT1yFf3VuBv26EQ=w1868-h1072" alt="Tickr Logo" id="logo">
    <h2>Password Reset - Tickr</h2>
    <p>We received a request to reset your Tickr account password. If you didn't make this request, you can safely ignore this email.</p>
    <a href="{reset_link}" class="reset-btn">Reset Password</a>
    <p>If the above button doesn't work, you can copy and paste the following link into your browser:</p>
    <p>{reset_link}</p>
  </div>
  <div class="footer">
    <p>Thank you for choosing Tickr! For more information, visit <a href="https://www.tickr.com">www.tickr.com</a></p>
  </div>
</body>

</html>
 """
                send_html_email(subject, to_email, html_content)
                context='sent'
                return render(request,'authentication/forgotpassword.html',{'context':context})
            else:
                context='bad'
                return render(request,'authentication/forgotpassword.html',{'context':context})
      else:
            user = get_user_by_username(useroremail)
            if user is not None:       
                subject = 'Tickr Account Password reset'
                to_email = f'{user.email}'
                reset_link = f'http://127.0.0.1:8000/reset/{user.username}/{user.email_token}'
                css = """<style>
    body {
      background: #FBFBFD;
      margin: 0;
      padding: 0;
      font-family: 'Arial', sans-serif;
    }

    .container {
      background: #d5d5f8;
      padding: 20px;
      border-radius: 10px;
      margin: 20px auto;
      max-width: 600px;
    }

    #logo {
      display: block;
      margin: 0 auto;
    }

    h2 {
      color: #7D4EF5;
      text-align: center;
    }

    p {
      color: #0B0910;
      text-align: center;
      line-height: 1.6;
    }

    .reset-btn {
      display: block;
      width: 100%;
      background: #461AB8;
      color: #EAE6F3;
      text-decoration: none;
      padding: 10px;
      border-radius: 5px;
      text-align: center;
      margin-top: 20px;
    }

    .footer {
      margin-top: 20px;
      text-align: center;
      color: #A489EA;
    }
  </style>"""
                html_content = f"""
                <!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tickr - Password Reset</title>
  {css}
</head>

<body>
  <div class="container">
    <img style="width:100%" src="https://lh3.googleusercontent.com/u/1/drive-viewer/AEYmBYQSeV576e5RJr18ITMLv2AyqPxkyOVZvEsA4sPbUujT0jMMvhpy-Il5V-N6CQ77-ImEmsRwd9AzsT9PT1yFf3VuBv26EQ=w1868-h1072" alt="Tickr Logo" id="logo">
    <h2>Password Reset - Tickr</h2>
    <p>We received a request to reset your Tickr account password. If you didn't make this request, you can safely ignore this email.</p>
    <a href="{reset_link}" class="reset-btn">Reset Password</a>
    <p>If the above button doesn't work, you can copy and paste the following link into your browser:</p>
    <p>{reset_link}</p>
  </div>
  <div class="footer">
    <p>Thank you for choosing Tickr! For more information, visit <a href="https://www.tickr.com">www.tickr.com</a></p>
  </div>
</body>

</html>
 """
                send_html_email(subject, to_email, html_content)
                context='sent'
                return render(request,'authentication/forgotpassword.html',{'context':context})
            else:
                context='bad'
                return render(request,'authentication/forgotpassword.html',{'context':context})
     return render(request,'authentication/forgotpassword.html')   

def emailactivation(request):
   if request.method == 'POST':
    useroremail = request.POST['usernameoremail']
    if is_email(useroremail):
            username = get_username_from_email(useroremail)
            user = get_user_by_username(username)
            if user is not None:
              if user.email_activated:
                    context='activated'
                    return render(request,'authentication/activateactivation.html',context)
              else:        
                subject = 'Tickr Account activation'
                to_email = f'{user.email}'
                activation_link = f'http://127.0.0.1:8000/activation/{user.username}/{user.email_token}'
                css = """<style>
    body {
      background: #FBFBFD;
      margin: 0;
      padding: 0;
      font-family: 'Arial', sans-serif;
    }

    .container {
      background: #d5d5f8;
      padding: 20px;
      border-radius: 10px;
      margin: 20px auto;
      max-width: 600px;
    }

    #logo {
      display: block;
      margin: 0 auto;
    }

    h2 {
      color: #7D4EF5;
      text-align: center;
    }

    p {
      color: #0B0910;
      text-align: center;
      line-height: 1.6;
    }

    .activate-btn {
      display: block;
      width: 100%;
      background: #461AB8;
      color: #EAE6F3;
      text-decoration: none;
      padding: 10px;
      border-radius: 5px;
      text-align: center;
      margin-top: 20px;
    }

    .footer {
      margin-top: 20px;
      text-align: center;
      color: #A489EA;
    }
  </style>"""
                html_content = f"""
                <!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tickr - Best Real-Time Chatting Website</title>
  
</head>
{css}

<body>
  <div class="container">
    <img style="width:100%" src="https://lh3.googleusercontent.com/u/1/drive-viewer/AEYmBYQSeV576e5RJr18ITMLv2AyqPxkyOVZvEsA4sPbUujT0jMMvhpy-Il5V-N6CQ77-ImEmsRwd9AzsT9PT1yFf3VuBv26EQ=w1868-h1072" alt="Tickr Logo" id="logo">
    <h2>Welcome to Tickr - The Best Real-Time Chatting Experience!</h2>
    <p>Tickr is your go-to platform for seamless and engaging real-time conversations. Connect with friends, family, and colleagues instantly and experience the joy of communication like never before.</p>
    <a href="{activation_link}" class="activate-btn">Activate Now</a>
    <p>Why Choose Tickr?</p>
    <ul>
      <li>Instant Messaging: Chat in real-time with anyone, anywhere.</li>
      <li>Intuitive Interface: Our user-friendly design makes chatting a breeze.</li>
      <li>End-to-End Encryption: Ensure your conversations are private and secure.</li>
      <li>Customizable Profiles: Personalize your Tickr experience.</li>
    </ul>
    <p>Click the button below to activate your Tickr account and start chatting!</p>
    
  </div>
  <div class="footer">
    <p>Thank you for choosing Tickr! For more information, visit <a href="https://www.tickr.com">www.tickr.com</a></p>
  </div>
</body>

</html>
                """
                send_html_email(subject, to_email, html_content)
                context='sent'
                return render(request,'authentication/activateactivation.html',{'context':context})
            else:
                context='bad'
                return render(request,'authentication/activateactivation.html',{'context':context})
    else:
            user = get_user_by_username(useroremail)
            if user is not None:
              if user.email_activated:
                    context='activated'
                    return render(request,'authentication/activateactivation.html',{'context':context})
              else:        
                subject = 'Tickr Account activation'
                to_email = f'{user.email}'
                activation_link = f'http://127.0.0.1:8000/activation/{user.username}/{user.email_token}'
                css = """<style>
    body {
      background: #FBFBFD;
      margin: 0;
      padding: 0;
      font-family: 'Arial', sans-serif;
    }

    .container {
      background: #d5d5f8;
      padding: 20px;
      border-radius: 10px;
      margin: 20px auto;
      max-width: 600px;
    }

    #logo {
      display: block;
      margin: 0 auto;
    }

    h2 {
      color: #7D4EF5;
      text-align: center;
    }

    p {
      color: #0B0910;
      text-align: center;
      line-height: 1.6;
    }

    .activate-btn {
      display: block;
      width: 100%;
      background: #461AB8;
      color: #EAE6F3;
      text-decoration: none;
      padding: 10px;
      border-radius: 5px;
      text-align: center;
      margin-top: 20px;
    }

    .footer {
      margin-top: 20px;
      text-align: center;
      color: #A489EA;
    }
  </style>"""
                html_content = f"""
                <!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tickr - Best Real-Time Chatting Website</title>
  
</head>
{css}

<body>
  <div class="container">
    <img style="width:100%" src="https://lh3.googleusercontent.com/u/1/drive-viewer/AEYmBYQSeV576e5RJr18ITMLv2AyqPxkyOVZvEsA4sPbUujT0jMMvhpy-Il5V-N6CQ77-ImEmsRwd9AzsT9PT1yFf3VuBv26EQ=w1868-h1072" alt="Tickr Logo" id="logo">
    <h2>Welcome to Tickr - The Best Real-Time Chatting Experience!</h2>
    <p>Tickr is your go-to platform for seamless and engaging real-time conversations. Connect with friends, family, and colleagues instantly and experience the joy of communication like never before.</p>
    <a href="{activation_link}" class="activate-btn">Activate Now</a>
    <p>Why Choose Tickr?</p>
    <ul>
      <li>Instant Messaging: Chat in real-time with anyone, anywhere.</li>
      <li>Intuitive Interface: Our user-friendly design makes chatting a breeze.</li>
      <li>End-to-End Encryption: Ensure your conversations are private and secure.</li>
      <li>Customizable Profiles: Personalize your Tickr experience.</li>
    </ul>
    <p>Click the button below to activate your Tickr account and start chatting!</p>
    
  </div>
  <div class="footer">
    <p>Thank you for choosing Tickr! For more information, visit <a href="https://www.tickr.com">www.tickr.com</a></p>
  </div>
</body>

</html>
                """
                send_html_email(subject, to_email, html_content)
                context='sent'
                return render(request,'authentication/activateactivation.html',{'context':context})
            else:
                context='bad'
                return render(request,'authentication/activateactivation.html',{'context':context})
   return render(request,'authentication/activateactivation.html')   
                  
            
def activation(request,username,uniqueid):
    user = get_user_by_username(username)
    print('ok')
    print(uniqueid)
    if user.email_token == uniqueid:
        print('ok2')
          
        user.email_token = generate_unique_email_token(100)
        user.email_activated=True
        user.save()
        return render(request,'authentication/accountactivated.html')
    else:
        return redirect('register')   
        
def activate(request, user_ip, username):
    pass
    return HttpResponse(f'this userip {user_ip} and this username{username}')
def resetpassword(request,username,uniqueid):
  if request.method == 'POST':   
    password = request.POST['password'] 
    confirmpassword = request.POST['confirmpassword']
    if password == confirmpassword:
     user = get_user_by_username(username)
     if user.email_token == uniqueid:
        print('ok2') 
        user.set_password(password)
        user.email_token = generate_unique_email_token
        user.save()
        context = 'done'
        return render(request,'authentication/resetpassword.html',{'context':context})
    else:
       context = 'wrong'
       user.email_token = generate_unique_email_token
       user.save()
       return render(request,'authentication/resetpassword.html',{'context':context})
  return render(request,'authentication/resetpassword.html')
def user_logout(request):
  user = request.user
  if user.is_authenticated:
    logout(request)
    return redirect('home')
  return redirect('home')  