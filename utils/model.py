from pydantic import BaseModel, Field
from typing import Optional, Union


class Login(BaseModel):
    account: str
    password: str
    accountRemember: str
    captchaToken: Optional[str]
    # csessionid: str = Field(None,description='session')
    csessionid: Union[None, str] = Field(None, description='session')
    sig: None
    verifyCode: None
    system: str = Field(None, min_length=1, max_length=100, description='系统')
    resellerCode: None

