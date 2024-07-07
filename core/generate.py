from config import CoreConfig
from model_generator import generate_sqlmodels


if __name__ == '__main__':    
    generate_sqlmodels(db_url=CoreConfig.DATABASE_URL, file_name=CoreConfig.MODEL_GEN_FILE)

