
import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from faker import Faker
from bs4 import BeautifulSoup
import lxml
import sympy as sp
import seaborn as sns


print("Лабораторна робота 5: тестування бібліотек\n")


# ------------------ TRY #1: requests ------------------
try:
    response = requests.get("https://api.github.com")
    print("Requests OK:", response.status_code)
except Exception as e:
    print("Requests ERROR:", e)


# ------------------ TRY #2: numpy ------------------
try:
    arr = np.array([1, 2, 3])
    print("NumPy OK:", arr * 10)
except Exception as e:
    print("NumPy ERROR:", e)


# ------------------ TRY #3: pandas ------------------
try:
    df = pd.DataFrame({
        "Name": ["Pasha", "Oleh", "Ira"],
        "Age": [18, 22, 19]
    })
    print("Pandas OK:\n", df)
except Exception as e:
    print("Pandas ERROR:", e)


# ------------------ TRY #4: matplotlib ------------------
try:
    plt.plot([1, 2, 3], [4, 1, 7])
    plt.title("Test Plot")
    plt.close()   # щоб не відкривало вікно
    print("Matplotlib OK")
except Exception as e:
    print("Matplotlib ERROR:", e)


# ------------------ TRY #5: Pillow ------------------
try:
    img = Image.new("RGB", (50, 50), color="blue")
    print("Pillow OK: image size =", img.size)
except Exception as e:
    print("Pillow ERROR:", e)
