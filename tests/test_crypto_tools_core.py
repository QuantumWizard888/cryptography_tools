import pytest
from crypto_tools_core import hash_generate_SHA256, hash_generate_SHA512, hash_generate_argon2, base64_encode, base64_decode

#? ### Description ###
#? Unit tests

test_string = "This is some Magic!"
test_base64_encoded_string = "VGhpcyBpcyBzb21lIE1hZ2ljIQ=="
test_string_sha256_hash = "3784c6841b178df23210f1444675635c490c1c9f91c40cb4a6d13e3b8a7f9031"
test_string_sha512_hash = "f099cb59038c856c7a71ff94082ba39dff9e2c585bb55e607576e653355a7d07a4211f14b393da7264600e645174bb5a12127c2c2590f14c98b946d4d563bc80"
test_string_argon2_hash_salt = "_ASkc9df8s*^"
test_string_argon2_hash = "$argon2id$v=19$m=65536,t=3,p=4$X0FTa2M5ZGY4cype$Pal2WrHip7O20iqeLy5H4K+B0wU8V01lBYW9PRO1V/g"

@pytest.mark.asyncio
async def test_hash_generate_SHA256():
    assert await hash_generate_SHA256(test_string) == test_string_sha256_hash


@pytest.mark.asyncio
async def test_hash_generate_SHA512():
    assert await hash_generate_SHA512(test_string) == test_string_sha512_hash


@pytest.mark.asyncio
async def test_hash_generate_argon2():
    assert await hash_generate_argon2(test_string, test_string_argon2_hash_salt) == test_string_argon2_hash


@pytest.mark.asyncio
async def test_base64_encode():
    assert await base64_encode(test_string) == test_base64_encoded_string


@pytest.mark.asyncio
async def test_base64_decode():
    assert await base64_decode(test_base64_encoded_string) == test_string