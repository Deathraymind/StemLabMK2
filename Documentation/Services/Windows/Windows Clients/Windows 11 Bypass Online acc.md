
---

# How to Install Windows 11 Without a Microsoft Account

This guide provides a simple trick to set up a local account during the installation of Windows 11, bypassing the requirement for a Microsoft account. This method works whether you're doing a clean install or setting up a store-bought computer.

## Step-by-Step Instructions

### Step 1: Start Windows 11 Installation

1. **Begin the Installation Process**:
   - Follow the Windows 11 installation process until you reach the "Choose a country" screen.

   ![Choose a country](image_url)

### Step 2: Open Command Prompt

1. **Open Command Prompt**:
   - Press `Shift + F10` to open a Command Prompt window.

   ![Launch command prompt](image_url)

### Step 3: Bypass Internet Requirement

1. **Enter Bypass Command**:
   - Type `OOBE\BYPASSNRO` and press Enter to disable the Internet connection requirement.

   ![OOBE\BYPASSNRO](image_url)

2. **Reboot**:
   - The computer will reboot and return you to the "Choose a country" screen.

### Step 4: Disable Internet Connection

1. **Open Command Prompt Again**:
   - Press `Shift + F10` again to reopen the Command Prompt.

2. **Release IP Configuration**:
   - Type `ipconfig /release` and press Enter to disable the Internet connection.

   ![ipconfig release](image_url)

3. **Close Command Prompt**:
   - Close the Command Prompt window by typing `exit` or clicking the close button.

### Step 5: Continue Installation

1. **Choose Country and Region**:
   - Continue with the installation by selecting your country, region, and keyboard layout options.

   ![Choose region and keyboard](image_url)

### Step 6: Bypass Network Connection

1. **Skip Network Connection**:
   - When the "Let's connect you to a network" screen appears, click on "I don't have Internet".

   ![Click I don't have Internet](image_url)

2. **Proceed with Limited Setup**:
   - Click on "Continue with limited setup".

   ![Continue with limited setup](image_url)

### Step 7: Complete the Installation

1. **Create a Local Account**:
   - Follow the remaining prompts to create a local user account and complete the Windows 11 installation process.

## Conclusion

By following these steps, you can install Windows 11 and set up a local account without requiring a Microsoft account. This method allows you to use Windows 11 with a local user account, giving you more control over your system setup.

---
