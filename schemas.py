from pydantic import BaseModel

#? ### Description ###
#? File contains schemas for data validation

class hash_object(BaseModel):
    string_value: str
    salt_value: str | None = None


class rnd_gen_object(BaseModel):
    rnd_value: int | str
    min_int_value: int | None = None
    max_int_value: int | None = None
    length_value: int | None = None


class enc_dec_object(BaseModel):
    string_value: str