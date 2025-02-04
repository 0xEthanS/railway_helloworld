# railway_helloworld
A hello world app created with fastapi to discover how railway works




## Start Project Locally:
    - 1.) Create Virtual Environment
        - python -m venv venv
    - 2.) Activate Virtual Environment
        - source venv/bin/activate
    - 3.) Upgrade pip
        - python -m pip install --upgrade pip
    - 4.) Add ".gitignore"
        - echo "*" > venv/.gitignore
        - Contents:
            # Ignore Python virtual environment and cache
            venv/
            __pycache__/

            # Ignore environment files
            .env.local

            # Ignore Vercel deployment folder
            .vercel/

            # Allow everything else
            *
    - 5.) Instal package
        - pip install -r requirements.txt


## Start Local Server:
    - fastapi dev app/main.py