import os

folders = ["tests", "pages", "api_tests", "utils", "reports", "config"]
files = {
    "tests": ["test_login.py", "test_cart.py", "test_checkout.py"],
    "pages": ["login_page.py", "product_page.py", "cart_page.py"],
    "api_tests": ["test_auth_api.py", "test_product_api.py"],
    "utils": ["config.py", "data_reader.py", "logger.py"],
    "config": ["config.json"]
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for folder, file_list in files.items():
    for file in file_list:
        open(os.path.join(folder, file), 'w').close()

print("✅ Folder structure created successfully!")
