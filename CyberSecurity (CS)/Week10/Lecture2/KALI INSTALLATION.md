# **Local Virtual Machine Installation Guide**

This document provides instructions for installing a local virtual machine on **Windows** and **macOS**. Follow the steps specific to your operating system.

---

## **Installation for Windows**

To set up a local virtual machine on Windows, you need the following tools:

1. **Oracle VM VirtualBox**  
2. **Kali Linux**  
3. Optionally, **7-Zip** (for extracting compressed files).

### **1\. Installing Oracle VM VirtualBox**

1. Navigate to the VirtualBox downloads page.  
2. Select the **Windows hosts** option to download the latest version of VirtualBox.  
3. Once downloaded:  
   * Double-click the file to start the setup.  
   * If prompted, select **Yes** to allow changes to your device.  
4. In the setup wizard:  
   * Click **Next** on the introductory screen.  
   * Confirm or customise settings, then click **Next**.  
5. If prompted with a warning about resetting network connections, click **Yes**.  
6. Address any dependency alerts by clicking **Yes** to proceed.  
7. When the installation is ready, click **Install** to begin.  
8. Once the installation is complete, click **Finish** to launch VirtualBox.

---

### **2\. Installing Kali Linux**

1. Navigate to the Kali Linux downloads page.  
2. Under the **Virtual Machines** section, select the **VirtualBox** option to download.  
3. Note that the downloaded file will be a large compressed file (approximately 2.9 GB).

---

### **3\. Installing 7-Zip**

If you need to extract the Kali Linux file:

1. Go to the [7-Zip downloads page](https://www.7-zip.org/).  
2. Download the **64-bit Windows** version.  
3. After downloading:  
   * Run the installer.  
   * Select **Install**, then **Close**.  
4. Open **7-Zip** from the Windows search box to confirm installation.

---

### **4\. Compiling All Three Installations**

1. Create a new folder named **KALI** for storing the extracted Kali Linux files.  
2. Right-click the downloaded Kali Linux file and select **Properties**.  
   * Change the **Opens with** option to **7-Zip**, then click **Apply** and **OK**.  
3. Extract the file by right-clicking and selecting **7-Zip \> Extract Here**.  
4. Open **Oracle VM VirtualBox** and click **Add**.  
5. Navigate to the **KALI** folder, select the extracted Kali Linux file, and click **Open**.  
6. Start the virtual machine by clicking **Start** in VirtualBox.  
7. Use the default login credentials (username: `kali`, password: `kali`). Change them later for security.

---

## **Installation for macOS**

On macOS, you'll use **UTM** instead of VirtualBox, and 7-Zip is not required.

### **1\. Installing UTM**

1. Go to the UTM downloads page and download the UTM software.  
2. Install UTM and launch it.

---

### **2\. Downloading and Installing Kali Linux**

1. Visit the Kali Linux downloads page.  
2. Select the **Installer Images** option and download the appropriate `.iso` file for macOS.

---

### **3\. Setting Up UTM with Kali Linux**

1. Open UTM and select **Create a New Virtual Machine**.  
2. Choose the **Virtualize** option.  
3. Select **Other** as the operating system and browse for the Kali Linux `.iso` file.  
4. Adjust the following settings:  
   * **Memory**: Set to 2048 MB.  
   * **Storage**: Allocate 32 GB.  
5. Name the VM (e.g., “Kali Linux”), check **Open VM Settings**, and save.  
6. In the VM settings:  
   * Add a new **Serial** device.  
   * Save the settings.  
7. Click the play button to start the VM and begin the Kali Linux installation process.

---

### **4\. Installing and Configuring Kali Linux**

1. Follow the on-screen installation prompts, selecting **Install** in the Terminal 1 window.  
2. Set your username and password to `kali` during the process.  
3. When partitioning, select **Guided – use the entire disk**.  
4. During software selection, choose:  
   * **GNOME**.  
   * **Default — recommended tools**.  
5. After installation:  
   * Eject the `.iso` file using the **Drive image options** icon.  
   * Restart the VM.  
6. Once the login screen appears, use `kali` as both username and password.

---

## **Notes**

* Make sure your system meets the requirements for running a virtual machine.  
* Use secure credentials to enhance the security of your setup after initial installation.

