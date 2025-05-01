from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.habit_log import HabitLog
from app.schemas.habit_log_schema import HabitLogCreate, HabitLogUpdate, HabitLogResponse
from app.auth.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/habit-logs", tags=["Habit Logs"])


@router.post("/", response_model=HabitLogResponse)
def create_habit_log(
    log: HabitLogCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # проверим, что привычка принадлежит этому юзеру
    habit = db.query(User).filter(User.user_id == current_user.user_id).join(User.habits).filter_by(habit_id=log.habit_id).first()
    if not habit:
        raise HTTPException(status_code=403, detail="Нет доступа к привычке")

    new_log = HabitLog(**log.dict())
    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    return new_log


@router.get("/", response_model=list[HabitLogResponse])
def get_logs(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(HabitLog).join(HabitLog.habit).filter(HabitLog.habit.has(user_id=current_user.user_id)).all()


@router.put("/{log_id}", response_model=HabitLogResponse)
def update_log(
    log_id: int,
    log_update: HabitLogUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    log = db.query(HabitLog).filter(HabitLog.habit_log_id == log_id).join(HabitLog.habit).filter(HabitLog.habit.has(user_id=current_user.user_id)).first()
    if not log:
        raise HTTPException(status_code=404, detail="Лог не найден или нет доступа")

    for key, value in log_update.dict(exclude_unset=True).items():
        setattr(log, key, value)

    db.commit()
    db.refresh(log)
    return log


@router.delete("/{log_id}", status_code=204)
def delete_log(
    log_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    log = db.query(HabitLog).filter(HabitLog.habit_log_id == log_id).join(HabitLog.habit).filter(HabitLog.habit.has(user_id=current_user.user_id)).first()
    if not log:
        raise HTTPException(status_code=404, detail="Лог не найден или нет доступа")

    db.delete(log)
    db.commit()
