from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker

# conexão local - MySQL
# engine = create_engine("mysql+mysqldb://root:@localhost:3306/maternidade")

# conexão supabase - PostgreSQL
engine = create_engine("postgresql://postgres.qciapfqtidaykoapeiqt:passwordToDatabase@@aws-0-sa-east-1.pooler.supabase.com:6543/postgres")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  
Base = declarative_base()

def get_db():     
    db = SessionLocal()     
    try:         
        yield db     
    finally:
        db.close()
