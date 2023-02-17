from fastapi import FastAPI, Request, Form, status, Depends
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from .models import Base, Task
from .database import SessionLocal, engine
Base.metadata.create_all(bind=engine)

app = FastAPI()


# DEFINE TEMPLATE AND STATIC DIRECTORIES:
templates = Jinja2Templates(directory="sql_app/templates")
app.mount("/static", StaticFiles(directory="sql_app/static"), name="static")


# DEPENDENCY
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# DEFINE START-UP EVENT IF DATABASE IS EMPTY:
@app.on_event("startup")
def startup_populate_db():
    db = SessionLocal()
    task_quantity = db.query(Task).count()
    if task_quantity == 0:
        tasks = [
            {"title": "Learn Flask Framework"},
            {"title": "Learn Django Framework"},
            {"title": "Learn FastAPI Framework"},
            {"title": "Learn MongoDB Framework"}
        ]
        for task in tasks:
            db.add(Task(**task))
        db.commit()
    else:
        pass


# READ OPERATION
@app.get("/")
def home_page(request: Request, db: Session = Depends(get_db)):
    all_tasks = db.query(Task).all()
    return templates.TemplateResponse("index.html", {
        "request": request,
        "tasks": all_tasks
    })


# ADD OPERATION
@app.post("/")
def add_new_task(
    request: Request, 
    new_task: str = Form(...),
    db: Session = Depends(get_db)
):
    
    control = db.query(Task).filter_by(title=new_task).first()
    if control is None:
        task = Task(title=new_task)
        db.add(task)
        db.commit()
        db.refresh(task)
    else:
        pass
    
    dynamic_url = app.url_path_for("home_page")
    return RedirectResponse(url=f"{dynamic_url}", status_code=status.HTTP_303_SEE_OTHER)


# DELETE OPERATION
@app.get("/{task_id}")
def delete_task(request: Request, task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter_by(id=task_id).first()
    db.delete(task)
    db.commit()
    dynamic_url = app.url_path_for("home_page")
    return RedirectResponse(url=f"{dynamic_url}", status_code=status.HTTP_303_SEE_OTHER)


# UPDATE OPERATION
@app.post("/{task_id}")
def update_task(
    request: Request, 
    task_id: int, 
    update_input: str = Form(...),
    db: Session = Depends(get_db)
):
    task = db.query(Task).filter_by(id=task_id).first()
    task.title = update_input
    db.commit()
    dynamic_url = app.url_path_for("home_page")
    return RedirectResponse(url=f"{dynamic_url}", status_code=status.HTTP_303_SEE_OTHER)
