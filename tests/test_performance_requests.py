import asyncio
import httpx
from time import perf_counter

#* test_performance_requests.py
#? File contains tests for undestanding the application performance (kind of) under different load

# <--- TEST INPUT DATA
test_string = "This is some Magic!" # Test string for , well, you, know, tests
test_base64_encoded_string = "VGhpcyBpcyBzb21lIE1hZ2ljIQ==" # base64 encoded test_string
test_string_argon2_hash_salt = "_ASkc9df8s*^" # Salt parameter for Argon2 hash generation
test_length = 1000 # Text Length for random string generation
# ---
url_sha256 = "http://127.0.0.1:8000/api/hashes/sha256"
payload_sha256 = {"string_value": test_string}
# ---
url_sha512 = "http://127.0.0.1:8000/api/hashes/sha512"
payload_sha512 = {"string_value": test_string}
# ---
url_argon2 = "http://127.0.0.1:8000/api/hashes/argon2"
payload_argon2 = {"string_value": test_string, "salt_value": test_string_argon2_hash_salt}
# ---
url_rnd_str_gen_string = "http://127.0.0.1:8000/api/random_generators/random_string"
payload_rnd_str_gen_string = {"rnd_value": 0, "length_value": test_length}
# ---
requests_count = 1000 # Number of requests
# ---
timeout = httpx.Timeout(10.0, read=None)
# --->


async def test_request(test_type: int):
    
    # SHA256
    if test_type == 1:
        async with httpx.AsyncClient() as client:
            response = await client.post(url_sha256, json=payload_sha256, timeout=timeout)
            #print(response.text)
    
    # SHA512
    elif test_type == 2:
        async with httpx.AsyncClient() as client:
            response = await client.post(url_sha512, json=payload_sha512, timeout=timeout)
            #print(response.text)
    
    # Argon2
    elif test_type == 3:
        async with httpx.AsyncClient() as client:
            response = await client.post(url_argon2, json=payload_argon2, timeout=timeout)
            #print(response.text)
    
    # Random string generation
    elif test_type == 4:
        async with httpx.AsyncClient() as client:
            response = await client.post(url_rnd_str_gen_string, json=payload_rnd_str_gen_string, timeout=timeout)
            #print(response.text)


async def main():
    time_start = perf_counter()
    tasks = [test_request(1) for _ in range(requests_count)] # (1) is running test requests for SHA256 hash generation
    await asyncio.tasks.gather(*tasks)
    time_end = perf_counter()
    print(f"[TIME OF EXECUTION]: {time_end - time_start} seconds")


if __name__ == "__main__":
    asyncio.run(main())