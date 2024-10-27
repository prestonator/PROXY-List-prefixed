import requests
import os
import sys


def test_source_repo():
    """Test connection to source repository"""
    url = "https://api.github.com/repos/TheSpeedX/PROXY-List"
    response = requests.get(url)

    if response.status_code == 200:
        print("✅ Successfully connected to source repository")
        return True
    else:
        print("❌ Failed to connect to source repository")
        print(f"Status code: {response.status_code}")
        print(f"Response: {response.text}")
        return False


def test_proxy_files():
    """Test access to proxy files"""
    base_url = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master"
    files = ["http.txt", "socks4.txt", "socks5.txt"]

    success = True
    for file in files:
        url = f"{base_url}/{file}"
        response = requests.get(url)

        if response.status_code == 200:
            print(f"✅ Successfully accessed {file}")
            print(f"Sample content: {response.text[:100]}...")
        else:
            print(f"❌ Failed to access {file}")
            print(f"Status code: {response.status_code}")
            success = False

    return success


if __name__ == "__main__":
    print("Testing repository connections...")
    repo_success = test_source_repo()
    print("\nTesting proxy files access...")
    files_success = test_proxy_files()

    if not repo_success or not files_success:
        sys.exit(1)
