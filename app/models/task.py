from app import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    completed_at = db.Column(db.DateTime, default=None)
    goal_id = db.Column(db.Integer, db.ForeignKey('goal.goal_id'), nullable=True)

    def to_dict(self):
        task_dict = {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "is_complete": (self.completed_at!=None)
        }
        if self.goal_id:
            task_dict["goal_id"] = self.goal_id
        return task_dict
    

    @classmethod
    def from_dict(cls, task_details):
        new_task = cls(
            title=task_details["title"],
            description=task_details["description"]
        )
        return new_task
