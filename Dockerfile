FROM python:3.9-slim

# Install system dependencies for Tkinter
RUN apt-get update && apt-get install -y \
    python3-tk \
    tk-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

# Ensure DISPLAY variable is passed at runtime for GUI
ENV DISPLAY=${DISPLAY}

CMD ["python", "Human_AI_Teaming_Starter_Pack/Python_App/main_app.py"]
