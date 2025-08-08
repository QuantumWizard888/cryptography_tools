import uvicorn
from crypto_tools_core import *
from fastapi import FastAPI, HTTPException
from schemas import hash_object, rnd_gen_object, enc_dec_object
from summary_routes import summary_dict

#* main.py
#? Main file that runs the application

app = FastAPI(
    title="CRYPTOGRAPHY TOOLS",
    description="API tools for hash generation and cryptography"
    )


# <--- HASHES
@app.post(
        "/api/hashes/sha256",
        tags=["Hashes"],
        summary=summary_dict["sha256"]
        )
async def post_hash_generate_SHA256_route(input_request: hash_object):
    hash_object_response = hash_object(string_value = await hash_generate_SHA256(input_str=input_request.string_value))

    return hash_object_response


@app.post(
        "/api/hashes/sha512",
        tags=["Hashes"],
        summary=summary_dict["sha512"]
        )
async def post_hash_generate_SHA512_route(input_request: hash_object):
    hash_object_response = hash_object(string_value = await hash_generate_SHA512(input_str=input_request.string_value))

    return hash_object_response


@app.post(
        "/api/hashes/argon2",
        tags=["Hashes"],
        summary=summary_dict["argon2"]
        )
async def post_hash_generate_argon2_route(input_request: hash_object):
    if len(input_request.salt_value) < 8:
        raise HTTPException(status_code=400, detail="Salt must be >= 8")
    hash_object_response = hash_object(string_value = await hash_generate_argon2(input_str=input_request.string_value, input_salt=input_request.salt_value))

    return hash_object_response
# --->


# <--- RANDOM DATA GENERATION
@app.post(
        "/api/random_generators/random_int_number",
        tags=["Random generators"],
        summary=summary_dict["rnd_int"]
        )
async def post_random_int_number_generate_route(input_request: rnd_gen_object):
    rnd_gen_object_response = rnd_gen_object(rnd_value = await random_int_number_generate(min_int=input_request.min_int_value, max_int=input_request.max_int_value))

    return rnd_gen_object_response


@app.post(
        "/api/random_generators/random_string",
        tags=["Random generators"],
        summary=summary_dict["rnd_str"]
        )
async def post_random_string_generate_route(input_request: rnd_gen_object):
    rnd_gen_object_response = rnd_gen_object(rnd_value = await random_string_generate(length=input_request.length_value))

    return rnd_gen_object_response
# --->


# <--- ENCODING/DECODING
@app.post(
        "/api/encoders_decoders/base64_encode",
        tags=["Encoding/Decoding"],
        summary=summary_dict["base64_enc"]
        )
async def post_base64_encode_route(input_request: enc_dec_object):
    enc_dec_object_response = enc_dec_object(string_value = await base64_encode(input_str=input_request.string_value))

    return enc_dec_object_response


@app.post(
        "/api/encoders_decoders/base64_decode",
        tags=["Encoding/Decoding"],
        summary=summary_dict["base64_dec"]
        )
async def post_base64_decode_route(input_request: enc_dec_object):
    enc_dec_object_response = enc_dec_object(string_value = await base64_decode(input_str=input_request.string_value))

    return enc_dec_object_response
# --->

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)