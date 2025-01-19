# URL-Shortener
please run these commands after cloning the repo 
go to the dir URL_Shortener
  pip install -r requirements.txt
  and activate the urlenv (virtual env)
  run the project wuth the below command 
  python manage.py runserver

this project has 3 apis 
  1. POST shorten/ to create a shorten url and store that in the database
      sample url  http://127.0.0.1:8000/shorten/
      <img width="639" alt="image" src="https://github.com/user-attachments/assets/75d98c69-6125-4e6f-867d-562484faf831" />

  3. GET <shorten_url> to check if url is active a then redirect to respective url else through error

  4. GET analytics/<shorten_url> return access logs of the shorten_url urls hits with time and ips
    <img width="639" alt="image" src="https://github.com/user-attachments/assets/8492761e-710d-4792-8261-afcc5e1d19a7" />

  
