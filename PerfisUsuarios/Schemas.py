from pydantic import BaseModel


class UserProfileCreate(BaseModel):

    user_id : int
    main_usage : str
    priorities : list[str]
    tech_profile : str
    budget : str
    pain_point : str