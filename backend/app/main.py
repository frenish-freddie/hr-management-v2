from fastapi import FastAPI
from app.database import engine
from app import models
from app.auth import router as auth_router
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas
from fastapi.middleware.cors import CORSMiddleware



models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Employee Login System")


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",   # React
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],  # GET, POST, PUT, DELETE
    allow_headers=["*"],
)


app.include_router(auth_router, prefix="/auth")

@app.get("/")
def home():
    return {"status": "Backend is running"}


@app.post("/jobs", response_model=schemas.JobResponse)
def create_job(job: schemas.JobCreate, db: Session = Depends(get_db)):
    new_job = models.Job(
        job_title=job.job_title,
        job_description=job.job_description,
        expected_close_date=job.expected_close_date,
        budget=job.budget,
        emp_id=job.emp_id
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job


@app.get("/jobs", response_model=list[schemas.JobResponse])
def get_jobs(db: Session = Depends(get_db)):
    jobs = db.query(models.Job).all()
    return jobs
