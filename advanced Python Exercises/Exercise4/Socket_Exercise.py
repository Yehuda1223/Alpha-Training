import requests
import os
import time
from functools import wraps


def timeTaken(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"⏱️ {func.__name__} took {end_time - start_time:.2f} seconds to complete")
        return result

    return wrapper


@timeTaken
def download_file(url, filename=None):
    try:
        response = requests.get(url)
        response.raise_for_status()  # בודק אם הבקשה הצליחה

        if not response.content:
            raise ValueError("❌ Error: Empty content received.")

        if filename is None:
            filename = os.path.basename(url.split("?")[0])  # חיתוך פרמטרים מיותרים

        file_path = os.path.join(os.getcwd(), filename)
        with open(file_path, "wb") as file:
            file.write(response.content)

        print(f"✅ The file is saved in: {file_path}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error downloading file: {e}")
    except ValueError as e:
        print(e)


@timeTaken
def download_all_files():
    download_file(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Matzov-unit-insignia-2020.png/330px-Matzov-unit-insignia-2020.png",
        "matzov2.png",
    )
    download_file(
        "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/logo_gmail_lockup_default_1x_rtl.png",
        "gmail.png",
    )
    download_file(
        "https://www.google.co.il/images/branding/googlelogo/2x/googlelogo_color_160x56dp.png",
        "google.png",
    )
    download_file(
        "https://www.meshek-milman.co.il/wp-content/uploads/2018/11/1200px-Intel-logo.svg_.png",
        "intel.png",
    )


def main():
    print("Hello")
    download_all_files()


if __name__ == "__main__":
    main()
