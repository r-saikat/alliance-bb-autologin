# alliance-bb-autologin
This contains a python script which may be used to login to alliance broadband automatically.

## Usage
1. Make sure that `Python 3` and `pip` are available on your system.
2. Install the required Python packages by the command:
    ```bash
    pip install -r requirements.txt
    ```
3. Edit your login credentials and gateway IP in lines 1, 2 and 3 of `autologin.py`. Then you can run the program using
   ```bash
   python3 autologin.py
   ```

## Cronjob
If required, you may also configure your linux - based router, raspberry pi, etc. to run this script at startup by configuring cron jobs, so that you don't need to execute the code everytime you switch on your router.
