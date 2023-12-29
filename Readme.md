Tickr - Realtime Chatting Application Overview Tickr is a real-time chatting application built using Django, Django Channels, WebSocket, and MySQL database. The application leverages the power of Django Channels to enable WebSocket communication, providing users with a seamless and interactive chatting experience.

Features Real-time chat: Enjoy instant messaging with other users in real-time. User authentication: Securely log in and authenticate users. Message history: Access and view your chat history. MySQL Database: Store and retrieve chat data efficiently using MySQL. Django Channels and WebSocket: Enable bidirectional communication for real-time updates. Redis Server: Utilize Redis for managing WebSocket connections and scaling the application. Prerequisites Make sure you have the following installed:

Python 3.12 Django 5.0 Django Channels 3.0.5 MySQL Database Redis Server Installation Clone the repository:

git clone github.com/ADITYA-CYBERGENESIS/Tickr---real-time-chating-webapplication.git Install dependencies: pip install -r requirements.txt Configure MySQL settings:

Update the DATABASES configuration in settings.py with your MySQL credentials.

Configure Redis settings:

Update the CHANNEL_LAYERS configuration in settings.py with your Redis server details.

Apply migrations: python manage.py migrate Run the development server: python manage.py runserver The application will be accessible at http://localhost:8000.

Usage Create a new account or log in. Access the chat interface to start real-time conversations. Enjoy the seamless chatting experience with other users. Contributions Contributions are welcome! Feel free to open issues or submit pull requests to improve the application.

License This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments Special thanks to the Django, Django Channels, WebSocket, MySQL, and Redis communities for their excellent tools and documentation. Happy chatting with Tickr! 🚀