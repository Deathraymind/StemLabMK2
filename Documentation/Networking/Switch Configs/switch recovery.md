

---

# Cisco Switch Recovery Procedure

Recovering a Cisco switch involves accessing the recovery system, which differs from a router's recovery system known as ROMMON. Follow the steps below to recover a Cisco switch.

## Entering Switch Recovery Mode

1. **Locate the Mode Button**: At the front of the switch, find the mode button.
2. **Hold Mode Button While Booting**: Hold down the mode button while booting the switch.
3. **Console into the Device**: Ensure you are consoled into the device using the following configurations:

    ```
    Consoling settings:
    - Baud rate: 9600
    ```

4. **Boot into System with Switch Option**: Upon booting, you will enter a system with a switch option.

## Switch Recovery Commands

Execute the following commands after booting into the system with the switch option:

```bash
flash_init
del flash:config.text
del flash:vlan.dat
boot
```

## Adjusting Baud Rate

1. **Pay Attention During Boot**: While the device boots, pay attention to the baud rate option.
2. **Set Baud Rate to 57600**: If necessary, change the baud rate to 57600 for decipherable text.
3. **Revert to Standard Baud Rate (9600)**: Once you have confirmed decipherable text, set the baud rate back to 9600. Use the following commands:

    ```bash
    enable
    write erase
    erase startup-config
    reload
    ```

4. **Verify Baud Rate**: Ensure that the baud rate has been set to 9600. If not, unplug and plug the switch back in.

## Uploading IOS Image via Xmodem

If the switch IOS is broken, follow these steps to upload the IOS image via Xmodem through serial:

1. **Enter Recovery Mode**: Hold the mode button during boot.
2. **Run Command**: Execute the following command:

    ```
    copy xmodem: flash:<filename>
    ```

    Replace `<filename>` with the actual name of the IOS image file (e.g., `c2960-lanbasek9-mz.150-2.SE11.bin`).

3. **Initiate Xmodem Transfer**: Follow the prompts to initiate the Xmodem transfer. In Minicom, press `Ctrl + A` then `S` to select the file to upload. This process may take several hours.

---
