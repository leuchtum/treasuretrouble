import pydantic


class BaseSchema(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid", from_attributes=True)
