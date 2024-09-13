from pydantic import BaseModel, EmailStr

class UserInstruction(BaseModel):
    user_instruction: str