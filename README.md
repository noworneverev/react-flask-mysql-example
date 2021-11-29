# react-flask-mysql-example

## Backend

### 1. Install Backend dependencies

```
pip install -r requirements.txt
```

### 2. Run MySQL Create Script

```
'CREATE TABLE `users` (\n  `id` varchar(25) NOT NULL,\n  `name` varchar(100) DEFAULT NULL,\n  `email` varchar(255) DEFAULT NULL,\n  PRIMARY KEY (`id`)\n) ENGINE=InnoDB DEFAULT CHARSET=latin1'
```

### 3. Modify config.json

Rename `config.json.example` to `config.json` and modify the configuration information of your MySQL

```
{
    "USER": "root",
    "PASSWORD": "your_password",
    "DB": "covid"
}
```

### 4. Run Flask App

```
python main.py
```

## Client

### 1. Install package.json dependencies

```
npm install
```

### 2. Start React app

```
npm start
```

## Framework

- [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)
- [React Admin](https://marmelab.com/react-admin/)
