# Predictions AI

This is a simple project to predict:
- A yield of a crops  basing on Nutrients and conditions provided.
- If basing on certain factors one has Malaria

## Getting Started

### 1. Create a virtual environment (Optional on windows)
```
$ python3 -m venv venv   #(If you have python version 3.11*, replace python3 with python3.11)
# Activate the virtual environment
$ source venv/bin/activate
```




### 2. Install dependencies
```
pip3 install -r requirements.txt
```
(To view more about tailwind integration, visit this [document](https://django-tailwind.readthedocs.io/en/latest/installation.html))

### 3. How to Run the project
```
 python3 manage.py runserver
```

### 4. After Running the project

| URL   |      Project      |  Note |
|----------|:-------------:|------:|
| http://127.0.0.1:8000/ |  Crops Yield Prediction | Predicts what basing on a number of given factors will be the crops yield |
| http://127.0.0.1:8000/malaria/ |    Malaria Prediction    |   Predicts if on a given factors an accurate prediction of a malaria infection is present |
| http://127.0.0.1:8000/irembo-com/ | redesign of irembo.com  |  A redesign using DJANGO |

### Contributors
[IRADUKUNDA Allelua Fiacre](https://github.com/irfiacre)

#### Feel free to contribute as well ^^'
