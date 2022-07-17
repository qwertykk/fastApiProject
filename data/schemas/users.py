from pydantic import (
    BaseModel,
    Field
)
from sqlalchemy.ext import hybrid

from data.enums.schema_examples import Schema1


class Method1(BaseModel):
    """The accepted post model for the edit user profile endpoint"""

    field1: str = Field(
        None,
        title="The new first_name to change our profile to",
        example="elon"
    )
    field2: str = Field(
        None,
        title="The new last_name to change our profile to",
        example="musk"
    )
    field3: str = Field(
        None,
        title="The new username to change our profile to",
        example="teamgoodpods"
    )
    field4: str = Field(
        None,
        title="The new website to change our profile to",
        example="https://www.website.com"
    )
    field5: str = Field(
        None,
        title="The new bio to change our profile to",
        example="This is a short new bio for this user"
    )
    field6: str = Field(
        None,
        title="The new mobile number to change our profile to",
        example="0444444444"
    )
    field7: bool = Field(
        None,
        title="Change the profile image to default",
        example=True
    )
    field8: Schema1 = Field(
        None,
        title="The user type of the listener. Can only be listener, podcaster",
        example=Schema1.example1
    )
    field9: str = Field(
        None,
        title="The user's facebook id obtained by the fe from fb's api",
        example="fdvdvdfvfdvfdfdv"
    )
    field10: str = Field(
        None,
        title="The user twitter id obtained by the fe when loggining in on twitter",
        example="fdvdvdfvfdvfdfdv"
    )


class Method2(BaseModel):
    """The accepted post model for the edit user profile endpoint"""

    field1: str = Field(
        None,
        title="The new first_name to change our profile to",
        example="elon"
    )
    field2: str = Field(
        None,
        title="The new last_name to change our profile to",
        example="musk"
    )
    field3: str = Field(
        None,
        title="The new username to change our profile to",
        example="teamgoodpods"
    )
    field4: str = Field(
        None,
        title="The new website to change our profile to",
        example="https://www.website.com"
    )
    field5: str = Field(
        None,
        title="The new bio to change our profile to",
        example="This is a short new bio for this user"
    )
