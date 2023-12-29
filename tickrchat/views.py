from django.shortcuts import render,redirect
from django.views.decorators.clickjacking import xframe_options_exempt
from django.contrib.auth.decorators import login_required
from customuserml.models import User
from .models import ChatThread,ChatMessage,GroupChatThread
from django.db.models import Q
from datetime import datetime
import pytz
from PIL import Image
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile
from django.utils.text import slugify
import uuid
from django.http import HttpResponse
import random
import string
from django.contrib.auth import get_user_model
from django import forms
from django.db.models import Max
from django.shortcuts import get_object_or_404
import razorpay

def get_thread_info(thread, current_user):
    # Assuming User has a username field
    if thread.user_one == current_user:
        other_user = thread.user_two
    else:
        other_user = thread.user_one

    # Find the latest message for the thread
    latest_message = ChatMessage.objects.filter(thread=thread).order_by('-sent_date', '-sent_time_24').first()

    thread_info = {
        'thread_id': thread.id,
        'thread_name': thread.thread_name,
        'other_user': {
            'id': other_user.id,
            'username': other_user.username,
             'avatar':other_user.avatar,
             'is_online':other_user.is_online,
             'first_name':other_user.first_name,
             'last_name':other_user.last_name
        },
        'latest_message': {
            'sender': latest_message.sender.username if latest_message else None,
            'message': latest_message.message if latest_message else None,
            'sent_time_12': latest_message.sent_time_12 if latest_message else None,
            'sent_time_24': latest_message.sent_time_24 if latest_message else None,
            'sent_date': latest_message.sent_date if latest_message else None,
        },
    }

    return thread_info

class GroupCreationForm(forms.Form):
    avatar = forms.FileField(required=False, widget=forms.FileInput(attrs={'class': 'custom-group-avatar-input','style': 'width: 0px; height: 0px; position: absolute; right: 10000px;'}))
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'custom-form-input', 'placeholder': 'Enter Group Name', 'required': True}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'custom-form-input', 'placeholder': 'Enter Group Bio', 'rows': 4, 'required': True}))
def generate_random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

# Example usage
def find_threads(request):
    current_user = request.user
    user_threads_one = ChatThread.objects.filter(user_one=current_user)
    user_threads_two = ChatThread.objects.filter(user_two=current_user)
    user_chat_threads = user_threads_one | user_threads_two
    other_users = []
    for thread in user_chat_threads:
        if thread.user_one == current_user:
            other_users.append(thread.user_two)
        else:
            other_users.append(thread.user_one)
    return other_users

def get_user_chat_threads(user):
    user_threads_one = ChatThread.objects.filter(user_one=user)
    user_threads_two = ChatThread.objects.filter(user_two=user)
    user_chat_threads = user_threads_one | user_threads_two
    return user_chat_threads
def get_time():
    ist = pytz.timezone('Asia/Kolkata')
    current_time = datetime.now(ist).strftime("%H:%M")
    return current_time
def get_date():
    current_date = datetime.now().strftime("%Y/%m/%d")
    return current_date
def get_chat_thread(user1, user2):
    user1_id = user1.id if isinstance(user1, User) else user1['id']
    user2_id = user2.id if isinstance(user2, User) else user2['id']

    try:
        chat_thread = ChatThread.objects.get(
            Q(user_one=user1_id, user_two=user2_id) | Q(user_one=user2_id, user_two=user1_id)
        )
        return chat_thread
    except ChatThread.DoesNotExist:
        return None

def is_image(file):
    try:
        # Open the file as an image
        img = Image.open(file)

        # Check if the file is an image
        if img.format.lower() in ['jpeg', 'png', 'gif']:
            return True
        else:
            return False
    except IOError:
        # Unable to open the file as an image
        return False

def get_user(user_id):
    try:
        user = User.objects.get(id=user_id)
        return user
    except User.DoesNotExist:
        return None
def get_user_instance(user_id):
    try:
        user = User.objects.get(id=user_id)
        return user
    except User.DoesNotExist:
        print('nouser')
        return None   
def get_chat_messages(chat_thread):
    try:
        chat_messages = ChatMessage.objects.filter(thread=chat_thread)
        return chat_messages
    except ChatThread.DoesNotExist:
        return None
def search_users(searchvalue):
    users = User.objects.filter(
        Q(username__icontains=searchvalue) |
        Q(first_name__icontains=searchvalue) |
        Q(last_name__icontains=searchvalue)
    )
    return users    
# def save_chat_image(thread_name, sender, message,sent_time_12,sent_time_24,sent_date,image):
#         return ChatMessage.objects.create(thread=thread_name, sender=sender, message=message,sent_time_12=sent_time_12,sent_time_24=sent_time_24,sent_date=sent_date,image=image)

def save_chat_image(thread, sender, message, sent_time_12, sent_time_24, sent_date, uploaded_file):
    # Generate a unique file name using slugified original file name and a UUID
    # file_name = f"{slugify(uploaded_file.name.split('.')[0])}_{uuid.uuid4().hex[:8]}.{uploaded_file.name.split('.')[-1]}"

    chat_message = ChatMessage(
        thread=thread,
        sender=sender,
        message=message,  # Assuming this is the message content
        sent_time_12=sent_time_12,
        sent_time_24=sent_time_24,
        sent_date=sent_date
    )
    image_data = uploaded_file.read()
    chat_message.image.save(uploaded_file.name, ContentFile(image_data), save=True)
    chat_message.save()    
def save_chat_file(thread_name, sender, message,sent_time_12,sent_time_24,sent_date,file):
        return ChatMessage.objects.create(thread=thread_name, sender=sender, message=message,sent_time_12=sent_time_12,sent_time_24=sent_time_24,sent_date=sent_date,file=file) 
    
    
@login_required(login_url='/login') 
def chat_home(request):
    current_user=request.user
    threads = get_user_chat_threads(request.user)
    threads_info = []
    for thread in threads:
        thread_info = get_thread_info(thread, current_user)
        threads_info.append(thread_info)
    return render(request,'tickrchat/chathome.html',{'users':threads_info})

@login_required(login_url='/login') 
@xframe_options_exempt
def chat_area(request,username,id):
    receiver_user= get_user(id)
    logged_user = request.user     
    chat_thread = get_chat_thread(receiver_user,logged_user)
    chat_messages = get_chat_messages(chat_thread)
    if not receiver_user ==  None:   
     return render(request,'tickrchat/chatarea.html',{'data':receiver_user,'chatmessages':chat_messages})
@login_required(login_url='/login') 
@xframe_options_exempt
def blankchat(request):
    return render(request,'tickrchat/blankchat.html')

@csrf_exempt     
def imageupload(request, usernamereceiver, id, username, currentuserid):
    print('received')
    user1 = get_user(currentuserid)
    user2 = get_user(id)

    if user1['username'] != username:
        print('error logged error ')
    elif user2['username'] != usernamereceiver:
        print('error receiver')
    elif user1['username'] == username and user2['username'] == usernamereceiver:
        thread = get_chat_thread(user1, user2)
        current_date = get_date()
        current_time = get_time()
        sender = get_user_instance(currentuserid)
        formatted_time_12 = (datetime.now().strftime("%I:%M %p")).lstrip('0')
        if request.method == 'POST':
            uploaded_file = request.FILES['file']
            if is_image(uploaded_file):
                msg = 'image'
                save_chat_image(thread, sender, msg, formatted_time_12, current_time, current_date, uploaded_file)

    # Return a simple success message as an HttpResponse
    return HttpResponse("Image uploaded successfully")       
        

def fileupload(request,usernamereceiver,id,username,currentuserid):
    pass

def groupchat(request):
    if request.method == 'POST':
        form = GroupCreationForm(request.POST, request.FILES)
        if form.is_valid():
            group_owner = request.user
            group_avatar = request.FILES.get('avatar')
            group_name = form.cleaned_data['name']
            group_bio = form.cleaned_data['bio']
            random_string = generate_random_string(100)
            nrandom_string = generate_random_string(7)

            group_instance = GroupChatThread.objects.create(
                group_owner=group_owner,
                thread_name=group_name,
                Groupbio=group_bio,
                groupuniqueid=random_string
            )

            filename = f'{group_instance.id}{nrandom_string}_{group_avatar.name}'
            group_instance.thread_avatar.save(filename, group_avatar)
            group_instance.save()
            return redirect('groupchathome')
    else:
        form = GroupCreationForm()

    threads = find_threads(request)
    return render(request, 'tickrchat/groupchathome.html', {'form': form, 'threads': threads})

        
def groupchat_area(request):
    return render(request,'tickrchat/groupchatarea.html')

def testing(request):
    
    return render(request,'home/homepage.html')


def searchpeoplechathome(request):
    if request.method == 'POST':
        search = request.POST.get('search', '').strip()
        if search:
            try:
                users = search_users(search)
                context = {'users': users, 'value': search}
                return render(request, 'tickrchat/searchpeoplechathome.html', context)
            except Exception as e:
                print(f"An error occurred: {e}")
    
    return render(request, 'tickrchat/searchpeoplechathome.html')

def profileupdate(request):
    user = request.user
    fname = user.first_name
    lname = user.last_name
    uavatar = user.avatar
    ubio = user.bio   
    context={'firstname':fname,'lastname':lname,'avatar':uavatar,'bio':ubio}             
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        bio = request.POST['bio']
        avatar = request.FILES.get('avatarfile')
        if not firstname == '' and not lastname == '' and not bio == '' :
            user.first_name = firstname
            user.last_name = lastname
            user.bio = bio
            filename = f'avatar_{avatar.name}'
            user.avatar.save(filename,avatar)
            user.is_updated = True
            user.save()
            return redirect('chathome')
    return render(request,'tickrchat/profilesetup.html',{'context':context})

def create_payment(request,price):
    client = razorpay.Client(auth=("rzp_test_eOoH8ico3N0zef", "t8nRAA5WMPwPbB5ZmIZ3O48g"))
    price = price*100
    # Create a Razorpay order
    order_amount = 50000  # Amount in paise (100 paise = 1 rupee)
    order_currency = 'INR'
    order_receipt = 'order_rcptid_11'

    order = client.order.create({
        'amount': order_amount,
        'currency': order_currency,
        'receipt': order_receipt,
        'payment_capture': '1'  # Auto-capture payments
    })

    return render(request, 'payment.html', {'order': order})