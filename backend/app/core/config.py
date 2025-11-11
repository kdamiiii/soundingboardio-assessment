from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "SoundingboardIO"
    DATABASE_URL: str = "sqlite:///./app.db"
    DEBUG: bool = True
    
    SECRET_KEY:str = "secrete_key_for_jwt_token_generation"
    ALGORITHM:str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES:int = 100

    class Config:
        env_file = ".env"

settings = Settings()