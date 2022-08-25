# IAS CLASSIFIER (django)

**A mobile web application for classifying invasive alien species plants**


**Install the Requirements and Run**

1. Install Python

   ```
   https://www.python.org/downloads/release/python-3910/
   ```
2. Clone the Repository to your desktop or download it

   ```
   https://github.com/kenji1902/AutoJoinZoom.git
   ```
3. Create a virtual environment

   ```
   python -m venv .venv
   ```
4. go to venv

   ```
   .venv/Scripts/activate.ps1
   ```
5. Install the requirements

   ```
   pip install requirements.txt 
   ```
6. Run the main Script

   ```
   python manage.py runserver 8080
   ```

**Run pktriot - "localhost to web"**
1. configure pktriot (if not configured)
    ```
    pktriot.exe configure
    ```
    [enter email and pass, select server]
2. copy domain name (hostname) and insert in this command
    ```
    pktriot.exe tunnel http add --domain "domain name here w/o quote" --destination localhost --http 8080 --letsencrypt
    ```
3. runserver
    ```
    pktriot.exe start
    ```
```

░░░░░░███████ ]▄▄▄▄▄▄▄▄▃
▂▄▅█████████▅▄▃▂
I███████████████████].
◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤…
```
