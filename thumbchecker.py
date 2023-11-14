# phpthumb_version_checker.py
# Written by Uruskan
# Date: 14/11/23

# This script is used to check the PHPThumb version used on a specific website.

import requests
from requests.exceptions import Timeout

def get_phpthumb_version(full_domain):
    # Construct the URL
    url = f"https://www.{full_domain}/include/3rdparty/PHPThumb/phpThumb.php?src="
    try:
        # Send an HTTP GET request and receive a response within 7 seconds
        response = requests.get(url, timeout=7)
        if response.status_code == 200:
            return response.text.strip()
        else:
            return f"Error: {response.status_code} - {response.reason}"
    except Timeout:
        # Return an error message if the request times out
        return "Error: Request timed out (7 seconds)"
    except requests.RequestException as e:
        # Return a general error message for other exceptions
        return f"Error: {e}"

def main():
    results = []

    while True:
        # Get the full domain from the user
        full_domain = input("Enter the full domain (e.g., example.com): ")

        if not full_domain:
            break

        version = get_phpthumb_version(full_domain)
        results.append(f"{full_domain}: {version}")

        # Display the phpThumb version to the user
        print("\nphpThumb version:")
        print(version)
        print("\n---\n")

    output_file = "phpthumb_versions.txt"
    with open(output_file, "w") as file:
        # Write the results to a file
        file.write("\n".join(results))

    # Results saved to the file
    print(f"\nResults saved to {output_file}")

if __name__ == "__main__":
    main()
