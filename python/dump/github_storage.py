import requests

GITHUB_TOKEN = "You TOKEN"  # Replace with your GitHub token
GIST_ID = "GIST_ID Last part of git URL"  # Replace with your actual Gist ID


def update_gist(gist_id, file_name, new_content):
    url = f"https://api.github.com/gists/{gist_id}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
    }
    print(url)
    data = {"files": {file_name: {"content": new_content}}}
    print(data)
    response = requests.patch(url, headers=headers, json=data)
    print(response)
    # if response.status_code == 200:
    #     print("Gist updated successfully!")
    # else:
    #     print("Failed to update Gist:", response.json())


# Example usage
update_gist(
    f"{GIST_ID}", "data.csv", "name,email\nJane Doe,jane@example.com"
)  # Replace with actual Gist ID


def read_gist(gist_id):
    url = f"https://api.github.com/gists/{gist_id}"
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    print(url)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        gist_data = response.json()
        print(gist_data["files"]["data.csv"].get("content"))
    else:
        print("Failed to read Gist:", response.json())


# Example usage
read_gist(GIST_ID)

