# 🔐 Guía: Configurar GitHub con SSH

Esta guía explica cómo configurar SSH para conectarte a GitHub desde tu equipo de forma segura y sin tener que ingresar usuario y contraseña en cada proyecto.

---

## ✅ ¿Por qué usar SSH?

- Evita ingresar usuario/token cada vez que haces `git push`
- Es más seguro que usar HTTPS con contraseña
- Se configura **una sola vez por equipo**

---

## 🧰 1. Verificar si ya tienes una clave SSH

```bash
ls ~/.ssh
```

Si ves `id_rsa` o `id_ed25519`, probablemente ya tienes una clave.

---

## 🛠️ 2. Crear una nueva clave SSH (si no existe)

```bash
ssh-keygen -t ed25519 -C "tu_correo@ejemplo.com"
```

Presiona Enter para aceptar la ruta por defecto y no usar passphrase (opcional).

---

## 🚀 3. Agregar la clave al agente SSH

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

---

## 📋 4. Copiar la clave pública al portapapeles

Linux/macOS:

```bash
cat ~/.ssh/id_ed25519.pub | pbcopy
```

Windows (Git Bash):

```bash
clip < ~/.ssh/id_ed25519.pub
```

---

## 🌐 5. Agregar la clave pública a GitHub

1. Ve a: [https://github.com/settings/keys](https://github.com/settings/keys)
2. Clic en "New SSH Key."
3. Pega la clave
4. Guarda

---

## 🔁 6. Usar SSH en tus proyectos

Por cada proyecto, ejecuta:

```bash
git remote set-url origin git@github.com:TU_USUARIO/nombre-del-repo.git
```

Ejemplo:

```bash
git remote set-url origin git@github.com:jonathantejo/procurement-pipeline.git
```

---

## 🔂 ¿Hay que configurarlo en cada proyecto?

- NO. Solo agregas la clave una vez por equipo.
- En cada nuevo proyecto solo apuntas a GitHub por SSH con `git remote set-url`.

---

## ✅ Verifica que funciona

```bash
git remote -v
git push
```

No debería pedirte ni usuario ni contraseña.

---
