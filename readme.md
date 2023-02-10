# LinkHub

LinkHub is a web application built using Flask framework to help students in their college who are not allowed to use phones but have access to computers. The application is designed to provide a platform for students to share links with each other, without the need for their phones.

# Features

- User authentication and registration
  Adding, viewing and deleting links
- Sharing links with other users
- A user-friendly interface

# Technologies Used

- Flask - A micro web framework written in Python
- SQLite - An open-source relational database management system
- HTML, CSS, and JavaScript - For building the front-end of the application

# Deployment

LinkHub is deployed on the cloud, so it can be accessed from anywhere with an internet connection.

```
https://salmansyyd.pythonanywhere.com
```

# Getting Started

To use LinkHub, follow the steps below:

Clone the repository:

```
$ git clone https://github.com/sayyed-salman/LinkHub.git
```

Change into the LinkHub directory:

```
$ cd LinkHub
```

Install the required packages:

```
$ pip install -r requirements.txt
```

Set up the database:

```
from link_hub import db
db.create_all()
exit()
```

Run the application:

```
$ flask run
```

The application will be running at http://localhost:5000/. You can now start sharing links with other users.

# Contribution

LinkHub is open-source and contributions are welcome. If you would like to contribute, please follow the steps below:

- Fork the repository
- Create a new branch for your contribution
- Make your changes
- Test your changes thoroughly
- Submit a pull request

# License

<img alt="GitHub" src="https://img.shields.io/github/license/sayyed-salman/LInkHub">

LinkHub is licensed under the MIT License.
