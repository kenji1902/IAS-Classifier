# IAS CLASSIFIER (django)

**A mobile web application for classifying invasive alien species plants**

**Install the Requirements and Run**

1. Install Python (3.9.13)

   ```
   https://www.python.org/downloads/release/python-3913/
   ```
2. Clone the Repository to your desktop or download it

   ```
   https://github.com/kenji1902/IAS-Classifier
   ```
3. Create a virtual environment

   ```
   python -m venv .venv
   ```
4. go to venv

   ```
   .venv/Scripts/activate.ps1
   Set-ExecutionPolicy Unrestricted (in admin powershell if '.venv/Scripts/activate.ps1' does not work)
   ```
5. Install the requirements

   ```
   pip install -r requirements.txt 
   ```
6. Install u2net Model

   - inside "classifier/u2net_BG_Remove/saved_models/u2net/" download the model below and move the file "u2net.pth" in the folder

   ```
   https://drive.google.com/u/0/uc?id=1ao1ovG1Qtx4b7EoskHXmi2E9rp5CHLcZ&export=download
   ```
7. Run the main Script

   ```
   python manage.py runserver 8080
   or
   python manage.py runserver_plus iphere:8080 --cert-file cert.pem --key-file key.pem
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
