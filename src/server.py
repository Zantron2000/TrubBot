"""
Python functions to handle SQL CRUD operations for the TrubBot
database. There is currently one table:

Images Table - Keeps track of file names and the id names associated with
them. Used for saving image data and retrieving found image

Members Table - Keeps track of members in the server

"""

from discord import Role
from src.database_utils import *

def rebuild_images_table():
    """Rebuilds the Images table"""

    exec_commit("""
        DROP TABLE IF EXISTS IMAGES;
        CREATE TABLE IMAGES(
            IMAGE_ID SERIAL PRIMARY KEY,
            IMAGE_NAME VARCHAR(300) UNIQUE NOT NULL,
            IMAGE_URL VARCHAR(300) UNIQUE NOT NULL
        );
    """)

def rebuild_roles_table():
    """Rebuilds the Roles table"""

    exec_commit("""
        DROP TABLE IF EXISTS ROLES;
        CREATE TABLE ROLES(
            ROLE_ID INT PRIMARY,
            CREATE_IMAGES BOOLEAN DEFAULT 0,
            READ_IMAGES BOOLEAN DEFAULT 0,
            DELETE_IMAGES BOOLEAN DEFAULT 0
        )
    """)

def create_image(image_name: str, image_url: str):
    """Attempts to save an image into the database"""

    try:
        exec_commit("INSERT INTO IMAGES(FILE_NAME, FILE_URL) VALUES((%s), (%s))", (image_name, image_url))

        return True
    except:
        return False

def retrieve_image_url(image_name: str):
    """Attempts to retrieve an image from the database"""

    try:
        return exec_commit("SELECT IMAGE_URL FROM IMAGES WHERE IMAGE_NAME = (%s)", (image_name,))
    except:
        return None

def delete_image(image_name: str):
    """Attempts to delete an image from the database"""

    try:
        exec_commit("DELETE FROM IMAGES WHERE IMAGE_NAME = (%s)", (image_name,))

        return True
    except:
        return False

def register_role(role: Role, c_img = 0, d_img = 0, r_img = 0):
    """Attempts to register a role into the database"""

    try:
        exec_commit("INSERT INTO ROLES VALUES((%s), (%s), (%s), (%s))", (role.id, c_img, r_img, d_img))

        return True
    except:
        return False

def unregister_role(role: Role):
    """Attempts to unregister from the database"""

    try:
        exec_commit("DELETE FROM ROLES WHERE ROLE_ID = (%s)", (role.id,))

        return True
    except:
        return False

def has_delete_image_role(roles: list[Role]):
    obtain_sql = ""

    for role in roles:
        permission = exec_get_one("SELECT DELETE_IMAGES FROM ROLES WHERE ROLE_ID = (%s)", role.id)
        if(permission == True):
            return True

    return False

def has_create_image_role(roles: list[Role]):
    try: 
        obtain_sql = ""

        for role in roles:
            permission = exec_get_one("SELECT CREATE_IMAGES FROM ROLES WHERE ROLE_ID = (%s)", role.id)
            if(permission == True):
                return True

        return False
    except:
        return False

def store_image(roles: list[Role], image_name: str, image_url: str):
    try:
        if has_create_image_role(roles):
            return create_image(image_name, image_url)
        else:
            return False
    except:
        return False

def remove_image(roles: list[Role], image_name: str):
    try:
        if has_delete_image_role(roles):
            return delete_image(image_name)
        else:
            return False
    except:
        return False
