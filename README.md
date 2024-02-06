# MailKeylogger

MailKeylogger is a Python script that captures keystrokes and periodically sends them via email. It runs silently in the background, logging all keystrokes typed by the user.

---

## 🚀 Getting Started

To use MailKeylogger, follow these steps:

1. **Clone the repository**:
   ```sh
   git clone https://github.com/LeatherFire/MailKeylogger.git
   cd MailKeylogger
   ```

2. **Run the script**:
   ```sh
   python mail_keylogger.py
   ```

3. **Configure email settings**:
   Open `mail_keylogger.py` in a text editor and replace the placeholder values for `emailadress`, `paswd`, and `youremail@gmail.com` with your email address and password.

4. **Run the script in the background**:
   Run the script in the background so that it can capture keystrokes silently. You can use tools like `nohup` on Unix systems or Task Scheduler on Windows.

---

## 📧 Email Configuration

Make sure to enable less secure app access in your Gmail account settings to allow MailKeylogger to send emails. For security reasons, it's recommended to use a dedicated email account for logging keystrokes.

---

## 💡 Note

- MailKeylogger runs silently in the background and logs all keystrokes typed by the user.
- It periodically sends the captured keystrokes via email to the specified email address.
- Use this tool responsibly and only on systems that you own or have explicit permission to monitor.

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue for feedback and suggestions or submit a pull request directly.

---

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
