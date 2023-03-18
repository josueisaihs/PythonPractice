import os

def environ(filename=".env"):
    """Reads the .env file and returns a dictionary of the environment variables"""
    with open(os.path.join(os.path.dirname(__file__), filename), "r") as f:
        env = {}
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            k, v = line.split('=', 1)
            env[k] = str(v).replace('"', '')
        return env